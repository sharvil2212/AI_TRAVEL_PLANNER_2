from langgraph.graph import StateGraph, END

from state import TravelState

from nodes import planner_node
from nodes import hotel_node
from nodes import budget_node

builder = StateGraph(TravelState)

builder.add_node("planner", planner_node)
builder.add_node("hotel", hotel_node)
builder.add_node("budget", budget_node)

builder.set_entry_point("planner")

builder.add_edge("planner", "hotel")
builder.add_edge("hotel", "budget")
builder.add_edge("budget", END)

graph = builder.compile()