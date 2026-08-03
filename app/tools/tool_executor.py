from mcp import ClientSession
from mcp import StdioServerParameters
from mcp import stdio_client


class ToolExecutor:
    """
    Executes tools through MCP.
    """

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

                return await session.list_tools()