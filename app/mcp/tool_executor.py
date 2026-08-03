from app.mcp.client import McpClient
from app.mcp.models import McpToolResult


class ToolExecutor:
    """
    Executes MCP tools.
    """

    def __init__(
        self,
        client: McpClient,
    ) -> None:
        self._client = client

    async def execute(
        self,
        tool_name: str,
        arguments: dict,
    ) -> McpToolResult:

        return await self._client.call_tool(
            tool_name=tool_name,
            arguments=arguments,
        )