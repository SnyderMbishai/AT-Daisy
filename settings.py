from pydantic import BaseSettings


class Settings(BaseSettings):
    API_KEY: str
    USER_NAME: str
    SENDER: str
    
    class Config:
        env_file = ".env"


settings = Settings()
