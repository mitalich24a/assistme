import ollama

from app.config.settings import settings
from app.core.interfaces.base_llm_provider import BaseLLMProvider


class OllamaProvider(BaseLLMProvider):

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

    async def chat(
        self,
        messages: list[dict],
        tools: list[dict] | None = None,
    ):

        kwargs = {
            "model": settings.ollama_model,
            "messages": messages,
        }

        if tools:
            kwargs["tools"] = tools

        return ollama.chat(**kwargs)