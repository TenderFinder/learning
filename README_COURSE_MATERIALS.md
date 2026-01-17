# Agentic AI Course - Complete Resource Index

## 📚 Course Structure

This repository contains a **complete dual-track course** on **Agentic AI with LangGraph, LangChain, and LlamaIndex using local models via Ollama**.

**Two Learning Paths**:
- **Technical Track** (`python/`) - For developers using Python, LangChain, LangGraph, LlamaIndex
- **Non-Technical Track** (`n8n/`) - For non-coders using n8n visual workflows

**Status**: Units 1-6 are **100% complete** with full instructor guides, exercises, and sample materials for both tracks.

### 📂 Directory Structure

```
langgraph/
├── AGENTIC_AI_CURRICULUM.md    # Main curriculum document
├── README_COURSE_MATERIALS.md # This file
│
├── python/                      # Technical Track
│   ├── sample_codes/            # Working code examples
│   │   ├── unit_01_introduction.py
│   │   ├── unit_02_environment_setup.py
│   │   ├── unit_03_langchain_fundamentals.py
│   │   ├── unit_04_langgraph_intro.py
│   │   ├── unit_05_advanced_langgraph.py
│   │   ├── unit_06_llamaindex_rag.py
│   │   └── ... (more units)
│   │
│   ├── exercises/               # Student exercises
│   │   ├── unit_01_exercises.md
│   │   ├── unit_02_exercises.md
│   │   ├── unit_03_exercises.md
│   │   ├── unit_04_exercises.md
│   │   ├── unit_05_exercises.md
│   │   ├── unit_06_exercises.md
│   │   └── ... (more units)
│   │
│   └── instructor_guide/        # Solutions and teaching tips
│       ├── unit_01_solutions.md
│       ├── unit_02_solutions.md
│       ├── unit_03_solutions.md
│       ├── unit_04_solutions.md
│       ├── unit_05_solutions.md
│       ├── unit_06_solutions.md
│       └── ... (more units)
│
└── n8n/                         # Non-Technical Track
    ├── README.md
    ├── curriculum/
    │   └── AGENTIC_AI_CURRICULUM_N8N.md
    ├── exercises/
    │   ├── unit_01_exercises.md
    │   ├── unit_02_exercises.md
    │   └── ... (more units)
    ├── workflows/
    │   └── README_WORKFLOWS.md
    └── instructor_guide/
        ├── unit_01_solutions.md
        └── ... (more units)
```

---

## 🎯 Course Overview

**Target Audience**: 
- **Technical Track**: Software developers, data scientists, ML engineers
- **Non-Technical Track**: Product owners, business analysts, scrum masters

**Duration**: 8-12 weeks  
**Format**: Self-paced or instructor-led  

**Prerequisites**: 
- **Technical**: Basic Python knowledge
- **Non-Technical**: None! Just curiosity and willingness to learn

### What You'll Learn

**Both Tracks**:
1. **Foundations** - Agent concepts, tools, memory
2. **Environment Setup** - Ollama, local models, dependencies
3. **Workflows** - Multi-step processes and chains
4. **State Machines** - Stateful workflows with LangGraph/n8n
5. **Advanced Patterns** - Multi-agent systems, tool integration
6. **RAG** - Knowledge bases and document Q&A

**Technical Track Also**:
- LangChain framework mastery
- LangGraph for complex workflows
- LlamaIndex for RAG systems
- Production deployment patterns

**Non-Technical Track Also**:
- Visual workflow design
- n8n automation platform
- Rapid prototyping
- Business process automation

---

## 📖 How to Use This Course

### For Students

1. **Start with the Curriculum**
   ```bash
   # Read the main curriculum first
   open AGENTIC_AI_CURRICULUM.md
   ```

2. **Follow This Sequence**:
   - Week 1: Unit 1 - Introduction
     - Read curriculum section
     - Run sample code: `python python/sample_codes/unit_01_introduction.py`
     - Complete exercises: `python/exercises/unit_01_exercises.md`
   
   - Week 2: Unit 2 - Environment Setup
     - Run: `python python/sample_codes/unit_02_environment_setup.py`
     - Complete: `python/exercises/unit_02_exercises.md`
   
   - Continue through all 12 units...

3. **Practice First**
   - Run all sample codes to understand concepts
   - Modify examples to experiment
   - Then attempt exercises

4. **Get Help**
   - Check instructor guide for hints (but try first!)
   - Join community forums
   - Review sample solutions

### For Instructors

1. **Preparation**
   - Review `AGENTIC_AI_CURRICULUM.md` thoroughly
   - Test all sample codes in your environment
   - Customize exercises for your class level

