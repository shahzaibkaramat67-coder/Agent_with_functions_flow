# function_tool/tool_function.py

from Agentic_Agent.model import ensure_llm
import json


def Tool_function(query):

    print("=" * 10, "Tool Selector", "=" * 10)

    llm = ensure_llm()

    prompt = f"""
You are a Tool Selection Agent.

Your job:
1. Understand the user's request.
2. Select the best available tool.
3. if tool not require then in "tool_name" return none
4. Create a concise tool query.
5. Return ONLY valid JSON.

Available Tools
---------------

SEARCH
Use for:
- internet information
- jobs
- companies
- news
- people
- tutorials
- programming help
- current events
- research
- public information

RAG
Use for:
- uploaded PDFs
- vector databases
- internal documents
- knowledge bases
- document retrieval

Rules
-----

1. Always choose exactly one tool.
2. If information is likely on the internet → SEARCH.
3. If information is inside documents → RAG.
4. Create a search query optimized for the selected tool.
5. Never explain your reasoning.
6. Return ONLY valid JSON.

Output Format

Return ONLY valid JSON.
Do not use markdown.
Do not use ```json fences.

{{
    "tool_name": "SEARCH",
    "query": "optimized query"
}}

User Query:
{query}
"""

    response = llm.invoke(prompt)

    print("response this is tool function", response)

    return json.loads(response)
