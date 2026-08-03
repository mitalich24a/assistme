from abc import ABC, abstractmethod
from typing import Any


class BaseLLMProvider(ABC):
    """
    Base contract for all LLM providers.
    """

    @property
    @abstractmethod
    def provider_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        **kwargs,
    ) -> str:
        raise NotImplementedError