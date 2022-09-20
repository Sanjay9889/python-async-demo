"""
Module docstring
"""
# System Libraries
import json
import os
import sys
from mock import patch, mock, MagicMock, mock_open

# Third party libraries
import pytest

# Local libraries
from valuation_api_response_test_data import (test_data,
                                              success_data,
                                              no_best_match)
from ihs_markit_polk_snowflake.common.utility import (
    add_suffix_to_file,
    get_secret,
    create_json,
    create_archive,
    write_to_text,
    write_to_csv,
    upload_to_s3,
    add_url_params,
    get_args,
)


def test_add_suffix_to_file():
    file_name = "fake_file.txt"
    prefix = "test"
    res = add_suffix_to_file(
        file_name,
        prefix)
    assert res == 'fake_file_test.txt'


def test_add_suffix_to_file_no_file():
    with pytest.raises(ValueError) as excinfo:
        res = add_suffix_to_file(
            None,
            'fake_prefix')
    assert 'Filename is required to work' in str(excinfo.value)


@mock.patch("boto3.session.Session")
def test_get_secret(mock_session_class):
    mock_session_object = mock.Mock()
    mock_client = mock.Mock()
    mock_client.get_secret_value.return_value = {
        'SecretString': '{\n  "username":"fake_username",\n  "password":"BdsjsnQw&XDWgaEeT9XGTT29"\n}'}
    mock_session_object.client.return_value = mock_client
    mock_session_class.return_value = mock_session_object

    res = get_secret('fake_secret_name', 'fake_aws_region')
    assert res == {'username': 'fake_username', 'password': 'BdsjsnQw&XDWgaEeT9XGTT29'}


def test_get_secret_no_secret_name():
    with pytest.raises(ValueError) as excinfo:
        res = get_secret(
            None,
            'fake_aws_region')
    assert 'Name of secret is missing' in str(excinfo.value)


def test_get_secret_no_region():
    with pytest.raises(ValueError) as excinfo:
        res = get_secret(
            'Fake_secret',
            None)
    assert 'Region name is missing' in str(excinfo.value)


@patch("json.dump", MagicMock(return_value=None))
def test_create_json():
    res = create_json('fake_data', 'fake_file', None)
    print(res)
    assert res == True


@patch("json.dump", MagicMock(return_value=None))
def test_create_json_key():
    res = create_json('fake_data', 'fake_file', 'fake_key')
    print(res)
    assert res == True


def test_create_json_no_data():
    with pytest.raises(ValueError) as excinfo:
        res = create_json(None, 'fake_file', 'fake_key')

    assert 'Data is needed to write in json file' in str(excinfo.value)


def test_create_json_no_file():
    with pytest.raises(ValueError) as excinfo:
        res = create_json('fake_data', None, 'fake_key')

    assert 'Json file is needed to write data' in str(excinfo.value)


def test_create_archive_no_file():
    with pytest.raises(ValueError) as excinfo:
        res = create_archive(None, 'fake_output.zip')

    assert 'Input file is missing' in str(excinfo.value)


def test_create_archive_no_output():
    with pytest.raises(ValueError) as excinfo:
        res = create_archive('fake_input_file.json', None)

    assert 'Output file is missing' in str(excinfo.value)
