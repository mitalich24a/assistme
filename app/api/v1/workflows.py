import uuid

from fastapi import APIRouter

from app.core.dependencies import runtime_executor
from app.execution.workflow_context import WorkflowContext
from app.schemas.sprint_planning_request import SprintPlanningRequest
from app.schemas.workflow_response import WorkflowResponse
from app.workflows.sprint_planning_workflow import SprintPlanningWorkflow

router = APIRouter()


@router.post(
    "/workflows/sprint-planning",
    response_model=WorkflowResponse,
)
async def sprint_planning(
    request: SprintPlanningRequest,
):

    context = WorkflowContext(
        workflow_id=str(uuid.uuid4()),
        workflow_name="SprintPlanning",
        input_data={
            "design_text": request.design_text,
        },
    )

    workflow = SprintPlanningWorkflow()

    await workflow.validate(context)

    definition = await workflow.build(context)

    results = await runtime_executor.execute(
        workflow=definition,
        context=context,
    )

    return WorkflowResponse(
        workflow_id=context.workflow_id,
        status="COMPLETED",
        results=[
            result.data
            for result in results
        ],
    )