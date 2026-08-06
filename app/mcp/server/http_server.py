from fastmcp import FastMCP

from app.config.settings import settings
from app.mcp.server.registry import register_tools


mcp = FastMCP("AssistMe")

register_tools(mcp)

mcp.run(
    transport="streamable-http",
    host=settings.mcp_host,
    port=settings.mcp_port,
)