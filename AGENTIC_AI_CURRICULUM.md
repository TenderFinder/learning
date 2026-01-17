# Agentic AI Course Curriculum
## A Comprehensive Guide to LangGraph, LlamaIndex, and Agentic Systems

**Target Audience**: Software developers new to Agentic AI  
**Duration**: 8-10 weeks (can be adjusted)  
**Tools**: Ollama (local models), LangGraph, LangChain, LlamaIndex  

---

## **Unit 1: Introduction to Agentic AI & Foundation Concepts**

### Week 1: Understanding Agentic AI
**Learning Objectives**:
- Understand what Agentic AI is and how it differs from traditional AI
- Learn the core concepts: agents, tools, memory, planning
- Explore real-world use cases

**Topics**:
1. **Key Components of Agentic Systems**
   - Large Language Models (LLMs)
   - Tools and function calling
   - Memory systems (short-term and long-term)
   - Planning and reasoning frameworks
   - Feedback loops and self-correction

2. **Real-World Applications**
   - Customer service automation
   - Research assistants
   - Code generation and debugging
   - Data analysis agents
   - Multi-agent systems

**Hands-on**:
- Install Python environment
- Set up Ollama
- Download and test your first local model (llama3, mistral)
- Simple LLM interaction examples

**Resources**:
- Papers: "ReAct: Synergizing Reasoning and Acting in Language Models"
- Blog posts on agent architectures

---

## **Unit 2: Setting Up the Development Environment**

### Week 2: Ollama, LangChain, and Tool Setup
**Learning Objectives**:
- Install and configure Ollama for local model deployment
- Set up Python environment with all necessary libraries
- Understand model selection and performance trade-offs

**Topics**:
1. **Ollama Setup and Configuration**
   - Installing Ollama on different platforms
   - Understanding model formats (GGUF)
   - Downloading models (llama3, mistral, phi, qwen)
   - Model quantization and performance considerations
   - Ollama API basics

2. **Python Environment Setup**
   ```bash
   # Create virtual environment
   python -m venv agentic-ai-env
   source agentic-ai-env/bin/activate  # On Windows: agentic-ai-env\Scripts\activate
   
   # Install core libraries
   pip install langchain langchain-community langgraph
   pip install llama-index llama-index-llms-ollama
   pip install chromadb faiss-cpu  # Vector databases
   pip install python-dotenv jupyter
   ```

3. **Understanding Local vs Cloud Models**
   - Trade-offs: privacy, cost, latency, capability
   - When to use local models
   - Model selection guide (size, performance, use case)

4. **Testing Your Setup**
   - Running models via Ollama CLI
   - Programmatic access via Python
   - Benchmarking performance

**Hands-on**:
- Install Ollama and pull 3 different models
- Create a simple Python script that queries Ollama
- Compare responses from different models
- Measure response time and quality

**Lab Exercise**:
Create a simple chatbot using Ollama and LangChain that can:
- Accept user input
- Generate responses using local LLM
- Maintain conversation history

---

## **Unit 3: LangChain Fundamentals**

### Week 3: Building Blocks of LangChain
**Learning Objectives**:
- Master LangChain core concepts
- Build chains and prompt templates
- Implement memory systems

**Topics**:
1. **LangChain Architecture**
   - Components: Models, Prompts, Chains, Agents
   - LangChain Expression Language (LCEL)
   - Runnables and compositions

2. **Working with LLMs in LangChain**
   ```python
   from langchain_community.llms import Ollama
   from langchain.prompts import PromptTemplate
   from langchain.chains import LLMChain
   
   llm = Ollama(model="llama3")
   prompt = PromptTemplate(
       input_variables=["topic"],
       template="Explain {topic} in simple terms:"
   )
   chain = prompt | llm
   ```

3. **Prompt Engineering**
   - Prompt templates and variables
   - Few-shot prompting
   - Chain-of-thought prompting
   - System prompts and role definitions
   
4. **Chains and Composition**
   - Simple chains
   - Sequential chains
   - Router chains
   - LCEL pipelines

5. **Memory Systems**
   - ConversationBufferMemory
   - ConversationSummaryMemory
   - ConversationBufferWindowMemory
   - Entity memory
   - Vector store-backed memory

**Hands-on**:
- Build various chain types
- Implement different memory strategies
- Create a multi-turn conversational agent
- Experiment with prompt templates

**Lab Exercise**:
Create a "Personal Assistant" that:
- Remembers conversation context
- Can answer questions about multiple topics
- Uses prompt templates for consistency
- Implements conversation summary for long chats

