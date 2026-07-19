from Tools.search.search import search
from Tools.Rag.retrive import retriver_ChromaDB

# from function_tool.final_result import final_result


def Tool_run(tool_name, query):

    tool_name = tool_name.lower()

    if tool_name == "search":
        tool_result = search(query)
    elif tool_name == "Rag":
        tool_result = retriver_ChromaDB(query)
    elif tool_name == "none":
        return "none"

    return tool_result
