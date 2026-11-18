from typing import Optional

from pydantic import EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_title: str = 'Путешествия'
    app_description: str = 'Сайт, дающий почувствовать себя Марком Поло'
    geoapify_api_key: str


    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()