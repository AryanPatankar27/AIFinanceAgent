from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the GROQ API key from environment variables
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise EnvironmentError("GROQ_API_KEY not set. Please set the GROQ_API_KEY environment variable.")

# Define the Web Agent
web_agent = Agent(
    name="Web Agent",
    role="Search the web",
    model=Groq(id="llama-3.3-70b-versatile", api_key=GROQ_API_KEY),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    instructions=["Always include sources."],
    markdown=True,
)

# Define the Finance Agent
finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="llama-3.3-70b-versatile", api_key=GROQ_API_KEY),
    tools=[YFinanceTools(
        stock_price=True,
        company_info=True,
        analyst_recommendations=True
    )],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display data."]
)

# Create a list of agents to simulate a team of agents
agents = [web_agent, finance_agent]

# Define a function to handle agent interaction
def execute_agents_response(message):
    # Collect responses from each agent in the team
    responses = []
    for agent in agents:
        response = agent.print_response(message)
        responses.append(response)
    
    return responses

# Execute the command for both agents
responses = execute_agents_response("Summarize analyst recommendations and share the latest news for NVDA")

# Print the responses from all agents
for response in responses:
    print(response)
