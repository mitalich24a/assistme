from app.config.settings import settings
from app.core.interfaces.base_llm_provider import BaseLLMProvider
from app.llm.ollama_provider import OllamaProvider


class LLMFactory:
    """
    Creates the configured LLM provider.
    """

    @staticmethod
    def create() -> BaseLLMProvider:

        if settings.llm_provider == "ollama":
            return OllamaProvider()

        raise ValueError(
            f"Unsupported LLM provider: {settings.llm_provider}"
        )