import os
from typing import Annotated, TypedDict
from dotenv import load_dotenv

from openai import OpenAI
from langchain_openai import ChatOpenAI

from langgraph.graph import StateGraph, END
from langchain_community.tools.tavily_search import TavilySearchResults

# Load environment variables from .env file
load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
tavily = os.getenv("TAVILY_API_KEY")

llm_name = "gpt-4o-mini"

client = OpenAI(api_key=openai_key)
model = ChatOpenAI(api_key=openai_key, model=llm_name)

# STEP 1: Build a Basic Chatbot
from langgraph.graph.message import add_messages


class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

# create tools
tool = TavilySearchResults(max_results=2)
tools = [tool]
# rest = tool.invoke("What is the capital of France?")
# print(rest)

model_with_tools = model.bind_tools(tools)

# Below, implement a BasicToolNode that checks the most recent
# message in the state and calls tools if the message contains tool_calls
import json
from langchain_core.messages import ToolMessage
from langgraph.prebuilt import ToolNode, tools_condition


def bot(state: State):
    # print(state.items())
    print(state["messages"])
    return {"messages": [model_with_tools.invoke(state["messages"])]}

# instantiate the ToolNode with the tools
tool_node = ToolNode(tools=[tool])
graph_builder.add_node("tools", tool_node)  # Add the node to the graph

# The `tools_condition` function returns "tools" if the chatbot asks to use a tool, and "__end__" if
# it is fine directly responding. This conditional routing defines the main agent loop.
graph_builder.add_conditional_edges(
    "bot",
    tools_condition,
)

# The first argument is the unique node name
# The second argument is the function or object that will be called whenever
# the node is used.
graph_builder.add_node("bot", bot)

# STEP 3: Add an entry point to the graph
graph_builder.set_entry_point("bot")

# STEP 4: Compile the graph
graph = graph_builder.compile()

res = graph.invoke({"messages": ["what is the capital of France? search by tavily"]})
print(res["messages"])

# while True:
#     user_input = input("User: ")
#     if user_input.lower() in ["quit", "exit", "q"]:
#         print("Goodbye!")
#         break
#     for event in graph.stream({"messages": ("user", user_input)}):
#         for value in event.values():
#             print("Assistant:", value["messages"][-1].content)
