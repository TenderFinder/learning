"""
Unit 2: Setting Up the Development Environment
Sample Code Examples

This file contains setup verification and configuration examples.
"""

import sys
import subprocess
import importlib.metadata
import config

# ============================================================================
# Example 1: Environment Verification
# ============================================================================

def example_1_verify_python():
    """Verify Python version and environment."""
    print("=" * 60)
    print("Example 1: Python Environment Verification")
    print("=" * 60)
    
    print(f"\nPython Version: {sys.version}")
    print(f"Python Executable: {sys.executable}")
    
    # Check if in virtual environment
    in_venv = sys.prefix != sys.base_prefix
    print(f"In Virtual Environment: {in_venv}")
    
    if in_venv:
        print(f"Virtual Env Path: {sys.prefix}")
    else:
        print("\n⚠️  WARNING: Not in a virtual environment!")
        print("   Consider creating one: python -m venv agentic-ai-env")
    print("\n")


# ============================================================================
# Example 2: Check Installed Packages
# ============================================================================

def example_2_check_packages():
    """Check if required packages are installed."""
    print("=" * 60)
    print("Example 2: Package Installation Check")
    print("=" * 60)
    
    required_packages = {
        'langchain': 'langchain',
        'langchain-community': 'langchain_community',
        'langgraph': 'langgraph',
        'llama-index': 'llama_index',
        'chromadb': 'chromadb',
    }
    
    print("\nChecking required packages...\n")
    
    all_installed = True
    for package_name, import_name in required_packages.items():
        try:
            version = importlib.metadata.version(package_name)
            print(f"✅ {package_name:20s} - v{version}")
        except importlib.metadata.PackageNotFoundError:
            print(f"❌ {package_name:20s} - NOT INSTALLED")
            all_installed = False
    
    if all_installed:
        print("\n✅ All required packages are installed!")
    else:
        print("\n⚠️  Some packages are missing. Install with:")
        print("   pip install langchain langchain-community langgraph llama-index chromadb")
    print("\n")


# ============================================================================
# Example 3: Ollama Connection Test
# ============================================================================

