import json
import os
from dotenv import load_dotenv
from google import genai
from prompts import TOOL_PROMPT

load_dotenv(".env")

_client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def decide_tool(task: str) -> dict:
    prompt = TOOL_PROMPT.format(task=task)

    response = _client.models.generate_content(
        model="models/gemini-3-flash-preview",
        contents=prompt,
    )

    raw = response.text.strip()
    print("🧠 RAW MODEL OUTPUT:\n", raw)

    try:
        decision = json.loads(raw)
    except json.JSONDecodeError:
        raise ValueError(f"❌ Invalid JSON returned:\n{raw}")

    required_keys = {"tool", "action", "arguments"}
    if not required_keys.issubset(decision):
        raise KeyError(f"❌ Missing keys in decision: {decision}")

    return decision