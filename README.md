<div align="center">
  <div style="display: flex; align-items: center; justify-content: center; gap: 20px;">
    <a href="https://loka.com">
      <img src="https://media.licdn.com/dms/image/v2/D4D0BAQGjlTZNkGk34w/company-logo_200_200/company-logo_200_200/0/1719824852415/loka_logo?e=2147483647&v=beta&t=b02H4t2HnGT1QvNFfSctVcPqMgaDojSW1OcJPA-Lk18" alt="Loka" width="105px" height="105px">
    </a>
    <span style="font-size: 24px; color: #666; margin: 0 10px;">×</span>
    <a href="https://strandsagents.com">
      <img src="https://strandsagents.com/latest/assets/logo-github.svg" alt="Strands Agents" width="55px" height="105px">
    </a>
  </div>

  <h1>
    Agentic Patterns 101 with Loka & Strands-Agents (AWS)
  </h1>

</div>

Welcome to **Agentic Patterns 101** - a comprehensive collection of practical implementations demonstrating various agentic design patterns using [Strands-Agents](https://strandsagents.com).

Whether you're building content generation pipelines, document processing systems, or complex multi-step AI workflows, these patterns provide tested foundations for your agentic applications.

<table>
  <thead>
    <tr>
      <th colspan="6" style="text-align: center; font-size: 1.5em; padding: 20px; background-color: #f8f9fa; border: 2px solid #dee2e6;">
        <strong>Agentic Patterns</strong>
      </th>
    </tr>
    <tr>
      <th>Pattern</th>
      <th>Description</th>
      <th>Key Characteristics</th>
      <th>Use Cases & Industries</th>
      <th>Implementation</th>
      <th>File Paths</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Sequential Workflow</strong><br>(Prompt Chaining)</td>
      <td>
        Tasks completed step by step, where each agent's output becomes input for the next. Divides larger tasks into a chain of smaller, well-defined steps with linear progression.
      </td>
      <td>
        • Fixed, linear sequence of steps<br><br>
        • Each step depends on the output of the previous step<br><br>
        • Minimal branching or deviation from the sequence
      </td>
      <td>
        <strong>Structured document generation</strong><br>
        Content creation like blog posts
        <br><br>
        <strong>Multi-step data processing</strong><br>
        Intelligent Document Processing (IDP) for Healthcare records or Invoices
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
