from core.message_handler import EmailMessageHandler
from core.rendering import JanjaTemplateRender
from core.url_shortener import BitlyURLShortener
from core.extraction import UserDataExtractor

from tests.testdata.messages import incoming_message, outcoming_message, outcoming_message_bad_shortener


def test_email_handler(mock_url_shortener_post, mock_auth_service):
    """Proccess incoming message."""
    message_handler = EmailMessageHandler(
        UserDataExtractor('test', 'test'),
        JanjaTemplateRender(),
        BitlyURLShortener('test', 'test')
    )
    result = message_handler.proccess_message(incoming_message.copy())
    messages = [message for message in result]
    assert len(incoming_message['users']) == len(messages)
    assert outcoming_message == messages[0].dict()


def test_email_handler_bad_shortener(mock_bad_url_shortener_post, mock_auth_service):
    """Process incoming message when url shortener is not available."""
    message_handler = EmailMessageHandler(
        UserDataExtractor('test', 'test'),
        JanjaTemplateRender(),
        BitlyURLShortener('test', 'test')
    )
    result = message_handler.proccess_message(incoming_message.copy())
    messages = [message for message in result]
    assert len(incoming_message['users']) == len(messages)
    assert outcoming_message_bad_shortener == messages[0].dict()
