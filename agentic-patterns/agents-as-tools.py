"""Example of agents as tools usage for HR Management."""
import os

from dotenv import load_dotenv
from strands import Agent, tool
from strands_tools import retrieve, http_request
from strands.models import BedrockModel

# Define the model for the agents
MODEL = BedrockModel(model_id="amazon.nova-lite-v1:0", temperature=0.7, max_tokens=3000)

# Define knowledge base
load_dotenv()
os.environ["KNOWLEDGE_BASE_ID"] = os.getenv("STRANDS_KNOWLEDGE_BASE_ID")
os.environ["AWS_REGION"] = os.getenv("STRANDS_KNOWLEDGE_BASE_REGION")

# Define prompts
EMPLOYEE_DATA_PROMPT = """
You are an Employee Data Specialist. You have access to employee records and company knowledge base.
Use the retrieve tool to search for relevant information from company documents, org charts, 
job descriptions, and employee databases.

Always be professional and respect employee privacy - only share information that would 
be appropriate for HR or management purposes.
"""

HR_ORCHESTRATOR_PROMPT = """
You are an HR Management Assistant that coordinates various HR functions. You have access to 
specialized HR agents that can help with different aspects of human resources management:

1. Employee Data Assistant - Employee records, organizational charts, department information
2. Leave Management Assistant - PTO, vacation requests, sick leave, time off policies  
3. Performance Review Assistant - Performance reviews, goal setting, career development
4. Recruitment Assistant - Hiring, job postings, candidate evaluation, recruitment strategy

When you receive a query, determine which specialist(s) can best help and route the request 
appropriately. You can also coordinate between multiple specialists if needed for complex requests.

Always maintain professionalism and respect employee privacy and confidentiality.
"""

RECRUITMENT_PROMPT = """
You are a Recruitment Specialist. You help with hiring processes, candidate evaluation,
job posting creation, and recruitment strategy. You understand job requirements and
can match candidates to positions effectively.

Focus on:
- Job requirement analysis
- Candidate screening criteria
- Interview question preparation
- Recruitment process optimization
- Diversity and inclusion in hiring
"""

LEAVE_MANAGEMENT_PROMPT = """
You are a Leave Management Specialist. You handle all aspects of employee time off.
Use the retrieve tool to access company leave policies, holiday calendars, and approval workflows.
"""

PERFORMANCE_REVIEW_PROMPT = """
You are a Performance Management Specialist. You handle performance reviews, goal setting,
and career development using company resources and best practices.
Always search for the latest company guidelines and templates before providing advice.
Focus on objective, constructive feedback aligned with company values and processes.
"""


@tool
def employee_data_assistant(query: str) -> str:
    """
    Handle employee data queries like finding employee information, department searches,
    organizational charts, and basic employee record management.
    """
    try:
        employee_agent = Agent(
            model=MODEL, system_prompt=EMPLOYEE_DATA_PROMPT, tools=[retrieve]
        )

        # Let the agent use retrieve to search company knowledge base
        enhanced_query = f"Search company knowledge base for: {query}"

        response = employee_agent(enhanced_query)
        return str(response)
    except Exception as e:
        return f"Error in employee data assistant: {str(e)}"


@tool
def leave_management_assistant(query: str) -> str:
    """
    Handle leave and PTO related queries including checking balances, submitting requests,
    approving time off, and providing leave policy information.
    """
    try:
        leave_agent = Agent(
            model=MODEL, system_prompt=LEAVE_MANAGEMENT_PROMPT, tools=[retrieve]
        )

        # First search company knowledge base, then supplement with current data
        enhanced_query = f"First, search company knowledge base for leave policies and procedures related to: {query}"

        response = leave_agent(enhanced_query)
        return str(response)
    except Exception as e:
        return f"Error in leave management assistant: {str(e)}"


@tool
def performance_review_assistant(query: str) -> str:
    """
    Handle performance review queries including review scheduling, performance analysis,
    goal setting, and career development planning.
    """
    try:
        performance_agent = Agent(
            model=MODEL, system_prompt=PERFORMANCE_REVIEW_PROMPT, tools=[retrieve]
        )

        # Search company knowledge base first, then use current data
        enhanced_query = f"Search company knowledge base for performance management resources related to: {query}"

        response = performance_agent(enhanced_query)
        return str(response)
    except Exception as e:
        return f"Error in performance review assistant: {str(e)}"


@tool
def recruitment_assistant(query: str) -> str:
    """
    Handle recruitment and hiring queries including job postings, candidate evaluation,
    interview processes, and hiring decisions.
    """
    try:
        recruitment_agent = Agent(
            model=MODEL,
            system_prompt=RECRUITMENT_PROMPT,
            tools=[retrieve, http_request],
        )

        response = recruitment_agent(query)
        return str(response)
    except Exception as e:
        return f"Error in recruitment assistant: {str(e)}"


if __name__ == "__main__":
    # Create the main orchestrator agent
    hr_orchestrator = Agent(
        model=MODEL,
        system_prompt=HR_ORCHESTRATOR_PROMPT,
        callback_handler=None,
        tools=[
            employee_data_assistant,
            leave_management_assistant,
            performance_review_assistant,
            recruitment_assistant,
        ],
    )

    # Example for employee lookup
    response = hr_orchestrator(
        "Can you find information about Sarah Johnson and tell me about her role and performance?"
    )

    # Example for leave request
    response = hr_orchestrator(
        "What is Mike Chen's current PTO balance and does he have any pending leave requests?"
    )

    # Example for performance review
    response = hr_orchestrator(
        "I need to prepare for Sarah Johnson's upcoming performance review. What are her current goals and recent achievements?"
    )

    # Example for recruitment query
    response = hr_orchestrator(
        "We need to hire a new software engineer for the Engineering team. What skills should we look for based on our current team composition?"
    )

    # Example with policy lookup
    response_policy = hr_orchestrator(
        "What is our current remote work policy and how many days per week can employees work from home?"
    )

    # Example with template search
    response_template = hr_orchestrator(
        "I need to conduct a performance review for a Software Engineer. Can you find our performance review template and suggest key areas to evaluate?"
    )

    # Example with compliance search
    response_compliance = hr_orchestrator(
        "What are the legal requirements for conducting layoffs in California, and do we have internal guidelines for this process?"
    )
