from pydantic import BaseModel, Field

from app.schemas.mcp_tool import McpTool


class McpToolResult(BaseModel):
    tools: list[McpTool] = Field(default_factory=list)