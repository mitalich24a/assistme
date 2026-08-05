from mcp import StdioServerParameters


SERVERS = {

    "assistme": StdioServerParameters(
        command="python",
        args=[
            "-m",
            "app.mcp.server.server",
        ],
    ),

    "filesystem": StdioServerParameters(
        command="npx",
        args=[
            "-y",
            "@modelcontextprotocol/server-filesystem",
            ".",
        ],
    ),

}