from fastmcp import FastMCP
from app.core.logging import configure_logging

configure_logging()

from app.mcp.server.registry import register_tools


mcp = FastMCP("AssistMe")

register_tools(mcp)


if __name__ == "__main__":
    mcp.run()