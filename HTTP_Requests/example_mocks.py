import pytest
import requests

def test_url(requests_mock):
    requests_mock.get('http://test.com', text='data')
    assert 'data' == requests.get('http://test.com').text