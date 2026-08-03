
  It is a modular multi-agent AI assistant platform that automates real-world workflows.
  It enables AI agents to
      Plan tasks
      Delegate work
      Execute actions
      Recover from failures
      Resume unfinished workflows
  It combines
    LLMs for reasoning
    MCP for standardized tool integration
    Memory for context and personalization
    Durable workflow execution for reliable, long-running tasks
    
Goals
    Automate multi-step workflows
    Coordinate specialized AI agents
    Integrate with external tools via MCP
    Support long-running workflows
    Recover safely from failures
    Enable extensibility through pluggable agents and tools
    
Use-Cases 
        Sprint Planning
            Design document → Task decomposition → Story point estimation → Dependency mapping → GitHub Issues
        Meeting Scheduling
        Travel Planning
        Monthly Expense Monitoring
        Email & Calendar Automation
        
Components
      FastAPI Host
      Coordinator Agent
      Planner Agent
      Worker Agents
      LLM Provider
      MCP Client
      MCP Servers
      Memory
      Workflow Engine
      Checkpoint Store
      Agent Registry
      Tool Registry
      Capability Registry
      Observability & Logging
