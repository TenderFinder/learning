"""
Unit 1: Introduction to Agentic AI & Foundation Concepts
Sample Code Examples

This file contains working examples for Unit 1 concepts.
"""

# ============================================================================
# Example 1: Basic Ollama Setup and First Interaction
# ============================================================================

from langchain_ollama import ChatOllama
import config

# Models to test - imported from config.py
models = config.get_comparison_models()

def example_1_basic_ollama():
    """
    Simple example of connecting to Ollama and getting a response.
    
    Prerequisites:
    - Ollama installed and running
    - deepseek-r1:8b model pulled (ollama pull deepseek-r1:8b)
    """
    print("=" * 60)
    print("Example 1: Basic Ollama Interaction")
    print("=" * 60)
    
    # Initialize Ollama with primary model from config
    llm = ChatOllama(model=config.PRIMARY_LLM_MODEL, temperature=config.CREATIVE_TEMPERATURE)
    
    # Simple query
    prompt = "Explain what an AI agent is in one sentence."
    response = llm.invoke(prompt)
    
    print(f"\nPrompt: {prompt}")
    print(f"\nResponse: {response}")
    print("\n")


# ============================================================================
# Example 2: Understanding Agent Components - Tool Use
# ============================================================================

from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """
    A simple calculator tool that evaluates mathematical expressions.
    
    Args:
        expression: A mathematical expression as a string (e.g., "2 + 2")
    
    Returns:
        The result of the calculation
    """
    try:
        result = eval(expression)
        return f"The result is: {result}"
    except Exception as e:
        return f"Error: {str(e)}"


@tool
def get_current_date() -> str:
    """Get the current date and time."""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def example_2_tools():
    """
    Demonstrates the concept of tools that agents can use.
    """
    print("=" * 60)
    print("Example 2: Agent Tools")
    print("=" * 60)
    
    # Using the calculator tool
    result1 = calculator.invoke({"expression": "15 * 7"})
    print(f"\nCalculator Tool: {result1}")
    
    # Using the date tool
    result2 = get_current_date.invoke({})
    print(f"Date Tool: {result2}")
    print("\n")


# ============================================================================
# Example 3: Memory Systems - Conversation History
# ============================================================================

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

def example_3_memory():
    """
    Demonstrates basic memory in a conversation.
    """
    print("=" * 60)
    print("Example 3: Memory System")
    print("=" * 60)
    
    llm = ChatOllama(model=config.PRIMARY_LLM_MODEL, temperature=config.CREATIVE_TEMPERATURE)
    
    # Create a conversation chain with modern memory pattern
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    
    chain = prompt | llm
    
    # Session storage
    store = {}
    
    def get_session_history(session_id: str):
        if session_id not in store:
            store[session_id] = InMemoryChatMessageHistory()
        return store[session_id]
    
    # Wrap with message history
    conversation = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history"
    )
    
    config = {"configurable": {"session_id": "demo_session"}}
    
    # First interaction
    print("\n--- First Interaction ---")
    response1 = conversation.invoke({"input": "My name is Alice and I'm learning about AI agents."}, config=config)
    print(f"Response: {response1.content}\n")
    
    # Second interaction - the agent should remember the name
    print("\n--- Second Interaction ---")  
    response2 = conversation.invoke({"input": "What's my name?"}, config=config)
    print(f"Response: {response2.content}\n")
    
    # Show the conversation history
    print("\n--- Conversation History ---")
    history = store["demo_session"]
    for msg in history.messages:
        print(f"{msg.type}: {msg.content}")
    print("\n")


# ============================================================================
# Example 4: Agent Loop Simulation
# ============================================================================

def example_4_agent_loop():
    """
    Simulates a simple agent reasoning loop: Think -> Act -> Observe.
    """
    print("=" * 60)
    print("Example 4: Agent Reasoning Loop")
    print("=" * 60)
    
    llm = ChatOllama(model=config.PRIMARY_LLM_MODEL, temperature=config.PRECISE_TEMPERATURE)
    
    # Simulate an agent solving a problem
    task = "What is 25 * 4?"
    
    print(f"\nTask: {task}")
    print("\n--- Agent Loop ---")
    
    # Step 1: Think
    think_prompt = f"""You are an AI agent. Given the task: "{task}"
    
Think step by step about how to solve this. What tool do you need?"""
    
    thinking = llm.invoke(think_prompt)
    print(f"\n1. THINK:\n{thinking}")
    
    # Step 2: Act (simulate using calculator)
    action = calculator.invoke({"expression": "25 * 4"})
    print(f"\n2. ACT (using calculator):\n{action}")
    
    # Step 3: Observe and respond
    observe_prompt = f"""The calculator returned: "{action}"
    
Based on this, provide a final answer to the task: "{task}" """
    
    final_response = llm.invoke(observe_prompt)
    print(f"\n3. OBSERVE & RESPOND:\n{final_response}")
    print("\n")


# ============================================================================
# Example 5: Exploring Real-World Use Cases
# ============================================================================

