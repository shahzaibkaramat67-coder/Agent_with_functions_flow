from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()


def get_llm():
    api_key = os.getenv("GEMINI_NEW_API_KEY")
    # print("GEMINI_API_KEY exists:", bool(os.getenv("GEMINI_API_KEY")))
    # print("GOOGLE_API_KEY exists:", bool(os.getenv("GOOGLE_API_KEY")))

    if not api_key:
        return None

    return GoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
    )


llm = get_llm()


def ensure_llm():
    if llm is None:
        raise ValueError(
            "GEMINI_API_KEY is not configured. Add it in the Streamlit sidebar or .env file."
        )
    return llm
