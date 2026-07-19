# from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

import os


def createChromaDB(file):

    # document = docuemt_load.load()
    # docuemt_load = PyPDFLoader(file_path)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size="700", chunk_overlap="100"
    )

    chunk = text_splitter.split_documents(documents=file)

    model_name = os.getenv("EMBADDING_MODEL_SENTENCE")

    embadding_model = HuggingFaceEmbeddings(model_name=model_name)

    Chroma.from_documents(
        document=chunk,
        embedding_function=embadding_model,
        persist_directory="Agent/Agentic_Agent/ChromaDB",
    )
