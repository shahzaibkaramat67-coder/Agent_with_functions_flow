# function_tool/evaluation.py

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
        return {"enough_information": False, "reason": "LLM returned invalid JSON."}


def evaluation(update_query, tool_result):

    print("=" * 10, "Evaluation", "=" * 10)

    llm = ensure_llm()

    prompt = f"""
You are an Evaluation Agent.

STRICT RULES:
1. Return valid JSON only.
2. No markdown.
3. No code fences.
4. No prose outside JSON.
5. Use exact keys: "enough_information" and "reason".
6. enough_information must be true or false.

Decide whether the current tool result can fully answer the user's request.

User Query:
{update_query}

Tool Result:
{tool_result}

Return exactly one of these formats:
{{"enough_information": true, "reason": ""}}
{{"enough_information": false, "reason": "Explain what information is missing."}}

IMPORTANT: Return only raw JSON.
"""

    response = llm.invoke(prompt)
    print("response from evaluation function ", response)

    return _parse_json_response(response)
