from fastapi import APIRouter

from app.tools.tool_executor import ToolExecutor

router = APIRouter()


@router.get("/mcp/tools")
async def list_tools():

    executor = ToolExecutor()

    tools = await executor.list_tools()

    return {
        "count": len(tools.tools),
        "tools": [
            {
                "name": tool.name,
                "description": tool.description,
            }
            for tool in tools.tools
        ],
    }