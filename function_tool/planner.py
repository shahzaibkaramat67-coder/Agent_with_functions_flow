# function_tool/planner.py

from Agentic_Agent.model import ensure_llm
import json


def _parse_json_response(raw_response):
    text = (
        raw_response.content if hasattr(raw_response, "content") else str(raw_response)
    )
    text = str(text).strip()

    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"action": "FINISH", "query": ""}


def Planner(user_query, tool_result, evaluation_reason):

    print("=" * 10, "Planner", "=" * 10)

    llm = ensure_llm()

    prompt = f"""
You are a Planning Agent.

STRICT RULES:
1. Output must be valid JSON only.
2. No markdown.
3. No code fences.
4. No explanation.
5. No extra text before or after the JSON.
6. Use exact keys: "action" and "query".
7. action must be one of: "SEARCH", "RAG", or "FINISH".

The previous attempt failed to gather enough information.

User Query:
{user_query}

Tool Result:
{tool_result}

Evaluation Reason:
{evaluation_reason}

Return one of these exact JSON structures:
{{"action": "SEARCH", "query": "new search query"}}
{{"action": "RAG", "query": "document query"}}
{{"action": "FINISH", "query": ""}}

IMPORTANT: Only return raw JSON. No commentary, no code fences, no markdown.
"""

    response = llm.invoke(prompt)
    print("Planner Response:", response)

    return _parse_json_response(response)
