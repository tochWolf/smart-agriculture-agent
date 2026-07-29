from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Smart Agriculture AI"
    DEBUG: bool = True
    GEMINI_API_KEY: str = ""
    WEATHER_API_KEY: str = ""
    FRONTEND_URL: str = "http://localhost:5173"

    class Config:
        env_file = ".env"

settings = Settings()
