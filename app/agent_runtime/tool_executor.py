from app.services.mcp_service import McpService


class ToolExecutor:
    """
    Executes tools requested by the LLM.
    """

    def __init__(self):

        self._mcp = McpService()

    async def execute(
        self,
        tool_name: str,
        arguments: dict,
    ):

        #
        # Version 1
        # Support one MCP tool.
        #

        if tool_name == "read_text_file":

            return await self._mcp.read_file(
                arguments["path"]
            )

        raise ValueError(
            f"Unsupported tool: {tool_name}"
        )