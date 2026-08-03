# Project Conventions

## Design Principles

- Single Responsibility Principle (SRP)
- Dependency Inversion Principle (DIP)
- Composition over Inheritance
- Interface-driven Design
- Asynchronous by Default
- Fail Fast
- Idempotent Operations

---

## Naming Conventions

Classes

- WorkflowController
- CoordinatorAgent
- PlannerAgent
- GitHubAgent

Interfaces

- BaseWorkflow
- BaseAgent
- BaseTool
- BaseMemoryProvider
- BaseLLMProvider

Files

snake_case.py

Examples

workflow_controller.py
planner_agent.py

---

## Folder Ownership

api/
    REST endpoints

workflows/
    Workflow implementations

execution/
    AgentSaga runtime

agents/
    AI agents

mcp/
    MCP client

memory/
    Memory providers

registry/
    Agent & Tool registry

llm/
    LLM abstraction

core/
    Common utilities

---

## Logging

Every workflow must log:

- Workflow ID
- Agent
- Step
- Duration
- Status
- Errors

---

## Error Handling

Create custom exceptions.

Examples

WorkflowException

AgentException

ToolException

CheckpointException

LLMException

---

## Response Format

Every API returns

{
    "workflow_id": "...",
    "status": "...",
    "data": {},
    "error": null
}

---

## Dependency Injection

Never instantiate dependencies directly.

Good

Coordinator(
    planner=planner,
    registry=registry
)

Bad

Coordinator()

inside creating Planner()

---

## Async First

All agents should expose async methods.

async execute()

async plan()

async validate()

---

## Testing

Every component should be independently testable.

Avoid hidden global state.