from function_tool.updateQuery import updateQuery
from function_tool.final_result import final_result
from function_tool.tool_function import Tool_function
from function_tool.evaluation import evaluation
from function_tool.planner import Planner
from function_tool.tool_run import Tool_run


def entryPoint(user_input):

    print("here we enter in the model")

    update_query = updateQuery(user_input)

    max_iteration = 3

    steps = []

    print("update_query", update_query)

    for iteration in range(max_iteration):

        print(f"======== iteration NO {iteration} ========")

        Tool_info = Tool_function(update_query)

        tool_name = Tool_info["tool_name"]
        query = Tool_info["query"]

        tool_result = Tool_run(tool_name, query)

        current_step = {
            "iteration": iteration + 1,
            "updated_query": update_query,
            "tool_name": tool_name,
            "tool_query": query,
            "tool_result": tool_result,
        }

        if tool_result == "none":

            answer = final_result(update_query, "")

            return {"final_answer": answer, "steps": steps, "status": "completed"}

        evaluation_result = evaluation(update_query, tool_result)

        current_step["evaluation"] = evaluation_result

        print("evaluation_result", evaluation_result)

        steps.append(current_step)

        if evaluation_result["enough_information"]:

            answer = final_result(update_query, tool_result)

            return {"final_answer": answer, "steps": steps, "status": "completed"}

        print("Running Planner...")

        plan = Planner(update_query, tool_result, evaluation_result["reason"])

        print("planner_result", plan)

        current_step["planner"] = plan

        action = plan["action"]

        if action == "FINISH":

            answer = final_result(update_query, tool_result)

            return {"final_answer": answer, "steps": steps, "status": "completed"}

        if action in ["SEARCH", "RAG"]:

            update_query = plan["query"]

            continue

    return {
        "final_answer": "Unable to gather enough information.",
        "steps": steps,
        "status": "failed",
    }


# from function_tool.updateQuery import updateQuery

# from function_tool.final_result import final_result

# from function_tool.tool_function import Tool_function
# from function_tool.evaluation import evaluation

# from function_tool.planner import Planner
# from function_tool.tool_run import Tool_run
# import json

# import json

# # from Agentic_Agent.model import llm


# def entryPoint(user_input):
#     print("here we eenter in the model")
#     update_query = updateQuery(user_input)

#     max_itration = 3

#     print("update_query", update_query)
#     for itrate in range(max_itration):

#         print(f"======== itration NO {itrate} =======")
#         Tool_info = Tool_function(update_query)
#         # tool_result_json = json.loads(tool_result)

#         tool_name = Tool_info["tool_name"]
#         query = Tool_info["query"]
#         # function_tool
#         tool_result = Tool_run(tool_name, query)

#         if tool_result == "none":
#             return final_result(update_query)

#         evaluation_result = evaluation(update_query, tool_result)

#         print("evaluation_result", evaluation_result)

#         if evaluation_result["enough_information"]:
#             return final_result(update_query, tool_result)

#         print("Running Planner...")

#         plan = Planner(update_query, tool_result, evaluation_result["reason"])
#         print("planner_result", plan)

#         action = plan["action"]

#         if action == "FINISH":
#             return final_result(update_query, tool_result)

#         if action in ["SEARCH", "RAG"]:
#             update_query = plan["query"]
#             continue

#     return "Unable to gather enough information."
