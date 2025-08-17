<div align="center" style="display: flex; align-items: center; justify-content: center; gap: 30px;">

  <a href="https://loka.com">
    <img src="https://media.licdn.com/dms/image/v2/D4D0BAQGjlTZNkGk34w/company-logo_200_200/company-logo_200_200/0/1719824852415/loka_logo?e=2147483647&v=beta&t=b02H4t2HnGT1QvNFfSctVcPqMgaDojSW1OcJPA-Lk18"
         alt="Loka" height="100px">
  </a>

  <span style="color: white; font-size: 40px; font-weight: bold; display: flex; align-items: center; justify-content: center;">×</span>

  <a href="https://strandsagents.com">
    <img src="https://strandsagents.com/latest/assets/logo-github.svg"
         alt="Strands Agents" height="100px">
  </a>

</div>

<h2 align="center">
  Agentic Patterns 101 with Loka & Strands-Agents (AWS)
</h2>


Welcome to **Agentic Patterns 101** - a comprehensive collection of practical implementations demonstrating various agentic design patterns using [Strands-Agents](https://strandsagents.com).

Whether you're building content generation pipelines, document processing systems, or complex multi-step AI workflows, these patterns provide tested foundations for your agentic applications.

<h3 align="center">
  Agentic Patterns
</h3>

| Pattern | Description | Key Characteristics | Use Cases & Industries | When to Use / When Not to Use | Implementation | File Paths |
|---------|-------------|-------------------|----------------------|---------------------------|----------------|------------|
| **Sequential Workflow** (Prompt Chaining) | Tasks are completed step by step, where each agent's (LLM's) output becomes the input for the next. This pattern divides a larger task into a chain of smaller, well-defined steps, ensuring that each stage builds directly on the previous one. It is ideal for processes that follow a predictable, linear progression without branching or parallelization. | • Fixed, linear sequence of steps<br>• Each step depends on the output of the previous step<br>• Minimal branching or deviation from the sequence | **Structured document generation:** Agent 1 creates an outline, Agent 2 generates content, and Agent 3 validates the content against predefined criteria - e.g., in Content Creation for blog posts, marketing copy, or reports<br><br>**Multi-step data processing:** Extract, transform, and summarize information from documents - e.g., in Intelligent Document Processing (IDP) for Healthcare records or Invoices<br><br>**Research workflow:** Agent 1 collects research references, Agent 2 synthesizes insights, Agent 3 formats a report - e.g., in Academic Research or Market Analysis | **Use when:** Tasks can be broken into discrete, ordered steps with predictable outcomes<br><br>**Avoid when:** Flexibility, parallel processing, or adaptive decision-making is required | **Function-based:** Direct function calls between agents<br><br>**Tool-based:** Uses Strands workflow tool with task dependencies | [`sequential-workflow.py`](./agentic-patterns/sequential-workflow.py)<br>[`sequential-workflow-tool.py`](./agentic-patterns/sequential-workflow-tool.py) |
| **Parallel Workflow** | Multiple agents (LLMs) execute tasks simultaneously, often starting from a shared input or from the output of a preceding step. This allows independent subtasks to run in parallel, reducing latency and improving efficiency. The results from parallel agents are typically aggregated or passed to a downstream step for integration. | • Multiple agents operate concurrently<br>• Steps can process shared or partitioned inputs<br>• Requires a mechanism to merge or coordinate results | **Content enrichment:** Agent 1 (LLM 1) drafts an article, while Agent 2 (LLM 2) in parallel checks grammar/style and Agent 3 (LLM 3) performs fact-checking - e.g., in Media & Publishing workflows for news or blog posts<br><br>**Multi-perspective analysis:** Agent 1 (LLM 1) structures a financial report, then Agent 2 (LLM 2) analyzes regulatory risks while Agent 3 (LLM 3) in parallel evaluates market sentiment - e.g., in Finance & Compliance domains | **Use when:** Subtasks are independent, can safely be run simultaneously, and merging results is straightforward<br><br>**Avoid when:** Steps are highly dependent on each other's outputs, or when sequencing is critical to correctness | **Tool-based:** Uses Strands workflow tool with parallel task execution | [`parallel-workflow-tool.py`](./agentic-patterns/parallel-workflow-tool.py) |
| **MCP Server Tools** | The Model Context Protocol (MCP) is an open standard that defines how applications provide context to Large Language Models (LLMs). MCP enables communication between agents and MCP servers, which expose additional tools that agents can call to extend their capabilities. These tools can range from database queries to APIs or custom business logic, allowing agents to act beyond their base reasoning abilities.<br><br>There are three standardized types of MCP servers, categorized by transport protocol:<br>STDIO (Standard Input/Output), usually when the client and the server are on the same side<br>SSE (server-sent events, currently being deprecated)<br>Streamable HTTP Events (the modern, preferred approach) | • Provide structured, standardized communication between agents and external tools<br>• Model-agnostic: any LLM can leverage MCP-defined tools<br>• Extend agent functionality with external data, APIs, or services<br>• Enable interoperability between multiple systems and agents | **Enterprise Data Access:** Agents retrieve structured data from ERP/CRM systems via MCP tools - e.g., in Enterprise IT or Customer Relationship Management<br><br>**Knowledge Retrieval:** An MCP server provides search or vector database querying tools - e.g., in Legal Tech for case document retrieval<br><br>**Operational Automation:** Agents call MCP-exposed APIs (via MCP tools) for scheduling, ticketing, or reporting - e.g., in Customer Support or HR Systems<br><br>**Healthcare & Life Sciences:** MCP tools that can expose access to medical ontologies or EHR (Electronic Health Records) queries in a standardized way | **Use when:** Agents need structured, standardized access to external tools, systems, or APIs in a way that is interoperable and vendor-neutral<br><br>**Avoid when:** The task is fully self-contained within the LLM (e.g., pure text summarization) or when a lightweight, direct API call without protocol overhead is sufficient | **MCP-based:** Uses MCP client to connect to standardized MCP servers | [`mcp-server-tools.py`](./agentic-patterns/mcp-server-tools.py) |

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.

## Repository Structure

```
├── .github/                                 # GitHub Actions workflows
│   ├── workflows/                           # GitHub Actions workflow files
│   │   └── uv-ci.yaml                       # uv (python) Continuous Integration workflow
│   └── dependabot.yaml                      # Configuration file for Dependabot
├── agentic-patterns/                        # Implementation directory
│   ├── mcp-server-tools.py                  # MCP server tools implementation
│   ├── parallel-workflow-tool.py            # Tool-based parallel workflow implementation
│   ├── sequential-workflow-tool.py          # Tool-based sequential workflow implementation
│   └── sequential-workflow.py               # Function-based sequential workflow implementation
├── .gitignore                               # Git ignore patterns
├── .pre-commit-config.yaml                  # Pre-commit hooks configuration
├── .python-version                          # Python version specification
├── LICENSE                                  # Project license
├── pyproject.toml                           # Pyproject configuration file
├── README.md                                # Project documentation
└── uv.lock                                  # uv lock file for dependencies
```
