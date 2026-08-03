import ollama

from app.core.interfaces.base_llm_provider import BaseLLMProvider
from app.config.settings import settings


class OllamaProvider(BaseLLMProvider):
    """
    Ollama implementation of BaseLLMProvider.
    """

    @property
    def provider_name(self) -> str:
        return "ollama"

    async def generate(
        self,
        prompt: str,
        **kwargs,
    ) -> str:

        response = ollama.chat(
            model=settings.ollama_model,
            messages=[
                    {
                        "role":"system",
                        "content": system_prompt,
                    },
                    {
                        "role":"user",
                        "content": user_prompt,
                    }
                ]
        )

        return response["message"]["content"]