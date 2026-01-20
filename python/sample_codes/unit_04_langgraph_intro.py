"""
Unit 4: Introduction to LangGraph
Sample Code Examples

This file demonstrates LangGraph fundamentals: states, nodes, edges, and workflows.
"""

from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END
import operator

# ============================================================================
# Example 1: Basic State Definition
# ============================================================================

class SimpleState(TypedDict):
    """A simple state with a counter."""
    count: int
    message: str


def example_1_basic_state():
    """Demonstrate basic state definition."""
    print("=" * 60)
    print("Example 1: Basic State Definition")
    print("=" * 60)
    
    # Create and use state
    state = SimpleState(count=0, message="Hello")
    print(f"\nInitialState: {state}")
    
    # Update state
    state["count"] = 5
    state["message"] = "Updated"
    print(f"Updated State: {state}\n")


# ============================================================================
# Example 2: Simple Linear Graph
# ============================================================================

class CounterState(TypedDict):
    count: Annotated[int, operator.add]
    messages: Annotated[list, operator.add]


def increment_node(state: CounterState) -> CounterState:
    """Node that increments the counter."""
    return {
        "count": 1,
        "messages": [f"Incremented to {state['count'] + 1}"]
    }


def double_node(state: CounterState) -> CounterState:
    """Node that doubles the counter."""
    new_count = state["count"] * 2
    return {
        "count": new_count,
        "messages": [f"Doubled to {new_count}"]
    }


def example_2_linear_graph():
    """Create a simple linear graph."""
    print("=" * 60)
    print("Example 2: Simple Linear Graph")
    print("=" * 60)
    
    # Create graph
    workflow = StateGraph(CounterState)
    
    # Add nodes
    workflow.add_node("increment", increment_node)
    workflow.add_node("double", double_node)
    
    # Define edges
    workflow.set_entry_point("increment")
    workflow.add_edge("increment", "double")
    workflow.add_edge("double", END)
    
    # Compile
    app = workflow.compile()
    
    # Run
    initial_state = {"count": 0, "messages": []}
    result = app.invoke(initial_state)
    
    print(f"\nInitial State: {initial_state}")
    print(f"Final State: {result}")
    print(f"\nMessages:")
    for msg in result["messages"]:
        print(f"  - {msg}")
    print()


# ============================================================================
# Example 3: Conditional Edges
# ============================================================================

class DecisionState(TypedDict):
    value: int
    path_taken: str
    is_even: bool


def check_even_node(state: DecisionState) -> DecisionState:
    """Check if value is even."""
    is_even = state["value"] % 2 == 0
    return {
        "value": state["value"],
        "is_even": is_even,
        "path_taken": ""
    }


def even_handler(state: DecisionState) -> DecisionState:
    """Handle even numbers."""
    return {
        "value": state["value"],
        "path_taken": "even_path",
        "is_even": state["is_even"]
    }


def odd_handler(state: DecisionState) -> DecisionState:
    """Handle odd numbers."""
    return {
        "value": state["value"],
        "path_taken": "odd_path",
        "is_even": state["is_even"]
    }


def route_based_on_parity(state: DecisionState) -> Literal["even", "odd"]:
    """Routing function for conditional edges."""
    return "even" if state["is_even"] else "odd"


def example_3_conditional_edges():
    """Demonstrate conditional routing."""
    print("=" * 60)
    print("Example 3: Conditional Edges")
    print("=" * 60)
    
    workflow = StateGraph(DecisionState)
    
    # Add nodes
    workflow.add_node("check", check_even_node)
    workflow.add_node("even", even_handler)
    workflow.add_node("odd", odd_handler)
    
    # Set entry point
    workflow.set_entry_point("check")
    
    # Add conditional edges
    workflow.add_conditional_edges(
        "check",
        route_based_on_parity,
        {
            "even": "even",
            "odd": "odd"
        }
    )
    
    # Both paths end
    workflow.add_edge("even", END)
    workflow.add_edge("odd", END)
    
    # Compile
    app = workflow.compile()
    
    # Test with even number
    print("\n--- Testing with even number (4) ---")
    result1 = app.invoke({"value": 4, "path_taken": "", "is_even": False})
    print(f"Result: {result1}")
    
    # Test with odd number
    print("\n--- Testing with odd number (7) ---")
    result2 = app.invoke({"value": 7, "path_taken": "", "is_even": False})
    print(f"Result: {result2}\n")


# ============================================================================
# Example 4: Loops and Cycles
# ============================================================================

class LoopState(TypedDict):
    count: int
    max_iterations: int
    history: Annotated[list, operator.add]


def process_node(state: LoopState) -> LoopState:
    """Process the current count."""
    new_count = state["count"] + 1
    return {
        "count": new_count,
        "max_iterations": state["max_iterations"],
        "history": [f"Iteration {new_count}"]
    }


def should_continue(state: LoopState) -> Literal["continue", "end"]:
    """Decide whether to continue or end."""
    if state["count"] < state["max_iterations"]:
        return "continue"
    else:
        return "end"


