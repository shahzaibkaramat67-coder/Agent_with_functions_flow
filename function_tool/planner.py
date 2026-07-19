# function_tool/planner.py

from Agentic_Agent.model import llm
import json


def Planner(user_query, tool_result, evaluation_reason):

    print("=" * 10, "Planner", "=" * 10)

    prompt = f"""
You are a Planning Agent.

The previous attempt failed to gather enough information.

Your task:
1. Analyze the user's original request.
2. Analyze the tool result.
3. Analyze the evaluation reason.
4. Decide the next best action.
5. Generate a better search query if another search is needed.

Available Actions:

1. SEARCH
   Use when more internet information is needed.

2. RAG
   Use when information should be searched from documents.

3. FINISH
   Use when no better action is possible.

Return ONLY valid JSON.

Output Format:


No explanation.
No markdown.
No extra text.

Return ONLY valid JSON.
Do not use markdown.
Do not use ```json fences.

{{
    "action": "SEARCH",
    "query": "new search query"
}}

OR

{{
    "action": "RAG",
    "query": "document query"
}}

OR

{{
    "action": "FINISH",
    "query": ""
}}

--------------------------------

User Query:
{user_query}

--------------------------------

Tool Result:
{tool_result}

--------------------------------

Evaluation Reason:
{evaluation_reason}

--------------------------------

Generate the next best action.
"""

    response = llm.invoke(prompt)

    print("Planner Response:", response)

    return json.loads(response)
