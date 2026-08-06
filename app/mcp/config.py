from enum import Enum

from pydantic import BaseModel


class McpTransport(str, Enum):

    STDIO = "stdio"

    HTTP = "http"


class McpServerConfig(BaseModel):

    name: str

    transport: McpTransport = McpTransport.STDIO

    command: list[str] | None = None

    url: str | None = None


SERVERS = [
    McpServerConfig(
        name="assistme",
        transport=McpTransport.STDIO,
        command=[
            "python",
            "-m",
            "app.mcp.server.server",
        ],
    ),
    McpServerConfig(
        name="filesystem",
        transport=McpTransport.STDIO,
        command=[
            "npx",
            "-y",
            "@modelcontextprotocol/server-filesystem",
            ".",
        ],
    ),
]