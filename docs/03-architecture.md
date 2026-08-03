# Architecture

## High-Level Architecture

AssistMe follows a modular, layered architecture where each component has a single responsibility.

The platform consists of:

- FastAPI Host
- Workflow Controller
- Coordinator Agent
- Planner Agent
- Worker Agents
- AgentSaga Runtime
- MCP Client
- External MCP Servers
- Memory Store
- Checkpoint Store

---

## Architecture Diagram

```text
                        User
                          │
                          ▼
                  FastAPI Host
                          │
                          ▼
                Workflow Controller
                          │
                          ▼
                 Coordinator Agent
                          │
                   Creates Execution Plan
                          │
                          ▼
                    Planner Agent
                          │
                 Generates Task Graph
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
     Worker Agent                    Worker Agent
          │                               │
          └───────────────┬───────────────┘
                          ▼
                  AgentSaga Runtime
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
   Checkpoint Store   Memory Store    Retry Engine
                          │
                          ▼
                     MCP Client
                          │
         ┌────────────────┼────────────────┐
         ▼                ▼                ▼
      GitHub          File System      Future Tools
```

---

# Architecture Layers

## Presentation Layer

Responsible for:

- REST APIs
- Swagger UI
- Request Validation
- Response Serialization

Technology

- FastAPI

---

## Orchestration Layer

Responsible for:

- Understanding user intent
- Selecting workflows
- Coordinating agents

Components

- Workflow Controller (workflow lifecycle)
- Coordinator Agent (agent orchestration)

---

## Planning Layer

Responsible for:

- Breaking goals into executable tasks
- Building dependency graphs

Components

- Planner Agent

---

## Execution Layer

Responsible for:

- Executing workflows
- Checkpointing
- Retry
- Resume
- Idempotency

Components

- AgentSaga Runtime

---

## Agent Layer

Responsible for:

- Performing specialized work

Examples

- GitHub Agent
- Document Agent
- Estimation Agent
- Publishing Agent

---

## Integration Layer

Responsible for:

- Tool discovery
- Tool execution
- Communication with external systems

Components

- MCP Client

---

## External Systems

Examples

- GitHub
- Local Files
- Google Drive (future)
- OneDrive (future)

---

# Architectural Principles

- Modular Design
- Separation of Concerns
- Extensibility
- Fault Tolerance
- Durable Execution
- Asynchronous Processing
- Idempotent Operations