2. **Teaching Approach**:
   - **Day 1-2**: Lecture + Theory (curriculum content)
   - **Day 3-4**: Live coding (sample codes)
   - **Day 5-6**: Lab time (student exercises)
   - **Day 7**: Review + Q&A

3. **Use Instructor Guides**:
   - Complete solutions available
   - Common pitfalls documented
   - Teaching tips included
   - Assessment rubrics provided

4. **Customize**:
   - Adjust difficulty based on class level
   - Add domain-specific examples
   - Extend exercises as needed

---

## 🚀 Quick Start Guide

### Prerequisites Installation

```bash
# 1. Install Python 3.8+
python --version  # Should be 3.8 or higher

# 2. Install Ollama
# Mac:
brew install ollama

# Linux:
curl https://ollama.ai/install.sh | sh

# Windows:
# Download from https://ollama.ai/download

# 3. Start Ollama
ollama serve  # Run in separate terminal

# 4. Pull required models
ollama pull llama3
ollama pull mistral
ollama pull nomic-embed-text
ollama pull phi3  # Optional

# 5. Create virtual environment
python -m venv agentic-ai-env
source agentic-ai-env/bin/activate  # Windows: agentic-ai-env\Scripts\activate

# 6. Install Python packages
pip install langchain langchain-community langgraph
pip install llama-index llama-index-llms-ollama llama-index-embeddings-ollama
pip install chromadb faiss-cpu
pip install python-dotenv jupyter requests
```

### Verify Installation

```bash
# Run the setup verification
python python/sample_codes/unit_02_environment_setup.py
```

Expected output: All checks ✅ passing

---

## 📝 Sample Codes Overview

### Unit 1: Introduction to Agentic AI
**File**: `python/sample_codes/unit_01_introduction.py`

**What's Covered**:
- ✅ Basic Ollama interaction
- ✅ Creating custom tools
- ✅ Implementing memory
- ✅ Agent loop simulation
- ✅ Real-world use cases
- ✅ Model comparison
- ✅ Planning and reasoning
- ✅ Feedback loops

**Run it**:
```bash
python python/sample_codes/unit_01_introduction.py
```

---

### Unit 2: Environment Setup
**File**: `python/sample_codes/unit_02_environment_setup.py`

**What's Covered**:
- ✅ Python environment verification
- ✅ Package installation checks
- ✅ Ollama connection testing
- ✅ LangChain integration
- ✅ LlamaIndex integration
- ✅ Embedding model testing
- ✅ Performance benchmarking
- ✅ Vector database setup

**Run it**:
```bash
python python/sample_codes/unit_02_environment_setup.py
```

---

### Unit 3: LangChain Fundamentals
**File**: `python/sample_codes/unit_03_langchain_fundamentals.py`

**What's Covered**:
- ✅ Prompt templates (simple, multi-variable, few-shot)
- ✅ LCEL (LangChain Expression Language)
- ✅ Chain composition
- ✅ Memory systems (Buffer, Window, Summary)
- ✅ Custom memory configurations

**Run it**:
```bash
python python/sample_codes/unit_03_langchain_fundamentals.py
```

---

### Unit 4: LangGraph Introduction
**File**: `python/sample_codes/unit_04_langgraph_intro.py`

**What's Covered**:
- ✅ State definitions
- ✅ Linear graphs
- ✅ Conditional edges
- ✅ Loops and cycles
- ✅ LLM integration in graphs
- ✅ Multi-step reasoning

**Run it**:
```bash
python python/sample_codes/unit_04_langgraph_intro.py
```

---

### Unit 6: LlamaIndex RAG
**File**: `python/sample_codes/unit_06_llamaindex_rag.py`

**What's Covered**:
- ✅ Document loading and indexing
- ✅ Vector store creation
- ✅ Query engines
- ✅ Chat engines (conversational RAG)
- ✅ Source node retrieval
- ✅ Different index types
- ✅ Streaming responses

**Run it**:
```bash
python python/sample_codes/unit_06_llamaindex_rag.py
```

---

## 📋 Exercises Overview

### Unit 1 Exercises
**File**: `python/exercises/unit_01_exercises.md`

