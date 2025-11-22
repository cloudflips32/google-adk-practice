# Tool Agent

This project demonstrates how to create a Google ADK agent that can use custom tools and built-in tools like Google Search.

## Overview

The tool agent is a Google ADK agent configured to use various tools. It demonstrates:
- Creating custom tools (like `getCurrentTime`)
- Using built-in tools (like `google_search`)
- Combining tools in an agent configuration

## Structure

```
2-tool-agent/
├── README.md
└── tool-agent/
    ├── __init__.py
    └── agent.py
```

## Components

### Agent Configuration (`tool-agent/agent.py`)

The agent is configured with:
- **Model**: `gemini-2.5-flash`
- **Name**: `root_agent`
- **Description**: Tool agent
- **Tools**: Currently configured to use the `getCurrentTime` custom tool

### Custom Tool: `getCurrentTime`

A custom tool function that returns the current time in `YYYY-MM-DD HH:MM:SS` format.

```python
def getCurrentTime(format: str) -> dict:
    """ Get the current time in the format YYYY-MM-DD HH:MM:SS """
    return {
        "currentTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
```

### Built-in Tool: `google_search`

The agent can also use the built-in `google_search` tool from `google.adk.tools`.

## Usage

### Importing the Agent

```python
from tool_agent import agent

# Access the agent
agent.root_agent
```

### Tool Configuration Notes

Based on the code comments in `agent.py`:

- ✅ `tools=[google_search]` - Works individually
- ✅ `tools=[getCurrentTime]` - Works individually  
- ❌ `tools=[google_search, getCurrentTime]` - Currently does not work when combined

**Note**: There appears to be an issue when combining multiple tools in the tools array. The agent works correctly with individual tools but encounters problems when both `google_search` and `getCurrentTime` are included together.

## Dependencies

The project requires the following dependencies (from `requirements.txt`):
- `google-adk[database]==1.0.0`
- `yfinance==0.2.56`
- `python-dotenv==1.1.0`
- `psutil==6.1.1`
- `litellm==1.55.10`
- `google-generativeai==0.21.1`

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure you have the necessary environment variables and API keys configured for Google ADK.

## Example Usage

```python
from tool_agent import agent

# The agent is now ready to use
# It can be invoked with queries that require tool usage
response = agent.root_agent.run("What time is it?")
```

## Known Issues

- Combining multiple tools (`google_search` and `getCurrentTime`) in the same tools array does not work correctly. Use tools individually until this issue is resolved.

## Next Steps

- Investigate why combining multiple tools causes issues
- Test with additional custom tools
- Explore other built-in tools available in `google.adk.tools`

