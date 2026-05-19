from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str

    OPENAI_API_KEY: str

    DATABASE_URL: str

    REDIS_URL: str

    SECRET_KEY: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()