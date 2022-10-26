import smtplib
import logging
from email.message import EmailMessage

from src.models.models import Email, EmailTemplate, Notification


logger = logging.getLogger(__name__)

class EmailSender:
    """Отправляет емэйл-письма"""
    def __init__(self, email_params, database):
        self.email_params = email_params
        self.database = database

    def get_smtp_server_connection(self):
        """Возвращает соединение с внешним почтовым SMTP сервером"""
        server = smtplib.SMTP_SSL(self.email_params.address, self.email_params.port)
        server.login(self.email_params.login, self.email_params.password)
        return server

    def send_html_email(self, sender_email: Email, email: EmailTemplate):
        """Отправляет письмо на указанные адреса"""
        server = self.get_smtp_server_connection()
        # Формируем письмо
        message = EmailMessage()
        message["From"] = sender_email
        message["To"] = email.email
        message["Subject"] = email.subject
        message.add_alternative(email.letter, subtype='html')
        # Отправляем письмо
        if self.allow_sending(email.notification_id, email.user_id):
            server.send_message(message)
            # Записываем факт отправки в БД
            notification = Notification(
                notification_id=email.notification_id,
                user_id=email.user_id,
                content_id=email.content_id,
                type='email'
            )
            self.database.save_notification_to_db(notification)
        # Закрываем соединение
        server.close()

    def allow_sending(self, notification_id, user_id):
        """Проверяет, что сообдение с данным notification_id для данного user_id не было отправлено"""
        # Если в БД нет записи об отправленном сообщении - разрешим отправку
        if not self.database.get_notification_by_id(notification_id, user_id):
            return True
        logger.warning(f'''Данное сообщение id: {notification_id} уже отправлялось 
                        данному пользователю {user_id}''')
        return False






