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

**What You'll Build**:
A Python virtual environment with all necessary dependencies installed and verified.

**Steps**:
1. **Create Virtual Environment**:
   - Open your terminal.
   - Run: `python -m venv agentic-ai-env`
   - Activate it:
     - Mac/Linux: `source agentic-ai-env/bin/activate`
     - Windows: `agentic-ai-env\Scripts\activate`

2. **Upgrade Pip**:
   - Run: `pip install --upgrade pip`

3. **Install Core Packages**:
   - Run: `pip install langchain langchain-community langgraph langchain-ollama`

4. **Install RAG & Data Tools**:
   - Run: `pip install llama-index llama-index-llms-ollama llama-index-embeddings-ollama chromadb`
   - Run: `pip install requests pandas matplotlib` (utilities)

5. **Verify Installation Script**:
   - Create `verify_setup.py`.
   - Import all packages (`import langchain`, `import langgraph`, etc.).
   - Print `package.__version__` for each.
   - Run the script: `python verify_setup.py`.

**Expected Output**:
```
✅ Virtual environment created: agentic-ai-env
✅ All packages installed successfully

Package Versions:
  langchain: 0.3.x
  langgraph: 0.2.x
  llama-index: 0.12.x
  chromadb: 0.6.x
```

---

## Exercise 2: Ollama Model Management (Beginner)

**Objective**: Practice managing Ollama models.

**What You'll Build**:
A script that interacts with the Ollama API to manage local models.

**Steps**:
1. **Pull Models**:
   - Run in terminal:
     - `ollama pull llama3`
     - `ollama pull nomic-embed-text`
     - `ollama pull mistral`

2. **Access API**:
   - Create `manage_models.py`.
   - Use `requests.get('http://localhost:11434/api/tags')` to get json data.

3. **Parse & Display**:
   - Iterate through the `models` list in the response.
   - Print the `name` and `size` (convert bytes to GB for readability).

4. **Test Model**:
   - Use `requests.post('http://localhost:11434/api/generate', ...)` to send a "hello" prompt to `mistral`.
   - Verify it responds.

5. **Cleanup**:
   - Programmatically delete `mistral` using the API `DELETE /api/delete`.
   - Verify it's gone from the list.

**Expected Output**:
```
=== Installed Ollama Models ===
llama3 | Size: 4.7 GB
nomic-embed-text | Size: 0.2 GB

Model 'mistral' deleted successfully.
```

---

## Exercise 3: Integration Testing Suite (Intermediate)

**Objective**: Create a comprehensive test suite for your setup.

**What You'll Build**:
A "health check" script that ensures your entire stack is communicating correctly.

**Steps**:
1. **Check Python**:
   - Use `sys.version` to assert Python >= 3.10.

2. **Check Ollama Connection**:
   - Try a simple HTTP GET to localhost:11434.
   - Catch `ConnectionError` and print a helpful "Is Ollama running?" message.

3. **Check Vector DB**:
   - Initialize a generic ChromaDB client (`chromadb.Client()`).
   - Create a dummy collection and delete it.

4. **Check LLM generation**:
   - Initialize `ChatOllama`.
   - Invoke with "hi". Assert response is not empty.

5. **Check Embeddings**:
   - Initialize `OllamaEmbeddings`.
   - Embed query "test". Assert result is a list of floats.

**Expected Output**:
```
=== Environment Test Suite ===

[✅] Python Version: 3.11.x
[✅] Virtual Environment: Active
[✅] Ollama Server: Running (v0.1.x)
[✅] LangChain Integration: Working
[✅] Vector Database: Working
...
Summary: 8/8 tests passed. Environment is ready! 🎉
```

---

## Exercise 4: Model Performance Benchmark (Intermediate)

**Objective**: Benchmark different models for performance.

**What You'll Build**:
A data-driven comparison of different LLMs running on your hardware.

**Steps**:
1. **Setup Prompts**:
   - Define a dictionary of prompts: `{"short": "Hi", "medium": "Explain AI", "long": "Write a story..."}`.

2. **Benchmark Loop**:
   - For each model (llama3, phi3):
     - For each prompt type:
       - Measure `start_time`.
       - Generate response.
       - Measure `end_time`.
       - Record `duration` and `token_count` (approx words * 1.3).

3. **Calculate Metrics**:
   - Tokens per second (TPS) = `total_tokens / total_time`.
   - Average latency.

4. **Visualize**:
   - Print a text-based table or generate a simple `.png` bar chart using `matplotlib`.

**Expected Output**:
```
=== Model Performance Benchmark ===

Model: llama3
  Avg Latency: 2.08s
  Tokens/Sec: 45.2

Model: phi3
  Avg Latency: 1.09s
  Tokens/Sec: 62.1

Fastest Model: phi3
```

