import pika
import json

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('127.0.0.1', 5672, credentials=credentials)
        # self.connection = pika.SelectConnection(parameters, on_open_callback=self.on_connected)
        # self.start()

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='sender', durable=True)



text = {
    "email": "durden191@yandex.ru",
    "letter": "Hello, Irina! You watched 1000 movies this week! Click the link bellow to see your special offer! \n https://bitly.is/3MUdF93",
    "subject": "Special offer",
    "content_id": "5dc33ad2-2985-4557-9cae-4cfe9da592a7",
    "user_id": "a789d932-1a10-4fbe-b620-4cc4b1b15c6f"
}

channel.basic_publish(exchange='',
                      routing_key='sender',
                      body=json.dumps(text))

connection.close()