import json
import os
from dotenv import load_dotenv
from google import genai
from prompts import ROUTER_PROMPT

load_dotenv(".env")

# ✅ THIS WAS MISSING
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def route_task(task):
    prompt = ROUTER_PROMPT.format(task=task)

    response = client.models.generate_content(
        model="models/gemini-3-flash-preview",
        contents=prompt
    )

    raw = (
        response.text
        or response.candidates[0].content.parts[0].text
    ).strip()

    print("RAW MODEL OUTPUT:\n", raw)

    try:
        decision = json.loads(raw)
    except json.JSONDecodeError:
        raise ValueError(f"Model did not return valid JSON:\n{raw}")

    if "chosen_agent" not in decision:
        raise KeyError(f"'chosen_agent' missing in response: {decision}")

    return decision