import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

PROMPT = """
You are an email summarization agent.

Given an email, return STRICT JSON with:
- summary (string)
- action_items (array of strings)
- urgency (low, medium, high)

Email:
{email}
"""

def summarize_email(email: str):
    prompt = PROMPT.format(email=email)

    response = client.models.generate_content(
        model="models/gemini-3-flash-preview",
        contents=prompt
    )

    raw = response.text.strip()
    return json.loads(raw)