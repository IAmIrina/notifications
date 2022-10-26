import os

from pydantic import BaseSettings


class MainSettings(BaseSettings):
    class Config:
        env_file_encoding = 'utf-8'
        use_enum_values = True


class ApiSettings(MainSettings):
    uvicorn_reload: bool = True
    project_name: str = 'Rabbit_api'


class DatabaseSettings(MainSettings):
    ...


class RabbitMQSettings(MainSettings):
    user_name: str = 'guest'
    password: str = 'guest'
    host: str = '127.0.0.1'
    port: int = 5672
    exchange: str = ''


db_settings = DatabaseSettings()

api_settings = ApiSettings()

rabbit_settings = RabbitMQSettings()

# Корень проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
