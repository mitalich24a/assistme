from abc import ABC, abstractmethod


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
    ) -> str:
        """
        Generate a response from the LLM.
        """
        raise NotImplementedError