# LiteLLM Agent

This project demonstrates how to create a Google ADK agent using the LiteLLM model wrapper, which allows you to use various LLM providers through a unified interface.

## Overview

The LiteLLM agent is a Google ADK agent configured to use the `LiteLlm` model wrapper, which enables using different LLM providers (like OpenAI, Anthropic, etc.) through OpenRouter. This example demonstrates:
- Configuring a LiteLLM model with OpenRouter
- Creating a custom tool (`get_dad_joke`)
- Building an agent that uses the tool to generate dad jokes

## Structure

```
3-litellm-agent/
├── README.md
└── litellm-agent/
    ├── __init__.py
    └── agent.py
```

## Components

### Agent Configuration (`litellm-agent/agent.py`)

The agent is configured with:
- **Model**: `LiteLlm` wrapper using `openrouter/openai/gpt-4o-mini`
- **Name**: `dad_joke_agent`
- **Description**: Agent that generates dad jokes
- **Tools**: `get_dad_joke` custom tool

### LiteLLM Model Setup

The agent uses the `LiteLlm` model wrapper from Google ADK, which provides a unified interface for various LLM providers:

```python
from google.adk.models.lite_llm import LiteLlm

model = LiteLlm(
    model="openrouter/openai/gpt-4o-mini",
    api_key=os.environ["OR_API_KEY"],
)
```

**Note**: You'll need to set the `OR_API_KEY` environment variable with your OpenRouter API key.

### Custom Tool: `get_dad_joke`

A custom tool function that returns a random dad joke from a predefined list:

```python
def get_dad_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a boomerang that doesn't come back? A stick.",
        # ... more jokes
    ]
    return random.choice(jokes)
```

The agent is instructed to only use this tool to generate jokes.

## Usage

### Prerequisites

1. Set up your OpenRouter API key:
   ```bash
   export OR_API_KEY="your-openrouter-api-key"
   ```

   Or on Windows:
   ```powershell
   $env:OR_API_KEY="your-openrouter-api-key"
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Importing the Agent

```python
from litellm_agent import agent

# Access the agent
agent.root_agent
```

### Example Usage

```python
from litellm_agent import agent

# The agent will use its tool to generate a dad joke
response = agent.root_agent.run("Tell me a dad joke!")
```

## Dependencies

The project requires the following dependencies (from `requirements.txt`):
- `google-adk[database]==1.0.0`
- `litellm==1.55.10` - LiteLLM library for unified LLM access
- `google-generativeai==0.21.1`
- `python-dotenv==1.1.0`
- `psutil==6.1.1`

## Key Features

- **Unified LLM Interface**: Uses LiteLLM to access various LLM providers through OpenRouter
- **Custom Tools**: Demonstrates how to create and use custom tools with agents
- **Model Flexibility**: Easy to switch between different models by changing the model string

## Supported Models

Through OpenRouter, you can use various models. Some examples:
- `openrouter/openai/gpt-4o-mini` (default in this example)
- `openrouter/anthropic/claude-3.5-sonnet`
- `openrouter/google/gemini-pro`
- And many more...

Check [OpenRouter's model list](https://openrouter.ai/models) for all available models.

## Configuration

To use a different model, simply modify the model string in `agent.py`:

```python
model = LiteLlm(
    model="openrouter/anthropic/claude-3.5-sonnet",  # Change this
    api_key=os.environ["OR_API_KEY"],
)
```

## Next Steps

- Experiment with different models through OpenRouter
- Add more tools to expand the agent's capabilities
- Implement more complex tool interactions
- Explore other features of the LiteLLM wrapper

