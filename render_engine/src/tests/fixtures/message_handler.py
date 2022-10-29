import pytest

from core.extraction import UserDataExtractor
from core.message_handler import EmailMessageHandler
from core.rendering import JanjaTemplateRender
from core.url_shortener import BitlyURLShortener


@pytest.fixture()
def email_message_handler():
    return EmailMessageHandler(
        UserDataExtractor('test', 'test'),
        JanjaTemplateRender(),
        BitlyURLShortener('test', 'test')
    )
