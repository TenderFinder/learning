# Unit 6: LlamaIndex RAG - Exercises

## Learning Objectives
- Build RAG systems with LlamaIndex
- Implement various indexing strategies
- Create custom retrievers
- Integrate with LangGraph agents

---

## Exercise 1: Build Your First RAG System (Beginner)

**Objective**: Create a simple document Q&A system.

**What You'll Build**:
A Python script that ingests a folder of text and answers questions about it.

**Steps**:
1. **Prepare Data**:
   - Create a folder `data/` and add `paul_graham_essay.txt` (or any text).

2. **Ingest Documents**:
   - `from llama_index.core import SimpleDirectoryReader`
   - `documents = SimpleDirectoryReader("./data").load_data()`

3. **Index Data**:
   - `from llama_index.core import VectorStoreIndex`
   - `index = VectorStoreIndex.from_documents(documents)`
   - Note: Use `Settings.embed_model = "local:nomic-embed-text"` if using Ollama.

4. **Query Engine**:
   - `query_engine = index.as_query_engine()`
   - `response = query_engine.query("What did the author do in college?")`

5. **Output**:
   - Print `response`.
   - Print `response.source_nodes[0]` to see where the answer came from.

**Expected Output**:
```
Answer: The author worked on writing and programming...
Source: .../data/essay.txt (Score: 0.85)
```

---

## Exercise 2: Hybrid Search (Intermediate)

**Objective**: Improve retrieval by mixing keywords and vectors.

**What You'll Build**:
A retriever that finds matches using both exact keywords ("Python 3.12") and semantic meaning ("coding language").

**Steps**:
1. **Setup**:
   - Install `llama-index-retrievers-bm25`.

2. **Create Indices**:
   - `vector_index = VectorStoreIndex.from_documents(docs)`
   - `bm25_retriever = BM25Retriever.from_defaults(docstore=vector_index.docstore, ...)`

3. **Combined Retriever**:
   - Use `QueryFusionRetriever` (or custom combination).
   - Retrieve top 5 from Vector, top 5 from BM25.
   - Re-rank or de-duplicate.

4. **Test Queries**:
   - "SpecificErrorCode123" (Should be caught by BM25).
   - "How do I fix a crash?" (Should be caught by Vector).

**Observation**:
- Notice how some queries work better with one method than the other.

---

## Exercise 3: Metadata Filters (Intermediate)

**Objective**: Use metadata for sophisticated retrieval.

**What You'll Build**:
A search engine that can filter by Year, Author, or Tag.

**Steps**:
1. **Create Tagged Documents**:
   - `doc1 = Document(text="...", metadata={"year": 2023, "tag": "AI"})`
   - `doc2 = Document(text="...", metadata={"year": 2024, "tag": "Crypto"})`

2. **Index**:
   - Build `VectorStoreIndex` from these documents.

3. **Define Filters**:
   - `from llama_index.core.vector_stores import MetadataFilters, ExactMatchFilter`
   - `filters = MetadataFilters(filters=[ExactMatchFilter(key="year", value=2024)])`

4. **Query**:
   - `engine = index.as_query_engine(filters=filters)`
   - Ask: "What happened recently?"
   - Verify it ONLY returns info from doc2.

---

## Exercise 4: Conversational RAG (Advanced)

**Objective**: Build a chat interface for your knowledge base.

**What You'll Build**:
A system that remembers " what you just asked" while looking up documents.

**Steps**:
1. **Chat Engine**:
   - `chat_engine = index.as_chat_engine(chat_mode="context", system_prompt="You are a helpful assistant.")`

2. **Conversation Loop**:
   - `while True:`
   - `q = input("User: ")`
   - `response = chat_engine.chat(q)`
   - `print(response)`

3. **Test Context**:
   - User: "What is the capital of France?" (System finds doc).
   - Bot: "Paris."
   - User: "What is the population there?" (System must infer 'there' means 'Paris').

---

## Exercise 5: Agentic RAG (Advanced)

**Objective**: Combine LlamaIndex with LangGraph for agentic retrieval.

**What You'll Build**:
A LangGraph agent that treats your Vector Store as a **Tool**.

**Steps**:
1. **Wrap LlamaIndex as Tool**:
   - Define a function `query_docs(query: str) -> str`.
   - Inside, call `query_engine.query(query)`.
   - Decorate with `@tool`.

2. **LangGraph Agent**:
   - Create a ReAct agent (from Unit 5).
   - Bind `query_docs` as its only tool.

3. **Complex Query**:
   - Ask: "Compare the revenue of Apple in 2023 vs 2024 based on the docs."
   - Agent Loop:
     - 1. Call `query_docs("Apple revenue 2023")`.
     - 2. Call `query_docs("Apple revenue 2024")`.
     - 3. Subtract/Compare in Python (or LLM reasoning).
     - 4. Final Answer.

**Success**: The agent makes *multiple* calls to the index to answer a multi-part question.

---

## Challenge Project: Personal Knowledge Base

**Objective**: Build a production-ready personal knowledge system.

**Requirements**:
1. **Supported Formats**: Ingest `.txt`, `.md`, and `.pdf` from a `docs/` folder.
2. **Persistence**: Save the index to disk (`index.storage_context.persist()`) so you don't rebuild it every time.
3. **CLI Interface**:
   - `python kb.py add <file>`
   - `python kb.py ask "<question>"`
4. **Citations**: output the filename of the source document with every answer.
5. **Robustness**: Handle empty query results gracefully ("I couldn't find that info").

**Deliverable**:
A `kb.py` script that acts as your second brain.

---

**Estimated Time**: 12-15 hours
**Prerequisites**: Units 1-5 completed
**Key Concepts**: RAG, Embeddings, Vector Search, Retrieval Strategies
