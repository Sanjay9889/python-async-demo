import argparse
import csv
import os

import boto3
import base64
from botocore.exceptions import ClientError
import json
import logging
from zipfile import ZipFile, ZIP_DEFLATED

try:
    from urllib import urlencode, unquote
    from urlparse import urlparse, parse_qsl, ParseResult
except ImportError:
    # Python 3 fallback
    from urllib.parse import (
        urlencode, unquote, urlparse, parse_qsl, ParseResult
    )

LOGGER = logging.getLogger(__name__)


def add_suffix_to_file(filename, suffix):
    """
    Add a sufix to given file
    """
    if filename is None:
        LOGGER.error("Filename is required to work")
        raise ValueError("Filename is required to work")
    try:
        name, ext = os.path.splitext(filename)
        return "{name}_{suffix}{ext}".format(name=name, suffix=suffix, ext=ext)
    except Exception as e:
        LOGGER.error(f"Unable to rename file and error was {e}")
        raise Exception(f"Unable to rename file  and error was {e}")


def get_secret(secret_name, region_name):
    """
    Connect to secret manager and get the secret
    """
    if not secret_name:
        LOGGER.error("Name of secret is missing")
        raise ValueError("Name of secret is missing")
    if not region_name:
        LOGGER.error("Region name is missing")
        raise ValueError("Region name is missing")

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    # Decrypts secret using the associated KMS key.
    # Depending on whether the secret is a string or binary, one of these fields will be populated.

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
        # Decrypts secret using the associated KMS key.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            secret = base64.b64decode(get_secret_value_response['SecretBinary'])
        return json.loads(secret)
    except ClientError as e:
        LOGGER.error(f"Unable to get the secret value and error was {e}")
        raise ClientError(f"Unable to get the secret value and error was {e}")
    except Exception as e:
        LOGGER.error(f"Unable to get the secret value and error was {e}")
        raise Exception(f"Unable to get the secret value and error was {e}")


def create_json(data, file, key=None):
    """
    create a requests.json file
    :param data: data to write in json file
    :param file: name of the json file
    :param key: Optional parameter
    :return:
    """
    if not data:
        LOGGER.error("Data is needed to write in json file")
        raise ValueError("Data is needed to write in json file")
    if not file:
        LOGGER.error("Json file is needed to write data")
        raise ValueError("Json file is needed to write data")
    try:
        if key is not None:
            data = {key: data}
        with open(file, "w") as file:
            json.dump(data, file)
        return True
    except Exception as e:
        LOGGER.error(f"Unable to create json file and error was {e}")
        raise Exception(f"Unable to create json file and error was {e}")


def create_archive(input_file, output_file):
    """
    create an archived file
    :param input_file: File that needs to be archived
    :param output_file: Archived file
    :return: True if success, error otherwise
    """
    if not input_file:
        LOGGER.error("Input file is missing")
        raise ValueError("Input file is missing")
    if not output_file:
        LOGGER.error("Output file is missing")
        raise ValueError("Output file is missing")
    try:
        with ZipFile(output_file, 'w', ZIP_DEFLATED) as zipObj:
            zipObj.write(input_file, arcname="requests.json")
        LOGGER.info("Archived request file created !!")
        return True
    except Exception as e:
        LOGGER.error(f"Unexpected error occurred and error was {e}")
        raise Exception(f"Unexpected error occurred and error was {e}")


def write_to_text(data_to_write, file, is_failure=False):
    """
    Write data to text file
    """
    if not data_to_write:
        raise ValueError("Data is needed to write in file")
    if not file:
        raise ValueError("File is needed to write data")
    try:
        with open(file, 'w') as fl:
            for data in data_to_write:
                if is_failure is True:
                    fl.write('%s\n' % data)
                else:
                    if isinstance(data, dict):
                        for key, value in data.items():
                            fl.write('%s, %s\n' % (key, value))
                    else:
                        LOGGER.error(f'Invalid data - {data}')
    except IOError as ex:
        LOGGER.error(f'IO error and error was {ex}')
        raise IOError(f'IO error and error was {ex}')
    except Exception as ex:
        LOGGER.error(f"Unable to write to text file and error was {ex}")
        raise Exception(f"Unable to write to text file and error was {ex}")


