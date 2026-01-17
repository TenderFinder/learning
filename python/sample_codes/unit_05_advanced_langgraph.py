"""
Unit 5: Advanced LangGraph Patterns
Sample Code Examples

This file demonstrates advanced LangGraph patterns including multi-agent systems,
tool integration, and human-in-the-loop workflows.
"""

from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END
from langchain_community.llms import Ollama
from langchain.agents import tool
import operator

# ============================================================================
# Example 1: Tool Integration in LangGraph
# ============================================================================

@tool
def search_web(query: str) -> str:
    """Search the web for information (simulated)."""
    # In production, use actual search API
    responses = {
        "langraph": "LangGraph is a library for building stateful, multi-agent applications.",
        "langgraph benefits": "Key benefits: state management, cycles, human-in-the-loop, persistence.",
        "default": f"Search results for: {query}"
    }
    return responses.get(query.lower(), responses["default"])

@tool
def calculator(expression: str) -> str:
    """Evaluate mathematical expressions."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"

class ToolAgentState(TypedDict):
    messages: Annotated[list, operator.add]
    question: str
    tool_calls: Annotated[list, operator.add]
    final_answer: str


def decide_tool(state: ToolAgentState) -> Literal["search", "calculate", "answer"]:
    """Decide which tool to use based on the question."""
    question = state["question"].lower()
    
    if any(word in question for word in ["search", "find", "what is", "who is"]):
        return "search"
    elif any(word in question for word in ["calculate", "compute", "+", "-", "*", "/"]):
        return "calculate"
    else:
        return "answer"


def search_node(state: ToolAgentState) -> ToolAgentState:
    """Execute search tool."""
    result = search_web.invoke({"query": state["question"]})
    return {
        "messages": [f"Search: {result}"],
        "tool_calls": ["search_web"],
        "question": state["question"],
        "final_answer": ""
    }


def calculate_node(state: ToolAgentState) -> ToolAgentState:
    """Execute calculator tool."""
    # Extract expression from question (simplified)
    question = state["question"]
    # Find numbers and operations
    import re
    expressions = re.findall(r'[\d\+\-\*/\(\)\.]+', question)
    
    if expressions:
        result = calculator.invoke({"expression": expressions[0]})
    else:
        result = "No valid expression found"
    
    return {
        "messages": [f"Calculate: {result}"],
        "tool_calls": ["calculator"],
        "question": state["question"],
        "final_answer": ""
    }


def answer_node(state: ToolAgentState) -> ToolAgentState:
    """Generate final answer using LLM."""
    llm = Ollama(model="llama3", temperature=0.7)
    
    context = "\n".join(state["messages"])
    prompt = f"""Based on this information:
{context}

Answer the question: {state["question"]}

Provide a clear, concise answer."""
    
    answer = llm.invoke(prompt)
    
    return {
        "messages": [f"Final answer: {answer}"],
        "tool_calls": [],
        "question": state["question"],
        "final_answer": answer
    }


def example_1_tool_integration():
    """Demonstrate tool integration in LangGraph."""
    print("=" * 60)
    print("Example 1: Tool Integration in LangGraph")
    print("=" * 60)
    
    # Build graph
    workflow = StateGraph(ToolAgentState)
    
    # Add nodes
    workflow.add_node("search", search_node)
    workflow.add_node("calculate", calculate_node)
    workflow.add_node("answer", answer_node)
    
    # Add conditional routing
    workflow.set_entry_point("search")  # Dummy entry
    workflow.add_conditional_edges(
        "search",
        lambda s: "answer",
        {"answer": "answer"}
    )
    workflow.add_conditional_edges(
        "calculate",
        lambda s: "answer",
        {"answer": "answer"}
    )
    workflow.add_edge("answer", END)
    
    # For this example, we'll manually route
    app = workflow.compile()
    
    # Test cases
    questions = [
        "What is LangGraph?",
        "Calculate 15 * 8",
        "What are the benefits of LangGraph?"
    ]
    
    for question in questions:
        print(f"\n--- Question: {question} ---")
        
        # Determine route
        route = "search" if any(w in question.lower() for w in ["what", "who", "where"]) else "calculate"
        
        # Simulate (for full implementation, use conditional entry point)
        if "calculate" in question.lower() or any(op in question for op in ['+', '-', '*', '/']):
            result = calculate_node({"messages": [], "question": question, "tool_calls": [], "final_answer": ""})
        else:
            result = search_node({"messages": [], "question": question, "tool_calls": [], "final_answer": ""})
        
        print(f"Tool used: {result['tool_calls']}")
        print(f"Result: {result['messages'][0]}")
    
    print()


# ============================================================================
# Example 2: Multi-Agent Collaboration
# ============================================================================

class MultiAgentState(TypedDict):
    task: str
    researcher_output: str
    writer_output: str
    editor_output: str
    final_output: str


def researcher_agent(state: MultiAgentState) -> MultiAgentState:
    """Research agent gathers information."""
    llm = Ollama(model="llama3", temperature=0.3)
    
    prompt = f"""You are a research agent. Research this topic: {state['task']}
    
Provide 3-4 key facts or insights."""
    
    research = llm.invoke(prompt)
    
    return {
        "task": state["task"],
        "researcher_output": research,
        "writer_output": "",
        "editor_output": "",
        "final_output": ""
    }


def writer_agent(state: MultiAgentState) -> MultiAgentState:
    """Writer agent creates content."""
    llm = Ollama(model="llama3", temperature=0.7)
    
    prompt = f"""You are a writer. Based on this research:

{state['researcher_output']}

