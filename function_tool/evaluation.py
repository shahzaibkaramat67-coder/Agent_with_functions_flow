# function_tool/evaluation.py

from Agentic_Agent.model import ensure_llm
import json


def evaluation(update_query, tool_result):

    print("=" * 10, "Evaluation", "=" * 10)

    llm = ensure_llm()

    prompt = f"""
You are an Evaluation Agent.

Your responsibility is to decide whether the user's request can be FULLY completed using the current tool results.

Do NOT check whether the tool results contain some relevant information.

Instead determine whether a complete, high-quality final answer can be generated.

Evaluation Process:

1. Identify the user's goals.
2. Identify what information is already available.
3. Identify what information is still missing.
4. Determine whether all user goals can be fulfilled.
5. Determine whether another search would likely improve the answer.

Rules:

- Return enough_information = true ONLY if every user goal can be completed.
- Return enough_information = false if important information is missing.
- Comparisons require enough information about all compared items.
- Recommendations require enough evidence to justify the recommendation.
- If the answer would be incomplete, return false.

Return ONLY valid JSON.

{{
    "enough_information": true,
    "reason": ""
}}

OR

{{
    "enough_information": false,
    "reason": "Explain what information is missing."
}}

User Query:
{update_query}

Tool Result:
{tool_result}
"""

    response = llm.invoke(prompt)

    print("response from evaluation function ", response)

    return json.loads(response)
