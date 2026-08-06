import sys
from enum import Enum

from pydantic import BaseModel

from app.config.settings import settings


class McpTransport(str, Enum):

    STDIO = "stdio"

    HTTP = "http"


class McpServerConfig(BaseModel):

    name: str

    transport: McpTransport

    command: list[str] | None = None

    url: str | None = None


if settings.mcp_transport == "stdio":

    assistme = McpServerConfig(
        name="assistme",
        transport=McpTransport.STDIO,
        command=[
            sys.executable,
            "-m",
            "app.mcp.server.server",
        ],
    )

elif settings.mcp_transport == "http":

    assistme = McpServerConfig(
        name="assistme",
        transport=McpTransport.HTTP,
        url=f"http://{settings.mcp_host}:{settings.mcp_port}/mcp",
    )

else:

    raise ValueError(
        f"Unsupported MCP transport: {settings.mcp_transport}"
    )


SERVERS = [

    assistme,

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