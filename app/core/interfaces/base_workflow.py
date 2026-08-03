from abc import ABC, abstractmethod

from app.execution.workflow_context import WorkflowContext
from app.execution.workflow_definition import WorkflowDefinition


class BaseWorkflow(ABC):
    """
    Base contract for all workflows.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Workflow name."""
        raise NotImplementedError

    @abstractmethod
    async def validate(
        self,
        context: WorkflowContext,
    ) -> None:
        """Validate workflow input."""
        raise NotImplementedError

    @abstractmethod
    async def build(
        self,
        context: WorkflowContext,
    ) -> WorkflowDefinition:
        """
        Build the workflow definition.
        """
        raise NotImplementedError

    @abstractmethod
    async def resume(
        self,
        context: WorkflowContext,
    ) -> None:
        """Resume workflow execution."""
        raise NotImplementedError