---

## **Unit 4: Introduction to LangGraph**

### Week 4: State Management and Graph-Based Workflows
**Learning Objectives**:
- Understand graph-based agent architectures
- Build stateful agents with LangGraph
- Implement conditional flows and cycles

**Topics**:
1. **Why LangGraph?**
   - Limitations of simple chains
   - Need for cyclic workflows
   - State management in complex agents
   - Human-in-the-loop scenarios

2. **Core LangGraph Concepts**
   - Nodes (functions that process state)
   - Edges (connections between nodes)
   - State (shared data structure)
   - Conditional edges
   - Graph compilation

3. **Building Your First Graph**
   ```python
   from langgraph.graph import StateGraph, END
   from typing import TypedDict
   
   class AgentState(TypedDict):
       messages: list
       next_action: str
   
   workflow = StateGraph(AgentState)
   workflow.add_node("process", process_function)
   workflow.add_node("decide", decision_function)
   workflow.set_entry_point("process")
   workflow.add_edge("process", "decide")
   workflow.add_conditional_edges("decide", should_continue)
   
   app = workflow.compile()
   ```

4. **State Management**
   - Defining state schemas
   - State updates and reducers
   - Immutable vs mutable state
   - State persistence

5. **Control Flow**
   - Linear flows
   - Conditional branches
   - Loops and cycles
   - Error handling and recovery

**Hands-on**:
- Build simple linear graphs
- Implement conditional routing
- Create cyclic workflows
- Add error handling

**Lab Exercise**:
Create a "Research Assistant" graph that:
- Accepts a research question
- Breaks it into sub-questions
- Processes each sub-question
- Aggregates results
- Uses conditional logic to determine when research is complete

---

## **Unit 5: Advanced LangGraph Patterns**

### Week 5: Multi-Agent Systems and Complex Workflows
**Learning Objectives**:
- Implement tool calling in graphs
- Build multi-agent systems
- Handle human-in-the-loop workflows
- Implement persistence and checkpointing

**Topics**:
1. **Tool Integration in LangGraph**
   - Defining tools with @tool decorator
   - Tool binding to LLMs
   - Tool calling and execution nodes
   - Error handling for tool failures
   
   ```python
   from langchain.tools import tool
   from langgraph.prebuilt import ToolExecutor
   
   @tool
   def search_web(query: str) -> str:
       """Search the web for information"""
       return search_api.search(query)
   
   tools = [search_web]
   tool_executor = ToolExecutor(tools)
   ```

2. **Agent Patterns**
   - ReAct (Reasoning + Acting) pattern
   - Plan-and-Execute pattern
   - Reflection and self-criticism
   - Tree of Thoughts
   - Multi-agent collaboration

3. **Multi-Agent Systems**
   - Agent roles and specialization
   - Inter-agent communication
   - Supervisor patterns
   - Collaborative vs competitive agents
   - Agent handoffs

4. **Human-in-the-Loop (HITL)**
   - Interrupt points
   - User approval workflows
   - Dynamic graph modification
   - Resume from interruption

5. **Persistence and Checkpointing**
   - Saving graph state
   - Resuming long-running workflows
   - State versioning
   - Debugging with checkpoints

**Hands-on**:
- Create tools and integrate with agents
- Build a ReAct agent
- Implement multi-agent collaboration
- Add HITL approval steps
- Implement state persistence

**Lab Exercise**:
Build a "Content Creation Team" with multiple agents:
- Researcher agent (gathers information)
- Writer agent (creates content)
- Editor agent (reviews and improves)
- Supervisor (coordinates workflow)
- Human approval before publishing

---

## **Unit 6: LlamaIndex - RAG and Knowledge Management**

### Week 6: Retrieval-Augmented Generation
**Learning Objectives**:
- Understand RAG architecture
- Build document indexing pipelines
- Implement semantic search
- Integrate LlamaIndex with LangGraph

**Topics**:
1. **Introduction to LlamaIndex**
   - What is RAG (Retrieval-Augmented Generation)?
   - Why LlamaIndex vs vanilla vector stores?
   - Core concepts: Documents, Nodes, Indexes, Retrievers, Query Engines

