import logging

from config.settings import settings
from core.consumer import RabbitConsumer
from core.extraction import UserDataExtractor
from core.publisher import RabbitPublisher
from core.rendering import JanjaTemplateRender, MessageHandler

logger = logging.getLogger()


if __name__ == '__main__':
    message_handler = MessageHandler(
        UserDataExtractor(settings.auth_server.url, settings.auth_server.authorization),
        JanjaTemplateRender()
    )
    consumer = RabbitConsumer(
        settings.consumer,
        RabbitPublisher(settings.publisher),
        message_handler
    )

    consumer.start()