def example_4_loops():
    """Demonstrate cyclic graphs with loops."""
    print("=" * 60)
    print("Example 4: Loops and Cycles")
    print("=" * 60)
    
    workflow = StateGraph(LoopState)
    
    # Add processing node
    workflow.add_node("process", process_node)
    
    # Set entry point
    workflow.set_entry_point("process")
    
    # Add conditional edge that can loop back
    workflow.add_conditional_edges(
        "process",
        should_continue,
        {
            "continue": "process",  # Loop back
            "end": END
        }
    )
    
    # Compile
    app = workflow.compile()
    
    # Run with 5 iterations
    print("\n--- Running with max 5 iterations ---")
    result = app.invoke({
        "count": 0,
        "max_iterations": 5,
        "history": []
    })
    
    print(f"\nFinal count: {result['count']}")
    print(f"History:")
    for item in result["history"]:
        print(f"  {item}")
    print()


# ============================================================================
# Example 5: LangGraph with LLM
# ============================================================================

from langchain_community.llms import Ollama
import config

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    question: str
    answer: str


def llm_node(state: AgentState) -> AgentState:
    """Node that calls LLM."""
    llm = Ollama(model=config.ALTERNATIVE_LLM_MODEL, temperature=config.CREATIVE_TEMPERATURE)
    
    question = state["question"]
    response = llm.invoke(f"Answer this question briefly: {question}")
    
    return {
        "messages": [f"Q: {question}", f"A: {response}"],
        "question": question,
        "answer": response
    }


def example_5_llm_graph():
    """Use LLM in a LangGraph workflow."""
    print("=" * 60)
    print("Example 5: LangGraph with LLM")
    print("=" * 60)
    
    workflow = StateGraph(AgentState)
    
    # Add LLM node
    workflow.add_node("ask_llm", llm_node)
    
    # Simple linear flow
    workflow.set_entry_point("ask_llm")
    workflow.add_edge("ask_llm", END)
    
    # Compile
    app = workflow.compile()
    
    # Run with a question
    print("\n--- Asking LLM a question ---")
    result = app.invoke({
        "messages": [],
        "question": "What is LangGraph in one sentence?",
        "answer": ""
    })
    
    print(f"\nQuestion: {result['question']}")
    print(f"Answer: {result['answer']}\n")


# ============================================================================
# Example 6: Multi-Step Reasoning Graph
# ============================================================================

class ReasoningState(TypedDict):
    task: str
    plan: str
    execution: str
    result: str


def plan_node(state: ReasoningState) -> ReasoningState:
    """Create a plan for the task."""
    llm = Ollama(model=config.ALTERNATIVE_LLM_MODEL, temperature=config.PRECISE_TEMPERATURE)
    
    task = state["task"]
    plan = llm.invoke(f"Create a step-by-step plan to: {task}")
    
    return {
        "task": task,
        "plan": plan,
        "execution": "",
        "result": ""
    }


def execute_node(state: ReasoningState) -> ReasoningState:
    """Execute the plan."""
    llm = Ollama(model=config.ALTERNATIVE_LLM_MODEL, temperature=config.PRECISE_TEMPERATURE)
    
    execution = llm.invoke(f"Execute this plan:\n{state['plan']}")
    
    return {
        "task": state["task"],
        "plan": state["plan"],
        "execution": execution,
        "result": ""
    }


def summarize_node(state: ReasoningState) -> ReasoningState:
    """Summarize the result."""
    llm = Ollama(model=config.ALTERNATIVE_LLM_MODEL, temperature=config.PRECISE_TEMPERATURE)
    
    result = llm.invoke(f"Summarize the outcome:\n{state['execution']}")
    
    return {
        "task": state["task"],
        "plan": state["plan"],
        "execution": state["execution"],
        "result": result
    }


def example_6_reasoning_graph():
    """Multi-step reasoning workflow."""
    print("=" * 60)
    print("Example 6: Multi-Step Reasoning Graph")
    print("=" * 60)
    
    workflow = StateGraph(ReasoningState)
    
    # Add nodes
    workflow.add_node("plan", plan_node)
    workflow.add_node("execute", execute_node)
    workflow.add_node("summarize", summarize_node)
    
    # Linear flow: plan -> execute -> summarize
    workflow.set_entry_point("plan")
    workflow.add_edge("plan", "execute")
    workflow.add_edge("execute", "summarize")
    workflow.add_edge("summarize", END)
    
    # Compile
    app = workflow.compile()
    
    # Run
    print("\n--- Running reasoning workflow ---")
    result = app.invoke({
        "task": "Learn Python basics in one week",
        "plan": "",
        "execution": "",
        "result": ""
    })
    
    print(f"\nTask: {result['task']}")
    print(f"\nPlan:\n{result['plan']}")
    print(f"\nExecution:\n{result['execution']}")
    print(f"\nResult:\n{result['result']}\n")


# ============================================================================
# Main execution
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("UNIT 4: Introduction to LangGraph - All Examples")
    print("=" * 60 + "\n")
    
    try:
        example_1_basic_state()
        example_2_linear_graph()
        example_3_conditional_edges()
        example_4_loops()
        print("\nThe following examples require Ollama to be running...")
        example_5_llm_graph()
        example_6_reasoning_graph()
        
        print("=" * 60)
        print("All examples completed successfully!")
        print("=" * 60 + "\n")
        
    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure Ollama is running with llama3 installed.")
