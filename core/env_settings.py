from pydantic_settings import BaseSettings
from functools import lru_cache


class EnvSettings(BaseSettings):
    TOKEN_SECRET: str

    class Config:
        env_file = ".env"
        case_sesitive = True
        extra = "ignore"


@lru_cache()
def get_environment_settings() -> EnvSettings:
    return EnvSettings(TOKEN_SECRET="")


EnvironmentSettings = get_environment_settings()
