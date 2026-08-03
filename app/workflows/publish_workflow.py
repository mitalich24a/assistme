from app.constants.capabilities import Capabilities
from app.core.interfaces.base_workflow import BaseWorkflow
from app.execution.workflow_context import WorkflowContext
from app.execution.workflow_definition import WorkflowDefinition
from app.execution.workflow_step import WorkflowStep


class PublishWorkflow(BaseWorkflow):
    """
    Publishes a planning result.
    """

    @property
    def name(self) -> str:
        return "PublishWorkflow"

    async def validate(
        self,
        context: WorkflowContext,
    ) -> None:

        if "planning" not in context.input_data:
            raise ValueError("planning is required.")

    async def build(
        self,
        context: WorkflowContext,
    ) -> WorkflowDefinition:

        return WorkflowDefinition(
            name=self.name,
            steps=[
                WorkflowStep(
                    name="Publish Sprint",
                    capability=Capabilities.PUBLISHING,
                ),
            ],
        )

    async def resume(
        self,
        context: WorkflowContext,
    ) -> WorkflowDefinition:

        return await self.build(context)