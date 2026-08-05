# AssistMe

AssistMe is an extensible AI Agent Platform built with Python, FastAPI, Large Language Models (LLMs), and the Model Context Protocol (MCP).

The platform enables AI agents to autonomously understand user requests, discover available tools, invoke local and remote capabilities, and execute multi-step workflows.

It demonstrates how modern AI agents can be built using an LLM-driven reasoning loop, dynamic MCP tool discovery, and autonomous tool execution.

---

## Features

- LLM-driven AI Agent Runtime
- Model Context Protocol (MCP) Client
- Custom FastMCP Server
- Dynamic MCP Tool Discovery
- Autonomous Tool Execution
- GitHub Issue Automation
- Document Analysis
- Async FastAPI Backend
- Extensible Tool Architecture

---

## Architecture

```
                 +----------------------+
                 |      FastAPI API     |
                 +----------+-----------+
                            |
                            v
                 +----------------------+
                 |    Agent Runtime     |
                 +----------+-----------+
                            |
                +-----------+-----------+
                |                       |
                v                       v
          Ollama / Qwen            MCP Client
                                       |
                    +------------------+------------------+
                    |                                     |
                    v                                     v
          Filesystem MCP Server              AssistMe MCP Server
                                                     |
                            +------------------------+------------------------+
                            |                         |                        |
                            v                         v                        v
                      Read File              Create Sprint Plan      Create GitHub Issue
```

---

## Components

### Agent Runtime

The Agent Runtime orchestrates the complete reasoning workflow by:

- Managing conversation history
- Connecting to multiple MCP servers
- Discovering available tools dynamically
- Executing tool calls requested by the LLM
- Feeding tool results back to the LLM
- Returning the final response

---

### MCP Client

The MCP Client is responsible for:

- Connecting to multiple MCP servers
- Managing MCP sessions
- Discovering available tools
- Routing tool execution to the appropriate MCP server

---

### MCP Server

The custom FastMCP server exposes reusable AI tools.

Current tools include:

- Read File
- Create Sprint Plan
- Create GitHub Issue

New tools can be added without modifying the Agent Runtime.

---

### GitHub Integration

Current capabilities:

- Create GitHub Issues

Planned capabilities:

- List Issues
- Update Issues
- Close Issues
- Pull Request Automation

---

### Document Processing

Supported document formats:

- Markdown
- Text
- PDF
- DOCX

---

## Example Workflow

```
User Prompt
      |
      v
Read README.md and create GitHub issues
      |
      v
Agent Runtime
      |
      v
read_file()
      |
      v
LLM analyzes project requirements
      |
      v
create_sprint_plan()
      |
      v
create_github_issue()
      |
      v
GitHub Repository
```

---

## Tech Stack

- Python 3.10+
- FastAPI
- FastMCP
- Ollama
- Qwen3
- MCP Python SDK
- Pydantic
- HTTPX
- AsyncIO

---

## Current Capabilities

- Read project documentation
- Analyze software requirements
- Generate engineering task plans
- Create GitHub issues automatically
- Discover MCP tools dynamically
- Execute multi-step AI workflows

---

## Roadmap

- Conversation Memory
- Retrieval-Augmented Generation (RAG)
- HTTP/SSE MCP Transport
- Multi-Agent Collaboration
- GitHub Pull Request Automation
- Jira Integration
- Slack Integration
- Vector Database Support
- Authentication & Authorization
- Plugin Marketplace

---

## Project Structure

```
app/
├── api/                # FastAPI endpoints
├── bootstrap/          # Startup and dependency management
├── config/             # Configuration and settings
├── core/               # Core interfaces and dependencies
├── document/           # Document readers and processing
├── exceptions/         # Custom exceptions
├── github/             # GitHub REST integration
├── llm/                # LLM providers
├── mcp/
│   ├── client/         # MCP client
│   ├── server/         # FastMCP server
│   └── mcp_session.py
├── prompts/            # System prompts
├── runtime/            # AI Agent Runtime
├── schemas/            # Pydantic models
└── utils/              # Utility functions
```

