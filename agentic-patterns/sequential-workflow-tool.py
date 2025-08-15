"""Example of a sequential workflow using three agents as a workflow tool (strands-agents-tools)"""

from strands import Agent
from strands.models import BedrockModel
from strands_tools import workflow

BLOG_PLANNER_INSTRUCTION = "You are a blog planner. Take the topic that is provided to you and create a detailed outline with 3 sections and key points for each section."
SECTION_WRITER_INSTRUCTION = "You are a blog writer. Take the outline provided by the blog planner and expand each section into a detailed paragraph."
EDITOR_INSTRUCTION = "You are a professional editor. Improve the following blog draft by fixing grammar, making sentences concise, and ensuring smooth flow."

if __name__ == "__main__":
    # Define the model we use for the agents (we want creative response that's why temp is high)
    bedrock_model = BedrockModel(
        model_id="us.amazon.nova-premier-v1:0",
        temperature=0.9,
    )

    # Create one Agent with one workflow tool
    blog_agent = Agent(tools=[workflow])

    # Creating the workflow
    blog_agent.tool.workflow(
        action="create",
        workflow_id="blog_agent_workflow",
        tasks=[
            {
                "task_id": "blog_planner",  # The unique ID for the Blog Planner agent
                "description": 'Create a detailed outline for the blog post about "The Future of AI in Content Creation"',  # The description of the task
                "system_prompt": BLOG_PLANNER_INSTRUCTION,  # The system prompt for the Blog Planner agent
                "priority": 5,  # The priority of the task (higher numbers indicate higher priority)
            },
            {
                "task_id": "section_writer",
                "description": "Expand each section of the outline into a detailed paragraph",
                "dependencies": ["blog_planner"],
                "system_prompt": SECTION_WRITER_INSTRUCTION,
                "priority": 4,
            },
            {
                "task_id": "editor",
                "description": "Edit the blog draft for clarity and conciseness",
                "dependencies": ["section_writer"],
                "system_prompt": EDITOR_INSTRUCTION,
                "priority": 3,
            },
        ],
    )

    # Start the workflow
    blog_agent.tool.workflow(
        action="start",
        workflow_id="blog_agent_workflow",
    )

    # Monitor the workflow progress
    blog_agent.tool.workflow(
        action="monitor",
        workflow_id="blog_agent_workflow",
    )
