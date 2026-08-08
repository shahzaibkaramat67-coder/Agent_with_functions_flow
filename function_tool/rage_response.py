from Agentic_Agent.model import ensure_llm


def Rag_response(template):
    llm = ensure_llm()

    system_prompt = f"""
    
    you are professioanl agent 
    you will get templete where will a query and content you have 
    to answer it like a professioanl
    
    
    template : {template}
    
    """

    response = llm.invoke(system_prompt)
    return response
