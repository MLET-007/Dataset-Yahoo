from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings): 
    app_name: str = "Yahoo Predict"

    model_config = SettingsConfigDict(extra='allow', env_file=".env")
