from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """mysql db"""
    POSTGRES_HOST: str = 'localhost'
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = 'fastapi'
    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: str = 'fastapi123456'

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        extra = "ignore"  # 忽略额外的输入


class RedisSettings(BaseSettings):
    """redis"""

    REDIS_HOST: str = 'localhost'
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: str = 'fastapi123456'

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        extra = "ignore"  # 忽略额外的输入


settings = Settings()
redis_settings = RedisSettings()
