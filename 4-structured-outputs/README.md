# Email Agent

The `email_agent` is a specialized AI agent designed to generate professional emails based on user queries. It leverages the `gemini-2.5-flash` model to produce structured outputs containing a subject line and an email body.

## Features

- **Structured Output**: Returns a JSON object with `subject` and `body` fields, ensuring easy integration with other systems.
- **Professional Tone**: Capable of adapting tone (formal, friendly) based on the context, though primarily focused on professional communication.
- **Schema Validation**: Uses Pydantic models to enforce the output structure.

## Usage

The agent is defined in `email_agent/agent.py` as `root_agent`.

### Input
A natural language query describing the email to be generated (e.g., "Write a follow-up email to a client about the project proposal").

### Output Schema
The agent returns data adhering to the `EmailContent` schema:

```python
class EmailContent(BaseModel):
    subject: str = Field(description="The subject of the email. This field should be concise and descriptive.")
    body: str = Field(description="The body of the email. Proper formatting, paragraphs, signature should be present.")
```

### Example Output

```json
{
  "subject": "Project Proposal Follow-up",
  "body": "Dear Client,\n\nI hope this email finds you well..."
}
```
