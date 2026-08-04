# AssistMe

> AI Agent Framework powered by LLMs, MCP (Model Context Protocol), and Tool Calling.

AssistMe is a modular AI agent platform built with **Python**, **FastAPI**, **Ollama**, and **MCP**. It enables Large Language Models to autonomously solve user requests by dynamically discovering and invoking both **local tools** and **MCP server tools**.

Instead of hardcoding workflows, the LLM acts as the reasoning engine while tools provide external capabilities such as file access, GitHub automation, document parsing, and more.

---

# Features

- AI Agent Runtime
- MCP Integration
- Local Tool Registry
- Hybrid Tool Execution
- Ollama / Qwen Support
- GitHub Integration
- Document Processing
- Extensible Plugin Architecture
- Async FastAPI Backend

---

# Architecture

```
                    User
                      │
                      ▼
                Agent Runtime
                      │
                      ▼
              Ollama (Qwen)
                      │
              Tool Calling Loop
                      │
         ┌────────────┴────────────┐
         ▼                         ▼
   Local Tool Registry        MCP Servers
         │                         │
         ▼                         ▼
    Read File               GitHub MCP
    Read PDF                Filesystem MCP
    Read DOCX               Future MCP Servers
         │
         └────────────┬────────────┘
                      ▼
                Tool Results
                      │
                      ▼
                   Ollama
```

---

# Project Structure

```
app/
│
├── api/
├── bootstrap/
├── config/
├── core/
├── document/
├── exceptions/
├── github/
├── llm/
├── mcp/
├── memory/
├── runtime/
├── tools/
├── services/
├── prompts/
├── publishing/
├── schemas/
└── utils/
```

---

# Core Components

## Agent Runtime

The Agent Runtime manages the complete reasoning loop.

Responsibilities:

- Maintains conversation history
- Opens MCP sessions
- Discovers available tools
- Sends tool definitions to the LLM
- Executes requested tools
- Returns tool results back to the LLM
- Continues until a final response is generated

---

## Local Tools

Local tools provide capabilities implemented inside AssistMe.

Examples:

- Read File
- Read PDF
- Read DOCX
- Create GitHub Issue
- List GitHub Issues

Adding a new capability only requires implementing `BaseTool` and registering it.

---

## MCP Integration

AssistMe supports Model Context Protocol (MCP).

During execution it automatically discovers tools exposed by connected MCP servers.

Examples:

- Filesystem
- GitHub
- Future integrations (Jira, Slack, Browser, etc.)

---

## Hybrid Tool Execution

When the LLM requests a tool:

- Local tools execute inside AssistMe.
- MCP tools execute through an MCP server.

The LLM does not need to know where a tool is implemented.

---

## LLM Provider

Current provider:

- Ollama
- Qwen3

The provider is isolated behind an abstraction layer, allowing future support for OpenAI, Anthropic, Gemini, and other models.

---

# Example

User prompt:

```
Read requirements.md and create GitHub Issues.
```

Execution:

```
User
    │
    ▼
LLM
    │
    ▼
read_file()
    │
    ▼
LLM
    │
    ▼
create_github_issue()
    │
    ▼
Done
```

No predefined workflow is required—the LLM determines which tools to invoke.

---

# Technology Stack

- Python 3.10+
- FastAPI
- AsyncIO
- Ollama
- Qwen3
- MCP (Model Context Protocol)
- Pydantic
- HTTPX

---

# Getting Started

Clone the repository:

```bash
git clone <repo-url>
cd assistme
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure environment variables:

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=qwen3:8b

GITHUB_OWNER=<owner>
GITHUB_REPO=<repo>
GITHUB_TOKEN=<token>
```

Run the application:

```bash
python run.py
```

Open Swagger:

```
http://localhost:8000/docs
```

