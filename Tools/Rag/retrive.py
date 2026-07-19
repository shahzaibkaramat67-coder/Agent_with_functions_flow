from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from function_tool.rage_response import Rag_response
import os


def retriver_ChromaDB(query):

    model = os.getenv("EMBADDING_MODEL_SENTENCE")
    Embedding_model = HuggingFaceEmbeddings(model=model)

    vectorStore = Chroma(
        embedding_function=Embedding_model,
        persist_directory="Agent/Agentic_Agent/ChromaDB",
    )

    retriver = vectorStore.as_retriever(
        search_type="mmr", search_kwargs={"k": 3, "fetch_k": 5, "lambda_mult": 0.7}
    )

    templetae = ChatPromptTemplate.from_template(
        [
            (
                "system",
                """ 
              you are a helpfull Ai Assistant use only the
               provided the context to answer the question 
               if the answer is not presnt in the context 
               say 'i could not find the answer in the document'
            """,
            ),
            ("human", "user Question {query} content {content}"),
        ]
    )

    retrive_query = retriver.invoke(query)

    content = " ".json(doc.page_content for doc in retrive_query)

    template = templetae.invoke({"query": query, "content": content})
    response = Rag_response(template)
    return response
