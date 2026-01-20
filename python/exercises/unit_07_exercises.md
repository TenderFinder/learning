# Unit 7: Integrating LlamaIndex with LangGraph - Exercises

## Learning Objectives
- Combine LlamaIndex retrieval with LangGraph agents
- Build agentic RAG systems
- Implement query routing and planning
- Create multi-index agent workflows

---

## Exercise 1: LlamaIndex as a LangGraph Tool (Intermediate)

**Objective**: Wrap a LlamaIndex query engine as a tool that a LangGraph agent can use.

**What You'll Build**:
A LangGraph agent that can choose when to search documents vs. when to answer from general knowledge.

**Steps**:
1. **Create Index**:
   - Load documents using `SimpleDirectoryReader`.
   - Build `VectorStoreIndex`.
   - Create query engine: `query_engine = index.as_query_engine()`.

2. **Wrap as Tool**:
   - Define function:
     ```python
     @tool
     def search_docs(query: str) -> str:
         """Search through technical documentation."""
         response = query_engine.query(query)
         return str(response)
     ```

3. **Build Agent**:
   - Create `AgentState` with `messages: Annotated[list, add_messages]`.
   - Bind `search_docs` to your LLM: `model.bind_tools([search_docs])`.
   - Use `ToolNode` from `langgraph.prebuilt`.

4. **Create Graph**:
   - Node 1: `agent` (calls LLM).
   - Node 2: `tools` (executes tool if called).
   - Conditional edge using `tools_condition`.

5. **Test**:
   - "What is LangGraph?" (Should call tool if docs contain that info).
   - "What is 2+2?" (Should answer directly, no tool).

**Expected Behavior**:
Agent intelligently decides when to retrieve from documents vs. answering from its own knowledge.

---

## Exercise 2: Multi-Index Routing Agent (Advanced)

**Objective**: Build an agent that routes queries to different indexes based on content.

**What You'll Build**:
A system with separate indexes for "Python docs", "JavaScript docs", and "DevOps docs" that intelligently routes queries.

**Steps**:
1. **Create Multiple Indexes**:
   - `python_index = VectorStoreIndex.from_documents(python_docs)`
   - `js_index = VectorStoreIndex.from_documents(js_docs)`
   - `devops_index = VectorStoreIndex.from_documents(devops_docs)`

2. **Create Specialized Tools**:
   - `@tool` for `search_python(query: str)`.
   - `@tool` for `search_javascript(query: str)`.
   - `@tool` for `search_devops(query: str)`.

3. **Routing Strategy**:
   - **Option A**: Let the LLM choose which tool (based on tool descriptions).
   - **Option B**: Add a "router" node that classifies the query first, then routes.

4. **Build Graph**:
   - If using Option A: Standard ReAct agent with all 3 tools.
   - If using Option B:
     - `classifier` node -> determines domain.
     - Conditional edge routes to appropriate index node.
     - Each index node -> synthesis node.

5. **Test Queries**:
   - "How do I use async/await in Python?" (Should use python tool).
   - "Explain Docker volumes" (Should use devops tool).
   - "What is a React hook?" (Should use javascript tool).

**Success Criteria**:
- Queries are routed to the correct index.
- Agent can combine information from multiple indexes if needed.

---

## Exercise 3: Self-Reflective RAG (Advanced)

**Objective**: Build an agent that critiques its own retrieved information.

**What You'll Build**:
A "Self-RAG" system where the agent retrieves, then checks if the retrieval was useful, and retrieves again if not.

**Steps**:
1. **State Definition**:
   - `question`: str
   - `retrieved_docs`: list
   - `answer`: str
   - `confidence`: str (low/medium/high)
   - `retrieval_count`: int

2. **Nodes**:
   - `retrieve_node`: Calls query engine, updates `retrieved_docs`.
   - `answer_node`: Generates answer based on docs.
   - `reflect_node`: LLM evaluates if answer quality is good (check for relevance, completeness).

3. **Routing Logic**:
   - If confidence is "high" -> END.
   - If confidence is "low" and `retrieval_count` < 3 -> `retrieve_node` (with a refined query).
   - If `retrieval_count` >= 3 -> END (give best answer you have).

4. **Build Graph**:
   - Entry: `retrieve_node`.
   - `retrieve` -> `answer` -> `reflect` -> (conditional) -> `retrieve` OR END.

5. **Test**:
   - Query: "How do I optimize database performance?" (Might need multiple retrievals).
   - Track how many retrieval iterations it takes.

**Expected Behavior**:
Agent retrieves, evaluates the quality, and retrieves again if the first attempt wasn't sufficient.

---

## Exercise 4: Query Decomposition Agent (Advanced)

**Objective**: Break complex queries into sub-questions.

**What You'll Build**:
An agent that takes a complex question, decomposes it, answers each part, then synthesizes.

**Steps**:
1. **Decomposition Node**:
   - Use LLM to break query into 2-4 sub-questions.
   - Store in state: `sub_questions: list[str]`.

2. **Answering Loop**:
   - For each sub-question:
     - Retrieve from index.
     - Store answer.