2. **Document Loading and Processing**
   ```python
   from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
   from llama_index.llms.ollama import Ollama
   from llama_index.embeddings.ollama import OllamaEmbedding
   
   # Load documents
   documents = SimpleDirectoryReader("./data").load_data()
   
   # Configure LLM and embeddings
   llm = Ollama(model="llama3")
   embed_model = OllamaEmbedding(model_name="nomic-embed-text")
   
   # Create index
   index = VectorStoreIndex.from_documents(
       documents,
       llm=llm,
       embed_model=embed_model
   )
   ```

3. **Embeddings and Vector Stores**
   - Text embeddings explained
   - Local embedding models (nomic-embed-text, mxbai-embed-large)
   - Vector databases (Chroma, FAISS, Qdrant)
   - Similarity search algorithms

4. **Indexing Strategies**
   - VectorStoreIndex
   - TreeIndex
   - ListIndex
   - KeywordTableIndex
   - Knowledge Graph Index
   - Composable indices

5. **Query Engines and Retrievers**
   - Basic query engine
   - Custom retrievers
   - Reranking strategies
   - Metadata filtering
   - Hybrid search (keyword + semantic)

6. **Advanced RAG Patterns**
   - Sentence window retrieval
   - Auto-merging retrieval
   - Recursive retrieval
   - Small-to-big retrieval
   - Query transformation
   - Sub-question query engine

**Hands-on**:
- Build a document indexing pipeline
- Experiment with different chunk sizes
- Compare embedding models
- Implement semantic search
- Try different retrieval strategies

**Lab Exercise**:
Create a "Document Q&A System" that:
- Ingests PDF and text documents
- Creates searchable index with local embeddings
- Answers questions using RAG
- Cites sources with page numbers
- Handles multi-document queries

---

## **Unit 7: Integrating LlamaIndex with LangGraph**

### Week 7: Building Intelligent RAG Agents
**Learning Objectives**:
- Combine LlamaIndex retrieval with LangGraph agents
- Build agentic RAG systems
- Implement query routing and planning

**Topics**:
1. **LlamaIndex as a Tool**
   - Wrapping query engines as LangChain tools
   - Using LlamaIndex in LangGraph nodes
   - Multi-index agents
   
   ```python
   from llama_index.core.tools import QueryEngineTool
   from langchain.agents import Tool
   
   query_engine = index.as_query_engine()
   
   query_tool = QueryEngineTool.from_defaults(
       query_engine=query_engine,
       name="document_search",
       description="Search through documentation"
   )
   ```

2. **Agentic RAG Patterns**
   - Query understanding and decomposition
   - Retrieval planning
   - Iterative retrieval and reasoning
   - Self-RAG (self-reflective retrieval)
   - Corrective RAG (CRAG)

3. **Multi-Index Agent Workflows**
   - Different indexes for different data types
   - Dynamic index selection
   - Cross-index synthesis
   - Index routing based on query

4. **Advanced Agent + RAG Patterns**
   - Research agents with sources
   - Summarization agents
   - Comparison and analysis agents
   - Report generation workflows

**Hands-on**:
- Create LlamaIndex tools for LangGraph
- Build an agent that decides when to retrieve
- Implement multi-step retrieval workflows
- Create agentic RAG with self-correction

**Lab Exercise**:
Build an "Intelligent Research Agent" that:
- Accepts complex research questions
- Breaks down into sub-questions
- Routes queries to appropriate indexes
- Synthesizes information from multiple sources
- Generates comprehensive reports with citations
- Self-corrects when information is insufficient

---

## **Unit 8: Memory and Context Management**

### Week 8: Long-Term Memory and Context
**Learning Objectives**:
- Implement persistent memory systems
- Manage context windows effectively
- Build knowledge graphs for agents

**Topics**:
1. **Memory Types in Agentic Systems**
   - Short-term (working memory)
   - Long-term (persistent knowledge)
   - Episodic memory (experience history)
   - Semantic memory (facts and concepts)

2. **Vector-Based Memory**
   - Storing conversation history in vector DBs
   - Semantic retrieval of past interactions
   - Memory consolidation strategies
   
3. **Graph-Based Memory**
   - Knowledge graphs with Neo4j/MemGraph
   - Entity extraction and relationship mapping
   - Graph RAG patterns
   - LlamaIndex knowledge graph index

4. **Context Window Management**
   - Token counting and management
   - Summarization strategies
   - Sliding window approaches
   - Hierarchical summarization

5. **Memory in LangGraph**
   - Persistent state across sessions
   - Memory checkpoints
   - State versioning and recovery

**Hands-on**:
- Implement vector-based memory
- Build a knowledge graph from conversations
- Create memory consolidation workflows
- Manage long conversation contexts

