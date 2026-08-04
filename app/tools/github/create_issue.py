from app.github.github_factory import GitHubFactory
from app.schemas.create_issue_request import CreateIssueRequest
from app.tools.base_tool import BaseTool


class CreateGitHubIssueTool(BaseTool):

    def __init__(self):

        self._github = GitHubFactory.create()

    @property
    def name(self) -> str:
        return "create_github_issue"

    @property
    def description(self) -> str:
        return (
            "Create a GitHub issue in the configured repository."
        )

    @property
    def input_schema(self) -> dict:

        return {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Issue title"
                },
                "body": {
                    "type": "string",
                    "description": "Issue description"
                }
            },
            "required": [
                "title",
                "body"
            ]
        }

    async def execute(
        self,
        arguments: dict,
    ):

        issue = CreateIssueRequest(
            title=arguments["title"],
            body=arguments["body"],
        )

        published_issue = await self._github.create_issue(
            issue,
        )

        return {
            "success": True,
            "issue_number": published_issue.issue_number,
            "title": published_issue.title,
            "url": published_issue.issue_url,
        }