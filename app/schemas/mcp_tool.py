from pydantic import BaseModel, Field


class McpTool(BaseModel):
    """
    MCP Tool metadata.
    """

    name: str

    description: str = ""

    input_schema: dict = Field(
        default_factory=dict,
    )