from abc import ABC
from abc import abstractmethod


class BaseTool(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Unique tool name exposed to the LLM.
        """
        ...

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Description shown to the LLM.
        """
        ...

    @property
    @abstractmethod
    def input_schema(self) -> dict:
        """
        JSON schema describing tool inputs.
        """
        ...

    @abstractmethod
    async def execute(
        self,
        arguments: dict,
    ):
        """
        Execute the tool.
        """
        ...