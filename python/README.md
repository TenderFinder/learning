# Technical Track - Agentic AI with Python

## 👨‍💻 Welcome Developers!

This is your dedicated learning path for **Agentic AI** using **LangChain, LangGraph, and LlamaIndex** with local models via **Ollama**. Build production-ready AI agents with code-first control.

---

## 👥 Who Is This For?

- ✅ Software Developers
- ✅ Data Scientists
- ✅ ML Engineers
- ✅ Backend Engineers
- ✅ Anyone comfortable with Python!

---

## 🎯 What You'll Learn

By the end of this course, you'll be able to:
- 🐍 Build AI agents with Python
- 🤖 Create autonomous systems with LangGraph
- 📚 Implement RAG with LlamaIndex
- 🔧 Use local models (Ollama - no API costs!)
- 🚀 Deploy production-ready applications
- 🧠 Design multi-agent architectures

---

## 📂 Folder Structure

```
python/
├── sample_codes/
│   ├── unit_01_introduction.py           ⭐ 8 examples
│   ├── unit_02_environment_setup.py      9 examples
│   ├── unit_03_langchain_fundamentals.py 10 examples
│   ├── unit_04_langgraph_intro.py        6 examples
│   ├── unit_05_advanced_langgraph.py     3 examples
│   └── unit_06_llamaindex_rag.py         7 examples
│
├── exercises/
│   ├── unit_01_exercises.md              8 exercises + challenge
│   ├── unit_02_exercises.md              8 exercises + challenge
│   ├── unit_03_exercises.md              6 exercises + challenge
│   ├── unit_04_exercises.md              7 exercises + challenge
│   ├── unit_05_exercises.md              8 exercises + challenge
│   └── unit_06_exercises.md              8 exercises + 2 challenges
│
├── instructor_guide/
│   ├── unit_01_solutions.md              Complete solutions
│   ├── unit_02_solutions.md              Environment setup guide
│   ├── unit_03_solutions.md              LangChain solutions
│   ├── unit_04_solutions.md              LangGraph solutions
│   ├── unit_05_solutions.md              Advanced patterns
│   ├── unit_06_solutions.md              RAG solutions
│   └── units_02-06_general_strategies.md Teaching strategies
│
└── README.md                              This file!
```

---

## 🚀 Quick Start (3 Steps)

### Step 1: Set Up Python Environment (5 minutes)

```bash
# Create virtual environment
python3 -m venv agentic-ai-env
source agentic-ai-env/bin/activate  # Windows: agentic-ai-env\Scripts\activate

# Install dependencies
pip install langchain langchain-community langgraph
pip install llama-index llama-index-llms-ollama llama-index-embeddings-ollama
pip install chromadb faiss-cpu python-dotenv
```

### Step 2: Install Ollama (5 minutes)

**Mac**:
```bash
brew install ollama
ollama serve  # Run in separate terminal
ollama pull llama3
ollama pull mistral
ollama pull nomic-embed-text
```

**Linux**:
```bash
curl https://ollama.ai/install.sh | sh
ollama serve
ollama pull llama3
```

**Windows**: Download from https://ollama.ai/download

### Step 3: Run Your First Example! (2 minutes)

```bash
cd python/sample_codes
python unit_01_introduction.py
```

🎉 **You just ran your first AI agent!**

---

## 📚 Learning Path

### Week-by-Week Plan

| Week | Unit | What You'll Build | Time |
|------|------|-------------------|------|
| 1 | Unit 1 | First agent, tools, memory | 10-12h |
| 2 | Unit 2 | Environment mastery, setup | 6-8h |
| 3 | Unit 3 | LangChain chains, prompts | 12-15h |
| 4 | Unit 4 | LangGraph state machines | 12-15h |
| 5 | Unit 5 | Advanced patterns, multi-agent | 15-18h |
| 6 | Unit 6 | RAG systems with LlamaIndex | 15-18h |
| 7 | Unit 7 | Integration patterns | 12-15h |
| 8 | Unit 8 | Advanced memory systems | 10-12h |
| 9 | Unit 9 | Production deployment | 12-15h |
| 10 | Unit 10 | Advanced architectures | 15-18h |
| 11 | Unit 11 | Domain applications | 12-15h |
| 12 | Unit 12 | Capstone project | 25-35h |

**Total**: ~160-210 hours (8-12 weeks)

---

## 🎓 How to Use These Materials

### For Self-Learning:

1. **Read the Main Curriculum**
   ```bash
   # From repository root
   open ../AGENTIC_AI_CURRICULUM.md
   ```

2. **Run Sample Code**
   ```bash
   cd sample_codes
   python unit_01_introduction.py  # Start here
   python unit_02_environment_setup.py
   # ... continue through units
   ```

3. **Complete Exercises**
   ```bash
   # Read exercises
   open exercises/unit_01_exercises.md
   
   # Create your solutions
   mkdir my_solutions
   # Code your answers
   ```

4. **Check Solutions (when stuck)**
   ```bash
   open instructor_guide/unit_01_solutions.md
   # But try first! Learning happens through struggle!
   ```

### For Instructor-Led Learning:

