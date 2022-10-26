import smtplib
from email.message import EmailMessage

from src.models.models import Email
from src.models.models import EmailTemplate


class EmailSender:
    """Отправляет емэйл-письма"""
    def __init__(self, email_params):
        self.email_params = email_params

    def get_smtp_server_connection(self):
        """Возвращает соединение с внешним почтовым SMTP сервером"""
        # TODO Добавить обработку исключений
        server = smtplib.SMTP_SSL(self.email_params.address, self.email_params.port)
        server.login(self.email_params.login, self.email_params.password)
        print("Соединение с сервером установлено")
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
        server.send_message(message)
        # Закрываем соединение
        server.close()


