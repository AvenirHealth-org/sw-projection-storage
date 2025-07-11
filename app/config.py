from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config: SettingsConfigDict = SettingsConfigDict(env_file=".env") # pyright: ignore[reportIncompatibleVariableOverride]
    app_name: str = "sw-projection-storage"
    cosmos_url: str = "xxx"
    cosmos_key: str = "xxx"
    cosmos_use_emulator: str = "False"
