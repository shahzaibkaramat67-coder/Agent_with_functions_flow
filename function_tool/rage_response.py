from Agentic_Agent.model import llm


def Rag_response(template):
    system_prompt = f"""
    
    you are professioanl agent 
    you will get templete where will a query and content you have 
    to answer it like a professioanl
    
    
    template : {template}
    
    """

    response = llm.invoke(system_prompt)
    return response
