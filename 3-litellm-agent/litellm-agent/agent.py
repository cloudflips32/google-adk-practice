import os
import random

from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

model = LiteLlm(
  model="openrouter/openai/gpt-4o-mini",
  api_key=os.environ["OR_API_KEY"],
)

def get_dad_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a boomerang that doesn't come back? A stick.",
        "What do you call a fish with no eyes? A fsh.",
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call a bear with no teeth? A gummy bear.",
        "Why don't bachelors like Git? Because they are afraid of committing.",
        "What do you call a computer that sings? A Dell.",
        "Why don't skeletons fight each other? They don't have the guts.",
    ]
    return random.choice(jokes)

root_agent = Agent(
    name='dad_joke_agent',
    model=model,
    description='Agent that generates dad jokes.',
    instruction="""
    You are a helpful assistant that generates dad some top-notch, off-the-wall dad jokes.
    Only use our `get_dad_joke` tool to generate jokes.
    """,
    tools=[get_dad_joke],
)
