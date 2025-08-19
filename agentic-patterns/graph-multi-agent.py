from strands import Agent
from strands.models import BedrockModel
from strands.multiagent import GraphBuilder

ROUTER_INSTRUCTION = (
    "Interpret the user's dinner request and dispatch tasks to appropriate agents."
)
RECIPE_CREATOR_INSTRUCTION = (
    "Propose a refined recipe suitable for the requested dinner style."
)
BEVERAGE_SUGGESTOR_INSTRUCTION = (
    "Suggest a beverage that complements the dinner style and recipe."
)
MUSIC_CURATOR_INSTRUCTION = "Curate a playlist that matches the dinner ambiance and enhances the dining experience."
DINNER_PLANNER_INSTRUCTION = (
    "Combine the outputs from RecipeAgent, BeverageAgent, and MusicAgent into a single structured DinnerPlan object. "
    "The DinnerPlan should have the following fields:"
    "1. recipe: include all recipe details with subfields:"
    "   - name (str)"
    "   - ingredients (list of str)"
    "   - preparation_time (int, in minutes)"
    "   - instructions (str)"
    "2. beverage: include beverage details with subfields:"
    "   - name (str)"
    "   - type (str, e.g., wine, cocktail, non-alcoholic)"
    "   - pairing_notes (str, explaining why it pairs with the recipe)"
    "3. music_playlist: include music details with subfields:"
    "   - title (str)"
    "   - tracks (list of objects, each with:"
    "       - track_name (str)"
    "       - artist (str)"
    "       - genre (str, e.g., Classical, Jazz, Pop)"
    "     )"
    "Return the combined DinnerPlan object in valid JSON format that matches the DinnerPlan Pydantic model exactly."
)

if __name__ == "__main__":
    user_query = "Dinner style: formal Italian evening with elegance."

    # Define the model for the agents
    model = BedrockModel(
        model_id="amazon.nova-lite-v1:0", temperature=0.7, max_tokens=3000
    )

    # Create specialized agents
    input_router = Agent(
        model=model,
        name="InputRouter",
        system_prompt=ROUTER_INSTRUCTION,
    )
    recipe_creator = Agent(
        model=model,
        name="RecipeAgent",
        system_prompt=RECIPE_CREATOR_INSTRUCTION,
    )
    beverage_suggester = Agent(
        model=model,
        name="BeverageAgent",
        system_prompt=BEVERAGE_SUGGESTOR_INSTRUCTION,
    )
    music_curator = Agent(
        model=model,
        name="MusicAgent",
        system_prompt=MUSIC_CURATOR_INSTRUCTION,
    )

    dinner_planner = Agent(
        model=model,
        name="DinnerPlanAgent",
        system_prompt=DINNER_PLANNER_INSTRUCTION,
    )

    # Build the multi-agent graph
    builder = GraphBuilder()

    # Add nodes for each agent
    builder.add_node(input_router)
    builder.add_node(recipe_creator)
    builder.add_node(beverage_suggester)
    builder.add_node(music_curator)
    builder.add_node(dinner_planner)

    # Define dependencies
    builder.add_edge(
        "InputRouter", "RecipeAgent"
    )  # Router → Recipe (user preference input)
    builder.add_edge(
        "InputRouter", "BeverageAgent"
    )  # Router → Beverage (user preference input)
    builder.add_edge(
        "RecipeAgent", "BeverageAgent"
    )  # Recipe → Beverage (recipe-specific input)
    builder.add_edge(
        "InputRouter", "MusicAgent"
    )  # Router → Music (user preference input)
    builder.add_edge(
        "RecipeAgent", "DinnerPlanAgent"
    )  # Recipe → Plan (recipe-specific input)
    builder.add_edge(
        "BeverageAgent", "DinnerPlanAgent"
    )  # Beverage → Plan (beverage-specific input)
    builder.add_edge(
        "MusicAgent", "DinnerPlanAgent"
    )  # Music → Plan (music-specific input)

    # Set the entry point/s for the graph (Optional - If not spesified, it will be auto-detected)
    builder.set_entry_point("InputRouter")
    graph = builder.build()

    # Execute the graph with a prompt
    result = graph(user_query)
