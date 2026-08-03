from abc import ABC, abstractmethod
from typing import Any

from app.execution.workflow_context import WorkflowContext
from app.schemas.agent_result import AgentResult


class BaseAgent(ABC):
    """
    Base contract for all AI agents.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Unique agent name.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Short description of the agent.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def capabilities(self) -> list[str]:
        """
        Capabilities supported by this agent.
        """
        raise NotImplementedError

    @abstractmethod
    async def run(
        self,
        context: WorkflowContext,
        **kwargs: Any,
    ) -> AgentResult:
        """
        Execute the assigned task.
        """
        raise NotImplementedError