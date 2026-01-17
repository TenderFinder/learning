# Unit 6: LlamaIndex RAG - Exercises

## Learning Objectives
- Build RAG systems with LlamaIndex
- Implement various indexing strategies
- Create custom retrievers
- Integrate with LangGraph agents

---

## Exercise 1: Build Your First RAG System (Beginner)

**Objective**: Create a simple document Q&A system.

**Tasks**:
1. Create a folder with 3-5 text files on a topic of your choice
2. Load documents using SimpleDirectoryReader
3. Create a VectorStoreIndex
4. Build a query engine
5. Test with at least 10 questions

**Requirements**:
- Use Ollama for LLM (llama3)
- Use Ollama for embeddings (nomic-embed-text)
- Print source documents for each answer

**Example Topics**:
- Personal notes/documentation
- Wikipedia articles on a subject
- Tutorial content
- Research papers

---

## Exercise 2: Advanced Retrieval Strategies (Intermediate)

**Objective**: Compare different retrieval approaches.

**Tasks**:
Test the same document set with:
1. VectorStoreIndex (semantic search)
2. KeywordTableIndex (keyword search)
3. Hybrid approach (combine both)

**Compare**:
- Accuracy of answers
- Response time
- Best use cases for each

**Test Questions** (10+):
- Factual questions
- Conceptual questions
- Questions needing context

---

## Exercise 3: Custom Metadata and Filtering (Intermediate)

**Objective**: Use metadata for sophisticated retrieval.

**Tasks**:
1. Create documents with rich metadata:
   - Author
   - Date
   - Category
   - Difficulty level
   - Tags
2. Implement filtered retrieval:
   - "Find beginner-level articles about Python"
   - "Show documents from 2024 about AI"
   - "Get advanced tutorials tagged 'machine-learning'"
3. Build a metadata-aware query engine

**Deliverable**: System that can filter by any metadata field

---

## Exercise 4: Conversational RAG (Advanced)

**Objective**: Build a chat interface for your knowledge base.

**Tasks**:
1. Create a knowledge base from documentation
2. Implement chat engine with context
3. Support multi-turn conversations:
   - Follow-up questions
   - Clarifications
   - Topic switches
4. Maintain conversation history
5. Track which documents were referenced

**Example Conversation**:
```
User: What is LangGraph?
Bot: [Answer with sources]

User: How does it differ from LangChain?
Bot: [Contextual answer referencing previous response]

User: Show me an example
Bot: [Code example from docs]
```

---

## Exercise 5: Multi-Document Analysis (Advanced)

**Objective**: Compare and synthesize information across documents.

**Tasks**:
Create a system that can:
1. Compare approaches from different documents
2. Find contradictions or agreements
3. Synthesize a comprehensive answer

**Example Query**:
"How do LangChain and LlamaIndex approach memory management? Compare their approaches."

**Requirements**:
- Load docs about both frameworks
- Retrieve relevant sections from each
- Generate comparative analysis
- Cite specific sources

---

## Exercise 6: Structured Data Extraction (Advanced)

**Objective**: Extract structured information from unstructured text.

**Tasks**:
1. Load documents containing information about people, places, or products
2. Extract structured data:
   ```python
   {
       "name": "...",
       "description": "...",
       "key_facts": [...],
       "related_entities": [...]
   }
   ```
3. Store in a structured format (JSON)
4. Enable querying the structured data

**Example**: Extract product information from reviews

---

## Exercise 7: Citation and Source Tracking (Intermediate)

**Objective**: Build a system with proper citations.

**Tasks**:
1. Create a RAG system that always includes:
   - Source document name
   - Page number (if applicable)
   - Relevant quote
   - Confidence score
2. Format citations properly
3. Handle multiple sources

**Expected Output Format**:
```
Answer: LangGraph is a library for building stateful agents...

Sources:
[1] langgraph_docs.pdf, p.3, Score: 0.95
    "LangGraph extends LangChain to enable..."

[2] langchain_blog.txt, Score: 0.87
    "The key difference is state management..."
```

---

## Exercise 8: Custom Embedding Models (Advanced)

**Objective**: Experiment with different embedding models.

**Tasks**:
1. Test same documents with different embeddings:
   - nomic-embed-text
   - mxbai-embed-large
   - all-minilm
2. Compare:
   - Retrieval accuracy
   - Speed
   - index size
3. Recommend best for different scenarios

**Metrics to track**:
- Embedding dimension
- Time to index
- Time to query
- Recall @K

---

## Challenge Project: Personal Knowledge Base

**Objective**: Build a production-ready personal knowledge system.

**Requirements**:
1. **Document Ingestion**:
   - Support multiple formats (PDF, TXT, MD, DOCX)
   - Automatic metadata extraction
   - Deduplication

2. **Indexing**:
   - Efficient chunking strategy
   - Metadata-enhanced indexing
   - Periodic re-indexing

3. **Querying**:
   - Natural language queries
   - Filtered search
   - Semantic + keyword hybrid

4. **Features**:
   - Conversational interface
   - Export answers to format (MD, PDF)
   - Source highlighting
   - Related document suggestions

5. **CLI Interface**:
   ```bash
   $ kb add document.pdf
   $ kb search "machine learning basics"
   $ kb chat
   $ kb export --query "AI concepts" --format pdf
   ```

**Bonus Features**:
- Web interface (Gradio/Streamlit)
- Auto-tagging with LLM
- Knowledge graph visualization
- Spaced repetition for learning
- Share knowledge bases

---

## Advanced Challenge: Agentic RAG System

**Objective**: Combine LlamaIndex with LangGraph for agentic retrieval.

**Tasks**:
Build a system that:
1. Analyzes query complexity
2. Decides retrieval strategy:
   - Simple query → direct retrieval
   - Complex query → decompose → multiple retrievals → synthesize
   - Ambiguous query → ask clarifying questions
3. Self-corrects if answer quality is low
4. Cites all sources

**Implementation**:
```python
class AgenticRAG:
    def query(self, question: str) -> Response:
        # 1. Analyze question
        # 2. Plan retrieval strategy
        # 3. Execute retrieval (potentially multiple rounds)
        # 4. Check answer quality
        # 5. Refine if needed
        # 6. Return with citations
```

**Test Scenarios**:
- Simple factual question
- Multi-hop reasoning question
- Question requiring synthesis
- Ambiguous question

---

## Optimization Exercise: Production RAG

**Objective**: Optimize RAG system for production.

**Tasks**:
1. Implement caching:
   - Query cache
   - Embedding cache
2. Add monitoring:
   - Query latency
   - Retrieval accuracy
   - Index size
3. Optimize chunk size (experiment with different sizes)
4. Implement incremental indexing
5. Add health checks

**Performance Goals**:
- < 2s query latency
- > 80% retrieval accuracy
- Efficient memory usage

---

**Estimated Time**: 12-15 hours
**Prerequisites**: Units 1-5 completed
**Key Concepts**: RAG, Embeddings, Vector Search, Retrieval Strategies
