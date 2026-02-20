from pydantic_settings import BaseSettings, SettingsConfigDict


class OllamaSettings(BaseSettings):

    model_config = SettingsConfigDict(
        env_prefix="ollama_",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    api_key: str


def get_ollama_settings() -> OllamaSettings:
    settings = OllamaSettings()
    return settings
