from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    #
    # Application
    #
    app_name: str = "AssistMe"

    app_version: str = "0.1.0"

    debug: bool = True

    #
    # LLM
    #
    llm_provider: str = "ollama"

    ollama_base_url: str = "http://localhost:11434"

    ollama_model: str = "qwen3:8b"

    openai_api_key: str = ""

    #
    # Publishing
    #
    publish_provider: str = "github"

    github_provider: str = "rest"

    github_owner: str = ""

    github_repo: str = ""

    github_token: str = ""

    #
    # MCP
    #
    mcp_transport: str = "stdio"

    mcp_host: str = "0.0.0.0"

    mcp_port: int = 9000

    #
    # Environment
    #
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:

    return Settings()


settings = get_settings()