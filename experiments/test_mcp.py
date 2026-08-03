import asyncio

from mcp import ClientSession
from mcp import StdioServerParameters
from mcp import stdio_client


async def main():

    server = StdioServerParameters(
        command="npx",
        args=[
            "-y",
            "@modelcontextprotocol/server-filesystem",
            ".",
        ],
    )

    async with stdio_client(server) as streams:

        read_stream, write_stream = streams

        async with ClientSession(
            read_stream,
            write_stream,
        ) as session:

            await session.initialize()

            tools = await session.list_tools()

            print(tools)


asyncio.run(main())