from email.message import EmailMessage

from src.models.models import Email


def send_html_email(server, sender_email: Email, recipients: list[Email], subject: str, body):
    """Отправляет письмо с помощью указанного почтового сервера"""
    # TODO Написать кастомный тип для емэйла с встроенной валидацией
    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = ",".join(recipients)
    message["Subject"] = subject
    message.add_alternative(body, subtype='html')
    # Отправляем письмо
    server.send_message(message)


