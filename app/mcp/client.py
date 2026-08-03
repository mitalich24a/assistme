from app.mcp.session import McpSession
from app.mcp.models import McpToolResult


class McpClient:
    """
    Generic MCP client.

    This class will later use the official MCP SDK
    to communicate with any MCP server.
    """

    def __init__(self) -> None:
        self._session = McpSession()

    async def connect(self) -> None:
        await self._session.connect()

    async def disconnect(self) -> None:
        await self._session.disconnect()

    async def call_tool(
        self,
        tool_name: str,
        arguments: dict,
    ) -> McpToolResult:

        raise NotImplementedError(
            "Real MCP implementation coming next."
        )