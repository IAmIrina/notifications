import json

import pika
import pika.exceptions

from src.utils.backoff import backoff
from src.models.models import EmailTemplate


class RabbitConsumer:
    def __init__(self, rabbit_params, email_sender) -> None:
        self.params = rabbit_params
        self.email_sender = email_sender
        credentials = pika.PlainCredentials(rabbit_params.username, rabbit_params.password)
        parameters = pika.ConnectionParameters(rabbit_params.host, rabbit_params.port, credentials=credentials)
        self.connection = pika.SelectConnection(parameters, on_open_callback=self.on_connected)
        self.start()


    def on_connected(self, connection):
        """Этот метод сработает, когда мы полностью подключимся к очереди, и создаст канал"""
        connection.channel(on_open_callback=self.on_channel_open)

    def on_channel_open(self, new_channel):
        self.channel = new_channel
        self.channel.queue_declare(
            queue=self.params.queue,
            durable=True,
            exclusive=False,
            auto_delete=False,
            callback=self.on_queue_declared)

    def on_queue_declared(self, frame):
        self.channel.basic_consume(self.params.queue, self.handle_delivery)

    def handle_delivery(self, channel, method, properties, body):
        """Сработывает каждый раз, когда мы получаем сообщение"""
        # Попробуем превратить наше сообщение в JSON
        try:
            message = json.loads(body)
        except json.JSONDecodeError:
            channel.basic_ack(delivery_tag=method.delivery_tag)
        # Отправляем сообщение
        email_to_send = EmailTemplate.parse_obj(message)
        self.email_sender.send_html_email(
            sender_email='durden191@yandex.ru',
            email=email_to_send
        )
        # Сообщаем очереди, что сообщение обработано, что сообщение обработано
        channel.basic_ack(delivery_tag=method.delivery_tag)

    @backoff()
    def start(self):
        """Запускает loop"""
        try:
            self.connection.ioloop.start()
        except KeyboardInterrupt:
            self.connection.close()
            self.connection.ioloop.start()