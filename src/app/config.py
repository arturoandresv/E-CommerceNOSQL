from pydantic_settings import BaseSettings
from pathlib import Path

# Find .env in the project root
env_path = Path(__file__).resolve().parent.parent.parent / ".env"

class Settings(BaseSettings):
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    DYNAMODB_TABLE: str
    REDIS_HOST: str
    REDIS_PORT: int

    class Config:
        env_file = str(env_path)

settings = Settings()