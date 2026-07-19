from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
    WebBaseLoader,
)


def file_loaders(file_path):

    if file_path.endswith(".pdf"):
        return PyPDFLoader(file_path).load()

    elif file_path.endswith(".txt"):
        return TextLoader(file_path).load()

    elif file_path.endswith(".docx"):
        return Docx2txtLoader(file_path).load()

    elif file_path.startswith("http"):
        return WebBaseLoader(file_path).load()

    else:
        return None
