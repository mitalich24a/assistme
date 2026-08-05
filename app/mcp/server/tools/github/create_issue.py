import logging


from app.github.github_rest_client import GitHubRestClient
from app.schemas.create_issue_request import (
    CreateIssueRequest,
)

logger = logging.getLogger(__name__)


def register_create_issue(
    mcp,
):

    @mcp.tool()
    async def create_github_issue(
        title: str,
        body: str,
    ) -> dict:
        """
        Create a GitHub issue in the configured repository.

        Use this tool whenever the user asks to:
        - create GitHub issues
        - publish tasks to GitHub
        - create issues from a README
        - convert engineering tasks into GitHub issues
        """

        logger.info("create_github_issue invoked")
        logger.info("Title: %s", title)

        client = GitHubRestClient()

        result = await client.create_issue(
            CreateIssueRequest(
                title=title,
                body=body,
            )
        )

        logger.info(
            "Created Issue #%s",
            result.issue_number,
        )

        return {
            "title": result.title,
            "issue_number": result.issue_number,
            "issue_url": result.issue_url,
        }