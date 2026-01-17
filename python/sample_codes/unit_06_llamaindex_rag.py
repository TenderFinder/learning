"""
Unit 6: LlamaIndex - RAG and Knowledge Management
Sample Code Examples

This file demonstrates RAG (Retrieval-Augmented Generation) with LlamaIndex.
"""

from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    Document,
    Settings
)
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
import os
import tempfile

# ============================================================================
# Setup: Configure LlamaIndex to use Ollama
# ============================================================================

def setup_llamaindex():
    """Configure LlamaIndex to use local Ollama models."""
    # Set up LLM
    Settings.llm = Ollama(model="llama3", request_timeout=120.0)
    
    # Set up embeddings
    Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")
    
    print("✅ LlamaIndex configured to use Ollama")


# ============================================================================
# Example 1: Create Documents and Simple Index
# ============================================================================

def example_1_simple_index():
    """Create a simple vector index from documents."""
    print("=" * 60)
    print("Example 1: Simple Vector Index")
    print("=" * 60)
    
    setup_llamaindex()
    
    # Create sample documents
    documents = [
        Document(text="LangChain is a framework for developing applications powered by language models."),
        Document(text="LangGraph is a library for building stateful, multi-agent applications with LLMs."),
        Document(text="LlamaIndex is a data framework for LLM applications, focused on RAG."),
        Document(text="Ollama allows you to run large language models locally on your machine."),
    ]
    
    print("\n--- Creating index from documents ---")
    index = VectorStoreIndex.from_documents(documents)
    
    # Query the index
    query_engine = index.as_query_engine()
    
    print("\n--- Querying the index ---")
    question = "What is LangGraph?"
    response = query_engine.query(question)
    
    print(f"\nQuestion: {question}")
    print(f"Answer: {response}")
    print()


# ============================================================================
# Example 2: Loading Documents from Directory
# ============================================================================

def example_2_directory_loading():
    """Load documents from a directory."""
    print("=" * 60)
    print("Example 2: Load Documents from Directory")
    print("=" * 60)
    
    setup_llamaindex()
    
    # Create a temporary directory with sample files
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create sample text files
        with open(os.path.join(tmpdir, "agents.txt"), "w") as f:
            f.write("""
AI agents are autonomous systems that can perceive their environment,
make decisions, and take actions to achieve specific goals. They use
language models to reason about tasks and interact with tools.
            """)
        
        with open(os.path.join(tmpdir, "rag.txt"), "w") as f:
            f.write("""
Retrieval-Augmented Generation (RAG) enhances language models by
retrieving relevant information from a knowledge base before generating
responses. This improves accuracy and reduces hallucinations.
            """)
        
        print(f"\n--- Loading documents from {tmpdir} ---")
        
        # Load all documents from directory
        documents = SimpleDirectoryReader(tmpdir).load_data()
        
        print(f"Loaded {len(documents)} documents")
        
        # Create index
        index = VectorStoreIndex.from_documents(documents)
        query_engine = index.as_query_engine()
        
        # Query
        question = "What is RAG?"
        print(f"\n--- Querying: {question} ---")
        response = query_engine.query(question)
        print(f"Answer: {response}\n")


# ============================================================================
# Example 3: Custom Query Engine with Similarity Top K
# ============================================================================

def example_3_custom_query_engine():
    """Customize query engine parameters."""
    print("=" * 60)
    print("Example 3: Custom Query Engine")
    print("=" * 60)
    
    setup_llamaindex()
    
    # Create more documents
    documents = [
        Document(text="Python is a high-level programming language known for its simplicity."),
        Document(text="JavaScript is primarily used for web development and runs in browsers."),
        Document(text="Rust is a systems programming language focused on safety and performance."),
        Document(text="Go is a statically typed language designed for building scalable systems."),
        Document(text="TypeScript is a superset of JavaScript that adds static typing."),
    ]
    
    index = VectorStoreIndex.from_documents(documents)
    
    # Create query engine with custom parameters
    query_engine = index.as_query_engine(
        similarity_top_k=2,  # Retrieve top 2 most similar chunks
        response_mode="compact"  # Compact response mode
    )
    
    question = "Tell me about web development languages"
    print(f"\n--- Question: {question} ---")
    print(f"Retrieving top 2 similar documents...\n")
    
    response = query_engine.query(question)
    print(f"Answer: {response}\n")


# ============================================================================
# Example 4: Chat Engine for Multi-Turn Conversations
# ============================================================================

