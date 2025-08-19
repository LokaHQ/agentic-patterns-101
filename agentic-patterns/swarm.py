from strands import Agent
from strands.models import BedrockModel
from strands.multiagent import Swarm
from strands.types.content import ContentBlock

if __name__ == "__main__":
    """
    Main function to execute the swarm process.
    """

    # Create the agents
    trend_analyst = Agent(
        model=BedrockModel(model_id="amazon.nova-pro-v1:0", temperature=0.7),
        system_prompt="You are a trend analyst who analyzes viral content. You can view images and videos to understand what visual elements are trending. Identify patterns in successful content and timing windows.",
    )
    meme_creator = Agent(
        model=BedrockModel(
            model_id="amazon.nova-canvas-v1:0", temperature=0.8
        ),  # Image generation model
        system_prompt="You are a visual meme creator who can both analyze existing memes and generate new ones. Create engaging visual content using trending formats. You can generate images and critique visual content.",
    )
    video_creator = Agent(
        model=BedrockModel(
            model_id="amazon.nova-reel-v1:0", temperature=0.8
        ),  # Video generation model
        system_prompt="You are a video content creator who can create new videos. Generate short-form videos and analyze what makes videos go viral on different platforms.",
    )
    copywriter = Agent(
        model=BedrockModel(model_id="amazon.nova-lite-v1:0", temperature=0.9),
        system_prompt="You are a social media copywriter. You can view images and videos to write appropriate captions and copy that matches the visual content.",
    )
    community_manager = Agent(
        model=BedrockModel(model_id="amazon.nova-lite-v1:0", temperature=0.6),
        system_prompt="You are a community manager who can analyze visual content and engagement patterns. You can view memes, videos, and posts to understand audience reactions.",
    )

    # Create the swarm
    viral_content_swarm = Swarm(
        [trend_analyst, meme_creator, video_creator, copywriter, community_manager],
        max_handoffs=15,
        max_iterations=10,
    )

    # Creating the prompt using ContentBlocks
    trending_meme_bytes = b"..."  # Placeholder for trending meme image bytes
    content_blocks = [
        ContentBlock(
            text="Create a viral campaign about AI breakthroughs. Something similar to the campaign from last year:"
        ),
        ContentBlock(image={"format": "png", "source": {"bytes": trending_meme_bytes}}),
    ]

    result = viral_content_swarm(content_blocks)

    print(f"Swarm Status: {result.status}")
    print(f"Node history: {[node.node_id for node in result.node_history]}")
