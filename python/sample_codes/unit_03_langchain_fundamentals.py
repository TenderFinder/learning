"""
Unit 3: LangChain Fundamentals
Sample Code Examples - 2026 Modernized Version

Demonstrates LCEL, modern memory patterns, and chain composition.
"""

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import trim_messages
from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableLambda
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from operator import itemgetter
import config

llm = ChatOllama(model=config.PRIMARY_LLM_MODEL, temperature=config.CREATIVE_TEMPERATURE)

# ============================================================================
# Example 1: LCEL Basics - Pipe Operator
# ============================================================================

def example_1_lcel_basics():
    """Demonstrate LangChain Expression Language (LCEL) basics."""
    print("=" * 60)
    print("Example 1: LCEL Basics")
    print("=" * 60)
    
    # Simple chain with pipe operator
    prompt = PromptTemplate.from_template("Tell me a fact about {topic}")
    chain = prompt | llm | StrOutputParser()
    
    result = chain.invoke({"topic": "Python programming"})
    print(f"\nResult: {result}\n")


# ============================================================================
# Example 2: Modern Memory with RunnableWithMessageHistory
# ============================================================================

def example_2_modern_memory():
    """Demonstrate modern memory pattern (2026 standard)."""
    print("=" * 60)
    print("Example 2: Modern Memory Pattern")
    print("=" * 60)
    
    # Create prompt with history placeholder
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
    
    # Wrap with history
    conversation = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history"
    )
    
    config_dict = {"configurable": {"session_id": "session_1"}}
    
    print("\n--- Turn 1 ---")
    r1 = conversation.invoke({"input": "My name is Alice and I love Python."}, config=config_dict)
    print(f"AI: {r1.content}")
    
    print("\n--- Turn 2 ---")
    r2 = conversation.invoke({"input": "What's my name?"}, config=config_dict)
    print(f"AI: {r2.content}")
    
    print("\n--- Turn 3 ---")
    r3 = conversation.invoke({"input": "What programming language do I love?"}, config=config_dict)
    print(f"AI: {r3.content}\n")


# ============================================================================
# Example 3: Sliding Window Memory (trim_messages)
# ============================================================================

def example_3_sliding_window():
    """Demonstrate sliding window memory with trim_messages."""
    print("=" * 60)
    print("Example 3: Sliding Window Memory")
    print("=" * 60)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    
    # Create trimmer (keeps last 4 messages = 2 exchanges)
    trimmer = trim_messages(
        strategy="last",
        token_counter=len,  # Simple character count
        max_tokens=500,
        include_system=True
    )
    
    chain = prompt | llm
    
    store = {}
    
    def get_session_history(session_id: str):
        if session_id not in store:
            store[session_id] = InMemoryChatMessageHistory()
        return store[session_id]
    
    conversation = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history"
    )
    
    config_dict = {"configurable": {"session_id": "window_session"}}
    
    print("\n--- Conversation with sliding window ---")
    turns = [
        "My favorite color is blue.",
        "I work as a data scientist.",
        "I have a dog named Max.",
        "What's my favorite color?",  # Might be forgotten
        "What's my dog's name?",
    ]
    
    for i, turn in enumerate(turns, 1):
        print(f"\nTurn {i}: {turn}")
        response = conversation.invoke({"input": turn}, config=config_dict)
        print(f"AI: {response.content}")
    
    print("\n")


# ============================================================================
# Example 4: LCEL Chain Composition (RunnableParallel)
# ============================================================================

def example_4_chain_composition():
    """Demonstrate parallel chain execution with LCEL."""
    print("=" * 60)
    print("Example 4: Parallel Chain Composition")
    print("=" * 60)
    
    # Define two different prompts
    joke_prompt = PromptTemplate.from_template("Tell a short joke about {topic}")
    fact_prompt = PromptTemplate.from_template("Tell an interesting fact about {topic}")
    
    # Create chains
    joke_chain = joke_prompt | llm | StrOutputParser()
    fact_chain = fact_prompt | llm | StrOutputParser()
    
    # Run in parallel
    parallel_chain = RunnableParallel(
        joke=joke_chain,
        fact=fact_chain
    )
    
    result = parallel_chain.invoke({"topic": "artificial intelligence"})
    
    print(f"\nJoke: {result['joke']}")
    print(f"\nFact: {result['fact']}\n")


# ============================================================================
# Example 5: Advanced LCEL - RunnablePassthrough and itemgetter
# ============================================================================

def example_5_advanced_lcel():
    """Demonstrate advanced LCEL patterns."""
    print("=" * 60)
    print("Example 5: Advanced LCEL Patterns")
    print("=" * 60)
    
    # Chain that passes input through and adds LLM analysis
    prompt = ChatPromptTemplate.from_template(
        "Analyze this text and provide 3 keywords: {text}"
    )
    
    chain = (
        RunnablePassthrough.assign(
            analysis=prompt | llm | StrOutputParser()
        )
    )
    
    result = chain.invoke({
        "text": "LangGraph enables building stateful, multi-actor applications with LLMs."
    })
    
    print(f"\nOriginal Text: {result['text']}")
    print(f"\nAnalysis: {result['analysis']}\n")


# ============================================================================
# Example 6: Few-Shot Prompting (Modern Pattern)
# ============================================================================

