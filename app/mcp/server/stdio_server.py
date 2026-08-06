from fastmcp import FastMCP

from app.mcp.server.registry import register_tools


mcp = FastMCP("AssistMe")

register_tools(mcp)

mcp.run(
    transport="stdio",
)