# function_tool/updateQuery.py

from Agentic_Agent.model import llm


def updateQuery(user_input):

    print("=" * 10, "Update Query", "=" * 10)

    prompt = f"""
You are a professional query rewriting agent.

Your task:
- Rewrite the user's query.
- Make it clear.
- Make it specific.
- Preserve the original meaning.

Rules:
- Do not answer.
- Do not explain.
- Return only the rewritten query.

User Query:
{user_input}
"""

    response = llm.invoke(prompt)
    print("response update Query", response)

    return response
