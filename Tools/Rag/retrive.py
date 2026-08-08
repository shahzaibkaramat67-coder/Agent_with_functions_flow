from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from function_tool.rage_response import Rag_response
import os


def retriver_ChromaDB(query):
    try:
        model = os.getenv(
            "EMBADDING_MODEL_SENTENCE", "sentence-transformers/all-MiniLM-L6-v2"
        )
        embedding_model = HuggingFaceEmbeddings(model=model)

        persist_directory = os.path.join("data", "chroma_db")
        vectorStore = Chroma(
            embedding_function=embedding_model,
            persist_directory=persist_directory,
        )

        retriever = vectorStore.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 3, "fetch_k": 5, "lambda_mult": 0.7},
        )

        template = ChatPromptTemplate.from_template(
            [
                (
                    "system",
                    """ 
                    You are a helpful AI assistant. Use only the provided context to answer the question.
                    If the answer is not present in the context, say 'I could not find the answer in the document.'
                    """,
                ),
                ("human", "user Question: {query}\n\nContext:\n{content}"),
            ]
        )

        relevant_docs = retriever.invoke(query)
        content = "\n\n".join(doc.page_content for doc in relevant_docs)

        prompt = template.invoke({"query": query, "content": content})
        return Rag_response(prompt)
    except Exception as exc:
        return f"RAG Error: {str(exc)}"