def example_3_test_ollama():
    """Test connection to Ollama."""
    print("=" * 60)
    print("Example 3: Ollama Connection Test")
    print("=" * 60)
    
    try:
        import requests
        
        # Check if Ollama server is running
        response = requests.get("http://localhost:11434/api/tags")
        
        if response.status_code == 200:
            models = response.json().get('models', [])
            print("\n✅ Ollama is running!")
            print(f"\nInstalled models ({len(models)}):")
            
            if models:
                for model in models:
                    name = model.get('name', 'unknown')
                    size = model.get('size', 0) / (1024**3)  # Convert to GB
                    print(f"  • {name:20s} ({size:.2f} GB)")
            else:
                print("  No models installed yet.")
                print("\n  Install a model with: ollama pull llama3")
        else:
            print(f"\n⚠️  Ollama responded with status code: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("\n❌ Cannot connect to Ollama!")
        print("   Make sure Ollama is running.")
        print("   Start it with: ollama serve")
    except ImportError:
        print("\n❌ 'requests' package not found!")
        print("   Install it with: pip install requests")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    
    print("\n")


# ============================================================================
# Example 4: Test Ollama with LangChain
# ============================================================================

def example_4_langchain_ollama():
    """Test Ollama integration with LangChain."""
    print("=" * 60)
    print("Example 4: LangChain + Ollama Integration")
    print("=" * 60)
    
    try:
        from langchain_community.llms import Ollama
        
        print("\nAttempting to connect to Ollama with LangChain...")
        
        llm = Ollama(
            model=config.ALTERNATIVE_LLM_MODEL,
            temperature=config.CREATIVE_TEMPERATURE,
            base_url="http://localhost:11434"
        )
        
        test_prompt = "Say 'Hello! Ollama is working!' in one sentence."
        
        print(f"\nSending test prompt: {test_prompt}")
        response = llm.invoke(test_prompt)
        
        print(f"\n✅ Response received:")
        print(f"{response}")
        print("\n✅ LangChain + Ollama is working correctly!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nTroubleshooting:")
        print("  1. Is Ollama running? (ollama serve)")
        print("  2. Is llama3 installed? (ollama pull llama3)")
        print("  3. Is langchain-community installed? (pip install langchain-community)")
    
    print("\n")


# ============================================================================
# Example 5: Test LlamaIndex with Ollama
# ============================================================================

def example_5_llamaindex_ollama():
    """Test Ollama integration with LlamaIndex."""
    print("=" * 60)
    print("Example 5: LlamaIndex + Ollama Integration")
    print("=" * 60)
    
    try:
        from llama_index.llms.ollama import Ollama
        from llama_index.core.llms import ChatMessage
        
        print("\nInitializing LlamaIndex with Ollama...")
        
        llm = Ollama(model=config.ALTERNATIVE_LLM_MODEL, request_timeout=config.DEFAULT_TIMEOUT)
        
        messages = [
            ChatMessage(role="system", content="You are a helpful assistant."),
            ChatMessage(role="user", content="Say 'LlamaIndex is working!' in one sentence.")
        ]
        
        print("\nSending test message...")
        response = llm.chat(messages)
        
        print(f"\n✅ Response received:")
        print(f"{response.message.content}")
        print("\n✅ LlamaIndex + Ollama is working correctly!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nTroubleshooting:")
        print("  1. Install LlamaIndex Ollama: pip install llama-index-llms-ollama")
        print("  2. Make sure Ollama is running")
        print("  3. Make sure llama3 is pulled: ollama pull llama3")
    
    print("\n")


# ============================================================================
# Example 6: Embedding Model Test
# ============================================================================

def example_6_test_embeddings():
    """Test embedding models with Ollama."""
    print("=" * 60)
    print("Example 6: Embedding Model Test")
    print("=" * 60)
    
    try:
        from llama_index.embeddings.ollama import OllamaEmbedding
        
        print("\nInitializing embedding model...")
        print("Model: nomic-embed-text")
        
        embed_model = OllamaEmbedding(
            model_name=config.EMBEDDING_MODEL,
            base_url="http://localhost:11434"
        )
        
        test_text = "This is a test sentence for embeddings."
        print(f"\nGenerating embedding for: '{test_text}'")
        
        embedding = embed_model.get_text_embedding(test_text)
        
        print(f"\n✅ Embedding generated successfully!")
        print(f"   Dimension: {len(embedding)}")
        print(f"   First 5 values: {embedding[:5]}")
        print(f"   Embedding type: {type(embedding)}")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nTroubleshooting:")
        print("  1. Pull embedding model: ollama pull nomic-embed-text")
        print("  2. Install package: pip install llama-index-embeddings-ollama")
    
    print("\n")


# ============================================================================
# Example 7: Performance Benchmark
# ============================================================================

def example_7_benchmark():
    """Benchmark model response time."""
    print("=" * 60)
    print("Example 7: Performance Benchmark")
    print("=" * 60)
    
    try:
        from langchain_community.llms import Ollama
        import time
        
        models_to_test = config.get_comparison_models()
        prompt = "What is 2+2? Answer in one word."
        
        print("\nBenchmarking models with prompt:", prompt)
        print("\n" + "-" * 60)
        
        for model_name in models_to_test:
            try:
                llm = Ollama(model=model_name)
                
                start_time = time.time()
                response = llm.invoke(prompt)
                end_time = time.time()
                
                elapsed = end_time - start_time
                
                print(f"\n{model_name.upper()}:")
                print(f"  ⏱️  Time: {elapsed:.2f}s")
                print(f"  💬 Response: {response.strip()}")
                
            except Exception as e:
                print(f"\n{model_name.upper()}:")
                print(f"  ❌ Error: Model not available")
                print(f"     Pull with: ollama pull {model_name}")
        
        print("\n" + "-" * 60)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
    
    print("\n")


# ============================================================================
# Example 8: Vector Database Setup
# ============================================================================

def example_8_vector_db():
    """Test vector database setup."""
    print("=" * 60)
    print("Example 8: Vector Database Setup")
    print("=" * 60)
    
    # Test ChromaDB
    print("\n--- Testing ChromaDB ---")
    try:
        import chromadb
        
        client = chromadb.Client()
        collection = client.create_collection(name="test_collection")
        
        # Add some test documents
        collection.add(
            documents=["This is a test document", "Another test document"],
            ids=["doc1", "doc2"]
        )
        
        # Query
        results = collection.query(
            query_texts=["test"],
            n_results=2
        )
        
        print("✅ ChromaDB is working!")
        print(f"   Found {len(results['documents'][0])} documents")
        
        # Cleanup
        client.delete_collection(name="test_collection")
        
    except Exception as e:
        print(f"❌ ChromaDB Error: {e}")
        print("   Install with: pip install chromadb")
    
    # Test FAISS
    print("\n--- Testing FAISS ---")
    try:
        import faiss
        import numpy as np
        
        # Create a simple index
        dimension = 128
        index = faiss.IndexFlatL2(dimension)
        
        # Add some vectors
        vectors = np.random.random((10, dimension)).astype('float32')
        index.add(vectors)
        
        # Search
        query = np.random.random((1, dimension)).astype('float32')
        distances, indices = index.search(query, 3)
        
        print("✅ FAISS is working!")
        print(f"   Index size: {index.ntotal} vectors")
        
    except Exception as e:
        print(f"❌ FAISS Error: {e}")
        print("   Install with: pip install faiss-cpu")
    
    print("\n")


# ============================================================================
# Example 9: Complete Setup Verification
# ============================================================================

def example_9_complete_verification():
    """Run a complete end-to-end test."""
    print("=" * 60)
    print("Example 9: Complete Setup Verification")
    print("=" * 60)
    
    checks = {
        "Python Environment": False,
        "Required Packages": False,
        "Ollama Running": False,
        "LangChain Integration": False,
        "LlamaIndex Integration": False,
        "Embedding Model": False,
        "Vector Database": False
    }
    
    # Check Python
    try:
        checks["Python Environment"] = sys.version_info >= (3, 8)
    except:
        pass
    
    # Check packages
    try:
        import langchain
        import langgraph
        import llama_index
        checks["Required Packages"] = True
    except:
        pass
    
    # Check Ollama
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags")
        checks["Ollama Running"] = response.status_code == 200
    except:
        pass
    
    # Check LangChain
    try:
        from langchain_community.llms import Ollama
        llm = Ollama(model=config.ALTERNATIVE_LLM_MODEL)
        llm.invoke("test")
        checks["LangChain Integration"] = True
    except:
        pass
    
    # Check LlamaIndex
    try:
        from llama_index.llms.ollama import Ollama
        llm = Ollama(model=config.ALTERNATIVE_LLM_MODEL)
        checks["LlamaIndex Integration"] = True
    except:
        pass
    
    # Check embeddings
    try:
        from llama_index.embeddings.ollama import OllamaEmbedding
        embed = OllamaEmbedding(model_name=config.EMBEDDING_MODEL)
        checks["Embedding Model"] = True
    except:
        pass
    
    # Check vector DB
    try:
        import chromadb
        checks["Vector Database"] = True
    except:
        pass
    
    # Print results
    print("\n📋 Setup Verification Results:\n")
    for check, status in checks.items():
        icon = "✅" if status else "❌"
        print(f"{icon} {check}")
    
    # Overall status
    all_passed = all(checks.values())
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 All checks passed! Your environment is ready!")
    else:
        print("⚠️  Some checks failed. Review the results above.")
    print("=" * 60 + "\n")


# ============================================================================
# Main execution
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("UNIT 2: Environment Setup - Verification & Tests")
    print("=" * 60 + "\n")
    
    example_1_verify_python()
    example_2_check_packages()
    example_3_test_ollama()
    example_4_langchain_ollama()
    example_5_llamaindex_ollama()
    example_6_test_embeddings()
    example_7_benchmark()
    example_8_vector_db()
    example_9_complete_verification()
    
    print("\n" + "=" * 60)
    print("Setup verification completed!")
    print("=" * 60 + "\n")
