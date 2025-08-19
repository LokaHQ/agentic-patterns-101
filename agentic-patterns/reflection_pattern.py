from pydantic import BaseModel, Field
from strands import Agent
from strands.models import BedrockModel


class JudgeOutput(BaseModel):
    """
    Model representing the feedback assessment from the judge agent.
    """

    needs_improvement: bool = Field(
        ..., description="Indicates if the screenwriting needs improvement."
    )
    feedback: str = Field(..., description="Feedback on the agent's screenwriting.")


if __name__ == "__main__":
    """
    Main entry point for the screenwriting assistant.
    """

    # Definining Agent
    agent = Agent(
        model=BedrockModel(
            model_id="amazon.nova-pro-v1:0",
            temperature=0.9,
        ),
        system_prompt="You are a screenwriting assistant. Help users create scripts, dialogues, and storylines. Critique existing works when asked to and provide suggestions for improvement.",
    )

    # User query
    user_query = "Write a dialogue between two characters. It needs to be a gripping thrilling scene."

    # Get initial screenwriting
    screenwriting = agent(user_query)

    # Run reflection_loop
    iteration = 1
    max_iterations = 3
    while iteration <= max_iterations:
        # Get feedback
        feedback_query = (
            "Please check this dialogue, and unless it's perfect, provide feedback: "
            + str(screenwriting)
        )
        feedback = agent.structured_output(JudgeOutput, feedback_query)

        # Check if feedback is needed
        if not feedback.needs_improvement:
            print("No feedback provided. Ending the loop.")
            break

        print("User feedback received. Processing...")

        # Adding feedback to screenwriting iteration
        screenwriting_feedback = (
            "Make this screenwriting better: "
            + str(screenwriting)
            + "\n With the following feedback: "
            + feedback.feedback
        )
        screenwriting = agent(screenwriting_feedback)

        iteration += 1
