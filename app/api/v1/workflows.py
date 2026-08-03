import uuid

from fastapi import APIRouter, File, Form, UploadFile

from app.core.dependencies import runtime_executor
from app.document.document_service import DocumentService
from app.execution.workflow_context import WorkflowContext
from app.utils.file_utils import FileUtils
from app.workflows.sprint_planning_workflow import SprintPlanningWorkflow

router = APIRouter()


@router.post("/workflows/sprint-planning")
async def sprint_planning(
    design_text: str | None = Form(default=None),
    document: UploadFile | None = File(default=None),
    publish: bool = Form(default=False),
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
        metadata={
            "publish": publish,
        },
    )

    workflow = SprintPlanningWorkflow()

    await workflow.validate(context)

    definition = await workflow.build(context)

    results = await runtime_executor.execute(
        workflow=definition,
        context=context,
    )

    #
    # Serialize Pydantic models
    #
    serialized_results = []

    for result in results:

        data = {}

        for key, value in result.data.items():

            if hasattr(value, "model_dump"):
                data[key] = value.model_dump()

            elif isinstance(value, list):

                serialized = []

                for item in value:

                    if hasattr(item, "model_dump"):
                        serialized.append(item.model_dump())
                    else:
                        serialized.append(item)

                data[key] = serialized

            else:
                data[key] = value

        serialized_results.append(data)

    return {
        "workflow_id": context.workflow_id,
        "status": "COMPLETED",
        "results": serialized_results,
    }