from mcp import ClientSession
from mcp import StdioServerParameters
from mcp import stdio_client

from app.schemas.mcp_tool import McpTool
from app.schemas.mcp_tool_result import McpToolResult


class McpService:

    def __init__(self):

        self.server = StdioServerParameters(
            command="npx",
            args=[
                "-y",
                "@modelcontextprotocol/server-filesystem",
                ".",
            ],
        )

    async def list_tools(self):

        async with stdio_client(self.server) as streams:

            read_stream, write_stream = streams

            async with ClientSession(
                read_stream,
                write_stream,
            ) as session:

                await session.initialize()

                response = await session.list_tools()

                return McpToolResult(
                    tools=[
                        McpTool(
                            name=tool.name,
                            description=tool.description,
                        )
                        for tool in response.tools
                    ]
                )

    async def read_file(
        self,
        path: str,
    ):

        async with stdio_client(self.server) as streams:

            read_stream, write_stream = streams

            async with ClientSession(
                read_stream,
                write_stream,
            ) as session:

                await session.initialize()

                return await session.call_tool(
                    "read_text_file",
                    {
                        "path": path,
                    },
                )