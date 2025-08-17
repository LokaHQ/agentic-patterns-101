"""Example of tool use Agent with MCP server tools"""

# from mcp.client.sse import sse_client - for HTTP MCP servers that use Server-Sent Events (SSE)
# from mcp.client.streamable_http import streamablehttp_client - for HTTP MCP servers that use Streamable HTTP Events
from mcp import StdioServerParameters, stdio_client  # for MCP servers that use STDIO
from strands import Agent
from strands.models import BedrockModel
from strands.tools.mcp import MCPClient

INSTRUCTION = "You are a Bioinformatics expert, that has a deep understanding of genomic data analysis and variant calling."

# Creating an STDIO client for the MCP server because that's the way to interact with this server
# https://awslabs.github.io/mcp/servers/aws-healthomics-mcp-server
mcp_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="uvx", args=["awslabs.aws-healthomics-mcp-server"]
        )
    )
)

# If the MCP server uses Server-Sent Events (SSE)
# mcp_client = MCPClient(lambda: sse_client("http://localhost:8000/sse"))

# If the MCP server uses Streamable HTTP Events
# mcp_client = MCPClient(lambda: streamablehttp_client("http://localhost:8000/mcp"))


if __name__ == "__main__":
    # Define the model we use for the agents
    bedrock_model = BedrockModel(
        model_id="us.amazon.nova-premier-v1:0",
        temperature=0.1,
    )

    # Create an agent with MCP tools - must be within the context of the MCP client
    with mcp_client:
        # Get the tools from the MCP server
        tools = mcp_client.list_tools_sync()

        # Create an agent with these tools
        agent = Agent(tools=tools, system_prompt=INSTRUCTION, model=bedrock_model)

        # Define the query/question and execute the agent
        query = "Help me create a new genomic variant calling workflow"
        result = agent(query)
        print("The result is:", result)
