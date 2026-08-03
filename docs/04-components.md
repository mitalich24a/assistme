# Components

## 1. FastAPI Host

### Purpose

Entry point for all client requests.

### Responsibilities

- Expose REST APIs
- Validate requests
- Invoke workflows
- Return responses
- Expose Swagger documentation

### Depends On

- Workflow Controller

---

## 2. Workflow Controller

### Purpose

Entry point for all workflow executions.

### Responsibilities

- Select workflow
- Initialize execution
- Start AgentSaga Runtime
- Return workflow ID
- Resume existing workflows

### Depends On

- Coordinator Agent
- AgentSaga Runtime

---

## 3. Coordinator Agent

### Purpose

Coordinate execution of a workflow.

### Responsibilities

- Understand workflow objective
- Select participating agents
- Delegate tasks
- Aggregate results
- Determine workflow completion

### Depends On

- Planner Agent
- Agent Registry

---

## 4. Planner Agent

### Purpose

Convert high-level goals into executable tasks.

### Responsibilities

- Analyze objective
- Generate execution plan
- Identify dependencies
- Determine execution order

### Depends On

- LLM Provider

---

## 5. Worker Agents

### Purpose

Execute specialized tasks.

### Examples

- Document Agent
- Estimation Agent
- GitHub Agent
- Publisher Agent

### Responsibilities

- Execute assigned task
- Call MCP tools
- Return results

### Depends On

- MCP Client
- LLM Provider

---

## 6. LLM Provider

### Purpose

Provide reasoning capabilities.

### Responsibilities

- Task planning
- Summarization
- Decision making
- Structured output generation

### Supported Providers

- OpenAI
- Anthropic
- Google Gemini
- Ollama (future)

---

## 7. AgentSaga Runtime

### Purpose

Execute workflows reliably.

### Responsibilities

- Execute workflow steps
- Checkpoint execution
- Retry failed steps
- Resume interrupted workflows
- Prevent duplicate execution

### Depends On

- Checkpoint Store
- Workflow Store

---

## 8. Checkpoint Store

### Purpose

Persist workflow execution state.

### Stores

- Workflow ID
- Current Step
- Completed Steps
- Failed Steps
- Retry Count
- Execution Status

---

## 9. Memory Store

### Purpose

Maintain workflow and conversational context.

### Stores

- User context
- Conversation history
- Agent outputs
- Workflow context

---

## 10. Agent Registry

### Purpose

Maintain available agents.

### Responsibilities

- Register agents
- Discover agents
- Lookup agent capabilities

---

## 11. Tool Registry

### Purpose

Maintain available tools.

### Responsibilities

- Register MCP tools
- Discover tools
- Resolve tool by capability

---

## 12. MCP Client

### Purpose

Communicate with external MCP servers.

### Responsibilities

- Discover tools
- Invoke tools
- Handle tool responses
- Handle tool failures

---

## 13. Document Provider

### Purpose

Load design documents from different sources.

### Supported Sources

- PDF
- DOCX
- Markdown
- Plain Text

### Future Sources

- Google Drive
- OneDrive
- GitHub
- Confluence

---

## 14. Observability

### Purpose

Provide execution visibility.

### Responsibilities

- Execution logs
- Agent traces
- Tool traces
- Workflow timeline
- Error reporting