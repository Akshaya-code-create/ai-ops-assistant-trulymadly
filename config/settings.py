import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    openai_api_key: str
    github_token: str
    openweather_api_key: str
    llm_model: str = 'gpt-4o-mini'
    log_level: str = 'INFO'
    max_retries: int = 3
    timeout: int = 30

settings = Settings()