| Exercise | Difficulty | Time | Topics |
|----------|-----------|------|--------|
| 1. First Ollama Interaction | Beginner | 30min | Setup, basics |
| 2. Building Tools | Intermediate | 1h | Tools, decorators |
| 3. Conversation Memory | Intermediate | 1.5h | Memory systems |
| 4. Agent Loop Simulator | Advanced | 2h | Agent patterns |
| 5. Multi-Model Comparison | Intermediate | 1h | Model selection |
| 6. Use Case Implementation | Advanced | 3h | Real applications |
| 7. Feedback & Self-Improvement | Advanced | 2h | Self-correction |
| 8. Tool Composition | Advanced | 2h | Complex workflows |
| **Challenge Project** | Advanced | 4-6h | Complete system |

### Unit 3 Exercises
**File**: `python/exercises/unit_03_exercises.md`

| Exercise | Difficulty | Time | Topics |
|----------|-----------|------|--------|
| 1. Advanced Prompt Templates | Intermediate | 1.5h | Prompting |
| 2. Chain Composition | Advanced | 2h | Chains |
| 3. Memory Comparison | Intermediate | 2h | Memory types |
| 4. Code Review Assistant | Advanced | 3h | Practical app |
| 5. LCEL Pipeline | Advanced | 2h | LCEL |
| 6. Streaming Responses | Intermediate | 1h | Streaming |
| **Challenge Project** | Advanced | 5-7h | Tutoring system |

### Unit 4 Exercises
**File**: `python/exercises/unit_04_exercises.md`

| Exercise | Difficulty | Time | Topics |
|----------|-----------|------|--------|
| 1. Simple State Machine | Beginner | 1h | States, nodes |
| 2. Conditional Routing | Intermediate | 2h | Conditionals |
| 3. Loop-Based Iteration | Intermediate | 2h | Loops |
| 4. Multi-Step Reasoning | Advanced | 3h | Complex graphs |
| 5. Parallel Execution | Advanced | 2h | Parallelism |
| 6. Human-in-the-Loop | Advanced | 2h | HITL |
| 7. Error Handling | Advanced | 2h | Robustness |
| **Challenge Project** | Advanced | 6-8h | Task planner |

### Unit 6 Exercises
**File**: `python/exercises/unit_06_exercises.md`

| Exercise | Difficulty | Time | Topics |
|----------|-----------|------|--------|
| 1. First RAG System | Beginner | 1.5h | Basic RAG |
| 2. Retrieval Strategies | Intermediate | 2h | Advanced retrieval |
| 3. Metadata Filtering | Intermediate | 2h | Metadata |
| 4. Conversational RAG | Advanced | 3h | Chat engines |
| 5. Multi-Document Analysis | Advanced | 2h | Synthesis |
| 6. Structured Extraction | Advanced | 3h | Data extraction |
| 7. Citation Tracking | Intermediate | 2h | Sources |
| 8. Custom Embeddings | Advanced | 2h | Embeddings |
| **Challenge Project** | Advanced | 8-10h | Knowledge base |

---

## 👨‍🏫 Instructor Resources

### Technical Track Instructor Guides
**Location**: `python/instructor_guide/`

**Complete for Units 1-6**:
- `unit_01_solutions.md` - Complete solutions, teaching tips, rubrics
- `unit_02_solutions.md` - Environment setup guide and troubleshooting
- `unit_03_solutions.md` - LangChain fundamentals solutions
- `unit_04_solutions.md` - LangGraph introduction solutions
- `unit_05_solutions.md` - Advanced LangGraph patterns
- `unit_06_solutions.md` - RAG and LlamaIndex solutions
- `units_02-06_general_strategies.md` - Teaching strategies across units

**What's Included**:
- ✅ Complete solutions for all exercises
- ✅ Common student mistakes and how to address them
- ✅ Teaching tips and strategies
- ✅ Discussion questions
- ✅ Grading rubrics
- ✅ Extension ideas
- ✅ Assessment criteria
- ✅ Time management suggestions

### Non-Technical Track Instructor Guides
**Location**: `n8n/instructor_guide/`

**Complete for Units 1-6**:
- `unit_01_solutions.md` - Visual workflow solutions and teaching strategies
- `unit_02_solutions.md` - n8n environment setup guide
- `unit_03_solutions.md` - Building workflows solutions
- `unit_04_solutions.md` - Stateful workflow solutions
- `unit_05_solutions.md` - Advanced patterns for n8n
- `unit_06_solutions.md` - RAG systems in n8n
- `units_02-06_general_strategies.md` - Teaching non-technical learners

**What's Included**:
- ✅ Complete workflow solutions
- ✅ Teaching strategies for non-technical audiences
- ✅ Common pitfalls and solutions
- ✅ Engagement strategies
- ✅ Assessment approaches
- ✅ Time estimates
- ✅ Success metrics

---

## 🎓 Learning Path Recommendations

