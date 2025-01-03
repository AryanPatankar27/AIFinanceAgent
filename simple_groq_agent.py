from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

agent=Agent(
    model=Groq(id="llama-3.3-70b-versatile")
)

agent.print_response("Write a 2 sentence poem between friendship of dosa and samosa")