def example_4_chat_engine():
    """Use chat engine for conversational RAG."""
    print("=" * 60)
    print("Example 4: Chat Engine (Conversational RAG)")
    print("=" * 60)
    
    setup_llamaindex()
    
    # Create knowledge base
    documents = [
        Document(text="""
Machine Learning is a subset of AI that enables systems to learn from data.
It includes supervised learning, unsupervised learning, and reinforcement learning.
        """),
        Document(text="""
Deep Learning is a subset of machine learning using neural networks with
multiple layers. It's particularly effective for image and speech recognition.
        """),
        Document(text="""
Natural Language Processing (NLP) focuses on the interaction between
computers and human language. It powers chatbots, translation, and sentiment analysis.
        """),
    ]
    
    index = VectorStoreIndex.from_documents(documents)
    
    # Create chat engine
    chat_engine = index.as_chat_engine(
        chat_mode="context",  # Use context from index
        verbose=False
    )
    
    print("\n--- Multi-turn conversation ---\n")
    
    # First question
    response1 = chat_engine.chat("What is machine learning?")
    print(f"User: What is machine learning?")
    print(f"Assistant: {response1}\n")
    
    # Follow-up question (uses conversation history)
    response2 = chat_engine.chat("What are its types?")
    print(f"User: What are its types?")
    print(f"Assistant: {response2}\n")
    
    # Another follow-up
    response3 = chat_engine.chat("How does it differ from deep learning?")
    print(f"User: How does it differ from deep learning?")
    print(f"Assistant: {response3}\n")


# ============================================================================
# Example 5: Retrieving Source Nodes
# ============================================================================

def example_5_source_nodes():
    """Retrieve and display source nodes with metadata."""
    print("=" * 60)
    print("Example 5: Retrieving Source Nodes")
    print("=" * 60)
    
    setup_llamaindex()
    
    # Create documents with metadata
    documents = [
        Document(
            text="The Eiffel Tower is located in Paris, France.",
            metadata={"source": "geography.txt", "category": "landmark"}
        ),
        Document(
            text="The Great Wall of China is one of the Seven Wonders.",
            metadata={"source": "history.txt", "category": "landmark"}
        ),
        Document(
            text="Machine learning algorithms learn patterns from data.",
            metadata={"source": "tech.txt", "category": "technology"}
        ),
    ]
    
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine(similarity_top_k=2)
    
    question = "Tell me about landmarks"
    print(f"\n--- Question: {question} ---\n")
    
    response = query_engine.query(question)
    
    print(f"Answer: {response}\n")
    print("--- Source Nodes ---")
    
    for i, node in enumerate(response.source_nodes, 1):
        print(f"\nSource {i}:")
        print(f"  Text: {node.text}")
        print(f"  Metadata: {node.metadata}")
        print(f"  Score: {node.score:.4f}")
    
    print()


# ============================================================================
# Example 6: Different Index Types
# ============================================================================

def example_6_index_types():
    """Demonstrate different index types."""
    print("=" * 60)
    print("Example 6: Different Index Types")
    print("=" * 60)
    
    setup_llamaindex()
    
    from llama_index.core import ListIndex, TreeIndex
    
    documents = [
        Document(text="First document about AI."),
        Document(text="Second document about machine learning."),
        Document(text="Third document about deep learning."),
    ]
    
    # Vector Index (already seen)
    print("\n--- Vector Store Index ---")
    vector_index = VectorStoreIndex.from_documents(documents)
    vector_response = vector_index.as_query_engine().query("What is AI?")
    print(f"Response: {vector_response}\n")
    
    # List Index (processes sequentially)
    print("\n--- List Index ---")
    list_index = ListIndex.from_documents(documents)
    list_response = list_index.as_query_engine().query("What is AI?")
    print(f"Response: {list_response}\n")
    
    # Tree Index (hierarchical)
    print("\n--- Tree Index ---")
    tree_index = TreeIndex.from_documents(documents)
    tree_response = tree_index.as_query_engine().query("What is AI?")
    print(f"Response: {tree_response}\n")


# ============================================================================
# Example 7: Streaming Responses
# ============================================================================

def example_7_streaming():
    """Stream responses for better UX."""
    print("=" * 60)
    print("Example 7: Streaming Responses")
    print("=" * 60)
    
    setup_llamaindex()
    
    documents = [
        Document(text="""
Streaming responses improve user experience by showing partial results
as they are generated, rather than waiting for the complete response.
This is especially useful for long-form content generation.
        """)
    ]
    
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine(streaming=True)
    
   question = "Explain streaming responses"
    print(f"\n--- Question: {question} ---")
    print("Answer (streaming): ", end="", flush=True)
    
    response = query_engine.query(question)
    
    # Stream the response
    for text in response.response_gen:
        print(text, end="", flush=True)
    
    print("\n")


# ============================================================================
# Main execution
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("UNIT 6: LlamaIndex - RAG Examples")
    print("=" * 60 + "\n")
    
    print("Prerequisites:")
    print("  1. Ollama running (ollama serve)")
    print("  2. LLM model: ollama pull llama3")
    print("  3. Embedding model: ollama pull nomic-embed-text")
    print("  4. Packages: pip install llama-index llama-index-llms-ollama llama-index-embeddings-ollama")
    print("\n")
    
    try:
        example_1_simple_index()
        example_2_directory_loading()
        example_3_custom_query_engine()
        example_4_chat_engine()
        example_5_source_nodes()
        example_6_index_types()
        example_7_streaming()
        
        print("=" * 60)
        print("All examples completed successfully!")
        print("=" * 60 + "\n")
        
    except Exception as e:
        print(f"\nError: {e}")
        print("\nTroubleshooting:")
        print("  - Ensure Ollama is running")
        print("  - Pull required models (llama3, nomic-embed-text)")
        print("  - Install required packages")
