from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):

    @property
    @abstractmethod
    def provider_name(self) -> str:
        pass

    @abstractmethod
    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        pass

    @abstractmethod
    async def chat(
        self,
        messages: list[dict],
    ) -> str:
        pass