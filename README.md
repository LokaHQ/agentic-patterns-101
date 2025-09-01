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

<table>
  <thead>
    <tr>
      <th colspan="5" style="text-align: center; font-size: 1.5em; padding: 20px; background-color: #f8f9fa; border: 2px solid #dee2e6;">
        <strong>Agentic Patterns</strong>
      </th>
    </tr>
    <tr>
      <th>Pattern</th>
      <th>Description & Key Characteristics</th>
      <th>Use Cases & Industries</th>
      <th>When to Use / When Not to Use</th>
      <th>File Paths</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Sequential Workflow</strong><br>(Prompt Chaining)</td>
      <td>Tasks completed step-by-step where each agent's output becomes input for the next.<br><br>• Linear sequence<br>• Each step depends on previous<br>• Minimal branching</td>
      <td><strong>Document generation:</strong> outline → content → validation<br><strong>Data processing:</strong> extract → transform → summarize<br><strong>Research:</strong> collect → synthesize → format</td>
      <td><strong>Use:</strong> Discrete, ordered steps<br><strong>Avoid:</strong> Need flexibility or parallel processing</td>
      <td><a href="./agentic-patterns/sequential-workflow.py"><code>sequential-workflow.py</code></a><br><a href="./agentic-patterns/sequential-workflow-tool.py"><code>sequential-workflow-tool.py</code></a></td>
    </tr>
    <tr>
      <td><strong>Parallel Workflow</strong></td>
      <td>Multiple agents execute tasks simultaneously, often from shared input or preceding step output.<br><br>• Concurrent execution<br>• Shared/partitioned inputs<br>• Result coordination needed</td>
      <td><strong>Content enrichment:</strong> draft + grammar check + fact-check in parallel<br><strong>Multi-perspective analysis:</strong> financial report + risk analysis + market sentiment</td>
      <td><strong>Use:</strong> Independent subtasks<br><strong>Avoid:</strong> Highly dependent outputs</td>
      <td><a href="./agentic-patterns/parallel-workflow-tool.py"><code>parallel-workflow-tool.py</code></a></td>
    </tr>
    <tr>
      <td><strong>LLM Routing</strong></td>
      <td>Automatically directs queries to the most appropriate model based on complexity, domain expertise, or computational requirements.<br><br>
      • Dynamic model selection <br>
      • Centralized routing logic</td>
      <td><strong>Software development:</strong> syntax questions → lightweight models, architecture → reasoning models<br><strong>Customer support:</strong> FAQ → fast models, troubleshooting → specialized models</td>
      <td><strong>Use:</strong> Query complexity varies significantly, cost optimization important<br><strong>Avoid:</strong> Similar complexity levels across queries, routing overhead exceeds benefits</td>
      <td><a href="./agentic-patterns/llm_routing.py"><code>llm_routing.py</code</a></td>
    </tr>
    <tr>
      <td><strong>Reflection Pattern</strong></td>
      <td>Agent generates initial output, receives feedback from judge agent, then refines work through iterative improvement cycles.<br><br>
      • Iterative improvement through feedback loops<<br>
      • Quality enhancement through refinement</td>
      <td><strong>Creative content:</strong> draft → critique → refinement for scripts, marketing copy<br><strong>Code review:</strong> generate → analyze → refactor based on feedback<br><strong>Research:</strong> findings → critique → strengthen analysis</td>
      <td><strong>Use:</strong> Output quality critical, iterative improvement adds value<br><strong>Avoid:</strong> Simple tasks, feedback overhead exceeds improvement value</td>
      <td><a href="./agentic-patterns/reflection_pattern.py"><code>reflection_pattern.py</code></td>
    </tr>
     <tr>
      <td><strong>Pure Tools</strong></td>
      <td>
        A single-agent pattern where tools handle specific domain logic while the agent orchestrates their usage through natural language interactions.
        <br><br>
        • Simple agent-tool architecture<br>
        • Natural language tool orchestration<br>
        • Model-powered tool intelligence<br>
        • Clean separation of concerns
      </td>
      <td>
        <strong>E-commerce:</strong> Inventory management and order processing<br>
        <strong>Data Management:</strong> create → read → update → delete → query<br>
        <strong>HR systems:</strong> Employee onboarding and performance tracking<br>
      </td>
      <td><strong>Use:</strong> Domain-specific applications with clear tool boundaries and shared state<br><strong>Avoid:</strong> Complex multi-step workflows requiring multiple specialized agents</td>
      <td><a href="./agentic-patterns/pure-tools.py"><code>pure-tools.py</code></a>
      </td>
    </tr>
    <tr>
      <td><strong>MCP Server Tools</strong></td>
      <td>Model Context Protocol enables standardized communication between agents and external tools/services via MCP servers.<br><br>• Standardized communication<br>• Model-agnostic<br>• External tool integration<br>• System interoperability</td>
      <td><strong>Enterprise data:</strong> ERP/CRM system access<br><strong>Knowledge retrieval:</strong> Vector DB queries<br><strong>Automation:</strong> Scheduling/ticketing APIs<br><strong>Healthcare:</strong> EHR/medical ontology access</td>
      <td><strong>Use:</strong> Structured external tool access<br><strong>Avoid:</strong> Self-contained tasks or simple API calls</td>
      <td><a href="./agentic-patterns/mcp-server-tools.py"><code>mcp-server-tools.py</code></a></td>
    </tr>
    <tr>
      <td><strong>Agents as Tools</strong></td>
      <td>
        A multi-agent pattern where individual agents expose their capabilities as callable tools, enabling orchestration by a central agent or system.
        <br><br>
        • Agents encapsulate domain-specific intelligence<br>
        • Flexible agent composition<br>
        • Scalable, modular architecture
      </td>
      <td>
        <strong>Customer Support:</strong> AI chatbots handling FAQs<br>
        <strong>Finance:</strong> Loan processing agents or fraud detection agents<br>
        <strong>Education:</strong> Adaptive learning agents or curriculum planning agents<br>
      </td>
      <td><strong>Use:</strong> Scenarios requiring multiple specialized agents to collaborate<br><strong>Avoid:</strong> Simple single-domain applications where one agent suffices</td>
      <td><a href="./agentic-patterns/agents-as-tools.py"><code>agents-as-tools.py</code></a>
      </td>
    </tr>
    <tr>
      <td><strong>Swarm</strong></td>
      <td> Multiple specialized agents work together as autonomous peers through shared working memory and self-organizing coordination.<br><br>• Autonomous coordination without central control<br>• Shared working memory for all agents<br>• Dynamic task distribution based on discoveries<br>• Peer-to-peer handoffs</td>
      <td><strong>Viral content creation:</strong> trend analysts, creators, copywriters collaborating fluidly<br><strong>Research investigation:</strong> specialists handing off based on emerging findings<br><strong>Crisis response:</strong> dynamic collaboration as situations evolve</td>
      <td><strong>Use:</strong> Unpredictable outcomes, creative collaboration<br><strong>Avoid:</strong> Clear hierarchies, central coordination preferred</td>
      <td><a href="./agentic-patterns/swarm.py"><code>swarm.py</code></a></td>
    </tr>
    <tr>
      <td><strong>Graph Multi-Agent Pattern</strong></td>
      <td>
        A deterministic DAG-based orchestration model where each node is an agent (or custom multi-agent), and edges represent execution dependencies.
        <br><br>
        • Deterministic execution order<br>
        • Clear dependency management<br>
        • Nested patterns and custom node types<br>
        • Conditional and multi-modal support
      </td>
      <td>
        <strong>Financial analysis:</strong> fetch → analyze → summarize → report<br>
        <strong>Content creation:</strong> research → draft → edit → publish<br>
        <strong>IoT:</strong> monitor → diagnose → optimize → alert<br>
        <strong>Healthcare:</strong> collect → analyze → diagnose → recommend<br>
      </td>
      <td><strong>Use:</strong> Complex workflows with clear agent dependencies<br><strong>Avoid:</strong> Simple pipelines better suited for Workflow pattern</td>
      <td><a href="./agentic-patterns/graph-multi-agent.py"><code>graph-multi-agent.py</code></a>
      <a href="./agentic-patterns/graph-multi-agent-tool.py"><code>graph-multi-agent-tool.py</code></a>
      </td>
    </tr>
  </tbody>
