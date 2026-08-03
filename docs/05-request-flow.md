# Request Flow

## Sprint Planning Workflow

### Step 1 - Receive Request

The client uploads a design document (PDF, DOCX, Markdown, or plain text) through the FastAPI REST API.

↓

### Step 2 - Workflow Initialization

The Workflow Controller:

- Validates the request
- Creates a Workflow ID
- Initializes the workflow
- Starts the AgentSaga Runtime

↓

### Step 3 - Planning

The Coordinator Agent:

- Identifies the workflow
- Selects participating agents
- Delegates planning to the Planner Agent

↓

### Step 4 - Execution Plan

The Planner Agent:

- Reads the design document
- Breaks it into engineering tasks
- Estimates story points
- Identifies task dependencies
- Produces an execution plan

↓

### Step 5 - Task Execution

Worker Agents execute their assigned tasks.

Examples:

- Document Agent
- Estimation Agent
- GitHub Agent
- Publisher Agent

↓

### Step 6 - Tool Execution

Worker agents invoke external tools through the MCP Client.

Examples:

- GitHub
- File System
- Future integrations

↓

### Step 7 - Checkpoint

After every completed step, AgentSaga:

- Saves workflow state
- Records completed tasks
- Persists execution progress

↓

### Step 8 - Recovery

If execution fails:

- Reload workflow state
- Resume from the last checkpoint
- Continue remaining tasks
- Prevent duplicate execution

↓

### Step 9 - Completion

Workflow status is updated to Completed and returned to the client.