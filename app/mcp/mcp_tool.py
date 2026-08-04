from pydantic import BaseModel


class McpTool(BaseModel):
    """
    Generic MCP Tool exposed by an MCP server.
    """

    name: str

    description: str = ""

    input_schema: dict