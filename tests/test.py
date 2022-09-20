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

def get_secret(secret_name, region_name):
    """
    Connect to secret manager and get the secret
    """
    if not secret_name:
        raise ValueError("Name of secret is missing")
    if not region_name:
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
        raise ClientError(f"Unable to get the secret value and error was {e}")
    except Exception as e:
        raise Exception(f"Unable to get the secret value and error was {e}")


def test_get_secret():
    secret = get_secret(FUZZY_MATCH_SECRET_NAME, 'us-east-1')
