from app.mcp.mcp_session import McpSession
from app.tools.registry import Registry


class HybridExecutor:

    def __init__(
        self,
        registry: Registry,
    ):

        self._registry = registry

    async def execute(
        self,
        session: McpSession,
        tool_name: str,
        arguments: dict,
    ):

        #
        # Local Tool
        #
        if self._registry.has(tool_name):

            tool = self._registry.get(tool_name)

            return await tool.execute(
                arguments,
            )

        #
        # MCP Tool
        #
        return await session.call_tool(
            tool_name,
            arguments,
        )