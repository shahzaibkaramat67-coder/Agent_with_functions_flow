from tavily import TavilyClient
import os


def search(query: str):
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        return "TAVILY_API_KEY is missing. Add it in the sidebar or .env file to enable web search."

    search_client = TavilyClient(api_key=api_key)

    print("=" * 10, "API TOOL", "=" * 10)

    try:
        response = search_client.search(query=query, max_results=5)
        context = ""

        for idx, result in enumerate(response["results"], start=1):
            context += f"""
Result {idx}

Title:
{result['title']}

Content:
{result['content']}

Source:
{result['url']}

{'=' * 50}
"""

        return context

    except Exception as exc:
        return f"API Error: {str(exc)}"
