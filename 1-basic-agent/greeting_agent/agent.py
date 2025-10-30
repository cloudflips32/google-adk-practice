from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.5-flash",
    description="A simple agent that greets the user",
    instructions="You are a greeting agent that always greets the user with a friendly message",
)