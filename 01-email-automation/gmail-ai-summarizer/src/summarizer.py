import json
import os
from dotenv import load_dotenv
from google import genai

load_dotenv(".env")

api_key = os.getenv("GOOGLE_API_KEY")
assert api_key, "GOOGLE_API_KEY is not loaded"

client = genai.Client(api_key=api_key)

def summarize_emails(emails):
    content = "\n\n".join(
        f"From: {e['from']}\nSubject: {e['subject']}\nBody: {e['body']}"
        for e in emails
    )

    prompt = f"""
You are an assistant that summarizes emails.

Return the result STRICTLY as valid JSON.
Do not add explanations.
Do not use markdown.

JSON format:
{{
  "key_points": [],
  "action_items": [],
  "urgent_messages": []
}}

Emails:
{content}
"""

    response = client.models.generate_content(
    model="models/gemini-3-flash-preview",
    contents=prompt,
)

    return json.loads(response.text)