# Unit 2: Setting Up the Development Environment - Exercises

## Learning Objectives
By completing these exercises, you will:
- Set up a complete development environment for agentic AI
- Verify all dependencies and tools
- Test integrations with Ollama
- Benchmark model performance
- Troubleshoot common setup issues

---

## Exercise 1: Complete Environment Setup (Beginner)

**Objective**: Set up your development environment from scratch.

**Tasks**:
1. Create a new virtual environment called `agentic-ai-env`
2. Activate the virtual environment
3. Install all required packages:
   - langchain
   - langchain-community
   - langgraph
   - llama-index
   - llama-index-llms-ollama
   - llama-index-embeddings-ollama
   - chromadb
   - requests
4. Create a Python script that verifies all packages are installed
5. Print the version of each package

**Expected Output**:
```
✅ Virtual environment created: agentic-ai-env
✅ All packages installed successfully

Package Versions:
  langchain: 0.1.x
  langgraph: 0.0.x
  llama-index: 0.9.x
  chromadb: 0.4.x
  ...
```

**Deliverable**: A bash/shell script that automates this setup process.

---

## Exercise 2: Ollama Model Management (Beginner)

**Objective**: Practice managing Ollama models.

**Tasks**:
1. Pull 3 different models:
   - llama3 (general purpose)
   - nomic-embed-text (embeddings)
   - mistral (alternative LLM)
2. Create a Python script that:
   - Lists all installed models
   - Shows model sizes
   - Shows when each was pulled
3. Test each model with a simple prompt
4. Remove one model and verify it's gone

**Expected Output**:
```
=== Installed Ollama Models ===

llama3
  Size: 4.7 GB
  Modified: 2 days ago
  Status: ✅ Working

nomic-embed-text
  Size: 274 MB
  Modified: 1 day ago
  Status: ✅ Working

mistral
  Size: 4.1 GB
  Modified: 3 hours ago
  Status: ✅ Working
```

**Hints**:
- Use the Ollama API at `http://localhost:11434/api/tags`
- Use `requests` library to interact with the API

---

## Exercise 3: Integration Testing Suite (Intermediate)

**Objective**: Create a comprehensive test suite for your setup.

**Tasks**:
Create a test file that checks:
1. Python version (must be >= 3.8)
2. Virtual environment status
3. All required packages installed
4. Ollama server running
5. LangChain + Ollama integration working
6. LlamaIndex + Ollama integration working
7. Embedding model available
8. Vector database (ChromaDB) working

**Requirements**:
- Each test should return ✅ (pass) or ❌ (fail)
- Failed tests should include troubleshooting suggestions
- Generate a final summary report

**Expected Output**:
```
=== Environment Test Suite ===

[✅] Python Version: 3.11.5
[✅] Virtual Environment: Active
[✅] Required Packages: All installed
[✅] Ollama Server: Running
[✅] LangChain Integration: Working
[✅] LlamaIndex Integration: Working
[✅] Embedding Model: Available
[✅] Vector Database: Working

=== Summary ===
8/8 tests passed
Environment is ready! 🎉
```

**Bonus**: Save the report as a JSON file with timestamps.

---

## Exercise 4: Model Performance Benchmark (Intermediate)

**Objective**: Benchmark different models for performance.

**Tasks**:
1. Create a benchmarking script that tests 3+ models
2. For each model, measure:
   - Response time for a short prompt (10 words)
   - Response time for a medium prompt (50 words)
   - Response time for a long prompt (200 words)
   - Memory usage (if possible)
3. Generate a comparison table
4. Visualize results (can use simple text-based charts)

**Test Prompts**:
- Short: "Count to five."
- Medium: "Explain what Python is and why it's popular for AI development."
- Long: "Write a detailed tutorial on installing and using Ollama for local AI model deployment, including troubleshooting tips."

**Expected Output**:
```
=== Model Performance Benchmark ===

Model: llama3
  Short Prompt:  0.45s
  Medium Prompt: 1.23s
  Long Prompt:   4.56s
  Avg Response:  2.08s

Model: mistral
  Short Prompt:  0.38s
  Medium Prompt: 1.01s
  Long Prompt:   3.89s
  Avg Response:  1.76s

Model: phi3
  Short Prompt:  0.25s
  Medium Prompt: 0.67s
  Long Prompt:   2.34s
  Avg Response:  1.09s

Fastest Model: phi3 (1.09s avg)
```

**Bonus**: Create a bar chart visualization of the results.

---

## Exercise 5: Error Handling and Troubleshooting (Advanced)

**Objective**: Handle common error scenarios gracefully.

**Tasks**:
Create a robust connection function that:
1. Attempts to connect to Ollama
2. Handles these error scenarios:
   - Ollama not running
   - Model not found
   - Network timeout
   - Invalid model name
3. Provides helpful error messages
4. Suggests fixes for each error type
5. Allows retry attempts

**Example Function Signature**:
```python
def connect_to_ollama(
    model_name: str,
    max_retries: int = 3,
    timeout: int = 30
) -> Ollama | None:
    """
    Robustly connect to Ollama with error handling.
    Returns Ollama instance or None if all retries fail.
    """
    pass
```

