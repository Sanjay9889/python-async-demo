"""
Module docstring
"""
# System Libraries
import os
import sys
from mock import patch, mock

# Third party libraries
import pytest

# Load environment variables


# Local libraries
from valuation_api_response_test_data import (test_data,
                                              success_data,
                                              no_best_match)
from ihs_markit_polk_snowflake.ihs_markit_polk_valuation import (
    create_header,
    get_authentication_token,
    get_best_match,
    add_suffix_to_file
)


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'http://someurl.com/test.json':
        return MockResponse({"jobId": "12345", "uploadUrl": {"url": "http://someurl.com/test.json", "fields": "data"}},
                            200)
    elif args[0] == 'http://someotherurl.com/anothertest.json':
        return MockResponse(
            {"jobId": "12345", "uploadUrl": {"url": "http://someotherurl.com/anothertest.json", "fields": "data"}}, 200)
    return MockResponse(None, 404)


def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'http://someurl.com/test.json':
        return MockResponse({"status": "success", "message": "requests file updated successfully"}, 200)
    return MockResponse(None, 404)


def mocked_start_job(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if 'valid' in args[0]:
        j = MockResponse({"status": "SUCCESS", "message": "Job started successfully"}, 200)
        return j.json()
    j = MockResponse({"status": "FAILED", "message": "Failed to start the job"}, 400)
    return j.json()


def mocked_monitor_status(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if 'valid' in args[0]:
        j = MockResponse({"status": "SUCCESS", "message": "IN-PROGRESS"}, 200)
        return j.json()
    j = MockResponse({"status": "FAILED", "message": "FAILED"}, 400)
    return j.json()


def mocked_get_token(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if 'valid' in args[0]:
        return MockResponse({"token_type": "fake_token_type", "access_token": "fake_token"}, 200)

    return MockResponse({"status": "FAILED", "message": "FAILED"}, 400)


def test_create_header():
    content_type = "application/x-www-form-urlencoded"
    token_type = "fake_test_token_type"
    access_token = "fake_test_token"
    res = create_header(content_type=content_type,
                        token_type=token_type,
                        access_token=access_token)
    assert res == {'Authorization': 'fake_test_token_type fake_test_token',
                   'content_type': 'application/x-www-form-urlencoded'}
    assert res['content_type'] == content_type


def test_create_header_no_token_type():
    content_type = "application/x-www-form-urlencoded"
    access_token = "fake_test_token"
    with pytest.raises(ValueError) as excinfo:
        res = create_header(
            content_type=content_type,
            access_token=access_token)
    assert 'Token type is required to work' in str(excinfo.value)


def test_create_header_no_content_type():
    token_type = "fake_test_token_type"
    access_token = "fake_test_token"
    with pytest.raises(ValueError) as excinfo:
        res = create_header(
            token_type=token_type,
            access_token=access_token)
    assert 'Content type is required to work' in str(excinfo.value)


def test_create_header_no_access_token():
    content_type = "application/x-www-form-urlencoded"
    token_type = "fake_test_token_type"
    with pytest.raises(ValueError) as excinfo:
        res = create_header(
            content_type=content_type,
            token_type=token_type,
        )
    assert 'Access token is required to work' in str(excinfo.value)


@mock.patch('requests.post', side_effect=mocked_get_token)
def test_get_authentication_token(mock_post):
    # Assert requests.post calls
    res = get_authentication_token('http://valid_url.com', 'fake_user', 'fake_password')
    assert res == ("fake_token_type", "fake_token")


def test_get_authentication_token_no_url():
    with pytest.raises(ValueError) as excinfo:
        res = get_authentication_token(None, 'fake_user', 'fake_password')
    assert 'Url is required to work' in str(excinfo.value)


def test_get_authentication_token_no_user():
    with pytest.raises(ValueError) as excinfo:
        res = get_authentication_token('http://fake_url.com', None, 'fake_password')
    assert 'Username is required to work' in str(excinfo.value)


def test_get_authentication_token_no_password():
    with pytest.raises(ValueError) as excinfo:
        res = get_authentication_token('http://fake_url.com', 'fake_user', None)
    assert 'Password is required to work' in str(excinfo.value)


def test_get_best_match():
    res = get_best_match(success_data)
    vin = 'KNDPM3AC8N7015597?odometer=13&date=2021-12-29'
    assert res[0][vin] == 31000
    assert res[1] == 1
    assert res[2] == 0
    assert res[3] == 0


def test_get_best_match_no_best_match():
    res = get_best_match(no_best_match)
    vin = 'WBA43AT0XNCJ44572?odometer=11&date=2021-12-31'
    assert res[0][vin] == ''
    assert res[1] == 1
    assert res[2] == 0
    assert res[3] == 1


def test_get_best_match_sucess_more_items():
    res = get_best_match(test_data)
    assert res[1] == 5
    assert res[2] == 5
    assert res[3] == 2


def test_add_suffix_to_file():
    filename = 'test_ihs_markit_polk_valuation_output.txt'
    suffix = 0
    res = add_suffix_to_file(filename, suffix)
    assert res == 'test_ihs_markit_polk_valuation_output_0.txt'

