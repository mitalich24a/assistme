from app.schemas.planning_result import PlanningResult


class PlanningMerger:
    """
    Merges partial PlanningResults produced by worker agents.
    """

    @staticmethod
    def merge(
        story_plan: PlanningResult,
        dependency_plan: PlanningResult,
    ) -> PlanningResult:

        dependency_lookup = {
            task.name: task
            for task in dependency_plan.tasks
        }

        for task in story_plan.tasks:

            dependency_task = dependency_lookup.get(
                task.name,
            )

            if dependency_task is not None:
                task.depends_on = dependency_task.depends_on

        return story_plan