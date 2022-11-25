from logging import config as logging_config

from pydantic import BaseSettings, Field
from src.core.logger import LOGGING


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
    dbname: str = Field(..., env='NOTIFICATION_DB')
    user: str = Field(..., env='NOTIFICATION_USER')
    password: str = Field(..., env='NOTIFICATION_PASSWORD')
    host: str = Field(..., env='NOTIFICATION_HOST')
    port: int = Field(..., env='NOTIFICATION_PORT')


class RabbitSettings(MainSettings):
    username: str = Field(..., env='RABBIT_USER')
    password: str = Field(..., env='RABBIT_USER_PASSWORD')
    host: str = Field('127.0.0.1', env='RABBIT_HOST')
    port: int = Field(5672, env='RABBIT_PORT')
    exchange: str = ''
    queue: str = Field(..., env='QUEUE')


email_server_settings = EmailServerSettings()
postgres_settings = PostgresSettings()
rabbit_settings = RabbitSettings()
logging_config.dictConfig(LOGGING)
