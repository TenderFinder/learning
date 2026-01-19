# Non-Technical Track - Agentic AI with n8n

## 🎨 Welcome Non-Technical Team Members!

This is your dedicated learning path for **Agentic AI** - no coding required! You'll learn the same powerful concepts as the technical track, but through **visual workflows** using n8n.

---

## 👥 Who Is This For?

- ✅ Product Owners / Product Managers
- ✅ Scrum Masters / Agile Coaches
- ✅ Business Analysts
- ✅ Project Managers
- ✅ Anyone interested in AI without coding!

---

## 🎯 What You'll Learn

By the end of this course, you'll be able to:
- 🎨 Build AI agents visually (no code!)
- 🤖 Create chatbots and automation
- 📊 Design complex workflows
- 💬 Understand technical AI concepts
- 🤝 Collaborate better with developers
- 🚀 Prototype AI solutions independently

---

## 📂 Folder Structure

```
non_technical/
├── curriculum/
│   └── AGENTIC_AI_CURRICULUM_N8N.md    ⭐ Your main guide
│
├── exercises/
│   ├── unit_01_exercises.md             8 hands-on exercises
│   ├── unit_02_exercises.md             (coming soon)
│   └── ...
│
├── workflows/
│   ├── unit_01_hello_world.json         Importable workflows
│   ├── unit_01_chatbot.json
│   └── ...
│
├── instructor_guide/
│   └── unit_01_solutions.md             For teachers
│
└── README.md                             This file!
```

---

## 🚀 Quick Start (3 Steps)

### Step 1: Install n8n (5-10 minutes)

**Option A: Cloud Version (Easiest - Recommended)**
```
1. Sign up at https://n8n.cloud
2. Free tier available - perfect for learning
3. No installation needed!
4. Works from any browser
```

**Option B: Self-Hosted with npx**
```bash
# Requires Node.js installed
npx n8n

# Access n8n at http://localhost:5678
# Press Ctrl+C to stop when done
```

**Option C: Docker (Most Flexible)**
```bash
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  n8nio/n8n
  
# Access n8n at http://localhost:5678
```

**Choose Option A if**: You want the easiest setup  
**Choose Option B if**: You have Node.js installed  
**Choose Option C if**: You use Docker regularly

### Step 2: Install Ollama (5 minutes)

**Ask your technical team to help with this step**, or follow:

**Mac**:
```bash
brew install ollama
ollama serve
ollama pull llama3
```

**Windows/Linux**: Download from https://ollama.ai

### Step 3: Create Your First Workflow! (5 minutes)

Open n8n and:
1. Click "Add node"
2. Search "Webhook"
3. Add it to canvas
4. Click "+) and add "Ollama"
5. Connect them
6. Test it!

🎉 **You just built your first AI workflow!**

---

## 📚 Learning Path

### Week-by-Week Plan

| Week | Unit | What You'll Build | Time |
|------|------|-------------------|------|
| 1 | Unit 1 | First chatbot, simple workflows | 8-10h |
| 2 | Unit 2 | Environment mastery, integrations | 6-8h |
| 3 | Unit 3 | Multi-step workflows, chains | 10-12h |
| 4 | Unit 4 | Stateful agents, decision trees | 10-12h |
| 5 | Unit 5 | Multi-agent systems | 12-14h |
| 6 | Unit 6 | Knowledge base Q&A (RAG) | 12-14h |
| 7 | Unit 7 | Integration with your tools | 10-12h |
| 8 | Unit 8 | Memory and context | 8-10h |
| 9 | Unit 9 | Production workflows | 10-12h |
| 10 | Unit 10 | Advanced patterns | 12-14h |
| 11 | Unit 11 | Your industry applications | 10-12h |
| 12 | Unit 12 | Capstone project | 20-30h |

**Total**: ~130-170 hours (8-12 weeks)

---

## 🎓 How to Use These Materials

### For Self-Learning:

