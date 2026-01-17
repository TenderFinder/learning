# 🎓 Agentic AI Learning Repository

**A comprehensive, dual-track curriculum for learning Agentic AI - designed for both technical and non-technical team members**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)](https://python.langchain.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Latest-green.svg)](https://langchain-ai.github.io/langgraph/)

---

## 🎯 What Is This Repository?

This repository is a **complete learning resource** for building **Agentic AI systems** - autonomous AI agents that can think, act, use tools, and collaborate. Whether you're a developer who wants to code AI agents or a product manager who wants to prototype visually, this curriculum has you covered.

### 🌟 Key Features:

- ✅ **Dual-Track Learning** - Technical (Python) and Non-Technical (n8n) paths
- ✅ **100% Local** - Uses Ollama (no API costs, privacy-first)
- ✅ **Production-Ready** - Real-world patterns and best practices
- ✅ **Comprehensive** - 12 units covering fundamentals to advanced topics
- ✅ **Hands-On** - 90+ exercises and 12+ challenge projects
- ✅ **Complete Materials for Units 1-6** - Sample code, exercises, and full instructor guides
- ✅ **Separated Solutions** - Individual instructor guides for each unit
- ✅ **Teaching Strategies** - Comprehensive guides for both technical and non-technical tracks

---

## 🎨 Two Learning Tracks, Same Concepts

### 👨‍💻 **Technical Track** (Python)
**For**: Developers, Data Scientists, ML Engineers

**Tools**: Python, LangChain, LangGraph, LlamaIndex, Ollama

**Approach**: Code-first, programmatic control, production deployment

📂 **Location**: [`python/`](./python/)

### 🎨 **Non-Technical Track** (n8n)
**For**: Product Owners, Business Analysts, Scrum Masters

**Tools**: n8n (visual workflow builder), Ollama

**Approach**: Visual-first, drag-and-drop, rapid prototyping

📂 **Location**: [`n8n/`](./n8n/)

### 🤝 **Why Both?**
Both tracks teach the **same AI concepts** - agents, tools, memory, RAG, multi-agent systems - just through different mediums. This enables:
- Better team collaboration
- Faster prototyping (non-tech) → Optimized implementation (tech)
- Shared vocabulary across the organization
- Inclusive AI literacy

---

## 📚 Curriculum Overview

This repository follows a **12-unit curriculum** covering the complete journey from AI fundamentals to production deployment:

### **Foundations (Units 1-2)**
- 🤖 **Unit 1**: Introduction to Agentic AI
  - What are AI agents and how do they work?
  - Core components: LLMs, tools, memory, planning
  - Real-world applications and use cases

- 🛠️ **Unit 2**: Environment Setup
  - Installing Ollama for local AI models
  - Setting up development environment
  - Model selection and performance optimization

### **Core Skills (Units 3-4)**
- 🔗 **Unit 3**: LangChain Fundamentals (Python) / Visual Chains (n8n)
  - Prompt engineering and templates
  - Building multi-step workflows
  - Memory systems and conversation management

- 📊 **Unit 4**: LangGraph State Machines
  - Graph-based agent architectures
  - Stateful workflows and conditional logic
  - Loops, cycles, and complex decision trees

### **Advanced Patterns (Units 5-6)**
- 🚀 **Unit 5**: Advanced Agent Patterns
  - Multi-agent systems and collaboration
  - Tool integration and ReAct pattern
  - Human-in-the-loop workflows

- 📚 **Unit 6**: RAG (Retrieval-Augmented Generation)
  - Building knowledge bases with LlamaIndex
  - Semantic search and document Q&A
  - Advanced retrieval strategies

### **Production & Specialization (Units 7-12)**
- 🔌 **Unit 7**: Integration Patterns
- 🧠 **Unit 8**: Memory & Context Management
- 🏭 **Unit 9**: Production Deployment
- 🎯 **Unit 10**: Advanced Architectures
- 💼 **Unit 11**: Domain-Specific Applications
- 🏆 **Unit 12**: Capstone Project

**Full Curriculum**: See [`AGENTIC_AI_CURRICULUM.md`](./AGENTIC_AI_CURRICULUM.md) for detailed syllabus

---

## 🚀 Quick Start

### For Developers (Python Track):

```bash
# 1. Clone the repository
git clone <repository-url>
cd langgraph

# 2. Set up Python environment
cd python
python3 -m venv agentic-ai-env
source agentic-ai-env/bin/activate

# 3. Install dependencies
pip install langchain langchain-community langgraph llama-index

# 4. Install Ollama
brew install ollama  # Mac
# or download from https://ollama.ai

# 5. Start Ollama and pull models
ollama serve
ollama pull llama3

# 6. Run your first example
python sample_codes/unit_01_introduction.py
```

📖 **Full Guide**: [`python/README.md`](./python/README.md)

### For Non-Technical Users (n8n Track):

```bash
# 1. Install n8n Desktop App
# Download from: https://n8n.io/download

# 2. Install Ollama (ask your tech team for help)
# Download from: https://ollama.ai

# 3. Open n8n and start building!
# Import workflows from: n8n/workflows/
```

📖 **Full Guide**: [`n8n/README.md`](./n8n/README.md)

---

## 📁 Repository Structure

```
langgraph/
│
├── 📄 README.md                          ⭐ You are here
├── 📄 AGENTIC_AI_CURRICULUM.md           Complete 12-unit curriculum
├── 📄 INDEX.md                           Detailed project index
├── 📄 MATERIALS_STATUS.md                Content completion status
│
├── 📁 python/                            🔧 TECHNICAL TRACK
│   ├── README.md                         Python track guide
│   ├── sample_codes/                     43+ working code examples
│   ├── exercises/                        45+ exercises (Units 1-6)
│   └── instructor_guide/                 Complete teaching resources
│
└── 📁 n8n/                               🎨 NON-TECHNICAL TRACK
    ├── README.md                         n8n track guide
    ├── curriculum/                       n8n-specific curriculum
    ├── exercises/                        48+ visual workflow exercises
    ├── workflows/                        Importable workflow templates
    └── instructor_guide/                 Teaching strategies for non-tech
```

---

## 🎓 What You'll Learn

### By the End of This Course:

**Everyone (Both Tracks)**:
- ✅ Understand AI agent architectures and patterns
- ✅ Build autonomous systems that can think and act
- ✅ Implement tools, memory, and planning
- ✅ Create RAG systems for knowledge Q&A
- ✅ Design multi-agent collaborations
- ✅ Deploy production-ready solutions

**Technical Track Also**:
- ✅ Master LangChain, LangGraph, and LlamaIndex
- ✅ Write production Python code for AI agents
- ✅ Optimize performance and handle edge cases
- ✅ Debug complex agent behaviors

**Non-Technical Track Also**:
- ✅ Build visual workflows without coding
- ✅ Prototype AI solutions rapidly
- ✅ Create specifications for developers
- ✅ Understand technical constraints

---

## 📊 Course Statistics

| Metric | Count |
|--------|-------|
| **Total Units** | 12 comprehensive units |
| **Learning Hours** | 160-210 hours (technical) / 130-170 hours (non-tech) |
| **Duration** | 8-12 weeks |
| **Sample Code Files** | 6 files, 43+ examples |
| **Exercises** | 90+ hands-on exercises |
| **Challenge Projects** | 12+ real-world projects |
| **Documentation Pages** | 250+ pages |
| **Workflow Templates** | 48+ importable n8n workflows |
| **Instructor Guides** | Complete for Units 1-6 (both tracks) |
| **Teaching Resources** | Solutions + strategies for each unit |

---

## 🛠️ Technologies Used

### Technical Track:
- **Python 3.8+** - Programming language
- **LangChain** - LLM application framework
- **LangGraph** - Stateful agent workflows
- **LlamaIndex** - RAG and document indexing
- **Ollama** - Local LLM inference
- **ChromaDB / FAISS** - Vector databases

### Non-Technical Track:
- **n8n** - Visual workflow automation
- **Ollama** - Local AI models
- **Integrations** - Slack, Google Sheets, Airtable, etc.

### Both Tracks:
- **Ollama Models**: llama3, mistral, phi3, nomic-embed-text
- **100% Local** - No cloud APIs required (privacy-first)
- **No API Costs** - Run everything on your machine

---

## 👥 Who Is This For?

### ✅ Perfect For:
- Software developers learning AI agent development
- Product managers wanting to prototype AI solutions
- Teams wanting to upskill in Agentic AI together
- Organizations building AI-first products
- Educators teaching modern AI development
- Anyone curious about autonomous AI systems

### ❌ Not Required:
- Prior AI/ML experience
- Cloud platform knowledge
- Expensive API credits
- Advanced mathematics background

---

## 🎯 Use Cases

### What Can You Build?

**After completing this course, you'll be able to create**:

1. **Customer Support Automation**
   - Intelligent ticket routing
   - Automated response generation
   - Escalation handling

2. **Research Assistants**
   - Multi-source information gathering
   - Fact verification and citation
   - Report generation

3. **Code Assistants**
   - Code review and suggestions
   - Documentation generation
   - Debugging helpers

4. **Knowledge Q&A Systems**
   - Company documentation bots
   - Internal knowledge bases
   - Training assistants

5. **Business Process Automation**
   - Workflow orchestration
   - Document processing
   - Decision support systems

6. **Content Creation Pipelines**
   - Multi-agent writing teams
   - SEO optimization
   - Quality assurance

---

## 📖 How to Use This Repository

### For Self-Learners:

1. **Choose Your Track** (Python or n8n)
2. **Read the Track README** (`python/README.md` or `n8n/README.md`)
3. **Follow the Curriculum** (`AGENTIC_AI_CURRICULUM.md`)
4. **Complete Exercises** in order
5. **Build Projects** to apply your learning
6. **Join Community** for support

### For Instructors:

1. **Review Full Curriculum** (`AGENTIC_AI_CURRICULUM.md`)
2. **Check Instructor Guides** (both tracks have complete solutions)
3. **Test All Materials** (sample codes and workflows)
4. **Customize for Your Class** (adjust pace and difficulty)
5. **Use Teaching Strategies** (documented in instructor guides)

### For Teams:

1. **Run Both Tracks in Parallel** (developers + non-technical)
2. **Weekly Sync Sessions** (share learnings across tracks)
3. **Collaborative Projects** (prototype in n8n, implement in Python)
4. **Build Together** (create real solutions for your organization)

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

- 🐛 **Report Bugs** - Found an issue? Open a GitHub issue
- 💡 **Suggest Improvements** - Have ideas? Share them!
- 📝 **Add Examples** - Built something cool? Contribute it!
- 🌍 **Translate** - Help make this accessible globally
- ⭐ **Star the Repo** - Show your support!

---

## 📞 Support & Community

### Getting Help:

- 📖 **Documentation** - Check track-specific READMEs
- 👨‍🏫 **Instructor Guides** - Solutions and troubleshooting
- 💬 **Community Forums** - LangChain Discord, n8n Community
- 🐛 **GitHub Issues** - Report bugs or ask questions

### Stay Updated:

- ⭐ **Star this repository** to get updates
- 👀 **Watch** for new releases
- 🔔 **Follow** for announcements

---

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

Built with:
- **LangChain** - For the amazing agent framework
- **LangGraph** - For stateful workflow capabilities
- **LlamaIndex** - For RAG and document indexing
- **Ollama** - For making local LLMs accessible
- **n8n** - For visual workflow automation
- **The AI Community** - For continuous innovation

---

## 🎉 Ready to Start?

### Choose Your Path:

**👨‍💻 I'm a Developer** → Start with [`python/README.md`](./python/README.md)

**🎨 I'm Non-Technical** → Start with [`n8n/README.md`](./n8n/README.md)

**📚 I Want to Learn More** → Read [`AGENTIC_AI_CURRICULUM.md`](./AGENTIC_AI_CURRICULUM.md)

**🗺️ I Want the Full Picture** → Check [`INDEX.md`](./INDEX.md)

---

**Let's build the future of AI together! 🚀🤖**

---

**Version**: 1.0  
**Created**: January 2026  
**Maintained by**: [@rahul-trip](https://github.com/rahul-trip)  
**Status**: ✅ Ready - Start Learning Today!
