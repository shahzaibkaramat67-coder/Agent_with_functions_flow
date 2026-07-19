# function_tool/final_result.py

from Agentic_Agent.model import llm


def final_result(user_query, information):

    print("=" * 10, "Final Result", "=" * 10)

    prompt = f"""
You are a professional AI assistant.

Answer the user's query using the provided information.

User Query:
{user_query}

Information:
{information}
"""

    response = llm.invoke(prompt)

    print("response final result ", response)

    return response
