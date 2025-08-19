from enum import Enum

from pydantic import BaseModel, Field
from strands import Agent
from strands.models import BedrockModel

ROUTER_INSTRUCTION = """
You are a helpful software development router that can route user queries to the appropriate agent.
Based on the user's question, determine the complexity of the query as:
simple, complex, or ambiguous.

- Simple queries can retrieve factual information but lack reasoning for complex system design.
- Complex queries require deeper understanding and reasoning about the system's architecture and design principles.
- Ambiguous queries are unclear and may require clarification before they can be properly routed.
"""


class RouteType(Enum):
    """
    Enumeration for the different types of routing that can be applied to a user query.
    """

    SIMPLE = "simple"
    COMPLEX = "complex"
    AMBIGUOUS = "ambiguous"


class RouteResponse(BaseModel):
    """
    Config Model representing the response from the routing process.
    """

    type: RouteType
    message: str = Field(..., description="The response message")


if __name__ == "__main__":
    """
    Main function to execute the routing process.
    """
    # User query to be routed
    user_query = "What is the difference between == and === in JavaScript?"

    # Other example queries:
    # complex_query = "Design a microservices architecture for a banking system with regulatory compliance"
    # ambiguous_query = "What is the best way to implement a feature?"

    # Initialize the routing model
    routing_model = BedrockModel(
        model_id="amazon.nova-lite-v1:0",
        temperature=0.6,
    )

    # Initialize the router agent
    router_agent = Agent(model=routing_model, system_prompt=ROUTER_INSTRUCTION)

    # Get structured response from user query
    response = router_agent.structured_output(RouteResponse, user_query)

    # Route the response based on its type

    # Handle simple response
    if response.type == RouteType.SIMPLE:
        print("Routing to simple response handler.")

        agent = Agent(
            model=BedrockModel(
                model_id="amazon.nova-pro-v1:0",
                temperature=0.9,
            ),
            system_prompt="You are a fast, efficient assistant for basic programming questions. Provide concise, accurate answers about syntax, commands, and simple explanations.",
        )

        agent_response = agent(user_query)

        print(f" Final response: {agent_response}")

    # Handle complex response
    elif response.type == RouteType.COMPLEX:
        print("Routing to complex response handler.")

        agent = Agent(
            model=BedrockModel(
                model_id="anthropic.claude-sonnet-4-20250514-v1:0",
                temperature=0.9,
            ),
            system_prompt="You are an expert software architect. Analyze complex system design problems, consider trade-offs, and provide detailed architectural guidance with reasoning.",
        )

        agent_response = agent(user_query)

        print(f" Final response: {agent_response}")

    # Handle ambiguous response
    elif response.type == RouteType.AMBIGUOUS:
        agent = Agent(
            model=BedrockModel(
                model_id="amazon.nova-pro-v1:0",
                temperature=0.9,
            ),
            system_prompt="You are an ambiguous query handler agent.",
        )

        agent_response = agent(user_query)

        print(f" Final response: {agent_response}")
