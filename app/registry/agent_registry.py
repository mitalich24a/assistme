from app.core.interfaces.base_agent import BaseAgent


class AgentRegistry:

    def __init__(self) -> None:
        self._agents: dict[str, BaseAgent] = {}

    def register(
        self,
        agent: BaseAgent,
    ) -> None:
        self._agents[agent.name] = agent

    def get(
        self,
        name: str,
    ) -> BaseAgent:
        return self._agents[name]

    def find(
        self,
        capability: str,
    ) -> BaseAgent:

        for agent in self._agents.values():

            if capability in agent.capabilities:
                return agent

        raise ValueError(
            f"No agent found for capability '{capability}'."
        )

    def all(self) -> list[BaseAgent]:
        return list(self._agents.values())