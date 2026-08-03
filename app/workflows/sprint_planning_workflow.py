import uuid

from app.core.interfaces.base_workflow import BaseWorkflow
from app.execution.workflow_context import WorkflowContext
from app.execution.workflow_definition import WorkflowDefinition
from app.execution.workflow_step import WorkflowStep


class SprintPlanningWorkflow(BaseWorkflow):

    @property
    def name(self) -> str:
        return "SprintPlanningWorkflow"

    async def validate(
        self,
        context: WorkflowContext,
    ) -> None:

        if "design_text" not in context.input_data:
            raise ValueError("design_text is required.")

    async def build(
        self,
        context: WorkflowContext,
    ) -> WorkflowDefinition:

        return WorkflowDefinition(
            name=self.name,
            steps=[
                WorkflowStep(
                    name="Generate Plan",
                    capability="planning",
                    input_data={
                        "prompt": context.input_data["design_text"],
                    },
                ),
            ],
        )

    async def resume(
        self,
        context: WorkflowContext,
    ) -> WorkflowDefinition:

        return await self.build(context)