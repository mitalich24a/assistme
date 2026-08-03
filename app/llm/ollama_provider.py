import ollama

from app.config.settings import settings
from app.core.interfaces.base_llm_provider import BaseLLMProvider


class OllamaProvider(BaseLLMProvider):
    """
    Ollama implementation of BaseLLMProvider.
    """

    @property
    def provider_name(self) -> str:
        return "ollama"

    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:

        response = ollama.chat(
            model=settings.ollama_model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
        )

        return response["message"]["content"]