from pydantic_settings import BaseSettings, SettingsConfigDict


class ClashAPISettings(BaseSettings):

    model_config = SettingsConfigDict(
        env_prefix="clash_",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    api_key: str


def get_clash_api_settings() -> ClashAPISettings:
    settings = ClashAPISettings()
    return settings
