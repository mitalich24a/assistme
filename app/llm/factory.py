from app.config.settings import settings
from app.core.interfaces.base_llm_provider import BaseLLMProvider


class LLMFactory:

    @staticmethod
    def create() -> BaseLLMProvider:

        if settings.llm_provider == "ollama":
            from app.llm.ollama_provider import OllamaProvider

            return OllamaProvider()

        raise ValueError(
            f"Unsupported provider: {settings.llm_provider}"
        )