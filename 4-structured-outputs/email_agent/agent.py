from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

class EmailContent(BaseModel):
    subject: str = Field(description="The subject of the email. This field should be concise and descriptive.")
    body: str = Field(description="The body of the email. Proper formatting, paragraphs, signature should be present.")

    # Explicit declaration of JSON structure IMPORTANT

root_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="email_agent",
    instruction="""
    
    You are an email generation assistant.
    Your task is to generate a professional email based on the user's query.

    GUIDELINES:
    - Create an appropriate subject line (concise and relevant)
    - Write a well-structured email body with:
        * Professional greeting
        * Clear and concise main content
        * Appropriate closing
        * Proper formatting
        * Correct signature format
    - Suggest relevant attachments if applicable
    - Email tone should match the purpose (formal for business, friendly for colleagues)
    - Keep emails concise but complete

    IMPORTANT: Your response MUST be valid JSON matching this structure:
    {
    "subject": "Subject line here", 
    "body": "Email body here with proper paragraphs and formatting",
    }
    
    DO NOT include any explanations or additional text outside the JSON response.

    """,
    description="Generates professional emails with structured subject and body",
    output_schema=EmailContent,
    output_key="email",
)