**Expected Behavior**:
```python
 Test 1: Valid model
llm = connect_to_ollama("llama3")
# ✅ Connected successfully

# Test 2: Model not found
llm = connect_to_ollama("fake-model")
# ❌ Model 'fake-model' not found
# 💡 Available models: llama3, mistral, phi3
# 💡 Pull with: ollama pull fake-model

# Test 3: Ollama not running
llm = connect_to_ollama("llama3")
# ❌ Cannot connect to Ollama server
# 💡 Start Ollama with: ollama serve
# 🔄 Retrying in 5 seconds... (1/3)
```

---

## Exercise 6: Multi-Framework Embedding Test (Intermediate)

**Objective**: Test embedding generation across different frameworks.

**Tasks**:
1. Generate embeddings for the same text using:
   - LlamaIndex's OllamaEmbedding
   - Direct Ollama API call
   - (Optional) HuggingFace sentence-transformers
2. Compare the results:
   - Are they identical?
   - What are the dimensions?
   - How long does each take?
3. Test with different embedding models (nomic-embed-text, mxbai-embed-large)

**Test Text**:
"AI agents are autonomous systems that use language models to reason and act."

**Expected Output**:
```
=== Embedding Comparison ===

Text: "AI agents are autonomous..."

Method 1: LlamaIndex OllamaEmbedding
  Model: nomic-embed-text
  Dimensions: 768
  Time: 0.123s
  First 5 values: [0.123, -0.456, 0.789, ...]

Method 2: Direct Ollama API
  Model: nomic-embed-text
  Dimensions: 768
  Time: 0.118s
  First 5 values: [0.123, -0.456, 0.789, ...]

✅ Results are identical!
```

---

## Exercise 7: Vector Database Setup and Testing (Intermediate)

**Objective**: Set up and test different vector databases.

**Tasks**:
1. Test ChromaDB:
   - Create a collection
   - Add 10 documents
   - Query with semantic search
   - Delete the collection
2. Test FAISS:
   - Create an index
   - Add 10 vectors
   - Search for nearest neighbors
3. Compare performance and ease of use

**Sample Documents**:
```python
documents = [
    "Python is a programming language.",
    "JavaScript runs in web browsers.",
    "Machine learning is a subset of AI.",
    # ... 7 more
]
```

**Expected Output**:
```
=== ChromaDB Test ===
✅ Collection created
✅ 10 documents added
✅ Query: "programming"
   Top 3 results:
   1. "Python is a programming language." (score: 0.95)
   2. "JavaScript runs in web browsers." (score: 0.78)
   3. ...
✅ Collection deleted

=== FAISS Test ===
✅ Index created (dimension: 768)
✅ 10 vectors added
✅ Search query
   Top 3 nearest neighbors:
   1. Index 0 (distance: 0.123)
   2. Index 1 (distance: 0.234)
   3. ...

=== Comparison ===
ChromaDB: Easier to use, more features
FAISS: Faster search, lower memory
```

---

## Exercise 8: Configuration Management (Advanced)

**Objective**: Create a configuration management system for your project.

**Tasks**:
1. Create a `config.yaml` file with:
   - Ollama settings (host, port, timeout)
   - Default models (LLM, embedding)
   - Vector DB settings
   - Logging preferences
2. Create a Python class that:
   - Loads configuration
   - Validates settings
   - Provides easy access to configs
   - Allows runtime overrides
3. Support environment variables (e.g., `OLLAMA_HOST`)

**Example `config.yaml`**:
```yaml
ollama:
  host: localhost
  port: 11434
  timeout: 120
  default_llm: llama3
  default_embedding: nomic-embed-text

vector_db:
  type: chromadb
  persist_directory: ./data/vectordb

logging:
  level: INFO
  file: ./logs/app.log
```

**Usage**:
```python
from config import Config

config = Config.load("config.yaml")

# Access settings
llm_model = config.ollama.default_llm
timeout = config.ollama.timeout

# Override at runtime
config.set("ollama.default_llm", "mistral")
```

---

## Challenge Project: Setup Automation Script

**Objective**: Create a complete setup automation script.

**Requirements**:
Your script should:
1. Check if Ollama is installed (install instructions if not)
2. Check if required models are available (pull if not)
3. Create virtual environment if needed
4. Install all Python packages
5. Run comprehensive tests
6. Generate a setup report
7. Provide next steps

**Bonus Features**:
- Cross-platform support (Mac, Linux, Windows)
- Interactive mode (asks user for preferences)
- Rollback on failure
- Configuration file generation

**Example Usage**:
```bash
$ python setup.py --auto

🚀 Agentic AI Environment Setup

✅ Ollama detected (v0.1.20)
🔍 Checking models...
   ⬇️  Pulling llama3... (4.7 GB)
   ✅ nomic-embed-text already installed
📦 Installing Python packages...
   ✅ langchain==0.1.0
   ✅ langgraph==0.0.20
   ...
🧪 Running tests...
   ✅ All tests passed!

✅ Setup complete!

Next steps:
  1. Activate virtual environment: source agentic-ai-env/bin/activate
  2. Run a test script: python test_ollama.py
  3. Start building!Check out the examples in ./examples/
```

---

## Submission Guidelines

For each exercise, provide:
1. Source code files
2. Requirements.txt (if applicable)
3. README with setup instructions
4. Test output/screenshots

## Evaluation Criteria

- **Completeness**: All tasks completed
- **Error Handling**: Graceful handling of errors
- **Code Quality**: Clean, well-documented code
- **Automation**: How automated is the process?
- **Usability**: Can someone else use your solution?

---

**Estimated Time**: 5-7 hours for all exercises
**Difficulty Progression**: Beginner → Intermediate → Advanced