1. **Preparation**
   - Review full curriculum
   - Test all sample codes
   - Verify environment setup
   - Prepare lab machines

2. **Class Structure**:
   - **Day 1-2**: Theory + Live Coding (curriculum + sample codes)
   - **Day 3-4**: Guided Labs (exercises 1-4)
   - **Day 5-6**: Independent Practice (exercises 5-8)
   - **Day 7**: Code Review + Q&A + Presentations

3. **Use Instructor Guide**
   - Complete solutions included
   - Common pitfalls documented
   - Grading rubrics provided
   - Time estimates given

---

## 🛠️ Prerequisites

### Required:
- ✅ **Python 3.8+** installed
- ✅ **Basic Python knowledge** (functions, classes, imports)
- ✅ **Terminal/command line** familiarity
- ✅ **Git** (for version control)

### Helpful (but not required):
- 📚 Understanding of async/await
- 🧠 Basic ML/AI concepts
- 🐳 Docker knowledge
- ☁️ Cloud platform experience

### Will Learn:
- 🤖 Agent architectures
- 🔗 LangChain framework
- 📊 LangGraph for workflows
- 📚 RAG with LlamaIndex
- 🚀 Production deployment

---

## 💡 Key Technologies

### Core Frameworks:

**LangChain** - Building blocks for LLM applications
```python
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
```

**LangGraph** - Stateful, cyclical workflows
```python
from langgraph.graph import StateGraph, END
```

**LlamaIndex** - RAG and document indexing
```python
from llama_index.core import VectorStoreIndex
```

**Ollama** - Local LLM inference
```python
from langchain_community.llms import Ollama
llm = Ollama(model="llama3")
```

---

## 📖 Sample Code Overview

### Unit 1: Introduction (8 Examples)
**File**: `sample_codes/unit_01_introduction.py`
- Basic Ollama interaction
- Creating custom tools
- Implementing memory
- Agent loop simulation
- Multi-model comparison

```bash
python sample_codes/unit_01_introduction.py
```

### Unit 2: Environment Setup (9 Examples)
**File**: `sample_codes/unit_02_environment_setup.py`
- Environment verification
- Package testing
- Ollama connection
- Performance benchmarking

```bash
python sample_codes/unit_02_environment_setup.py
```

### Unit 3: LangChain Fundamentals (10 Examples)
**File**: `sample_codes/unit_03_langchain_fundamentals.py`
- Prompt templates
- Chain composition
- Memory systems
- LCEL patterns

```bash
python sample_codes/unit_03_langchain_fundamentals.py
```

### Unit 4: LangGraph Introduction (6 Examples)
**File**: `sample_codes/unit_04_langgraph_intro.py`
- State definitions
- Conditional routing
- Loops and cycles
- Multi-step reasoning

```bash
python sample_codes/unit_04_langgraph_intro.py
```

### Unit 5: Advanced LangGraph (3 Examples)
**File**: `sample_codes/unit_05_advanced_langgraph.py`
- Tool-enabled agents
- Multi-agent systems
- ReAct pattern

```bash
python sample_codes/unit_05_advanced_langgraph.py
```

### Unit 6: LlamaIndex RAG (7 Examples)
**File**: `sample_codes/unit_06_llamaindex_rag.py`
- Document indexing
- Query engines
- Chat engines
- Streaming responses

```bash
python sample_codes/unit_06_llamaindex_rag.py
```

---

## ✏️ Exercises Overview

### Unit 1: Introduction (8 exercises + 1 challenge)
- First Ollama interaction
- Building custom tools
- Conversation memory
- Agent loop simulator
- Multi-model comparison
- **Challenge**: Personal AI Assistant

### Unit 2: Environment Setup (8 exercises + 1 challenge)
- Complete environment setup
- Ollama model management
- Integration testing
- Performance optimization
- **Challenge**: Setup Automation Script

### Unit 3: LangChain (6 exercises + 1 challenge)
- Advanced prompt templates
- Chain composition
- Memory systems comparison
- Code review assistant
- **Challenge**: AI Learning Tutor

### Unit 4: LangGraph (7 exercises + 1 challenge)
- Simple state machine
- Conditional routing
- Loop-based iteration
- Multi-step reasoning
- **Challenge**: AI Task Planner

### Unit 5: Advanced LangGraph (8 exercises + 1 challenge)
- Tool-enabled agent
- Multi-agent collaboration
- ReAct pattern implementation
- **Challenge**: Research Assistant

### Unit 6: RAG (8 exercises + 2 challenges)
- First RAG system
- Retrieval strategies
- Conversational RAG
- Multi-document analysis
- **Challenges**: Knowledge Base + Agentic RAG

---

## 🤝 Working with Non-Technical Team

### You're Learning the Same Concepts!

| You (Python) | Non-Tech (n8n) | Same Concept |
|--------------|----------------|--------------|
| Functions | Nodes | Building blocks |
| Code | Workflows | Logic flow |
| Variables | Expressions | Data |
| Imports | Connections | Dependencies |

### How to Collaborate:

1. **They Prototype in n8n**
   - Visual proof-of-concept
   - Business logic defined
   - Clear requirements