def example_6_few_shot():
    """Demonstrate few-shot prompting with LCEL."""
    print("=" * 60)
    print("Example 6: Few-Shot Prompting")
    print("=" * 60)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a sentiment analyzer. Classify text as positive, negative, or neutral."),
        ("human", "I love this product! → positive"),
        ("ai", "Understood. Positive sentiment."),
        ("human", "This is terrible. → negative"),
        ("ai", "Understood. Negative sentiment."),
        ("human", "It's okay I guess. → neutral"),
        ("ai", "Understood. Neutral sentiment."),
        ("human", "{text} →")
    ])
    
    chain = prompt | llm | StrOutputParser()
    
    texts = [
        "This is amazing!",
        "I'm disappointed.",
        "It works as expected."
    ]
    
    print("\n--- Sentiment Analysis ---")
    for text in texts:
        result = chain.invoke({"text": text})
        print(f"{text} → {result}")
    
    print("\n")


# ============================================================================
# Example 7: Streaming Responses
# ============================================================================

def example_7_streaming():
    """Demonstrate streaming responses with LCEL."""
    print("=" * 60)
    print("Example 7: Streaming Responses")
    print("=" * 60)
    
    prompt = ChatPromptTemplate.from_template("Write a short story about {topic}")
    chain = prompt | llm
    
    print("\nStreaming response:")
    print("-" * 40)
    for chunk in chain.stream({"topic": "a robot learning to paint"}):
        print(chunk.content, end="", flush=True)
    print("\n")


# ============================================================================
# Example 8: Custom Runnable Lambda
# ============================================================================

def example_8_custom_runnable():
    """Demonstrate custom processing with RunnableLambda."""
    print("=" * 60)
    print("Example 8: Custom Runnable Functions")
    print("=" * 60)
    
    def count_words(text):
        return {"text": text, "word_count": len(text.split())}
    
    def create_prompt(data):
        return f"Summarize this {data['word_count']}-word text: {data['text']}"
    
    chain = (
        RunnableLambda(count_words) 
        | RunnableLambda(create_prompt)
        | llm
        | StrOutputParser()
    )
    
    text = "LangChain is a framework for developing applications powered by language models."
    result = chain.invoke(text)
    
    print(f"\nOriginal: {text}")
    print(f"Summary: {result}\n")


# ============================================================================
# Example 9: Multi-Step Chain (Sequential Processing)
# ============================================================================

def example_9_multi_step():
    """Demonstrate multi-step processing chain."""
    print("=" * 60)
    print("Example 9: Multi-Step Chain")
    print("=" * 60)
    
    # Step 1: Generate topic ideas
    topic_prompt = ChatPromptTemplate.from_template(
        "Generate 3 blog post topics about {subject}. List them as: 1. ... 2. ... 3. ..."
    )
    
    # Step 2: Expand first topic
    expand_prompt = ChatPromptTemplate.from_template(
        "From these topics: {topics}\n\nWrite a brief outline for topic #1"
    )
    
    chain = (
        {"topics": topic_prompt | llm | StrOutputParser()}
        | expand_prompt
        | llm
        | StrOutputParser()
    )
    
    result = chain.invoke({"subject": "artificial intelligence"})
    print(f"\nResult:\n{result}\n")


# ============================================================================
# Example 10: Session-Based Memory with Multiple Users
# ============================================================================

def example_10_multi_session():
    """Demonstrate multi-user session management."""
    print("=" * 60)
    print("Example 10: Multi-Session Memory")
    print("=" * 60)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    
    chain = prompt | llm
    store = {}
    
    def get_session_history(session_id: str):
        if session_id not in store:
            store[session_id] = InMemoryChatMessageHistory()
        return store[session_id]
    
    conversation = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history"
    )
    
    # User 1
    print("\n--- User 1 (Alice) ---")
    config_alice = {"configurable": {"session_id": "alice"}}
    r1 = conversation.invoke({"input": "My name is Alice."}, config=config_alice)
    print(f"AI: {r1.content}")
    
    # User 2
    print("\n--- User 2 (Bob) ---")
    config_bob = {"configurable": {"session_id": "bob"}}
    r2 = conversation.invoke({"input": "My name is Bob."}, config=config_bob)
    print(f"AI: {r2.content}")
    
    # Check isolation
    print("\n--- Back to User 1 ---")
    r3 = conversation.invoke({"input": "What's my name?"}, config=config_alice)
    print(f"AI: {r3.content}")
    
    print("\n--- Back to User 2 ---")
    r4 = conversation.invoke({"input": "What's my name?"}, config=config_bob)
    print(f"AI: {r4.content}\n")


# ============================================================================
# Main execution
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("UNIT 3: LangChain Fundamentals (2026 Modernized)")
    print("=" * 60 + "\n")
    
    try:
        example_1_lcel_basics()
        example_2_modern_memory()
        example_3_sliding_window()
        example_4_chain_composition()
        example_5_advanced_lcel()
        example_6_few_shot()
        example_7_streaming()
        example_8_custom_runnable()
        example_9_multi_step()
        example_10_multi_session()
        
        print("=" * 60)
        print("All examples completed successfully!")
        print("=" * 60 + "\n")
        
    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure:")
        print("1. Ollama is running")
        print("2. Required packages: pip install langchain langchain-ollama langchain-core")
