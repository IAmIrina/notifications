import uuid
import datetime as dt

from psycopg2.extensions import connection
import psycopg2.extras

from src.models.models import Notification


class PostgresService:
    """Управляет взаимодействием с БД POstgreSQL"""
    def __init__(self, pg_conn: connection, tablename: str):
        self.pg_conn = pg_conn
        self.tablename = tablename
        psycopg2.extras.register_uuid()  # Позволяет сервису принимать uuid в качестве параметров

    def execute_query(self, query: str, values=None):
        """Выполняет SQL запрос и возвращает результат запроса"""
        with self.pg_conn.cursor() as curs:
            if values:
                curs.execute(query, values)
            else:
                curs.execute(query)
                result = curs.fetchall()
                return result

    def save_notification_to_db(self, notification: Notification) -> None:
        """Сохраняет уведомление в БД"""
        query = f'''INSERT INTO {self.tablename} (notification_id, user_id, content_id, type, created_at)
                    VALUES (%s, %s, %s, %s, %s);'''
        values = (
                notification.notification_id,
                notification.user_id,
                notification.content_id,
                notification.type,
                str(dt.datetime.now()).split('.')[0]
                )
        self.execute_query(query, values)

    def get_notifications(self):
        """Возвращает все уведомления из БД"""
        query = f"SELECT * FROM notifications;"
        result = self.execute_query(query)

        return result

    def get_notification_by_id(self, notification_id: uuid.UUID, user_id: uuid.UUID):
        """Возвращает уведомление по notification_id"""
        query = f"""SELECT * FROM notifications
                  WHERE notification_id='{notification_id}' AND user_id='{user_id}';"""

        result = self.execute_query(query)
        return result[0] if result else None
