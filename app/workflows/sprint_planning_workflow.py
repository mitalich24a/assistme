from app.constants.capabilities import Capabilities
from app.core.interfaces.base_workflow import BaseWorkflow
from app.execution.workflow_context import WorkflowContext
from app.execution.workflow_definition import WorkflowDefinition
from app.execution.workflow_step import WorkflowStep


class SprintPlanningWorkflow(BaseWorkflow):
    """
    Sprint Planning workflow.
    """

    @property
    def name(self) -> str:
        return "SprintPlanning"

    async def validate(
        self,
        context: WorkflowContext,
    ) -> None:

        design_text = context.input_data.get("design_text")

        if not design_text:
            raise ValueError("design_text is required.")

    async def build(
        self,
        context: WorkflowContext,
    ) -> WorkflowDefinition:

        return WorkflowDefinition(
            name=self.name,
            steps=[
                WorkflowStep(
                    name="Generate Sprint Plan",
                    capability=Capabilities.PLANNING,
                    input_data={},
                ),
            ],
        )

    async def resume(
        self,
        context: WorkflowContext,
    ) -> WorkflowDefinition:

        return await self.build(context)