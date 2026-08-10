# function_tool/tool_function.py

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
        # Force a valid fallback instead of crashing the app.
        return {"tool_name": "SEARCH", "query": ""}


def Tool_function(query):

    print("=" * 10, "Tool Selector", "=" * 10)

    llm = ensure_llm()

    prompt = f"""
You are a Tool Selection Agent.

STRICT RULES:
1. Output must be valid JSON only.
2. No markdown.
3. No code fences.
4. No explanation.
5. No extra text before or after JSON.
6. Use exact keys: "tool_name" and "query".
7. tool_name must be one of: "SEARCH", "RAG", or "NONE".
8. query must be a short optimized search query.

Choose the correct tool based on the user request.

User Query:
{query}

Return JSON in this exact format:
{{"tool_name": "SEARCH", "query": "optimized query"}}

IMPORTANT: Return only raw JSON. Do not wrap it in markdown or text.
"""

    response = llm.invoke(prompt)
    print("response this is tool function", response)

    return _parse_json_response(response)
