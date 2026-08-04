from app.runtime.agent_runtime import AgentRuntime
from app.tools.registry import Registry

#
# Local Tools
#
from app.tools.filesystem.read_file import ReadFileTool
from app.tools.github.create_issue import CreateGitHubIssueTool


#
# Registry
#
registry = Registry()

registry.register(
    ReadFileTool(),
)

registry.register(
    CreateGitHubIssueTool(),
)


#
# Agent Runtime
#
agent_runtime = AgentRuntime(
    registry=registry,
)

registry.register(
    ReadFileTool(),
)

registry.register(
    CreateGitHubIssueTool(),
)