1. **Start with Curriculum**
   ```
   Open: curriculum/AGENTIC_AI_CURRICULUM_N8N.md
   Read: Unit 1 completely
   ```

2. **Do the Exercises**
   ```
   Open: exercises/unit_01_exercises.md
   Complete: Each exercise in order
   Test: Everything works before moving on
   ```

3. **Import Workflow Templates**
   ```
   In n8n: Import workflow
   Select: workflows/unit_01_*.json files
   Study: How they're built
   Modify: Make them your own!
   ```

4. **Check Solutions (if stuck)**
   ```
   Read: instructor_guide/unit_01_solutions.md
   But try first! Learning happens through struggle!
   ```

### For Instructor-Led Learning:

1. **Preparation**
   - Read full curriculum
   - Test all workflows
   - Prepare your n8n instance
   - Ensure Ollama is ready

2. **Class Structure**:
   - **Day 1-2**: Theory + Live Demo (curriculum)
   - **Day 3-4**: Build Together (exercises 1-4)
   - **Day 5-6**: Independent Practice (exercises 5-8)
   - **Day 7**: Review + Q&A + Show  & Tell

3. **Use Instructor Guide**
   - Complete solutions included
   - Teaching strategies documented
   - Common pitfalls listed
   - Troubleshooting tips provided

---

## 🛠️ Tools You'll Need

### Required:
- ✅ **n8n** (desktop or cloud)
- ✅ **Ollama** (or OpenAI API key)
- ✅ **Web browser**
- ✅ **Curiosity!**

### Optional (but helpful):
- 📧 **Email account** (for testing)
- 💬 **Slack workspace** (for chat integrations)
- 📊 **Google account** (for Sheets/Docs)
- 🗂️ **Airtable/Notion** (for databases)

### Don't Need:
- ❌ Coding experience
- ❌ Technical background
- ❌ Terminal/command line knowledge
- ❌ To understand algorithms

---

## 💡 Key Concepts (Visual Understanding)

### 1. Nodes = Lego Blocks
Each node is a block. Connect them to build something amazing!

### 2. Workflows = Recipes
Like cooking: take ingredients (input) → follow steps (nodes) → get dish (output)

### 3. AI Agents = Smart Assistants
They can think (AI), do things (tools), and remember (memory)

### 4. Tools = Hands for AI
AI brain + hands (calculator, search, email) = useful agent

### 5. Memory = Context
Like talking to someone who remembers you!

---

## 🎯 Success Stories

### What Others Have Built:

**Sarah (Product Owner)**:
- Built customer feedback analyzer
- Automatically tags and routes requests
- Saves 10 hours/week

**Mike (Scrum Master)**:
- Created sprint planning assistant
- Generates sprint reports
- Sends updates to Slack

**Lisa (Business Analyst)**:
- Built requirements generator
- Analyzes stakeholder feedback
- Creates draft user stories

**You can too!**

---

## 🤝 Working with Your Technical Team

### You're Learning the Same Concepts!

| You (n8n) | Tech Team (Code) | Same Concept |
|-----------|------------------|--------------|
| Nodes | Functions | Building blocks |
| Workflows | Programs | Logic flow |
| Expressions | Variables | Data |
| Connections | Data flow | Information movement |

### How to Collaborate:

1. **Prototype in n8n**
   - Build visual proof-of-concept
   - Test your idea
   - Show to team

2. **Developers Optimize**
   - They can code-ify your workflow
   - Make it faster/scalable
   - You provided the spec!

3. **You Both Win**
   - Faster ideation (you)
   - Clear requirements (them)
   - Better products (everyone)

---

## 📖 Parallel Learning

Your curriculum is **synchronized** with the technical track:

| Unit | You Learn (n8n) | They Learn (Code) | Same Goal |
|------|-----------------|-------------------|-----------|
| 1 | Visual agents | Python agents | Understand agents |
| 2 | n8n setup | Ollama + Python | Environment ready |
| 3 | Visual chains | LangChain code | Multi-step workflows |
| 4 | Visual state machines | LangGraph | Stateful agents |
| 6 | Visual RAG | LlamaIndex code | Knowledge Q&A |