---

## Exercise 5: Error Handling and Troubleshooting (Advanced)

**Objective**: Handle common error scenarios gracefully.

**What You'll Build**:
A robust wrapper function for connecting to LLMs that never crashes.

**Steps**:
1. **Define Function**:
   - `connect_to_ollama(model_name: str, max_retries: int)`.

2. **Implement Retry Logic**:
   - Use a `while` loop (attempts < max_retries).
   - Use `try/except` block inside.

3. **Handle Specific Errors**:
   - `ConnectionError` -> "Ollama not reachable. Retrying in 5s..."
   - `ResponseError` (404) -> "Model not found. Pulling model..." (Simulate or actually run pull).
   - `Timeout` -> "Request timed out."

4. **Test**:
   - Call with "fake-model" (should error/pull).
   - Kill Ollama server and call (should retry/fail gracefully).

**Expected Output**:
```
Attempting connection to 'llama3'... Success.
Attempting connection to 'fake-model'...
❌ Model not found.
💡 Suggestion: Run `ollama pull fake-model`
```

---

## Exercise 6: Multi-Framework Embedding Test (Intermediate)

**Objective**: Test embedding generation across different frameworks.

**What You'll Build**:
A script comparing embeddings from LangChain and direct API calls.

**Steps**:
1. **Setup**:
   - Text: "AI agents are autonomous."
   - Model: `nomic-embed-text`.

2. **Method 1 (LangChain)**:
   - Use `OllamaEmbeddings`.
   - `embed_query(text)`.
   - Record vector and expected dimension (e.g., 768).

3. **Method 2 (Raw API)**:
   - Use `requests.post` to `/api/embeddings`.
   - Parse JSON for `embedding`.

4. **Compare**:
   - Verify both lists are almost equal (floating point tolerance).
   - Compare generation time.

**Expected Output**:
```
Method 1 (LangChain): Dimension 768 | Time 0.1s
Method 2 (API):       Dimension 768 | Time 0.09s
✅ Embeddings match!
```

---

## Exercise 7: Vector Database Setup and Testing (Intermediate)

**Objective**: Set up and test different vector databases.

**What You'll Build**:
A script to ingest, store, and query text using ChromaDB.

**Steps**:
1. **Initialize Chroma**:
   - `import chromadb`.
   - Create a persistent client: `chromadb.PersistentClient(path="./chroma_db")`.

2. **Create Collection**:
   - `client.get_or_create_collection("my_docs")`.

3. **Add Documents**:
   - Prepare list of docs ["Python is cool", "Javascript is web", ...].
   - Add them to collection with IDs ["id1", "id2", ...]. (`chromadb` handles embeddings automatically by default, or you can pass your own).

4. **Query**:
   - `collection.query(query_texts=["coding language"], n_results=1)`.
   - Print the result and distance.

**Expected Output**:
```
=== ChromaDB Test ===
✅ Collection created
✅ 10 documents added
✅ Query: "programming"
   Result: "Python is cool" (Distance: 0.4)
```

---

## Exercise 8: Configuration Management (Advanced)

**Objective**: Create a configuration management system for your project.

**What You'll Build**:
A robust Config class that loads settings from `config.yaml` and environment variables.

**Steps**:
1. **Create YAML**:
   - `config.yaml` with keys for `ollama_url`, `default_model`, `timeout`.

2. **Create Config Class**:
   - Method `load_yaml()`: Reads the file.
   - Method `load_env()`: Checks `os.environ` for overrides (e.g., `OLLAMA_URL`).

3. **Validation**:
   - Ensure `timeout` is a positive integer.
   - Ensure `default_model` is a non-empty string.

4. **Usage**:
   - In your main app: `cfg = Config()` -> `llm = ChatOllama(model=cfg.model)`.

**Example config.yaml**:
```yaml
ollama:
  host: localhost
  model: llama3
```

---

## Challenge Project: Setup Automation Script

**Objective**: Create a complete setup automation script.

**What You'll Build**:
A "one-click" setup script (`setup.py`) for new developers.

**Steps**:
1. **System Check**:
   - Detect OS (Mac/Windows/Linux).
   - Check if Ollama binary exists in PATH.

2. **Model Hydration**:
   - Check if `llama3` is pulled. If not, subprocess call `ollama pull llama3`.

3. **Environment**:
   - Check if running in a venv. If not, warn user.
   - Install dependencies via `pip install -r requirements.txt`.

4. **Validation**:
   - Run the integration test suite from Exercise 3.

5. **Reporting**:
   - Print a nice summary with emoji status indicators.

**Example Usage**:
```bash
$ python setup.py --auto

🚀 Agentic AI Environment Setup
...
✅ Setup complete! Ready to build.
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
