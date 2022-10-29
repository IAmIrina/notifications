import logging

from config.settings import settings
from core.consumer import RabbitConsumer
from core.extraction import UserDataExtractor
from core.message_handler import EmailMessageHandler
from core.publisher import RabbitPublisher
from core.rendering import JanjaTemplateRender
from core.url_shortener import BitlyURLShortener

logger = logging.getLogger()


if __name__ == '__main__':
    message_handler = EmailMessageHandler(
        UserDataExtractor(settings.auth_server.url, settings.auth_server.authorization),
        JanjaTemplateRender(),
        BitlyURLShortener(settings.bitly.endpoint, settings.bitly.access_token),
    )
    consumer = RabbitConsumer(
        settings.consumer,
        RabbitPublisher(settings.publisher),
        message_handler
    )

    consumer.start()
