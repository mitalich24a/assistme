import uuid

from fastapi import APIRouter
from fastapi import File
from fastapi import Form
from fastapi import UploadFile

from app.core.dependencies import workflow_manager
from app.document.document_service import DocumentService
from app.execution.workflow_context import WorkflowContext
from app.utils.file_utils import FileUtils

router = APIRouter()


@router.post("/execute")
async def execute(
    user_request: str = Form(...),
    design_text: str | None = Form(default=None),
    document: UploadFile | None = File(default=None),
):

    #
    # Uploaded document
    #
    if document:

        file_path = FileUtils.save(
            document,
        )

        design_text = DocumentService.extract(
            file_path,
        )

    context = WorkflowContext(
        workflow_id=str(uuid.uuid4()),
        input_data={
            "user_request": user_request,
            "design_text": design_text,
        },
    )

    results = await workflow_manager.execute(
        context,
    )

    serialized_results = []

    for result in results:

        data = {}

        for key, value in result.data.items():

            if hasattr(value, "model_dump"):

                data[key] = value.model_dump()

            elif isinstance(value, list):

                data[key] = [
                    item.model_dump()
                    if hasattr(item, "model_dump")
                    else item
                    for item in value
                ]

            else:

                data[key] = value

        serialized_results.append(data)

    return {
        "workflow_id": context.workflow_id,
        "status": "COMPLETED",
        "workflow": context.memory.get(
            "workflow",
        ),
        "results": serialized_results,
    }