from abc import ABC
from abc import abstractmethod

from app.execution.workflow_context import WorkflowContext
from app.execution.workflow_definition import WorkflowDefinition


class BaseWorkflow(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    async def validate(
        self,
        context: WorkflowContext,
    ) -> None:
        ...

    @abstractmethod
    async def build(
        self,
        context: WorkflowContext,
    ) -> WorkflowDefinition:
        ...