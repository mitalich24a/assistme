from mcp import StdioServerParameters

from app.mcp.mcp_session import McpSession


class McpService:

    def __init__(self):

        self._server = StdioServerParameters(
            command="npx",
            args=[
                "-y",
                "@modelcontextprotocol/server-filesystem",
                ".",
            ],
        )

    def create_session(self) -> McpSession:

        return McpSession(self._server)