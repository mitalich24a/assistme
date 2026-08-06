from app.config.settings import settings

from fastmcp import FastMCP
from app.mcp.server.registry import register_tools

mcp = FastMCP("AssistMe")

register_tools(mcp)

if settings.mcp_transport == "stdio":

    mcp.run(
        transport="stdio",
    )

elif settings.mcp_transport == "http":

    mcp.run(
        transport="streamable-http",
        host=settings.mcp_host,
        port=settings.mcp_port,
    )