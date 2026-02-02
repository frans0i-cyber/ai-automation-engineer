import os
import json
from dotenv import load_dotenv
from google import genai
from .prompts import PLANNER_PROMPT

load_dotenv(".env")

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def create_plan(task: str):
    prompt = PLANNER_PROMPT.format(task=task)

    response = client.models.generate_content(
        model="models/gemini-3-flash-preview",
        contents=prompt
    )

    raw = response.text.strip()
    print("RAW MODEL OUTPUT:\n", raw)

    plan = json.loads(raw)

    if "plan" not in plan:
        raise ValueError("Missing plan in response")

    return plan