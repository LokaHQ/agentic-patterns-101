"""Example of pure tools usage for Trip Planning."""

from strands import Agent, tool
from strands.models import BedrockModel

SUGGESTION_INSTRUCTION = (
    "Suggest one specific, practical travel activity for {destination}."
    "Provide a concise recommendation (1-2 sentences) that includes:"
    "- A specific attraction, landmark, or experience"
    "- Brief context about why it's worth doing"
    "Example format: Visit [specific place] and [what you can do/see there]."
)


class TripPlanner:
    """Tracks destinations, travel dates, and planned activities."""

    def __init__(self):
        """Initialize an empty TripPlanner with no destinations or activities."""
        self.destinations = []
        self.itinerary = {}

    @tool
    def add_destination(self, city: str, start_date: str, end_date: str) -> str:
        """Add a destination to the trip with travel dates."""
        self.destinations.append(city)
        self.itinerary[city] = {
            "start_date": start_date,
            "end_date": end_date,
            "activities": [],
        }
        return f"{city} added to your trip from {start_date} to {end_date}."

    @tool
    def add_activity(self, city: str, activity: str) -> str:
        """Add an activity to a city's itinerary."""
        if city in self.itinerary:
            self.itinerary[city]["activities"].append(activity)
            return f"Added activity '{activity}' to {city} itinerary."
        return f"{city} is not in your trip."

    @tool
    def view_itinerary(self) -> str:
        """Generate a human-readable summary of the entire trip itinerary."""
        summary = ""
        for city, details in self.itinerary.items():
            summary += f"{city} ({details['start_date']} to {details['end_date']}):\n"
            for activity in details["activities"]:
                summary += f"  - {activity}\n"
        return summary if summary else "No destinations planned yet."


@tool
def suggest_activity(destination: str, agent: Agent) -> str:
    """Suggest a key activity for a given destination using the agent's model."""

    # Fill in the destination in the instruction
    prompt = SUGGESTION_INSTRUCTION.format(destination=destination)

    # Create a temporary agent with just the model for this generation
    temp_agent = Agent(model=agent.model)
    suggestion = temp_agent(prompt)

    return f"Suggestion for {destination}: {suggestion}"


if __name__ == "__main__":
    # Define the model for the agents
    model = BedrockModel(
        model_id="amazon.nova-lite-v1:0", temperature=0.7, max_tokens=3000
    )

    # Define planner and agent
    planner = TripPlanner()
    agent = Agent(
        tools=[
            suggest_activity,
            planner.add_destination,
            planner.add_activity,
            planner.view_itinerary,
        ],
        model=model,
    )

    # Example Usage
    response = agent("Add Tokyo as a destination from 2025-10-01 to 2025-10-07")
    response = agent("Suggest an activity for Tokyo and add it to my itinerary")
    response = agent("Show me my complete travel itinerary")
