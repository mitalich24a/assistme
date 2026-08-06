import json

from mcp import ClientSession
from mcp import StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.client.streamable_http import streamable_http_client

from app.mcp.config import McpTransport
from app.schemas.mcp_tool import McpTool
from app.schemas.mcp_tool_result import McpToolResult


class Session:

    def __init__(
        self,
        name: str,
        server,
    ):

        self._name = name
        self._server = server

        self._client = None
        self._session = None
        self._read_stream = None
        self._write_stream = None

    @property
    def name(self):

        return self._name

    async def __aenter__(self):

        if self._server.transport == McpTransport.STDIO:

            server = StdioServerParameters(
                command=self._server.command[0],
                args=self._server.command[1:],
            )

            self._client = stdio_client(
                server,
            )

        elif self._server.transport == McpTransport.HTTP:

            self._client = streamable_http_client(
                self._server.url,
            )

        else:

            raise ValueError(
                f"Unsupported transport: {self._server.transport}"
            )

        streams = await self._client.__aenter__()

        self._read_stream = streams[0]
        self._write_stream = streams[1]

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

    async def list_tools(
        self,
    ) -> McpToolResult:

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

    async def list_ollama_tools(
        self,
    ) -> list[dict]:

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
        arguments,
    ):

        print("\n" + "=" * 80)
        print("MCP CALL TOOL")
        print("=" * 80)
        print("Tool:", tool_name)
        print("Arguments:", arguments)
        print("Arguments Type:", type(arguments))

        if isinstance(arguments, str):

            print("Parsing JSON string arguments...")

            arguments = json.loads(
                arguments,
            )

        print("Arguments After Parsing:", arguments)

        result = await self._session.call_tool(
            tool_name,
            arguments,
        )

        print("MCP Tool Success")

        return result