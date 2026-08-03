from app.github.github_factory import GitHubFactory
from app.schemas.create_issue_request import CreateIssueRequest
from app.schemas.planning_result import PlanningResult
from app.schemas.publish_result import PublishResult


class GitHubPublishingService:
    """
    Publishes a PlanningResult to GitHub.
    """

    def __init__(self) -> None:
        self._github = GitHubFactory.create()

    async def publish(
        self,
        planning: PlanningResult,
    ) -> PublishResult:

        result = PublishResult(
            repository="",
            issues=[],
        )

        for task in planning.tasks:

            issue = await self._github.create_issue(
                CreateIssueRequest(
                    title=task.name,
                    body=f"""
## Description

{task.description}

## Story Points

{task.story_points}

## Depends On

{", ".join(task.depends_on) if task.depends_on else "None"}
""".strip(),
                )
            )

            result.issues.append(issue)

        return result