3. **Synthesis Node**:
   - Combine all sub-answers into coherent final answer.

4. **Graph Structure**:
   - `decompose` -> `answer_sub_q_1` -> `answer_sub_q_2` -> ... -> `synthesize` -> END.
   - Or use a loop with index tracking.

5. **Complex Query Test**:
   - "Compare the performance of microservices vs monolithic architecture in terms of scalability, maintainability, and deployment complexity."
   - Should decompose into:
     - "What is the scalability of microservices?"
     - "What is the scalability of monoliths?"
     - "What is the maintainability of microservices?"
     - ... etc.

**Expected Flow**:
```
Query: [complex question]
Decomposed into: [Q1, Q2, Q3]
Answering Q1: [sub-answer 1]
Answering Q2: [sub-answer 2]
...
Final Synthesis: [comprehensive answer]
```

---

## Exercise 5: Corrective RAG (CRAG) (Expert)

**Objective**: Implement a system that detects irrelevant retrievals and falls back to web search.

**What You'll Build**:
A CRAG agent that evaluates retrieval quality and uses alternative sources if needed.

**Steps**:
1. **State**:
   - `query`: str
   - `retrieved_docs`: list
   - `relevance_score`: float
   - `web_results`: str (optional fallback)
   - `final_answer`: str

2. **Nodes**:
   - `retrieve_from_index`: Standard RAG retrieval.
   - `grade_documents`: LLM judges if docs are relevant (returns score 0-1).
   - `web_search`: Simulated web search (or real API like Tavily).
   - `generate_answer`: Creates answer from best available source.

3. **Routing**:
   - If `relevance_score` > 0.7 -> Use retrieved docs.
   - If `relevance_score` < 0.7 -> Use web search.

4. **Graph**:
   - `retrieve` -> `grade` -> (conditional):
     - High score -> `generate_answer`.
     - Low score -> `web_search` -> `generate_answer`.

5. **Test Cases**:
   - Query in your docs (should use index).
   - Query NOT in your docs (should fall back to web).

**Success**:
Agent adaptively chooses the best information source based on retrieval quality.

---

## Exercise 6: Report Generation with Citations (Advanced)

**Objective**: Build an agent that generates a formatted research report.

**What You'll Build**:
A system that researches a topic, gathers info from multiple sources, and outputs a markdown report with citations.

**Steps**:
1. **Research Phase**:
   - Take input: "Research topic: [X]".
   - Decompose into 3-5 sub-topics.
   - Retrieve documents for each.

2. **Citation Tracking**:
   - For every retrieved chunk, track `source_file` and `page_number`.
   - Store in state: `citations: list[Citation]`.

3. **Report Generation**:
   - Use an LLM to write sections.
   - Insert citation markers `[1]`, `[2]`, etc.
   - Generate "References" section at end.

4. **Output Format**:
   ```markdown
   # Research Report: [Topic]
   
   ## Executive Summary
   [Generated summary]
   
   ## Section 1: [Subtopic]
   [Content with citations [1], [2]]
   
   ## Section 2: [Subtopic]
   ...
   
   ## References
   [1] source_file.pdf, p.15
   [2] another_file.txt
   ```

5. **Test**:
   - Input: "Research the history of neural networks".
   - Verify citations are accurate and formatted correctly.

**Deliverable**:
A complete markdown report that could be published.

---

## Challenge Project: Multi-Domain Expert System

**Objective**: Build a production-ready system that serves as an expert in multiple domains.

**Requirements**:
1. **Multiple Indexes**:
   - At least 3 domains (e.g., "Legal", "Medical", "Technical").
   - Each with its own specialized index.

2. **Intelligent Routing**:
   - Classifier determines which domain(s) to query.
   - Can query multiple domains if question spans them.

3. **Advanced RAG**:
   - Implements at least 2 of: Self-RAG, CRAG, Query Decomposition.

4. **Citation and Sourcing**:
   - Every answer includes source attribution.
   - Confidence scores for each piece of information.

5. **API Interface**:
   - FastAPI endpoint: `POST /ask` with `{"question": "..."}`.
   - Response includes answer, sources, and confidence.

6. **Monitoring**:
   - Log all queries and retrieval paths.
   - Track which indexes are used most.

**Example Interaction**:
```json
POST /ask
{
  "question": "What are the legal implications of using AI in medical diagnosis?"
}

Response:
{
  "answer": "...",
  "sources": [
    {"domain": "legal", "file": "medical_law.pdf", "confidence": 0.9},
    {"domain": "medical", "file": "ai_diagnostics.pdf", "confidence": 0.85}
  ],
  "domains_queried": ["legal", "medical"],
  "retrieval_strategy": "multi-domain-parallel"
}
```

**Success Criteria**:
- Handles cross-domain queries correctly.
- Provides transparent sourcing.
- Production-ready error handling.

---

**Estimated Time**: 15-18 hours for all exercises  
**Difficulty**: Intermediate to Expert  
**Prerequisites**: Units 1-6 completed, especially Units 5 and 6
**Key Concepts**: Agentic RAG, Query Routing, Multi-Index Systems, Self-Reflection
