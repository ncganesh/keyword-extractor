from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "NLP as a Service"

    class Config:
        env_file = ".env"

settings = Settings()
