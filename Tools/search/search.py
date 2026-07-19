from tavily import TavilyClient
import os

search_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def search(query: str):

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

    except Exception as e:

        return f"API Error: {str(e)}"
