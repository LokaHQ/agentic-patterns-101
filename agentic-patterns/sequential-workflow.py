"""Example of a sequential workflow using three agents as a python function (or class) resembeling pipeline"""

from strands import Agent
from strands.models import BedrockModel

BLOG_PLANNER_INSTRUCTION = "You are a blog planner. Take the topic that is provided to you and create a detailed outline with 3 sections and key points for each section."
SECTION_WRITER_INSTRUCTION = "You are a blog writer. Take the outline provided by the blog planner and expand each section into a detailed paragraph."
EDITOR_INSTRUCTION = "You are a professional editor. Improve the following blog draft by fixing grammar, making sentences concise, and ensuring smooth flow."


def sequential_workflow(
    blog_planner_agent: Agent,
    section_writer_agent: Agent,
    editor_agent: Agent,
    topic: str,
) -> str:
    """
    A sequential workflow that involves three agents:
    1. Blog planner to create an outline.
    2. Section writer to write the blog post based on the outline.
    3. Editor to edit the blog post.

    Args:
        topic (str): The topic for the blog post.
        blog_planner_agent (Agent): The agent responsible for creating the blog outline.
        section_writer_agent (Agent): The agent responsible for writing the blog post.
        editor_agent (Agent): The agent responsible for editing the blog post.

    Returns:
        str: The final edited blog post.
    """

    print("Starting sequential workflow for topic:", topic)

    # Step 1: Create a blog outline
    outline = blog_planner_agent(topic)
    print("Blog outline created:", outline)

    # Step 2: Write the blog post based on the outline
    draft = section_writer_agent(outline)
    print("Blog draft created:", draft)

    # Step 3: Edit the blog post
    final_post = editor_agent(draft)
    print("Final blog post created:", final_post)

    return final_post


if __name__ == "__main__":
    # Define the model we use for the agents (we want creative response that's why temp is high)
    bedrock_model = BedrockModel(
        model_id="us.amazon.nova-premier-v1:0",
        temperature=0.9,
    )

    # Step 1: Agent that creates a blog outline
    blog_planner_agent = Agent(
        model=bedrock_model,
        system_prompt=BLOG_PLANNER_INSTRUCTION,
        callback_handler=None,  # Optional: You can provide a callback handler for logging or monitoring
    )

    # Step 2: Agent that writes the blog post
    section_writer_agent = Agent(
        model=bedrock_model,
        system_prompt=SECTION_WRITER_INSTRUCTION,
        callback_handler=None,  # Optional: You can provide a callback handler for logging or monitoring
    )

    # Step 3: Agent that edits the blog post
    editor_agent = Agent(
        system_prompt=EDITOR_INSTRUCTION,
        model=bedrock_model,
        callback_handler=None,  # Optional: You can provide a callback handler for logging or monitoring
    )

    # Define the topic for the blog post and create the sequential workflow
    topic = "The Future of AI in Content Creation"
    final_post = sequential_workflow(
        blog_planner_agent=blog_planner_agent,
        section_writer_agent=section_writer_agent,
        editor_agent=editor_agent,
        topic=topic,
    )
    print("Final blog post created:", final_post)
