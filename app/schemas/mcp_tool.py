from pydantic import BaseModel


class McpTool(BaseModel):
    name: str
    description: str