**Lab Exercise**:
Build a "Personal Knowledge Assistant" that:
- Remembers all past conversations
- Extracts and stores facts about users
- Builds a knowledge graph over time
- Recalls relevant past interactions
- Learns preferences and patterns

---

## **Unit 9: Production Patterns and Best Practices**

### Week 9: Deployment, Monitoring, and Optimization
**Learning Objectives**:
- Optimize agent performance
- Implement proper error handling
- Monitor and debug agent systems
- Deploy agents to production

**Topics**:
1. **Performance Optimization**
   - Model selection for production
   - Caching strategies
   - Parallel execution
   - Streaming responses
   - Batch processing

2. **Error Handling and Resilience**
   - Retry mechanisms
   - Fallback strategies
   - Circuit breakers
   - Graceful degradation
   - Error recovery in graphs

3. **Testing Agentic Systems**
   - Unit testing individual nodes
   - Integration testing workflows
   - Evaluation frameworks
   - LLM-as-judge patterns
   - Benchmarking agent performance

4. **Observability and Debugging**
   - Logging strategies
   - Tracing with LangSmith/LangFuse
   - Debugging graph execution
   - Performance profiling
   - Cost tracking (even with local models)

5. **Deployment Patterns**
   - Containerization with Docker
   - API endpoints with FastAPI
   - Background job processing
   - Scaling strategies
   - Security considerations

6. **Prompt Management**
   - Version control for prompts
   - Prompt testing and evaluation
   - Prompt optimization workflows
   - A/B testing prompts

**Hands-on**:
- Add comprehensive error handling
- Implement caching and optimization
- Create monitoring dashboards
- Containerize an agent application
- Build REST API for agent

**Lab Exercise**:
Production-ready "Customer Support Agent":
- Handles errors gracefully
- Implements retry logic
- Logs all interactions
- Exposes REST API
- Includes health checks and monitoring
- Dockerized for deployment

---

## **Unit 10: Advanced Agent Architectures**

### Week 10: Cutting-Edge Patterns
**Learning Objectives**:
- Implement advanced reasoning patterns
- Build autonomous agent systems
- Explore frontier research in agents

**Topics**:
1. **Advanced Reasoning Patterns**
   - Chain-of-Thought (CoT)
   - Tree of Thoughts (ToT)
   - Graph of Thoughts (GoT)
   - Reflexion (self-reflection)
   - Self-consistency
   - Successive refinement

2. **Planning and Strategy**
   - Task decomposition
   - Hierarchical planning
   - Plan-and-Execute frameworks
   - Dynamic re-planning
   - Multi-step reasoning

3. **Multi-Agent Collaboration**
   - Debate-based systems
   - Consensus mechanisms
   - Role-playing scenarios
   - Competitive vs cooperative agents
   - Society of Mind patterns

4. **Tool Creation and Evolution**
   - Agents that create tools
   - Meta-learning in agents
   - Code generation for tools
   - Tool documentation generation

5. **Autonomous Agents**
   - Goal-driven behavior
   - Self-improvement mechanisms
   - Continuous learning
   - Environment interaction
   - Agent simulation frameworks

6. **Emerging Patterns**
   - Vision-language agents
   - Multimodal reasoning
   - Agent-computer interface (ACI)
   - Browser automation agents
   - Code execution agents

**Hands-on**:
- Implement Tree of Thoughts
- Build a multi-agent debate system
- Create self-improving workflows
- Experiment with autonomous behaviors

**Lab Exercise**:
Build a "Software Development Team Simulator":
- Product Manager agent (defines requirements)
- Architect agent (designs system)
- Developer agent (writes code)
- QA agent (tests and validates)
- Agents debate and collaborate
- Self-correct and iterate on feedback

---

## **Unit 11: Domain-Specific Applications**

### Week 11: Real-World Use Cases
**Learning Objectives**:
- Apply concepts to specific domains
- Build production-ready applications
- Integrate with external systems

**Topics**:
1. **Code Agents**
   - Code understanding and analysis
   - Code generation and completion
   - Debugging assistants
   - Refactoring agents
   - Documentation generation

2. **Data Analysis Agents**
   - SQL query generation
   - Data exploration and visualization
   - Statistical analysis
   - Report generation
   - Pandas/data manipulation agents

3. **Research and Writing Agents**
   - Literature review automation
   - Academic paper analysis
   - Content generation pipelines
   - Citation management
   - Fact-checking workflows

4. **Business Process Automation**
   - Email automation
   - Document processing
   - Workflow orchestration
   - Decision support systems

