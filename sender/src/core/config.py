from pydantic import BaseSettings, Field


class MainSettings(BaseSettings):
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class EmailServerSettings(MainSettings):
    address: str = Field(..., env='EMAIL_SERVER_ADDRESS')
    port: int = Field(..., env='EMAIL_SERVER_PORT')
    login: str = Field(..., env='EMAIL_ACCOUNT_LOGIN')
    password: str = Field(..., env='EMAIL_ACCOUNT_PASSWORD')

class PostgresSettings(MainSettings):
    dbname: str = Field('notifications', env='POSTGRES_DB')
    user: str = Field(..., env='POSTGRES_USER')
    password: str = Field(..., env='POSTGRES_PASSWORD')
    host: str = Field('localhost', env='POSTGRES_HOST')
    port: int = Field(5432, env='POSTGRES_PORT')


class RabbitSettings(MainSettings):
    username: str = Field(..., env='RABBIT_USER')
    password: str = Field(..., env='RABBIT_USER_PASSWORD')
    host: str = '127.0.0.1'
    port: int = 5672
    exchange: str = ''
    queue: str = 'sender'

# Загружаем настройки
email_server_settings = EmailServerSettings()
postgres_settings = PostgresSettings()
rabbit_settings = RabbitSettings()
