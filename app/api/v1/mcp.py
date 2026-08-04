from fastapi import APIRouter

from app.constants.capabilities import Capabilities
from app.core.dependencies import coordinator
from app.execution.workflow_context import WorkflowContext
from app.schemas.read_file_request import ReadFileRequest

router = APIRouter()


@router.get("/mcp/tools")
async def list_tools():

    context = WorkflowContext(
        workflow_id="mcp",
        workflow_name="MCP",
        input_data={},
    )

    result = await coordinator.execute(
        context=context,
        capability=Capabilities.MCP,
    )

    return result.data["mcp"].model_dump()


@router.post("/mcp/read-file")
async def read_file(
    request: ReadFileRequest,
):

    context = WorkflowContext(
        workflow_id="mcp",
        workflow_name="MCP",
        input_data={},
    )

    result = await coordinator.execute(
        context=context,
        capability=Capabilities.MCP,
        path=request.path,
    )

    return result.data