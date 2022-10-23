import logging

from config.settings import settings
from core.consumer import RabbitConsumer
from core.extraction import UserDataExtractor
from core.publisher import RabbitPublisher
from core.rendering import JanjaTemplateRender, MessageHandler
from core.url_shortener import Bitly

logger = logging.getLogger()


if __name__ == '__main__':
    message_handler = MessageHandler(
        UserDataExtractor(settings.auth_server.url, settings.auth_server.authorization),
        JanjaTemplateRender(),
        Bitly(settings.bitly.endpoint, settings.bitly.access_token),
    )
    consumer = RabbitConsumer(
        settings.consumer,
        RabbitPublisher(settings.publisher),
        message_handler
    )

    consumer.start()
