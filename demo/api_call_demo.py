import logging
import os, stat

import backoff
import requests
from async_timeout import timeout
from dotenv import load_dotenv, find_dotenv

try:
    from urllib import urlencode, unquote
    from urlparse import urlparse, parse_qsl, ParseResult
except ImportError:
    # Python 3 fallback
    from urllib.parse import (
        urlencode, unquote, urlparse, parse_qsl, ParseResult
    )
from common.logging import setup_logging
from common.utility import (get_args,
                            add_suffix_to_file,
                            get_secret,
                            divide_chunks,
                            upload_to_s3,
                            write_to_text)
from aiohttp import ClientSession, ClientError
import asyncio
from aiolimiter import AsyncLimiter

# Gets or creates a LOGGER
LOGGER = logging.getLogger(__name__)


def create_header(**kwargs):
    """
    Create header to be used in valuation api call
    :param kwargs:
    :return:
    """
    if kwargs is None:
        raise ValueError("kwargs is required to work")

    _content_type = kwargs.get("content_type", None)
    _token_type = kwargs.get("token_type", None)
    _access_token = kwargs.get("access_token", None)
    if _content_type is None:
        raise ValueError("Content type is required to work")
    if _token_type is None:
        raise ValueError("Token type is required to work")
    if _access_token is None:
        raise ValueError("Access token is required to work")

    try:
        _header = dict()
        _header['content_type'] = _content_type
        _header['Authorization'] = f"{_token_type} {_access_token}"
        return _header
    except KeyError as e:
        raise KeyError(f"Missing a Key - {e}")
    except Exception as e:
        raise Exception(f"Unexpected error occurred and error was {e}")


def get_authentication_token(api_url, api_user, api_password):
    """
    Get valuation api authentication token
    :return:
    """
    if api_url is None:
        raise ValueError("Url is required to work")
    if api_user is None:
        raise ValueError("Username is required to work")
    if api_password is None:
        raise ValueError("Password is required to work")
    try:
        headers = dict()
        headers["content-type"] = "application/x-www-form-urlencoded"
        grant_type_data = "grant_type=client_credentials"
        res = requests.post(api_url,
                            headers=headers,
                            data=grant_type_data,
                            auth=(api_user, api_password))
        if res.status_code == 200:
            return res.json()["token_type"], res.json()["access_token"]
        else:
            return False, False
    except KeyError as key_error:
        raise KeyError(f"Unable to find a key and error was {key_error}")
    except Exception as e:
        raise Exception(f"Unexpected error occurred and error was {e}")


async def get_best_match(payload, records, status_code):
    """
    The best match in the valuation api result
    """
    try:
        pass
    except Exception as ex:
        LOGGER.error(f"Error in getting best match and error was {e}")
        return ex


def backoff_handler(details):
    """
    Backoff Handler
    :param details:
    :return:
    """
    # Avoid reporting the api key to logs
    wait = details.get("wait")
    tries = details.get("tries")
    target = details.get("target")
    args = details.get("args")
    kwargs = details.get("kwargs")
    session = kwargs.get("session")
    throttler = kwargs.get("throttler")
    LOGGER.warning(
        f"Backing off {wait} seconds after {tries} tries "
        f"calling function {target} with args {args} and kwargs "
        f"session: {session}"
        f"throttler: {throttler}"
    )


def giveup_handler(details):
    """
    Giveup Handler
    :param details:
    :return:
    """
    # Avoid reporting the api key to logs
    wait = details.get("wait")
    tries = details.get("tries")
    target = details.get("target")
    args = details.get("args")
    kwargs = details.get("kwargs")
    session = kwargs.get("session")
    LOGGER.warning(
        f"Give-up {wait} seconds after {tries} tries "
        f"calling function {target} with args {args} and kwargs "
        f"session: {session}"
        )
    return details


@backoff.on_exception(
    backoff.expo,
    ClientError,
    max_tries=5,
    max_time=600,
    jitter=backoff.full_jitter,
)
async def get_valuation(url, payload, session, semaphore, limiter):
    """
    Call fuzzy match api
    :param url:
    :param session:
    :param semaphore:
    :param payload:
    :return:
    """
    global header
    async with semaphore:
        async with limiter:
            async with session.get(url, headers=header) as response:
                status_code = response.status
                # This triggers the backoff to happen
                if status_code not in (200, 400, 404):
                    global is_token_refreshed
                    if status_code == 401 and is_token_refreshed is False:
                        is_token_refreshed = True
                        _token_type, _access_token = get_authentication_token(
                            AUTHENTICATION_API,
                            user,
                            password
                        )
                        header = create_header(content_type="application/x-www-form-urlencoded",
                                               token_type=_token_type,
                                               access_token=_access_token)
                        raise ClientError(status_code)
                    raise ClientError(status_code)
                if status_code in (400, 404):
                    mmr = {payload: '' + ',' + ' ' + str(status_code)}
                    return mmr
                try:
                    asynch_response = await response.json()
                    mmr = await get_best_match(payload, asynch_response, str(status_code))
                    return mmr
                except Exception as ex:
                    LOGGER.error(f"Error in get valuation and error was {ex}")
                    return ex


