from langchain_google_genai import GoogleGenerativeAI

# from langchain.agents import create_agent
from dotenv import load_dotenv
import os

load_dotenv()


# from langchain_ollama import ChatOllama

# llm = ChatOllama(model="qwen3:4b", temperature=0)


llm = GoogleGenerativeAI(
    model="gemini-2.5-flash-lite", google_api_key=os.getenv("GEMINI_API_KEY")
)
