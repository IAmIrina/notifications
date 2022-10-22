import smtplib
from email.message import EmailMessage


sender_email = 'from@email.com'
recipient_email = 'to@email.com'

server = smtplib.SMTP('localhost', 25)  # Подключаетесь к локальному smtp-серверу
message = EmailMessage()

message["From"] = sender_email
message["To"] = ",".join([recipient_email])
message["Subject"] = 'Добро пожаловать в Practix!'

with open('test_template.html') as f:
    message.set_content(f.read())


# Отправляем письмо
server.send_message(message)

server.close()  # Закрываете соединение с smtp-сервером