def write_to_csv(data_to_write, filename):
    """
    Write the data to csv file
    :param data_to_write:
    :param filename:
    :return:
    """
    if not data_to_write:
        LOGGER.error("Data is needed to write in csv file")
        raise ValueError("Data is needed to write in file")
    if not filename:
        LOGGER.error("CSV file is needed to write data")
        raise ValueError("File is needed to write data")
    try:
        with open(filename, 'w') as file:
            w = csv.writer(file)
            w.writerow(["VIN", "MMR"])
            w.writerows(data_to_write.items())
        LOGGER.info("The result is written to csv file")
    except Exception as e:
        LOGGER.error(f"Unable to write to csv and error was {e}")
        raise Exception(f"Unable to write to csv and error was {e}")


def upload_to_s3(file_to_upload, s3_bucket, s3_key_space):
    """
    Write the result to s3 bucket
    :param s3_key_space:
    :param s3_bucket:
    :param file_to_upload:
    :return:
    """
    if not s3_bucket:
        LOGGER.error("S3 bucket is missing")
        raise ValueError("S3 bucket is missing")
    if not s3_key_space:
        LOGGER.error("Key space is missing")
        raise ValueError("S3 bucket is missing")
    if not file_to_upload:
        LOGGER.error("File is missing")
        raise ValueError("File is missing")
    try:
        s3 = boto3.resource('s3')
        _bucket = s3.Bucket(s3_bucket)
        _bucket.upload_file(file_to_upload, s3_key_space)
        LOGGER.info(f"Uploaded the result {s3_key_space} to {_bucket}")
    except ClientError as e:
        LOGGER.error(f"Unable to write to s3 bucket and error was {e}")
        raise ClientError(f"Unable to write to s3 bucket and error was {e}")
    except Exception as e:
        LOGGER.error(f"Unable to write to s3 bucket and error was {e}")
        raise Exception(f"Unable to write to s3 bucket and error was {e}")


def add_url_params(url, params):
    """ Add GET params to provided URL being aware of existing.
    :param url: string of target URL
    :param params: dict containing requested params to be added
    :return: string with updated URL
    """
    # Unquoting URL first so we don't loose existing args
    url = unquote(url)
    # Extracting url info
    parsed_url = urlparse(url)
    # Extracting URL arguments from parsed URL
    get_args = parsed_url.query
    # Converting URL arguments to dict
    parsed_get_args = dict(parse_qsl(get_args))
    # Merging URL arguments dict with new params
    parsed_get_args.update(params)

    # Bool and Dict values should be converted to json-friendly values
    # you may throw this part away if you don't like it :)
    parsed_get_args.update(
        {k: json.dumps(v) for k, v in parsed_get_args.items()
         if isinstance(v, (bool, dict))}
    )

    # Converting URL argument to proper query string
    encoded_get_args = urlencode(parsed_get_args, doseq=True)
    # Creating new parsed result object based on provided with new
    # URL arguments. Same thing happens inside of urlparse.
    updated_url = ParseResult(
        scheme=parsed_url.scheme,
        netloc=parsed_url.netloc,
        path=parsed_url.path,
        params=parsed_url.params,
        query=encoded_get_args,
        fragment=parsed_url.fragment
    ).geturl()

    return updated_url


def fuzzy_match_to_text(data_to_write, file, value_to_include):
    """
    Write the result to text file. the text file should include command separated api input and caid
    : data_to_write: Data that needs to be written in file
    : file: name of the file
    : value_to_include: If key is present in value_to_include then write in file, ignore otherwise
    """
    try:

        with open(file, 'w') as fl:
            for item in data_to_write:
                url = ''
                for key in value_to_include:
                    value = item.get(key)
                    if not url:
                        url = value
                    else:
                        url = url + ' | ' + str(value)
                fl.write('%s \n' % url)
    except FileNotFoundError as e:
        LOGGER.error(f'File {file} not found and error was {e}')
    except KeyError as e:
        LOGGER.error(f'Error in processing caid and error was {e}')
    except Exception as e:
        LOGGER.error(f'Unable to write to text file and error was {e}')


def get_args():
    """
    Gets the arguments from the command line
    :return:
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-s",
        "--step",
        help="""Type of step new or used""",
        required=True,
    )

    parser.add_argument("-r",
                        "--retry",
                        default=False,
                        required=False,
                        action="store_true",
                        help="Re-try the failures")

    args, unknown = parser.parse_known_args()
    if unknown:
        LOGGER.warning(f"Passed in extraneous args: {unknown}")
    return args


def divide_chunks(big_list, chunk_size):
    """
    Divide a big list into multiple chunks of chunk_size each
    """
    # looping till length l
    for i in range(0, len(big_list), chunk_size):
        yield big_list[i:i + chunk_size]
