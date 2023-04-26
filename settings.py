from pydantic import BaseSettings


class Settings(BaseSettings):
    API_KEY: str = ""
    USERNAME: str = ""