### Fast Track (4 weeks)
For experienced developers who want core concepts quickly:
- **Week 1**: Units 1-2 (Foundation + Setup)
- **Week 2**: Units 3-4 (LangChain + LangGraph basics)
- **Week 3**: Units 5-7 (Advanced LangGraph + RAG)
- **Week 4**: Units 9-10 (Production + Advanced patterns)
- Skip: Deep dives, focus on key exercises only

### Standard Track (8-10 weeks)
Recommended for most learners:
- **Weeks 1-2**: Units 1-2
- **Weeks 3-4**: Units 3-5
- **Weeks 5-6**: Units 6-8
- **Weeks 7-8**: Units 9-10
- **Weeks 9-10**: Units 11-12 + Capstone
- Complete all exercises and challenge projects

### Comprehensive Track (12+ weeks)
For those who want to master everything:
- **1 week per unit** (12 weeks)
- Complete all exercises
- Do all challenge projects
- Add personal projects
- Contribute to open source

---

## 💡 Tips for Success

### For Self-Learners

1. **Don't Skip Setup**
   - Unit 2 is crucial - get everything working first
   - Test thoroughly before moving on

2. **Code Along**
   - Don't just read - type and run every example
   - Modify examples to understand them better

3. **Do the Exercises**
   - Theory is 20%, practice is 80%
   - Start with beginner, progress to advanced

4. **Build Projects**
   - Apply learnings to real problems
   - Start small, iterate
   - Share your work

5. **Join the Community**
   - Ask questions (LangChain Discord, forums)
   - Help others
   - Share your projects

### For Study Groups

1. **Weekly Schedule**
   - Meet 2x per week
   - Session 1: Theory + live coding
   - Session 2: Lab time + Q&A

2. **Collaborative Learning**
   - Pair programming on exercises
   - Code reviews
   - Presentation of solutions

3. **Project Showcase**
   - End of unit demos
   - Peer feedback
   - Shared learning

---

## 🛠️ Troubleshooting

### Common Issues and Fixes

**Issue**: Ollama connection refused
```bash
# Solution: Start Ollama server
ollama serve
```

**Issue**: Model not found
```bash
# Solution: Pull the model
ollama pull llama3
```

**Issue**: Import error for langchain_community
```bash
# Solution: Install package
pip install langchain-community
```

**Issue**: Slow responses
```
# Solutions:
# 1. Use smaller models (phi3 instead of llama3)
# 2. Reduce context length
# 3. Use quantized models
```

**Issue**: Out of memory
```
# Solutions:
# 1. Close other applications
# 2. Use smaller models
# 3. Reduce batch size
```

### Getting Help

1. **Check instructor guide** - Solutions and tips
2. **Review sample code** - Working examples
3. **Community forums** - Ask questions
4. **GitHub issues** - Report bugs
5. **Office hours** - If in class setting

---

## 📚 Additional Resources

### Official Documentation
- [LangChain Docs](https://python.langchain.com/docs/)
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
- [LlamaIndex Docs](https://docs.llamaindex.ai/)
- [Ollama Docs](https://ollama.ai/docs)

### Recommended Reading
- **Papers**:
  - ReAct: Reasoning and Acting
  - Reflexion: Self-Reflection for Agents
  - Tree of Thoughts
  - RAG Survey Papers

- **Blogs**:
  - LangChain blog
  - LlamaIndex blog
  - AI Engineering Newsletter

### Video Resources
- LangChain YouTube channel
- Conference talks on agents
- Tutorial series

### Books
- "Building LLM Powered Applications"
- "Hands-On Large Language Models"
- "AI Agents in Action"

---

## 🏆 Capstone Project Ideas

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

## 📄 License

This curriculum is provided for educational purposes. Feel free to:
- Use for personal learning
- Adapt for corporate training
- Share with attribution
- Contribute improvements

---

## 🤝 Contributing

Improvements welcome!
- Fix typos or errors
- Add more examples
- Suggest better approaches
- Share your solutions

---

## 📧 Contact & Support

For questions or feedback:
- Open an issue
- Join community Discord
- Email: [your-email]

---

**Version**: 1.0  
**Last Updated**: January 2026  
**Maintained by**: [@rahul-trip](https://github.com/rahul-trip)

---

## 🚀 Ready to Start?

1. ✅ Read the main curriculum: `AGENTIC_AI_CURRICULUM.md`
2. ✅ Set up your environment: `Unit 2`
3. ✅ Run your first example: `python python/sample_codes/unit_01_introduction.py`
4. ✅ Start learning!

**Happy Learning! 🎉**
