from strands import Agent
from strands_tools import graph
from strands.models import BedrockModel

GRAPH_AGENT_INSTRUCTION = "Create a graph of agents to interpret the user's dinner request and dispatch tasks to appropriate agents."

if __name__ == "__main__":
    user_query = "Dinner style: formal Italian evening with elegance."

    # Define the model for the agents
    model = BedrockModel(
        model_id="amazon.nova-lite-v1:0", temperature=0.7, max_tokens=3000
    )

    agent = Agent(tools=[graph], system_prompt=GRAPH_AGENT_INSTRUCTION)
    agent(user_query)