async def wrap_get_valuation(func, *args, **kwargs):
    try:
        return await func(*args, **kwargs)
    except (ClientError, TimeoutError, Exception) as err:
        status_code = str(err)
        payload = kwargs.get('payload')
        data_for_retries.append(payload)
        mmr = {payload: '' + ',' + ' ' + status_code}
        return mmr


async def main(payloads):
    tasks = []
    sema = asyncio.Semaphore(10)
    limiter = AsyncLimiter(int(RATE_LIMIT) * 60)
    async with ClientSession() as session:
        async with timeout(None):
            for payload in payloads:
                task = asyncio.ensure_future(wrap_get_valuation(
                    get_valuation,
                    url=API + payload.strip('\n'),
                    payload=payload.strip('\n'),
                    session=session,
                    semaphore=sema,
                    limiter=limiter,
                ))
                tasks.append(task)

            responses = await asyncio.gather(*tasks)
            return responses


if __name__ == '__main__':
    # Load environment variables so globals (in local imports) can be set
    load_dotenv(find_dotenv(), verbose=False)
    BUCKET = os.getenv("EXPORT_BUCKET")
    VALUATION_SECRET_NAME = os.getenv("VALUATION_SECRET_NAME")
    API = os.getenv("API")
    AUTHENTICATION_API = os.getenv('AUTHENTICATION_API')
    RESULT = os.getenv("RESULT")
    INPUT = os.getenv("INPUT")
    RESULT_FILE = os.getenv("RESULT_FILE")
    output_key_space = os.getenv("output_key_space")
    log_key_space = os.getenv("log_key_space")
    INGEST_DATE = os.getenv("INGEST_DATE")
    BATCH_SIZE = os.getenv("BATCH_SIZE")
    data_for_retries = []

    # To get the command line arguments
    cmd_args = get_args()
    LOG_FILE = os.getenv("LOG_FILE")
    setup_logging(LOG_FILE)
    RATE_LIMIT = os.getenv("RATE_LIMIT")
    loop = asyncio.get_event_loop()
    try:
        with open(INPUT) as file:
            valuation_inputs = file.readlines()
    except IOError:
        LOGGER.exception("Unable to read valuation input file")
        raise

    secret = get_secret(VALUATION_SECRET_NAME, 'us-east-1')
    if not secret:
        LOGGER.error("Unable to get secrets")
        raise ValueError("Unable to get secrets")

    user, password = secret["valuation_api_user"], secret["valuation_api_password"]

    token_type, access_token = get_authentication_token(
        AUTHENTICATION_API,
        user,
        password
    )
    if access_token is False:
        LOGGER.error("Unable to get access token")
        raise ValueError("Unable to get access token")

    header = create_header(content_type="application/x-www-form-urlencoded",
                           token_type=token_type,
                           access_token=access_token)

    chunked_list = list(divide_chunks(big_list=valuation_inputs, chunk_size=int(BATCH_SIZE)))
    LOGGER.info(
        f"Chunked size- {len(chunked_list)}"
    )
    batch_counter = 0
    try:
        for params in chunked_list:
            is_token_refreshed = False
            batch_counter += 1
            LOGGER.info(
                f"Starting batch number [{batch_counter}] out of [{len(chunked_list)}] "
            )

            results = loop.run_until_complete(
                asyncio.ensure_future(
                    main(payloads=params)
                )
            )
            if results:
                LOGGER.info(f"Size of result {len(results)}")
                LOGGER.info(f"Preparing to write results [{len(results)}]")
                result = add_suffix_to_file(RESULT, batch_counter)
                result_file = add_suffix_to_file(RESULT_FILE, batch_counter)

                LOGGER.info(f"Valuation result file {result}")
                write_to_text(results, result)
                LOGGER.info(f"Wrote results [{len(results)}]")
                LOGGER.info(f"Number of result MMR written: [{len(results)}]")
                LOGGER.info(f"Start writing results to s3")
                upload_to_s3(result, BUCKET, output_key_space + "/" + result_file)
                LOGGER.info(
                    f"""Upload {result} file to  -
                                {BUCKET + '/' + output_key_space + "/" + result_file}"""
                )
                LOGGER.info(
                    f"Finished batch number [{batch_counter}] out of [{len(chunked_list)}]"
                )
            else:
                LOGGER.error(
                    f"Result not generated, error in api call"
                )
                raise ValueError("Result not generated, error in api call")

        LOGGER.info("************************ Processing Completed ******************************")
    except Exception as e:
        LOGGER.error(f'Unable to process the request and error was {e}')
        raise Exception(f'Unable to process the request and error was {e}')
    finally:
        # Upload log file to s3
        upload_to_s3(
            LOG_FILE,
            BUCKET,
            log_key_space
        )
        loop.close()