Write a short article about: {state['task']}"""
    
    article = llm.invoke(prompt)
    
    return {
        "task": state["task"],
        "researcher_output": state["researcher_output"],
        "writer_output": article,
        "editor_output": "",
        "final_output": ""
    }


def editor_agent(state: MultiAgentState) -> MultiAgentState:
    """Editor agent reviews and improves."""
    llm = Ollama(model="llama3", temperature=0.5)
    
    prompt = f"""You are an editor. Review and improve this article:

{state['writer_output']}

Make it more clear and concise."""
    
    edited = llm.invoke(prompt)
    
    return {
        "task": state["task"],
        "researcher_output": state["researcher_output"],
        "writer_output": state["writer_output"],
        "editor_output": edited,
        "final_output": edited
    }


def example_2_multi_agent():
    """Demonstrate multi-agent collaboration."""
    print("=" * 60)
    print("Example 2: Multi-Agent Collaboration")
    print("=" * 60)
    
    # Build workflow
    workflow = StateGraph(MultiAgentState)
    
    # Add agents as nodes
    workflow.add_node("researcher", researcher_agent)
    workflow.add_node("writer", writer_agent)
    workflow.add_node("editor", editor_agent)
    
    # Linear workflow: research -> write -> edit
    workflow.set_entry_point("researcher")
    workflow.add_edge("researcher", "writer")
    workflow.add_edge("writer", "editor")
    workflow.add_edge("editor", END)
    
    # Compile
    app = workflow.compile()
    
    # Run
    print("\n--- Running multi-agent workflow ---")
    task = "AI agents in software development"
    
    result = app.invoke({
        "task": task,
        "researcher_output": "",
        "writer_output": "",
        "editor_output": "",
        "final_output": ""
    })
    
    print(f"\nTask: {task}")
    print(f"\n[1] Research Phase:")
    print(result["researcher_output"][:200] + "...")
    print(f"\n[2] Writing Phase:")
    print(result["writer_output"][:200] + "...")
    print(f"\n[3] Editing Phase (Final):")
    print(result["final_output"])
    print()


# ============================================================================
# Example 3: Human-in-the-Loop (Simulated)
# ============================================================================

class HITLState(TypedDict):
    content: str
    status: str
    feedback: str
    approved: bool


def generate_content(state: HITLState) -> HITLState:
    """Generate initial content."""
    llm = Ollama(model="llama3", temperature=0.7)
    
    content = llm.invoke("Write a short introduction to LangGraph")
    
    return {
        "content": content,
        "status": "pending_review",
        "feedback": "",
        "approved": False
    }


def review_checkpoint(state: HITLState) -> Literal["revise", "approve"]:
    """Simulate human review (in real app, this would pause for human input)."""
    # Simulated: auto-approve for demo
    # In production, this would interrupt and wait for human input
    print("\n--- Human Review Checkpoint ---")
    print(f"Content: {state['content'][:100]}...")
    print("\nOptions: [approve/revise]")
    
    # Simulate approval (in real scenario, get user input)
    decision = "approve"  # Simulated
    print(f"Decision: {decision}")
    
    return decision


def revise_content(state: HITLState) -> HITLState:
    """Revise based on feedback."""
    llm = Ollama(model="llama3", temperature=0.7)
    
    prompt = f"""Revise this content based on feedback:

Content: {state['content']}
Feedback: {state['feedback']}

Provide improved version."""
    
    revised = llm.invoke(prompt)
    
    return {
        "content": revised,
        "status": "pending_review",
        "feedback": "",
        "approved": False
    }


def approve_content(state: HITLState) -> HITLState:
    """Approve content."""
    return {
        "content": state["content"],
        "status": "approved",
        "feedback": "",
        "approved": True
    }


def example_3_hitl():
    """Demonstrate human-in-the-loop pattern."""
    print("=" * 60)
    print("Example 3: Human-in-the-Loop (Simulated)")
    print("=" * 60)
    
    workflow = StateGraph(HITLState)
    
    # Add nodes
    workflow.add_node("generate", generate_content)
    workflow.add_node("revise", revise_content)
    workflow.add_node("approve", approve_content)
    
    # Set up workflow
    workflow.set_entry_point("generate")
    
    # After generation, review
    workflow.add_conditional_edges(
        "generate",
        review_checkpoint,
        {
            "approve": "approve",
            "revise": "revise"
        }
    )
    
    # After revision, review again
    workflow.add_conditional_edges(
        "revise",
        review_checkpoint,
        {
            "approve": "approve",
            "revise": "revise"
        }
    )
    
    workflow.add_edge("approve", END)
    
    # Compile
    app = workflow.compile()
    
    # Run
    print("\n--- Running HITL workflow ---")
    result = app.invoke({
        "content": "",
        "status": "draft",
        "feedback": "",
        "approved": False
    })
    
    print(f"\nFinal Status: {result['status']}")
    print(f"Approved: {result['approved']}")
    print(f"\nFinal Content:\n{result['content']}")
    print()


# ============================================================================
# Main execution
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("UNIT 5: Advanced LangGraph Patterns")
    print("=" * 60 + "\n")
    
    print("NOTE: These examples require Ollama with llama3 model.\n")
    
    try:
        example_1_tool_integration()
        
        print("\nRunning multi-agent example (may take a minute)...")
        example_2_multi_agent()
        
        print("\nRunning HITL example...")
        example_3_hitl()
        
        print("\n" + "=" * 60)
        print("All examples completed!")
        print("=" * 60 + "\n")
        
    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure:")
        print("- Ollama is running")
        print("- llama3 model is installed")
        print("- All dependencies are up to date")
