from abc import ABC, abstractmethod
from app.schemas.tool_result import ToolResult


class BaseTool(ABC):
    """
    Base contract for all tools.
    """

    @property
    @abstractmethod
    def tool_name(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def description(self) -> str:
        raise NotImplementedError

    @abstractmethod
    async def execute(
        self,
        **kwargs: Any,
    ) -> ToolResult:
        """
        Execute the tool.
        """
        raise NotImplementedError