# 🚀 AssistMe – Multi-Agent AI Workflow Platform

> An extensible multi-agent orchestration platform that converts software design documents into executable engineering plans using specialized AI agents, durable workflow execution, MCP integration, and automated GitHub publishing.

---

# Architecture

```
                        +----------------------+
                        |      FastAPI API     |
                        +----------+-----------+
                                   |
                                   v
                     +---------------------------+
                     |      Workflow Engine       |
                     +---------------------------+
                                   |
                    Runtime Executor (Retry + Resume)
                                   |
                                   v
                     +---------------------------+
                     |     Coordinator Agent      |
                     +---------------------------+
                                   |
                    Capability Based Routing
                                   |
      -------------------------------------------------------------
      |                         |                                |
      v                         v                                v
 Planner Agent           Publisher Agent                 Future Agents
      |
      |
      +------------------------------------------------------+
      |                                                      |
      v                                                      |
+-------------+                                              |
| Task Worker |                                              |
+-------------+                                              |
      |                                                      |
      v                                                      |
+-------------+                                              |
| Story Point |                                              |
+-------------+                                              |
      |                                                      |
      v                                                      |
+-------------+                                              |
| Dependency  |                                              |
+-------------+                                              |
      |                                                      |
      v                                                      |
+-------------+                                              |
| Review      |                                              |
+-------------+                                              |
      |                                                      |
      +------------------------------------------------------+
                                   |
                                   v
                         Workflow Memory
                                   |
                                   v
                       GitHub Publishing Service
                                   |
                                   v
                            GitHub Issues
```

---

# Features

## AI Multi-Agent System

- Coordinator Agent
- Planner Agent
- Publisher Agent
- Specialized Worker Agents
    - Task Generator
    - Story Point Estimator
    - Dependency Analyzer
    - Review Agent

---

## Workflow Engine

- Durable Workflow Execution
- Retry Executor
- Checkpointing
- Resume after failure
- Workflow Context
- Shared Workflow Memory

---

## LLM

- Ollama Integration
- Provider abstraction
- Async support
- Structured JSON generation

---

## MCP

- Model Context Protocol
- Persistent MCP Sessions
- Tool Discovery
- Tool Invocation
- Filesystem MCP
- Extensible for GitHub MCP

---

## Publishing

Automatically creates GitHub Issues from generated sprint plans.

Each issue contains

- Description
- Story Points
- Dependencies

---

## Extensible Provider Model

Current Providers

- Ollama
- GitHub REST

Future Providers

- OpenAI
- Claude
- GitHub MCP
- Jira
- Azure DevOps

---

# Project Structure

```
app/
│
├── agents/
│   ├── coordinator
│   ├── planner
│   ├── publisher
│   └── workers/
│
├── api/
│
├── checkpoint/
│
├── coordinator/
│
├── execution/
│
├── github/
│
├── llm/
│
├── mcp/
│
├── prompts/
│
├── publishing/
│
├── runtime/
│
├── schemas/
│
└── services/
```

---

# Workflow

```
Design Document

        │

        ▼

Task Generator

        │

        ▼

Story Point Agent

        │

        ▼

Dependency Agent

        │

        ▼

Review Agent

        │

        ▼

Planner Agent

        │

        ▼

Workflow Memory

        │

        ▼

Publisher Agent

        │

        ▼

GitHub Issues
```

---

# Tech Stack

Backend

- Python 3.10
- FastAPI
- AsyncIO
- Pydantic

AI

- Ollama
- Qwen3
- MCP

Infrastructure

- GitHub REST API
- HTTPX

Architecture

- Multi-Agent Systems
- Workflow Engine
- Durable Execution
- Capability Routing
- Shared Workflow Memory

---

# Example

Input

```
Build a customer support platform using FastAPI,
Redis,
PostgreSQL,
Kafka,
and MCP.
```

Generated Tasks

```
✅ Design REST APIs

✅ Build Planner Agent

✅ Integrate LLM

✅ Implement MCP Client

✅ Create Tool Registry

...

```

Automatically publishes

```
GitHub Issue #68

GitHub Issue #69

GitHub Issue #70

...
```

---

# Current Capabilities

| Feature | Status |
|----------|--------|
| FastAPI Platform | ✅ |
| Workflow Engine | ✅ |
| Runtime Executor | ✅ |
| Durable Execution | ✅ |
| Retry Executor | ✅ |
| Checkpointing | ✅ |
| Resume Execution | ✅ |
| Workflow Memory | ✅ |
| Agent Registry | ✅ |
| Coordinator Agent | ✅ |
| Planner Agent | ✅ |
| Publisher Agent | ✅ |
| Worker Agents | ✅ |
| LLM Integration | ✅ |
| MCP Integration | ✅ |
| Persistent MCP Sessions | ✅ |
| GitHub Publishing | ✅ |
| Capability Routing | ✅ |
| Multi-Agent Collaboration | ✅ |

---

# Roadmap

- Parallel Worker Execution
- Observability
- OpenTelemetry
- GitHub MCP Publishing
- Jira Publishing
- Slack Notifications
- Human Approval Workflow
- Dynamic Agent Planning

---

# Running

## Install

```bash
git clone https://github.com/<your-repo>

cd assistme

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

---

## Configure

```
OLLAMA_MODEL=qwen3:8b

GITHUB_OWNER=...

GITHUB_REPO=...

GITHUB_TOKEN=...
```

---

## Run

```
python run.py
```

---

## API

```
POST

/api/v1/workflows/sprint-planning
```

---

# Design Principles

- Single Responsibility
- Dependency Injection
- Provider Abstraction
- Capability Based Routing
- Durable Workflows
- Shared Agent Memory
- Retry with Backoff
- Extensibility First

---

# Why This Project?

This project demonstrates how modern AI applications can be built as **collaborative multi-agent systems** rather than a single LLM call. It combines workflow orchestration, durable execution, provider abstraction, MCP-based tool integration, and automated GitHub publishing into a modular architecture suitable for long-running engineering workflows.