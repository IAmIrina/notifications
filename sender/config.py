from pydantic import BaseSettings, Field


class MainSettings(BaseSettings):
    class Config:
        env_file = './.env'
        env_file_encoding = 'utf-8'


class EmailServerSettings(MainSettings):
    server_address: str = Field(..., env='EMAIL_SERVER_ADDRESS')
    server_port: int = Field(..., env='EMAIL_SERVER_PORT')
    login: str = Field(..., env='EMAIL_ACCOUNT_LOGIN')
    password: str = Field(..., env='EMAIL_ACCOUNT_PASSWORD')

class PostgresSettings(MainSettings):
    db_name: str = Field('notifications', env='POSTGRES_DB')
    user: str = Field(..., env='POSTGRES_USER')
    password: str = Field(..., env='POSTGRES_PASSWORD')
    host: str = Field('localhost', env='POSTGRES_HOST')
    port: int = Field(5432, env='POSTGRES_PORT')

# Загружаем настройки
email_server_settings = EmailServerSettings()
postgres_settings = PostgresSettings()

