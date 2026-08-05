from mcp import ClientSession
from mcp import StdioServerParameters
from mcp import stdio_client

from app.schemas.mcp_tool import McpTool
from app.schemas.mcp_tool_result import McpToolResult


class McpSession:

    def __init__(
        self,
        server: StdioServerParameters,
    ):

        self._server = server

        self._client = None
        self._session = None
        self._read_stream = None
        self._write_stream = None

    async def __aenter__(self):

        self._client = stdio_client(
            self._server,
        )

        streams = await self._client.__aenter__()

        self._read_stream, self._write_stream = streams

        self._session = ClientSession(
            self._read_stream,
            self._write_stream,
        )

        await self._session.__aenter__()

        await self._session.initialize()

        return self

    async def __aexit__(
        self,
        exc_type,
        exc_val,
        exc_tb,
    ):

        if self._session:
            await self._session.__aexit__(
                exc_type,
                exc_val,
                exc_tb,
            )

        if self._client:
            await self._client.__aexit__(
                exc_type,
                exc_val,
                exc_tb,
            )

    async def list_tools(self) -> McpToolResult:

        response = await self._session.list_tools()

        tools = []

        for tool in response.tools:

            input_schema = getattr(
                tool,
                "inputSchema",
                None,
            )

            if input_schema is None:
                input_schema = getattr(
                    tool,
                    "input_schema",
                    {},
                )

            tools.append(
                McpTool(
                    name=tool.name,
                    description=tool.description or "",
                    input_schema=input_schema,
                )
            )

        return McpToolResult(
            tools=tools,
        )

    async def list_ollama_tools(self) -> list[dict]:

        result = await self.list_tools()

        return [
            {
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.input_schema,
                },
            }
            for tool in result.tools
        ]

    async def call_tool(
        self,
        tool_name: str,
        arguments: dict,
    ):

        result = await self._session.call_tool(
            tool_name,
            arguments,
        )

        return result