import os
import smtplib
from email.message import EmailMessage
from jinja2 import Environment, FileSystemLoader


sender_email = 'from@email.com'
recipient_email = 'to@email.com'

server = smtplib.SMTP('localhost', 25)  # Подключаетесь к локальному smtp-серверу
message = EmailMessage()

message["From"] = sender_email
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
