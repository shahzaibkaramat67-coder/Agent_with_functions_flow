from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()


def resolve_google_key():
    return os.getenv("GEMINI_NEW_API_KEY")


def resolve_model_name():
    return (
        os.getenv("GEMINI_API_MODEL")
        or os.getenv("GEMINI_API_MODEL_LITE")
        or "gemini-2.5-flash"
    )


def get_llm():
    api_key = resolve_google_key()
    if not api_key:
        return None

    return GoogleGenerativeAI(
        model=resolve_model_name(),
        google_api_key=api_key,
    )


llm = None


def ensure_llm():
    global llm
    api_key = resolve_google_key()
    if not api_key:
        raise ValueError(
            "No valid Google Gemini API key found. Add GEMINI_NEW_API_KEY in the sidebar or .env file."
        )

    llm = get_llm()
    return llm
