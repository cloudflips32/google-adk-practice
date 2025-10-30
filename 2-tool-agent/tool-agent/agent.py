from datetime import datetime
from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

def getCurrentTime(format: str) -> dict:
    """ Get the current time in the format YYYY-MM-DD HH:MM:SS """
    return {
        "currentTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Tool agent.',
    instruction="""
    You are a helpful assistant that can use the following tools: - google_search
    """,
    tools=[getCurrentTime],
    # tools=[google_search], <- Works!
    # tools=[getCurrentTime], <- Works!
    
    # tools=[google_search, getCurrentTime], <- Does not work !@!@!@!@!@$%^@&$$%$!@`1`
)
