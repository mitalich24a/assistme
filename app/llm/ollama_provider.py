import time

import ollama

from app.config.settings import settings


class OllamaProvider:

    def __init__(self):

        self._client = ollama.AsyncClient(
            host=settings.ollama_base_url,
        )

    async def chat(
        self,
        messages: list,
        tools: list,
    ):

        print(
            "\nCalling Ollama..."
        )

        start = time.time()

        response = await self._client.chat(
            model=settings.ollama_model,
            messages=messages,
            tools=tools,
        )

        print(
            f"Ollama Response Time: {time.time()-start:.2f}s"
        )

        return response

    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ):

        response = await self._client.chat(
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

        return response.message.content