**You speak the same language, use different tools!**

---

## 🎨 Learning Style: Visual First

This course is designed for visual thinkers:
- 📊 Diagrams everywhere
- 🎨 Color-coded workflows
- 🎯 Click, don't type
- 👁️ See data flow in real-time
- 🖱️ Drag and drop

**No black screens. No cryptic code. Just visual creativity!**

---

## 💪 You Can Do This!

### Common Fears (and the Truth):

❌ "I can't code"
✅ **You don't need to!** n8n is visual

❌ "This is too technical"
✅ **You know business logic** - this is just visualizing it

❌ "I'll break something"
✅ **Impossible!** Workflows can be undone

❌ "I won't keep up with developers"
✅ **You're learning the same concepts**, just visually

❌ "AI is complicated"
✅ **Not when you see it visually!**

---

## 📞 Getting Help

### When Stuck:

1. **Check the workflows folder**
   - Import working examples
   - See how they're built

2. **Read instructor guide**
   - Solutions for all exercises
   - Troubleshooting tips

3. **n8n Community**
   - https://community.n8n.io
   - Super helpful and friendly!

4. **Your Tech Team**
   - They can help with Ollama
   - You can share workflows

5. **YouTube**
   - Search "n8n AI tutorials"
   - Lots of video guides

---

## 🏆 Certification Projects

### Unit 6 Project: Knowledge Base Bot
Build a bot that answers questions about your company/product docs

### Unit 9 Project: Production Workflow
Create a real workflow you'll use daily at work

### Unit 12 Project: Capstone
Full AI solution solving a real business problem

**Share your projects! Build your portfolio!**

---

## 📊 Track Your Progress

### Unit Checklist:

- [ ] Unit 1: Built my first chatbot ✅
- [ ] Unit 2: Environment fully set up ✅
- [ ] Unit 3: Created multi-step workflow ✅
- [ ] Unit 4: Built stateful agent ✅
- [ ] Unit 5: Multi-agent collaboration ✅
- [ ] Unit 6: Knowledge Q&A system ✅
- [ ] Unit 7: Real tool integrations ✅
- [ ] Unit 8: Implemented memory ✅
- [ ] Unit 9: Production-ready workflow ✅
- [ ] Unit 10: Advanced patterns ✅
- [ ] Unit 11: Industry application ✅
- [ ] Unit 12: Capstone completed! 🎉

---

## 🎉 Ready to Start?

### Your First 30 Minutes:

```
Minute 0-10: Install n8n
Minute 10-15: Open and explore interface
Minute 15-20: Read Unit 1 introduction
Minute 20-30: Build "Hello World" workflow

That's it! You're an AI builder now! 🎨🤖
```

### Next Steps:

1. Open `curriculum/AGENTIC_AI_CURRICULUM_N8N.md`
2. Read Unit 1 completely
3. Open `exercises/unit_01_exercises.md`
4. Start with Exercise 1
5. Have fun!

---

## 🌟 Remember:

> "You don't need to code to build AI.  
> You need to think logically and be creative.  
> n8n lets you do both visually!"

**Welcome to the world of visual AI development! Let's build something amazing! 🚀**

---

## 📄 File Quick Reference

- 📖 **Main Curriculum**: `curriculum/AGENTIC_AI_CURRICULUM_N8N.md`
- ✏️ **Exercises**: `exercises/unit_XX_exercises.md`
- 🔧 **Workflows**: `workflows/*.json` (import into n8n)
- 👨‍🏫 **Solutions**: `instructor_guide/unit_XX_solutions.md`
- 📘 **This README**: You are here!

---

**Version**: 1.0  
**Created**: January 2026  
**For**: Non-Technical Learners  
**Parallel to**: Technical Python Track  
**Tool**: n8n (visual workflow automation)

**Let's get started! 🎨🤖**
