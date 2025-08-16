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

<h1 align="center">
  Agentic Patterns 101 with Loka & Strands-Agents (AWS)
</h1>


Welcome to **Agentic Patterns 101** - a comprehensive collection of practical implementations demonstrating various agentic design patterns using [Strands-Agents](https://strandsagents.com).

Whether you're building content generation pipelines, document processing systems, or complex multi-step AI workflows, these patterns provide tested foundations for your agentic applications.

<table>
  <thead>
    <tr>
      <th colspan="7" style="text-align: center; font-size: 1.5em; padding: 20px; background-color: #f8f9fa; border: 2px solid #dee2e6;">
        <strong>Agentic Patterns</strong>
      </th>
    </tr>
    <tr>
      <th>Pattern</th>
      <th>Description</th>
      <th>Key Characteristics</th>
      <th>Use Cases & Industries</th>
      <th>When to Use / When Not to Use</th>
      <th>Implementation</th>
      <th>File Paths</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Sequential Workflow</strong><br>(Prompt Chaining)</td>
      <td>
        Tasks are completed step by step, where each agent's (LLM's) output becomes the input for the next. This pattern divides a larger task into a chain of smaller, well-defined steps, ensuring that each stage builds directly on the previous one. It is ideal for processes that follow a predictable, linear progression without branching or parallelization.
      </td>
      <td>
        • Fixed, linear sequence of steps<br><br>
        • Each step depends on the output of the previous step<br><br>
        • Minimal branching or deviation from the sequence
      </td>
      <td>
        <strong>Structured document generation:</strong> Agent 1 creates an outline, Agent 2 generates content, and Agent 3 validates the content against predefined criteria - e.g., in Content Creation for blog posts, marketing copy, or reports
        <br><br>
        <strong>Multi-step data processing:</strong> Extract, transform, and summarize information from documents - e.g., in Intelligent Document Processing (IDP) for Healthcare records or Invoices
        <br><br>
        <strong>Research workflow:</strong> Agent 1 collects research references, Agent 2 synthesizes insights, Agent 3 formats a report - e.g., in Academic Research or Market Analysis
      </td>
      <td>
        <strong>Use when:</strong> Tasks can be broken into discrete, ordered steps with predictable outcomes
        <br><br>
        <strong>Avoid when:</strong> Flexibility, parallel processing, or adaptive decision-making is required
      </td>
      <td>
        <table style="border: none; margin: 0;">
          <tr style="border: none;">
            <td style="border: none; padding: 5px 0;"><strong>Function-based</strong></td>
          </tr>
          <tr style="border: none;">
            <td style="border: none; padding: 0 0 10px 0; font-size: 0.9em;">Direct function calls between agents</td>
          </tr>
          <tr style="border: none;">
            <td style="border: none; padding: 5px 0;"><strong>Tool-based</strong></td>
          </tr>
          <tr style="border: none;">
            <td style="border: none; padding: 0; font-size: 0.9em;">Uses Strands workflow tool with task dependencies</td>
          </tr>
        </table>
      </td>
      <td>
        <table style="border: none; margin: 0;">
          <tr style="border: none;">
            <td style="border: none; padding: 5px 0;">
              <a href="./agentic-patterns/sequential-workflow.py"><code>sequential-workflow.py</code></a>
            </td>
          </tr>
          <tr style="border: none;">
            <td style="border: none; padding: 5px 0;">
              <a href="./agentic-patterns/sequential-workflow-tool.py"><code>sequential-workflow-tool.py</code></a>
            </td>
          </tr>
        </table>
      </td>
    </tr>
    <tr>
      <td><strong>Parallel Workflow</strong></td>
      <td>
        Multiple agents (LLMs) execute tasks simultaneously, often starting from a shared input or from the output of a preceding step. This allows independent subtasks to run in parallel, reducing latency and improving efficiency. The results from parallel agents are typically aggregated or passed to a downstream step for integration.
      </td>
      <td>
        • Multiple agents operate concurrently<br><br>
        • Steps can process shared or partitioned inputs<br><br>
        • Requires a mechanism to merge or coordinate results
      </td>
      <td>
        <strong>Content enrichment:</strong> Agent 1 (LLM 1) drafts an article, while Agent 2 (LLM 2) in parallel checks grammar/style and Agent 3 (LLM 3) performs fact-checking - e.g., in Media & Publishing workflows for news or blog posts
        <br><br>
        <strong>Multi-perspective analysis:</strong> Agent 1 (LLM 1) structures a financial report, then Agent 2 (LLM 2) analyzes regulatory risks while Agent 3 (LLM 3) in parallel evaluates market sentiment - e.g., in Finance & Compliance domains
      </td>
      <td>
        <strong>Use when:</strong> Subtasks are independent, can safely be run simultaneously, and merging results is straightforward
        <br><br>
        <strong>Avoid when:</strong> Steps are highly dependent on each other's outputs, or when sequencing is critical to correctness
      </td>
      <td>
        <table style="border: none; margin: 0;">
          <tr style="border: none;">
            <td style="border: none; padding: 5px 0;"><strong>Tool-based</strong></td>
          </tr>
          <tr style="border: none;">
            <td style="border: none; padding: 0; font-size: 0.9em;">Uses Strands workflow tool with parallel task execution</td>
          </tr>
        </table>
      </td>
      <td>
        <table style="border: none; margin: 0;">
          <tr style="border: none;">
            <td style="border: none; padding: 5px 0;">
              <a href="./agentic-patterns/parallel-workflow-tool.py"><code>parallel-workflow-tool.py</code></a>
            </td>
          </tr>
        </table>
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
