from fastapi import APIRouter

from app.services.mcp_service import McpService

router = APIRouter()

service = McpService()


@router.get("/tools")
async def list_tools():

    async with service.create_session() as session:
        return await session.list_tools()