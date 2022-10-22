import os
import uuid
from email.message import EmailMessage

from psycopg2.extras import DictCursor
from jinja2 import Environment, FileSystemLoader

from config import email_server_settings, postgres_settings
from services.servers import get_smtp_server_connection
from db.connections import create_pg_conn
from db.postgres import PostgresService
from models import Notification


if __name__ == '__main__':
    with create_pg_conn(**postgres_settings.dict(), cursor_factory=DictCursor) as pg_conn:



        postgres_service = PostgresService(pg_conn=pg_conn, tablename='notifications')
        postgres_service.save_notification_to_db(random_notification)

        recipient_email = 'durden191@yandex.ru'

        # Подключаемся к серверу
        server = get_smtp_server_connection(
                address=email_server_settings.server_address,
                port=email_server_settings.server_port,
                login=email_server_settings.login,
                password=email_server_settings.password,
                )

        message = EmailMessage()

        message["From"] = recipient_email
        message["To"] = ",".join([recipient_email])
        message["Subject"] = 'Добро пожаловать в Practix!'

        with open('test_template.html') as f:
            message.set_content(f.read())


        env = Environment(loader=FileSystemLoader(f'{os.path.dirname(__file__)}'))  # Указываем расположение шаблонов
        template = env.get_template('test_template.html')  # Загружаем нужный шаблон в переменную

        output = template.render()

        # Отправляем письмо
        message.add_alternative(output, subtype='html')
        server.send_message(message)
        server.close()  # Закрываете соединение с smtp-сервером
