
from app.mcp.server.tools.filesystem.read_file import register_read_file
from app.mcp.server.tools.github.create_issue import register_create_issue
from app.mcp.server.tools.planning.create_sprint_plan import (
    register_create_sprint_plan,
)


def register_tools(
    mcp,
):

    register_read_file(
        mcp,
    )

    register_create_issue(
        mcp,
    )

    register_create_sprint_plan(
        mcp,
    )