def example_5_use_cases():
    """
    Demonstrates different agent use case patterns.
    """
    print("=" * 60)
    print("Example 5: Agent Use Case Patterns")
    print("=" * 60)
    
    llm = ChatOllama(model=config.PRIMARY_LLM_MODEL, temperature=config.CREATIVE_TEMPERATURE)
    
    # Use Case 1: Customer Service Agent
    print("\n--- Use Case 1: Customer Service ---")
    cs_prompt = """You are a customer service agent. A customer says:
    "I can't log into my account. I've tried resetting my password twice."
    
Respond in a helpful, empathetic manner and suggest next steps."""
    
    cs_response = llm.invoke(cs_prompt)
    print(f"Agent Response:\n{cs_response}")
    
    # Use Case 2: Research Assistant
    print("\n\n--- Use Case 2: Research Assistant ---")
    research_prompt = """You are a research assistant. Your task is to help analyze this question:
    "What are the key differences between LangChain and LangGraph?"
    
Outline the steps you would take to research this question."""
    
    research_response = llm.invoke(research_prompt)
    print(f"Agent Response:\n{research_response}")
    
    # Use Case 3: Code Debugging Assistant
    print("\n\n--- Use Case 3: Code Debugging ---")
    debug_prompt = """You are a code debugging assistant. A developer shows you this error:
    
    ```python
    def calculate_average(numbers):
        return sum(numbers) / len(numbers)
    
    result = calculate_average([])
    ```
    
    Error: ZeroDivisionError: division by zero
    
Identify the issue and suggest a fix."""
    
    debug_response = llm.invoke(debug_prompt)
    print(f"Agent Response:\n{debug_response}")
    print("\n")


# ============================================================================
# Example 6: Comparing Different Models
# ============================================================================

def example_6_model_comparison():
    """
    Compare responses from different models for the same task.
    
    Prerequisites:
    - Multiple models pulled (deepseek-r1:8b, llama2-uncensored, lama3-groq-tool-use3)
    """
    print("=" * 60)
    print("Example 6: Model Comparison")
    print("=" * 60)
    
    prompt = "Explain the concept of 'agent autonomy' in 20 words or less."
    
    for model_name in models:
        try:
            print(f"\n--- {model_name.upper()} ---")
            llm = ChatOllama(model=model_name, temperature=0.5)
            response = llm.invoke(prompt)
            print(f"Response: {response}")
        except Exception as e:
            print(f"Error with {model_name}: {e}")
            print("Make sure to pull the model: ollama pull {model_name}")
    
    print("\n")


# ============================================================================
# Example 7: Planning and Reasoning
# ============================================================================

def example_7_planning():
    """
    Demonstrates how agents plan multi-step tasks.
    """
    print("=" * 60)
    print("Example 7: Agent Planning")
    print("=" * 60)
    
    llm = ChatOllama(model=config.PRIMARY_LLM_MODEL, temperature=config.PRECISE_TEMPERATURE)
    
    complex_task = """Plan a birthday party for 20 people this weekend."""
    
    planning_prompt = f"""You are an AI planning agent. Break down this task into sub-tasks:

Task: {complex_task}

Create a numbered list of sub-tasks needed to complete this task."""
    
    plan = llm.invoke(planning_prompt)
    print(f"\nTask: {complex_task}")
    print(f"\n--- Agent's Plan ---\n{plan}")
    print("\n")


# ============================================================================
# Example 8: Feedback Loops
# ============================================================================

def example_8_feedback():
    """
    Demonstrates agent self-correction through feedback.
    """
    print("=" * 60)
    print("Example 8: Feedback and Self-Correction")
    print("=" * 60)
    
    llm = ChatOllama(model=config.PRIMARY_LLM_MODEL, temperature=config.CREATIVE_TEMPERATURE)
    
    # Initial attempt
    print("\n--- Initial Attempt ---")
    task = "Write a haiku about artificial intelligence"
    response1 = llm.invoke(task)
    print(f"Agent's First Attempt:\n{response1}")
    
    # Self-critique
    print("\n--- Self-Critique ---")
    critique_prompt = f"""You wrote this haiku:

{response1}

Critique it: Does it follow the 5-7-5 syllable pattern? Be honest."""
    
    critique = llm.invoke(critique_prompt)
    print(f"Self-Critique:\n{critique}")
    
    # Improved version
    print("\n--- Improved Version ---")
    improve_prompt = f"""Based on your critique, write an improved haiku about AI that strictly follows 5-7-5."""
    
    response2 = llm.invoke(improve_prompt)
    print(f"Improved Haiku:\n{response2}")
    print("\n")


# ============================================================================
# Main execution
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("UNIT 1: Introduction to Agentic AI - Sample Code")
    print("=" * 60 + "\n")
    
    print("NOTE: Make sure Ollama is running and you have pulled the required models:")
    print("  ollama pull deepseek-r1:8b")
    print("  ollama pull llama2-uncensored")
    print("  ollama pull lama3-groq-tool-use3")
    print("\n")
    
    try:
        # Run all examples
        example_1_basic_ollama()
        example_2_tools()
        example_3_memory()
        example_4_agent_loop()
        example_5_use_cases()
        
        # Model comparison (may fail if models not available)
        print("\nAttempting model comparison (skip if models not available)...")
        try:
            example_6_model_comparison()
        except:
            print("Skipping model comparison - ensure all models are pulled")
        
        example_7_planning()
        example_8_feedback()
        
        print("\n" + "=" * 60)
        print("All examples completed successfully!")
        print("=" * 60 + "\n")
        
    except Exception as e:
        print(f"\n\nError: {e}")
        print("\nMake sure:")
        print("1. Ollama is running (check with: ollama list)")
        print("2. Required packages are installed (pip install langchain langchain-community)")
        print("3. At least one model is pulled (ollama pull deepseek-r1:8b)")