5. **Integration Patterns**
   - API integration
   - Database connectivity
   - File system operations
   - External tool calling
   - Web scraping and automation

**Hands-on**:
- Build domain-specific agents for your field
- Integrate with real APIs and databases
- Create end-to-end automation workflows

**Lab Exercise**:
Choose one domain and build a complete agent system:
- Code Assistant OR Data Analyst OR Research Assistant
- Full RAG pipeline with relevant documents
- Tool integration
- Error handling and monitoring
- Production-ready API

---

## **Unit 12: Capstone Project**

### Week 12: Build Your Own Agentic System
**Learning Objectives**:
- Design and implement a complete agentic system
- Apply all learned concepts
- Present and document your work

**Project Requirements**:
Your capstone project should include:

1. **Core Components** (Mandatory):
   - LangGraph-based agent workflow
   - LlamaIndex RAG implementation
   - At least 3 custom tools
   - Memory/state management
   - Error handling and resilience

2. **Advanced Features** (Choose at least 3):
   - Multi-agent collaboration
   - Human-in-the-loop workflows
   - Advanced retrieval strategies
   - Self-reflection/improvement
   - Streaming responses
   - Multimodal capabilities
   - Knowledge graph integration
   - Production deployment

3. **Documentation**:
   - Architecture diagram
   - Setup instructions
   - API documentation
   - Design decisions and trade-offs
   - Testing strategy
   - Performance benchmarks

4. **Presentation**:
   - Live demo
   - Code walkthrough
   - Challenges and solutions
   - Future improvements

**Example Project Ideas**:
1. **Autonomous Research Assistant**
   - Multi-source information gathering
   - Fact verification
   - Report generation with citations
   - Self-directed research planning

2. **Code Review Agent**
   - Analyzes pull requests
   - Suggests improvements
   - Checks for security issues
   - Generates review comments

3. **Personal Learning Tutor**
   - Adapts to student knowledge level
   - Generates practice problems
   - Provides explanations
   - Tracks progress over time

4. **Business Intelligence Agent**
   - Connects to databases
   - Generates SQL queries
   - Creates visualizations
   - Writes analytical reports

5. **Smart Document Processor**
   - Ingests various file types
   - Extracts structured data
   - Answers questions
   - Generates summaries

---

## **Appendix: Resources and References**

### Essential Documentation
- **LangChain**: https://python.langchain.com/docs/
- **LangGraph**: https://langchain-ai.github.io/langgraph/
- **LlamaIndex**: https://docs.llamaindex.ai/
- **Ollama**: https://ollama.ai/

### Recommended Models (via Ollama)
- **General Purpose**: llama3, llama3.1, llama3.2
- **Fast**: phi3, gemma2
- **Coding**: codellama, deepseek-coder
- **Embeddings**: nomic-embed-text, mxbai-embed-large, all-minilm
- **Specialized**: mistral, qwen2.5, solar

### Papers and Research
1. "ReAct: Synergizing Reasoning and Acting in Language Models"
2. "Reflexion: Language Agents with Verbal Reinforcement Learning"
3. "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
4. "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
5. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
6. "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection"
7. "CRAG: Corrective Retrieval Augmented Generation"
8. "GraphRAG: Unlocking LLM discovery on narrative private data"

### Community Resources
- **LangChain Discord**: Active community for questions
- **GitHub Repositories**: 
  - awesome-langgraph
  - awesome-llamaindex
  - agent-examples
- **YouTube Channels**: 
  - LangChain official
  - AI Engineer tutorials
- **Blogs**:
  - LangChain blog
  - LlamaIndex blog
  - Towards Data Science

### Tools and Utilities
- **Vector Databases**: 
  - ChromaDB (easiest for local)
  - FAISS (fast, no server needed)
  - Qdrant (production-ready)
  - Weaviate, Pinecone (cloud options)

- **Observability**:
  - LangSmith (official LangChain)
  - LangFuse (open source)
  - Phoenix (Arize AI)

- **Development Tools**:
  - Jupyter Notebooks
  - VS Code with Python extensions
  - Postman (API testing)
  - Docker (containerization)

### Practice Datasets
- Sample documents for RAG:
  - Wikipedia dumps
  - arXiv papers
  - Company documentation
  - Books (Project Gutenberg)
  - Research papers (Semantic Scholar)

---

## **Teaching Tips and Best Practices**

### For Instructors

