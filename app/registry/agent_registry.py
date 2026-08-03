from app.core.interfaces.base_agent import BaseAgent


class AgentRegistry:
    """
    Registry for all available agents.
    """

    def __init__(self) -> None:
        self._agents: dict[str, BaseAgent] = {}

    def register(
        self,
        agent: BaseAgent,
    ) -> None:
        """
        Register an agent.
        """
        self._agents[agent.name] = agent

    def get(
        self,
        name: str,
    ) -> BaseAgent:
        """
        Get an agent by its unique name.
        """
        if name not in self._agents:
            raise ValueError(
                f"Agent '{name}' is not registered."
            )

        return self._agents[name]

    def find(
        self,
        capability: str,
    ) -> BaseAgent:
        """
        Find the first agent supporting the given capability.
        """
        for agent in self._agents.values():
            if capability in agent.capabilities:
                return agent

        raise ValueError(
            f"No agent found for capability '{capability}'."
        )

    def all(
        self,
    ) -> list[BaseAgent]:
        """
        Return all registered agents.
        """
        return list(self._agents.values())