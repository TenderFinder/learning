"""
Configuration file for Agentic AI Sample Codes
===============================================

This file contains centralized configuration for all sample code files.
Modify the model names here to change them across all examples.

Ensure the models you specify are already pulled in Ollama:
    ollama pull <model-name>
"""

# ============================================================================
# LLM Models Configuration
# ============================================================================

# Primary LLM model used in most examples
# Recommended: A fast, capable model for general tasks
PRIMARY_LLM_MODEL = "llama3-groq-tool-use"

# Alternative LLM model (used in Units 3-6)
# Good for testing and comparison
ALTERNATIVE_LLM_MODEL = "llama2-uncensored"

# List of models for comparison/testing
# Used in examples that compare multiple models
COMPARISON_MODELS = [
    "llama2-uncensored",
    "deepseek-r1:8b", 
    "llama3-groq-tool-use"
]

# ============================================================================
# Embedding Models Configuration
# ============================================================================

# Embedding model for vector operations and RAG
# Used in LlamaIndex examples and vector database operations
EMBEDDING_MODEL = "nomic-embed-text"

# ============================================================================
# Default Temperature Settings
# ============================================================================

# Temperature for creative/exploratory tasks
CREATIVE_TEMPERATURE = 0.7

# Temperature for precise/deterministic tasks  
PRECISE_TEMPERATURE = 0.3

# Temperature for balanced tasks
BALANCED_TEMPERATURE = 0.5

# ============================================================================
# Timeout Settings
# ============================================================================

# Default timeout for Ollama requests (in seconds)
DEFAULT_TIMEOUT = 60.0

# Extended timeout for complex operations (in seconds)
EXTENDED_TIMEOUT = 120.0

# ============================================================================
# Helper Functions
# ============================================================================

def get_primary_model():
    """Get the primary LLM model name."""
    return PRIMARY_LLM_MODEL

def get_alternative_model():
    """Get the alternative LLM model name."""
    return ALTERNATIVE_LLM_MODEL

def get_embedding_model():
    """Get the embedding model name."""
    return EMBEDDING_MODEL

def get_comparison_models():
    """Get list of models for comparison."""
    return COMPARISON_MODELS

def print_config():
    """Print current configuration."""
    print("=" * 60)
    print("Current Model Configuration")
    print("=" * 60)
    print(f"Primary LLM Model:     {PRIMARY_LLM_MODEL}")
    print(f"Alternative LLM Model: {ALTERNATIVE_LLM_MODEL}")
    print(f"Embedding Model:       {EMBEDDING_MODEL}")
    print(f"Comparison Models:     {', '.join(COMPARISON_MODELS)}")
    print("=" * 60)

# ============================================================================
# Validation
# ============================================================================

def validate_models():
    """
    Validate that configured models are available in Ollama.
    Returns True if all models are available, False otherwise.
    """
    import subprocess
    
    try:
        # Get list of available models
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            check=True
        )
        
        available_models = result.stdout.lower()
        
        # Check each configured model
        all_models = [PRIMARY_LLM_MODEL, ALTERNATIVE_LLM_MODEL, EMBEDDING_MODEL] + COMPARISON_MODELS
        missing_models = []
        
        for model in set(all_models):  # Use set to avoid duplicates
            # Extract base model name (before :)
            base_model = model.split(':')[0].lower()
            if base_model not in available_models:
                missing_models.append(model)
        
        if missing_models:
            print("\n⚠️  WARNING: The following models are not available in Ollama:")
            for model in missing_models:
                print(f"   - {model}")
            print("\nPull missing models with:")
            for model in missing_models:
                print(f"   ollama pull {model}")
            print()
            return False
        else:
            print("\n✅ All configured models are available!")
            return True
            
    except FileNotFoundError:
        print("\n❌ Ollama is not installed or not in PATH")
        return False
    except subprocess.CalledProcessError:
        print("\n❌ Failed to check Ollama models. Is Ollama running?")
        return False

# ============================================================================
# Auto-validation on import (optional - can be commented out)
# ============================================================================

if __name__ == "__main__":
    print_config()
    print()
    validate_models()