2. **You Optimize in Code**
   - Implement scalable version
   - Add error handling
   - Deploy to production

3. **Everyone Wins**
   - Faster ideation
   - Better communication
   - Superior products

---

## 🎯 Learning Outcomes

### After Units 1-6, You'll Be Able To:

**Technical Skills**:
- ✅ Build AI agents with LangChain
- ✅ Create stateful workflows with LangGraph
- ✅ Implement RAG systems with LlamaIndex
- ✅ Use Ollama for local inference
- ✅ Handle tools, memory, and state
- ✅ Debug complex agent behaviors

**Conceptual Understanding**:
- ✅ Agent architectures and patterns
- ✅ Prompt engineering best practices
- ✅ Memory management strategies
- ✅ RAG system design
- ✅ Multi-agent coordination
- ✅ Production considerations

---

## 🛠️ Troubleshooting

### Common Issues:

**Ollama connection refused**:
```bash
# Start Ollama server
ollama serve
```

**Model not found**:
```bash
# Pull the model
ollama pull llama3
```

**Import errors**:
```bash
# Reinstall packages
pip install --upgrade langchain langchain-community langgraph
```

**Slow responses**:
```python
# Use smaller models
llm = Ollama(model="phi3")  # Faster than llama3
```

**Out of memory**:
```bash
# Use quantized models or reduce context
ollama pull llama3:8b-instruct-q4_0
```

---

## 📞 Getting Help

### Resources:

1. **Instructor Guide**
   - `instructor_guide/unit_XX_solutions.md`
   - Complete solutions and explanations

2. **Official Documentation**
   - [LangChain Docs](https://python.langchain.com/docs/)
   - [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
   - [LlamaIndex Docs](https://docs.llamaindex.ai/)
   - [Ollama Docs](https://ollama.ai/docs)

3. **Community**
   - LangChain Discord
   - GitHub Discussions
   - Stack Overflow

4. **Your Team**
   - Share learnings with non-technical track
   - Collaborate on projects

---

## 🏆 Capstone Projects

### Ideas for Unit 12:

1. **AI Research Assistant**
   - Multi-source information gathering
   - Citation management
   - Report generation

2. **Code Review System**
   - Automated PR reviews
   - Security analysis
   - Best practice suggestions

3. **Personal Knowledge Management**
   - Note organization
   - Semantic search
   - Knowledge graph

4. **Customer Support Automation**
   - Ticket classification
   - Response generation
   - Escalation handling

5. **Content Creation Pipeline**
   - Multi-agent collaboration
   - SEO optimization
   - Quality assurance

---

## 📊 Track Your Progress

### Unit Checklist:

- [ ] Unit 1: Built first agent ✅
- [ ] Unit 2: Environment fully configured ✅
- [ ] Unit 3: Mastered LangChain ✅
- [ ] Unit 4: Built stateful LangGraph ✅
- [ ] Unit 5: Multi-agent system working ✅
- [ ] Unit 6: RAG system deployed ✅
- [ ] Unit 7: Integrated with external tools ✅
- [ ] Unit 8: Advanced memory implemented ✅
- [ ] Unit 9: Production deployment complete ✅
- [ ] Unit 10: Advanced patterns mastered ✅
- [ ] Unit 11: Domain application built ✅
- [ ] Unit 12: Capstone completed! 🎉

---

## 🎉 Ready to Start?

### Your First 30 Minutes:

```bash
# Minute 0-10: Set up environment
python3 -m venv agentic-ai-env
source agentic-ai-env/bin/activate
pip install langchain langchain-community

# Minute 10-15: Install Ollama
brew install ollama  # or download
ollama serve &
ollama pull llama3

# Minute 15-20: Test installation
python sample_codes/unit_02_environment_setup.py

# Minute 20-30: Run first example
python sample_codes/unit_01_introduction.py

# You're an AI engineer now! 🚀
```

### Next Steps:

1. Read `../AGENTIC_AI_CURRICULUM.md` (Unit 1)
2. Run all examples in `sample_codes/unit_01_introduction.py`
3. Open `exercises/unit_01_exercises.md`
4. Start coding!

---

## 🌟 Remember:

> "The best way to learn is by building.  
> Every error is a lesson.  
> Every agent you create is progress.  
> Keep coding, keep learning!"

**Welcome to the world of Agentic AI development! Let's build something amazing! 🚀**

---

## 📄 File Quick Reference

- 📖 **Main Curriculum**: `../AGENTIC_AI_CURRICULUM.md`
- 🔧 **Sample Codes**: `sample_codes/unit_XX_*.py`
- ✏️ **Exercises**: `exercises/unit_XX_exercises.md`
- 👨‍🏫 **Solutions**: `instructor_guide/unit_XX_solutions.md`
- 📘 **This README**: You are here!

---

**Version**: 1.0  
**Created**: January 2026  
**For**: Technical Developers  
**Parallel to**: Non-Technical n8n Track  
**Stack**: Python + LangChain + LangGraph + LlamaIndex + Ollama

**Let's get started! 👨‍💻🤖**
