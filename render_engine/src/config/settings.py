from logging import config as logging_config

from config.logger import LOGGING
from pydantic import BaseSettings


class DotEnvMixin(BaseSettings):
    class Config:
        env_file = '.env'


class RabbitMQSettings(DotEnvMixin):
    username: str = 'guest'
    password: str = 'guest'
    host: str = '127.0.0.1'
    port: int = 5672
    exchange: str = ''
    queue: str


class Auth_server_settings(DotEnvMixin):
    url: str = 'http://127.0.0.1:8000/userinfo'
    authorization: str = 'BASIC fjdkjfdjkjdjfdkfdf434r543re=='


class Bitly(DotEnvMixin):
    endpoint: str = 'https://api-ssl.bitly.com/v4/shorten'
    access_token: str


def get_params(cls, env_prefix_name: str):
    class Params(cls):
        class Config:
            env_prefix = f'{env_prefix_name}_'
    return Params()


class Settings(DotEnvMixin):
    project_name: str = 'Notification render service.'
    auth_server: Auth_server_settings = get_params(Auth_server_settings, 'auth')
    consumer: RabbitMQSettings = get_params(RabbitMQSettings, 'rabbit_consumer')
    publisher: RabbitMQSettings = get_params(RabbitMQSettings, 'rabbit_publisher')
    bitly: Bitly = get_params(Bitly, 'bitly')


settings = Settings()

logging_config.dictConfig(LOGGING)
