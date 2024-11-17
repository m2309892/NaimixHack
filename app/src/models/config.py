from pydantic_settings import BaseSettings


class Config(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_DB: str
    POSTGRES_PORT: str
    reset_db: bool
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

config = Config(_env_file='.env', _env_file_encoding='utf-8')