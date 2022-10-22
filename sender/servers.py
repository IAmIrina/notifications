import smtplib


def get_smtp_server_connection(address: str, port: int, login: str, password: str):
    """Возвращает соединение с внешним почтовым SMTP сервером"""
    server = smtplib.SMTP_SSL(address, port)
    server.login(login, password)

    return server

    # TODO Добавить обработку исключений
