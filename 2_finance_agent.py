from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools
import os

load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

agent=Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True,stock_fundamentals=True,analyst_recommendations=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display data."]
)

agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA")