"""
Unit 3: LangChain Fundamentals
Sample Code Examples - CONTINUED

Complete version with all memory types and advanced patterns.
"""

from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, ConversationChain
from langchain.memory import (
    ConversationBufferMemory,
    ConversationSummaryMemory,
    ConversationBufferWindowMemory
)

llm = Ollama(model="llama3", temperature=0.7)

# ============================================================================
# Example 6: ConversationBufferMemory (Complete)
# ============================================================================

def example_6_buffer_memory():
    """Demonstrate conversation buffer memory."""
    print("=" * 60)
    print("Example 6: Conversation Buffer Memory")
    print("=" * 60)
    
    memory = ConversationBufferMemory()
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )
    
    print("\n--- Turn 1 ---")
    response1 = conversation.predict(input="Hi, my name is Alice and I love Python programming.")
    print(f"AI: {response1}")
    
    print("\n--- Turn 2 ---")
    response2 = conversation.predict(input="What's my name?")
    print(f"AI: {response2}")
    
    print("\n--- Turn 3 ---")
    response3 = conversation.predict(input="What programming language do I love?")
    print(f"AI: {response3}")
    
    print("\n--- Memory Contents ---")
    print(memory.buffer)
    print("\n")


# ============================================================================
# Example 7: ConversationBufferWindowMemory
# ============================================================================

def example_7_window_memory():
    """Demonstrate window memory (keeps last K interactions)."""
    print("=" * 60)
    print("Example 7: Conversation Window Memory")
    print("=" * 60)
    
    # Keep only last 2 interactions
    memory = ConversationBufferWindowMemory(k=2)
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=False
    )
    
    print("\nHaving a conversation with window size = 2")
    print("(Only remembers last 2 exchanges)\n")
    
    turns = [
        "My favorite color is blue.",
        "I work as a data scientist.",
        "I have a dog named Max.",
        "What's my favorite color?",  # Should forget this
        "What's my dog's name?",       # Should remember this
    ]
    
    for i, turn in enumerate(turns, 1):
        print(f"--- Turn {i} ---")
        print(f"Human: {turn}")
        response = conversation.predict(input=turn)
        print(f"AI: {response}\n")
    
    print("--- Final Memory State ---")
    print(memory.buffer)
    print("\n")


# ============================================================================
# Example 8: ConversationSummaryMemory
# ============================================================================

def example_8_summary_memory():
    """Demonstrate summary memory (summarizes old conversations)."""
    print("=" * 60)
    print("Example 8: Conversation Summary Memory")
    print("=" * 60)
    
    memory = ConversationSummaryMemory(llm=llm)
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=False
    )
    
    print("\nHaving a longer conversation...")
    print("(Memory will summarize to save tokens)\n")
    
    conversation.predict(input="Hi! I'm a software developer working on AI projects.")
    conversation.predict(input="I'm particularly interested in LangChain and agent systems.")
    conversation.predict(input="I've been coding for about 5 years now.")
    conversation.predict(input="What do you know about me?")
    
    print("\n--- Summary in Memory ---")
    print(memory.buffer)
    print("\n")


# ============================================================================
# Example 9: Custom Memory with Metadata
# ============================================================================

def example_9_custom_memory():
    """Demonstrate memory with metadata and custom keys."""
    print("=" * 60)
    print("Example 9: Memory with Metadata")
    print("=" * 60)
    
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    
    # Manually add context
    memory.save_context(
        {"input": "User's name is Bob"},
        {"output": "Noted! I'll remember that Bob is the user."}
    )
    
    memory.save_context(
        {"input": "Bob is learning LangGraph"},
        {"output": "Great! LangGraph is perfect for building agentic workflows."}
    )
    
    # Retrieve memory
    print("\n--- Memory Variables ---")
    print(memory.load_memory_variables({}))
    print("\n")


# ============================================================================
# Example 10: Combining Chains and Memory
# ============================================================================

def example_10_chains_with_memory():
    """Demonstrate combining custom chains with memory."""
    print("=" * 60)
    print("Example 10: Custom Chains with Memory")
    print("=" * 60)
    
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        input_key="question",
        output_key="answer"
    )
    
    prompt = PromptTemplate(
        input_variables=["chat_history", "question"],
        template="""You are a coding tutor. Use the conversation history to provide personalized help.

Chat History:
{chat_history}

Student Question: {question}

Your Response:"""
    )
    
    chain = LLMChain(
        llm=llm,
        prompt=prompt,
        memory=memory,
        output_key="answer",
        verbose=False
    )
    
    print("\n--- Tutoring Session ---\n")
    
    q1 = "I'm learning Python. Can you help me understand lists?"
    print(f"Student: {q1}")
    a1 = chain.predict(question=q1)
    print(f"Tutor: {a1}\n")
    
    q2 = "How do I add items to a list?"
    print(f"Student: {q2}")
    a2 = chain.predict(question=q2)
    print(f"Tutor: {a2}\n")
   
    q3 = "What was the first thing I asked you?"
    print(f"Student: {q3}")
    a3 = chain.predict(question=q3)
    print(f"Tutor: {a3}\n")


# ============================================================================
# Main execution
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("UNIT 3: LangChain Fundamentals - All Examples")
    print("=" * 60 + "\n")
    
    try:
        example_6_buffer_memory()
        example_7_window_memory()
        example_8_summary_memory()
        example_9_custom_memory()
        example_10_chains_with_memory()
        
        print("=" * 60)
        print("All examples completed successfully!")
        print("=" * 60 + "\n")
        
    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure Ollama is running and llama3 is installed.")
