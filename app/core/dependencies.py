from app.coordinator.coordinator_agent import CoordinatorAgent
from app.llm.factory import LLMFactory
from app.planner.planner_agent import PlannerAgent
from app.registry.agent_registry import AgentRegistry
from app.execution.runtime.runtime_executor import RuntimeExecutor


# LLM
llm_provider = LLMFactory.create()

# Agents
planner_agent = PlannerAgent(
    llm_provider=llm_provider,
)

# Registry
agent_registry = AgentRegistry()
agent_registry.register(planner_agent)

# Coordinator
coordinator = CoordinatorAgent(
    registry=agent_registry,
)

# Runtime
runtime_executor = RuntimeExecutor(
    coordinator=coordinator,
)