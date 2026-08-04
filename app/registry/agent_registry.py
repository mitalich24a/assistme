from app.core.interfaces.base_agent import BaseAgent


class AgentRegistry:

    def __init__(self):

        self._agents: list[BaseAgent] = []

    def register(
        self,
        agent: BaseAgent,
    ) -> None:

        self._agents.append(agent)

    def get(
        self,
        capability: str,
    ) -> BaseAgent | None:

        for agent in self._agents:

            if capability in agent.capabilities:
                return agent

        return None

    def all(
        self,
    ) -> list[BaseAgent]:

        return self._agents