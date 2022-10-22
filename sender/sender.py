from psycopg2.extras import DictCursor

from config import email_server_settings, postgres_settings
from services.servers import get_smtp_server_connection
from db.connections import create_pg_conn
from db.postgres import PostgresService
from models import Notification
from services.email_service import send_html_email

RECIPIENT_EMAILS = ['durden191@yandex.ru', 'alexvkleschov@gmail.com']


if __name__ == '__main__':
    with create_pg_conn(**postgres_settings.dict(), cursor_factory=DictCursor) as pg_conn:
        # Подключения
        postgres_service = PostgresService(pg_conn=pg_conn, tablename='notifications')
        # Подключаемся к серверу
        server = get_smtp_server_connection(**email_server_settings.dict())

        # Отправляем письмо
        with open('test_template.html') as f:
            send_html_email(server, email_server_settings.login, RECIPIENT_EMAILS, 'New Letter Test', f.read())

        server.close()  # Закрываете соединение с smtp-сервером

