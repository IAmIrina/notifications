from http import HTTPStatus
from unittest.mock import Mock, patch

import pytest

from tests.testdata.messages import auth_response, bitly_response


@pytest.fixture()
def mock_url_shortener_post():
    with patch('core.url_shortener.requests.post') as post:
        json = bitly_response
        post.return_value = Mock(status_code=HTTPStatus.OK, json=lambda: json)
        yield post


@pytest.fixture()
def mock_bad_url_shortener_post():
    with patch('core.url_shortener.requests.post') as post:
        json = bitly_response
        post.return_value = Mock(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, json=lambda: json)
        yield post


@pytest.fixture()
def mock_auth_service():
    with patch('core.extraction.requests.get') as get:
        json = auth_response
        get.return_value = Mock(status_code=HTTPStatus.OK, json=lambda: json)
        yield get
