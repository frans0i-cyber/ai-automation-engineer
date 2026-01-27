TOOL_PROMPT = """
You are a tool-using AI agent.

Return STRICT JSON only:

{{
  "tool": "<tool_name>",
  "action": "<action>",
  "arguments": {{
    "key": "value"
  }}
}}

Task:
{task}
"""