1. **Start Simple**
   - Begin each unit with minimal working examples
   - Add complexity incrementally
   - Ensure everyone gets the basics before advancing

2. **Hands-On First**
   - Code along together for key concepts
   - "Learn by doing" is most effective
   - Provide working examples to build upon

3. **Common Pitfalls**
   - Model selection confusion (guide on when to use which)
   - Context window limitations (teach early)
   - Prompt engineering importance (emphasize throughout)
   - State management in graphs (use clear examples)
   - Over-engineering (start simple, add features)

4. **Interactive Sessions**
   - Live coding demonstrations
   - Debugging sessions (show how to troubleshoot)
   - Group discussions on design decisions
   - Code reviews of student projects

5. **Pacing**
   - Each unit should be 1-1.5 weeks
   - Allow flexibility for deeper dives
   - Provide optional advanced materials
   - Regular check-ins on understanding

6. **Assessment Ideas**
   - Weekly mini-projects
   - Code reviews
   - Architecture design exercises
   - Debugging challenges
   - Peer presentations

### Study Strategy for Students

1. **Active Learning**
   - Don't just read—code along
   - Experiment beyond examples
   - Break things and fix them

2. **Build a Portfolio**
   - Document each project
   - Create GitHub repository
   - Share learnings via blog posts

3. **Community Engagement**
   - Join Discord communities
   - Ask questions
   - Share your solutions
   - Help others

4. **Deep Dive Topics**
   - Pick areas of interest for deeper exploration
   - Read research papers
   - Try variations and experiments

---

## **Weekly Schedule Template**

### Recommended Structure for Each Week:

**Day 1-2: Theory and Concepts** (3-4 hours)
- Video content or lectures
- Reading documentation
- Understanding fundamentals
- Q&A session

**Day 3-4: Hands-On Practice** (4-5 hours)
- Live coding sessions
- Follow-along tutorials
- Small exercises
- Debugging practice

**Day 5-6: Lab Exercises** (5-6 hours)
- Independent project work
- Applying concepts
- Experimentation
- Troubleshooting

**Day 7: Review and Discussion** (2-3 hours)
- Code review
- Share solutions
- Discuss challenges
- Preview next week

**Total Time**: ~15-20 hours per week

---

## **Quick Reference: Key Commands**

### Ollama Commands
```bash
# List available models
ollama list

# Pull a model
ollama pull llama3

# Run a model
ollama run llama3

# Check running models
ollama ps

# Remove a model
ollama rm llama3

# Show model info
ollama show llama3

# Pull embedding model
ollama pull nomic-embed-text
```

### Common Code Patterns

**Initialize Ollama with LangChain**:
```python
from langchain_community.llms import Ollama

llm = Ollama(model="llama3", temperature=0.7)
response = llm.invoke("Hello!")
```

**Initialize Ollama with LlamaIndex**:
```python
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

llm = Ollama(model="llama3", request_timeout=120.0)
embed_model = OllamaEmbedding(model_name="nomic-embed-text")
```

**Basic LangGraph Structure**:
```python
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator

class State(TypedDict):
    messages: Annotated[list, operator.add]

def node_function(state: State) -> State:
    # Process state
    return {"messages": [new_message]}

graph = StateGraph(State)
graph.add_node("node1", node_function)
graph.set_entry_point("node1")
graph.add_edge("node1", END)
app = graph.compile()

result = app.invoke({"messages": []})
```

**Basic RAG with LlamaIndex**:
```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("./data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("Your question here")
```

---

## **Conclusion**

This curriculum provides a comprehensive journey from understanding basic agentic concepts to building production-ready AI agents. The focus on local models with Ollama ensures privacy, cost-effectiveness, and hands-on learning.

**Key Takeaways**:
- ✅ Progressive learning from basics to advanced
- ✅ Hands-on practice with every concept
- ✅ Complete coverage of LangGraph, LangChain, and LlamaIndex
- ✅ Real-world applications and patterns
- ✅ Production-ready practices
- ✅ Capstone project for portfolio

**Success Metrics**:
By the end of this course, students should be able to:
- Design and implement agentic AI systems independently
- Choose appropriate tools and patterns for specific problems
- Build RAG applications with custom knowledge bases
- Deploy production-ready agent systems
- Understand and implement advanced agent architectures
- Collaborate on and contribute to agentic AI projects

Good luck with your teaching journey! 🚀

---

**Version**: 1.0  
**Last Updated**: January 2026  
**Maintainer**: Add your details here  
**License**: Add license if sharing publicly
