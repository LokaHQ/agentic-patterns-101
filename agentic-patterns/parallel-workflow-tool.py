"""Example of parallel workflow using three agents as a workflow tool (strands-agents-tools)"""

from strands import Agent
from strands.models import BedrockModel
from strands_tools import workflow

CEO_INSTRUCTION = "You are CEO. Your goal is to ensure the company's success and make high-level decisions."
FINANCE_INSTRUCTION = "You are finance expert. Always analyze the question and solution from a financial perspective."
LEGAL_INSTRUCTION = "You are legal expert. Always analyze the question and solution from a legal perspective."


if __name__ == "__main__":
    # Define the model we use for the agents
    bedrock_model = BedrockModel(
        model_id="us.amazon.nova-premier-v1:0",
        temperature=0.1,
    )

    # Create one Agent with one workflow tool
    solution_agent = Agent(tools=[workflow])

    # Creating the workflow
    solution_agent.tool.workflow(
        action="create",
        workflow_id="solution_agent_workflow",
        tasks=[
            {
                "task_id": "ceo_agent",  # The unique ID for the CEO Agent
                "description": "How to increase the efficiency of the team?",  # The description of the task
                "system_prompt": CEO_INSTRUCTION,  # The system prompt for the CEO Agent
                "priority": 5,  # The priority of the task (higher numbers indicate higher priority)
            },
            {
                "task_id": "finance_agent",
                "description": "Analyze the financial implications of the proposed solutions",
                "dependencies": ["ceo_agent"],
                "system_prompt": FINANCE_INSTRUCTION,
                "priority": 3,
            },
            {
                "task_id": "legal_agent",
                "description": "Ensure all proposed solutions comply with legal regulations",
                "dependencies": ["ceo_agent"],
                "system_prompt": LEGAL_INSTRUCTION,
                "priority": 3,
            },
        ],
    )

    # Start the workflow
    solution_agent.tool.workflow(
        action="start",
        workflow_id="solution_agent_workflow",
    )

    # Monitor the workflow progress
    solution_agent.tool.workflow(
        action="monitor",
        workflow_id="solution_agent_workflow",
    )
