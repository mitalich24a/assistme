from app.agents.planner_agent import PlannerAgent
from app.agents.publisher_agent import PublisherAgent
from app.coordinator.coordinator_agent import CoordinatorAgent
from app.execution.runtime.runtime_executor import RuntimeExecutor
from app.llm.factory import LLMFactory
from app.publishing.publishing_service import PublishingService
from app.registry.agent_registry import AgentRegistry

#
# Providers
#
llm_provider = LLMFactory.create()

publishing_service = PublishingService.create()

#
# Agents
#
planner_agent = PlannerAgent(
    llm_provider=llm_provider,
)

publisher_agent = PublisherAgent(
    publishing_service=publishing_service,
)

#
# Registry
#
agent_registry = AgentRegistry()

agent_registry.register(
    planner_agent,
)

agent_registry.register(
    publisher_agent,
)

#
# Coordinator
#
coordinator = CoordinatorAgent(
    registry=agent_registry,
)

#
# Runtime
#
runtime_executor = RuntimeExecutor(
    coordinator=coordinator,
)