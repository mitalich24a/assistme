import uuid

from fastapi import APIRouter, File, Form, UploadFile

from app.core.dependencies import runtime_executor
from app.document.document_service import DocumentService
from app.execution.workflow_context import WorkflowContext
from app.schemas.workflow_response import WorkflowResponse
from app.utils.file_utils import FileUtils
from app.workflows.sprint_planning_workflow import SprintPlanningWorkflow

router = APIRouter()


@router.post(
    "/workflows/sprint-planning",
    response_model=WorkflowResponse,
)
async def sprint_planning(
    design_text: str | None = Form(default=None),
    document: UploadFile | None = File(default=None),
):

    #
    # Either pasted text OR uploaded document
    #
    if document:

        file_path = FileUtils.save(document)

        design_text = DocumentService.extract(file_path)

    if not design_text:
        raise ValueError(
            "Either design_text or document must be provided."
        )

    context = WorkflowContext(
        workflow_id=str(uuid.uuid4()),
        workflow_name="SprintPlanning",
        input_data={
            "design_text": design_text,
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