</table>

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.

## Repository Structure

```
├── .github/                                 # GitHub Actions workflows
│   ├── workflows/                           # GitHub Actions workflow files
│   │   └── uv-ci.yaml                       # uv (python) Continuous Integration workflow
│   └── dependabot.yaml                      # Configuration file for Dependabot
├── agentic-patterns/                        # Implementation directory
│   ├── agents-as-tools.py                   # Agents as tools orchestration workflow
│   ├── graph-multi-agent-tool.py            # Tool-based graph multi-agent implementation
│   ├── graph-multi-agent.py                 # Graph multi-agent implementation
|   ├── llm_routing.py                       # LLM Routing Implementation
│   ├── mcp-server-tools.py                  # MCP server tools implementation
│   ├── parallel-workflow-tool.py            # Tool-based parallel workflow implementation
│   ├── pure-tools.py                        # Pure tools implementation
|   ├── reflection_pattern.py                # Reflection Pattern implementation
│   ├── sequential-workflow-tool.py          # Tool-based sequential workflow implementation
│   ├── sequential-workflow.py               # Function-based sequential workflow implementation
│   └── swarm.py                             # Swarm pattern implementation
├── assets/                                  # Diagrams
│   └── strands_agents_pattern.drawio       # Diagrams for strands agents pattern
├── .gitignore                               # Git ignore patterns
├── .pre-commit-config.yaml                  # Pre-commit hooks configuration
├── .python-version                          # Python version specification
├── LICENSE                                  # Project license
├── pyproject.toml                           # Pyproject configuration file
├── README.md                                # Project documentation
└── uv.lock                                  # uv lock file for dependencies
```
