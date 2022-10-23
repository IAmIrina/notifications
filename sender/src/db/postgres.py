import uuid

from psycopg2.extensions import connection
import psycopg2.extras

from src.models.models import Notification


class PostgresService:
    """Управляет взаимодействием с БД POstgreSQL"""
    def __init__(self, pg_conn: connection, tablename: str):
        self.pg_conn = pg_conn
        self.tablename = tablename
        psycopg2.extras.register_uuid()  # Позволяет сервису принимать uuid в качестве параметров

    def execute(self, query: str, values: tuple = tuple()):
        """Выполняет один SQL запрос"""
        curs = self.pg_conn.cursor()
        curs.execute(query, values)
        curs.close()


    def save_notification_to_db(self, notification: Notification) -> None:
        """Сохраняет уведомление в БД"""
        query = f'''INSERT INTO {self.tablename} (notification_id, user_id, content_id, type)
                    VALUES (%s, %s, %s, %s);'''
        values = (
                notification.notification_id,
                notification.user_id,
                notification.content_id,
                notification.type,
                )
        self.execute(query, values)

    def get_notifications(self):
        """Возвращает все уведомления из БД"""
        query = f"SELECT * FROM notifications;"
        curs = self.pg_conn.cursor()
        curs.execute(query, tuple())
        return curs.fetchall()

    def get_notification_by_id(self, notification_id: uuid.UUID):
        """Возвращает уведомление по notification_id"""
        query = f"""SELECT * FROM notifications
                  WHERE notification_id='{notification_id}';"""

        curs = self.pg_conn.cursor()
        curs.execute(query)
        result = curs.fetchall()
        return result[0] if result else None
