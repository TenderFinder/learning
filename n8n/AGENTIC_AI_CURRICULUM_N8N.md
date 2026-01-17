# Agentic AI Course - Non-Technical Track
## Using n8n for No-Code AI Agent Development

**Target Audience**: Product Owners, Scrum Masters, Business Analysts, Non-Technical Team Members  
**Duration**: 8-10 weeks (aligned with technical track)  
**Tools**: n8n (visual workflow automation), Ollama (local AI), No coding required!  

---

## 📋 Course Overview

This course teaches the **same Agentic AI concepts** as the technical track, but using **n8n's visual interface** instead of code. You'll learn to build AI agents, workflows, and automation without writing a single line of code!

### Why n8n for Non-Technical Learners?

- ✅ **Visual Workflow Builder** - Drag and drop, no coding
- ✅ **AI Integration** - Connect to Ollama, OpenAI, and more
- ✅ **Same Concepts** - Learn agents, tools, memory, just visually
- ✅ **Real-World Skills** - Build production-ready automations
- ✅ **Empowerment** - Understand what your tech team is building

---

## 🎯 Learning Outcomes

By the end of this course, you will be able to:
- 🎨 Design and build AI agent workflows visually
- 🤖 Create chatbots and automation without code
- 📊 Understand agent concepts (tools, memory, planning)
- 🔧 Integrate AI into business processes
- 💬 Communicate effectively with technical teams
- 🚀 Prototype AI solutions independently

---

## 📚 Course Structure (12 Units - Synced with Technical Track)

---

## **Unit 1: Introduction to Agentic AI (Visual Concepts)**

### Week 1: Understanding AI Agents Through n8n
**Learning Objectives**:
- Understand what AI agents are
- Learn key components visually
- See real-world applications
- Set up your n8n environment

**Topics**:
1. **Key Components of Agentic Systems** (Visual Understanding)
   - 🤖 **AI Models** (LLMs) - The "brain" that thinks and responds
   - 🔧 **Tools** - Actions the agent can take (search, calculate, send email)
   - 💾 **Memory** - How agents remember conversations
   - 📋 **Workflows** - The sequence of actions
   - 🔄 **Feedback Loops** - How agents improve

2. **Real-World Applications**
   - Customer service automation
   - Content creation assistants
   - Data analysis and reporting
   - Email and task automation
   - Research and information gathering

3. **n8n vs Traditional Automation**
   - Static workflows → Intelligent agents
   - Rule-based → AI-powered decisions
   - Fixed → Adaptive responses

**Hands-on**:
- Install n8n (desktop or cloud)
- Connect to Ollama
- Create your first "Hello World" AI workflow
- Test with a simple chatbot

**Visual Examples**:
- See pre-built agent workflows
- Understand node connections
- Learn the n8n interface

---

## **Unit 2: Setting Up Your n8n Environment**

### Week 2: Installation and Configuration
**Learning Objectives**:
- Install n8n successfully
- Set up Ollama connection
- Configure AI models
- Understand the n8n interface

**Topics**:
1. **n8n Installation Options**
   - Desktop app (easiest for beginners)
   - Cloud version (n8n.cloud)
   - Docker (with help from tech team)
   
2. **Connecting to Ollama**
   - What is Ollama? (local AI models)
   - Installing Ollama
   - Testing the connection in n8n
   - Choosing models (llama3, mistral, etc.)

3. **n8n Interface Tour**
   - Workflow canvas
   - Node library
   - Workflow execution
   - Debugging tools
   - Saving and sharing workflows

4. **Your First Workflow**
   - Create a simple webhook → AI → response workflow
   - Test with different inputs
   - See results in real-time

**Hands-on**:
- Install n8n desktop app
- Connect to Ollama
- Create 3 simple workflows:
  - Text completion
  - Question answering
  - Simple chatbot

**Deliverable**: Working n8n instance with Ollama connected

---

## **Unit 3: Building Workflows (Visual "Chains")**

### Week 3: Creating Multi-Step Workflows
**Learning Objectives**:
- Build multi-step workflows (chains)
- Use templates effectively
- Implement conditional logic
- Save and reuse workflows

**Topics**:
1. **Understanding Workflow Components**
   - 🟢 **Trigger Nodes** - What starts the workflow
   - 🔵 **Action Nodes** - What the workflow does
   - 🟡 **AI Nodes** - Where intelligence happens
   - 🔴 **Output Nodes** - Where results go

2. **Building Your First Chain**
   - Input → Process → Output
   - Example: Blog post generator
     1. Get topic (webhook/form)
     2. Generate outline (AI)
     3. Write introduction (AI)
     4. Format and send (email/save)

3. **Using Templates and Prompts**
   - Pre-built prompt templates
   - Customizing prompts visually
   - Few-shot examples (showing AI how to respond)
   - System prompts (giving AI personality)

4. **Conditional Logic (IF/THEN)**
   - Route based on AI response
   - Handle different scenarios
   - Error handling visually
   - Fallback options

5. **Saving State (Memory)**
   - Storing conversation history
   - Using databases visually
   - Session management
   - Context retention

**Hands-on**:
- Build a content creation pipeline
- Create a customer support workflow
- Implement conditional routing
- Add memory to a chatbot

**Visual Workflows to Create**:
1. Email classifier (urgent/normal/spam)
2. Meeting notes summarizer
3. FAQ answerer with memory

---

## **Unit 4: Building Stateful Agents (Visual State Machines)**

### Week 4: Creating Agent Workflows with States
**Learning Objectives**:
- Understand agent states visually
- Build decision trees
- Implement loops and cycles
- Create multi-step reasoning

**Topics**:
1. **What Are States?**
   - Visual representation of agent status
   - Example states: waiting, processing, completed, error
   - How agents move between states
   - Tracking state visually in n8n

2. **Building State-Based Workflows**
   - Start state → Processing → Decision → End
   - Visual state indicators
   - State transitions
   - Handling state changes

3. **Decision Trees (Visual Conditionals)**
   - IF/THEN/ELSE visually
   - Multiple branches
   - Route based on AI decisions
   - Example: Customer inquiry router
     - Question → Classify → Route to appropriate response

4. **Loops and Iterations**
   - When to repeat steps
   - Loop until condition met
   - Example: Research assistant
     - Ask question → Search → Check if enough info → Loop or Finish

5. **Multi-Step Reasoning**
   - Break complex tasks into steps
   - Execute steps in sequence
   - Combine results
   - Example: Report generator
     1. Gather data
     2. Analyze each section
     3. Synthesize findings
     4. Format report

**Hands-on**:
- Build order processing workflow
- Create iterative research assistant
- Implement approval workflow
- Build multi-step problem solver

**Visual Workflows**:
1. Task approval system (request → approve/reject → notify)
2. Iterative content improver (generate → review → improve → repeat)
3. Customer onboarding flow (collect info → validate → setup → confirm)

---

## **Unit 5: Advanced Workflow Patterns**

### Week 5: Multi-Agent Systems and Complex Automation
**Learning Objectives**:
- Build multi-agent workflows
- Implement human approval steps
- Create parallel processing
- Handle errors gracefully

**Topics**:
1. **Multi-Agent Workflows (Specialist Agents)**
   - Different workflows for different tasks
   - Agent collaboration visually
   - Example: Content creation team
     - Researcher agent → Writer agent → Editor agent
   - Connecting workflows together

2. **Human-in-the-Loop**
   - Pause for approval
   - Send notifications
   - Wait for human input
   - Resume after approval
   - Example: Social media post approval
     - Draft → Review → Approve/Reject → Post/Revise

3. **Parallel Processing**
   - Run multiple tasks simultaneously
   - Merge results
   - Example: Product research
     - Search 3 sources at once → Combine results → Summarize

4. **Error Handling**
   - What to do when AI fails
   - Retry mechanisms
   - Fallback options
   - Error notifications
   - Example: If AI unavailable → Use default response → Notify admin

5. **Workflow Management**
   - Naming conventions
   - Organizing workflows
   - Version control (basic)
   - Documentation within n8n
   - Sharing with team

**Hands-on**:
- Build content creation team (3 agents)
- Create approval workflow
- Implement parallel data gathering
- Add comprehensive error handling

**Projects**:
1. Blog post creation pipeline (research → write → edit → review → publish)
2. Customer support system (classify → route → respond → escalate if needed)
3. Data enrichment workflow (gather from 3 sources → merge → clean → save)

---

## **Unit 6: Knowledge Bases and Q&A Systems (Visual RAG)**

### Week 6: Building Smart Question-Answering Systems
**Learning Objectives**:
- Understand RAG (Retrieval-Augmented Generation) visually
- Build document Q&A systems
- Implement semantic search
- Create knowledge base chatbots

**Topics**:
1. **What is RAG?** (Visual Explanation)
   - Problem: AI doesn't know your specific information
   - Solution: Give AI access to your documents
   - Visual flow: Question → Search docs → Find relevant info → Answer with AI
   
2. **Building a Knowledge Base**
   - Upload documents (PDF, Word, text)
   - Index documents (n8n vector store)
   - Make searchable
   - Tools: Pinecone, Qdrant, or Supabase (visual setup)

3. **Creating Q&A Workflows**
   ```
   User Question
        ↓
   Search Knowledge Base
        ↓
   Retrieve Relevant Sections
        ↓
   Send to AI with Context
        ↓
   Get Answer with Sources
   ```

4. **Semantic Search** (Understanding Meaning)
   - Beyond keyword matching
   - Find conceptually similar content
   - Example: "How do I reset password?" finds "password recovery instructions"
   
5. **Building Conversational Q&A**
   - Remember conversation context
   - Follow-up questions
   - Clarifications
   - Example conversation:
     - User: "What are your refund policies?"
     - Bot: [Answer from knowledge base]
     - User: "What about digital products?"
     - Bot: [Contextual answer remembering previous question]

**Hands-on**:
- Build document Q&A system
- Create FAQ chatbot
- Implement semantic search
- Add conversation memory

**Projects**:
1. Company knowledge base (employee handbook Q&A)
2. Product documentation assistant
3. Meeting notes search and summarize

---

## **Unit 7: Integrating Everything (Visual Integration)**

### Week 7: Connecting AI with Your Tools
**Learning Objectives**:
- Connect n8n workflows to real applications
- Integrate with business tools
- Build end-to-end automation
- Create practical AI assistants

**Topics**:
1. **n8n Integration Ecosystem**
   - 400+ pre-built integrations
   - Common tools:
     - 📧 Email (Gmail, Outlook)
     - 💬 Chat (Slack, Teams, Discord)
     - 📊 Spreadsheets (Google Sheets, Excel)
     - 🗂️ Databases (Airtable, Notion)
     - 📝 Documents (Google Docs)
     - 🎫 Project Management (Jira, Trello)

2. **Building Integrated Workflows**
   - Example 1: Email Assistant
     - New email → Classify → Draft response → Send or await approval
   - Example 2: Slack Bot
     - Slack message → Understand intent → Query knowledge base → Respond
   - Example 3: Report Generator
     - Trigger (schedule) → Gather data → Analyze with AI → Create doc → Email team

3. **Combining AI with LlamaIndex-like Features**
   - Document indexing workflows
   - Retrieval workflows
   - Multi-source synthesis
   - All visual, no code

4. **Real Business Use Cases**
   - Customer support automation
   - Content creation pipeline
   - Data analysis and reporting
   - Meeting assistance
   - Research automation

**Hands-on**:
- Build Slack AI assistant
- Create email automation
- Implement report generator
- Connect to Google Sheets for data

**Projects**:
1. Automated customer support (Email → AI classification → Response → Human for complex)
2. Content calendar automation (Topic → Research → Draft → Review → Schedule)
3. Daily digest generator (Gather news → Summarize → Format → Send)

---

## **Unit 8: Managing Context and Memory**

### Week 8: Building Smarter Agents with Memory
**Learning Objectives**:
- Implement different memory types
- Manage conversation context
- Build persistent knowledge
- Track user preferences

**Topics**:
1. **Types of Memory (Visual Understanding)**
   - 💬 **Short-term** - Current conversation only
   - 📚 **Long-term** - Remember across sessions
   - 👤 **User-specific** - Personal preferences and history
   - 🏢 **Shared** - Team knowledge base

2. **Implementing Memory in n8n**
   - Using databases (Airtable, Notion)
   - Session storage
   - User profiles
   - Conversation history

3. **Context Window Management**
   - How much can AI remember at once?
   - Summarizing old conversations
   - Keeping relevant context
   - Example: Summarize after 10 messages

4. **Building Persistent Assistants**
   - Remember user preferences
   - Track interaction history
   - Learn over time
   - Example: Personal AI assistant that knows your style

**Hands-on**:
- Build chatbot with memory
- Create user preference system
- Implement conversation summaries
- Build knowledge accumulation workflow

---

## **Unit 9: Production Best Practices**

### Week 9: Building Reliable Workflows
**Learning Objectives**:
- Deploy workflows reliably
- Monitor performance
- Handle errors gracefully
- Optimize costs and speed

**Topics**:
1. **Workflow Reliability**
   - Testing before deployment
   - Error handling strategies
   - Retry logic
   - Fallback options
   - Notifications when things fail

2. **Monitoring and Debugging**
   - Execution logs
   - Understanding errors
   - Testing workflows
   - Tracking success rates

3. **Performance Optimization**
   - Reducing steps
   - Caching results
   - Choosing right AI models
   - Parallel vs sequential processing

4. **Security and Privacy**
   - Protecting sensitive data
   - Access control
   - Secure credentials
   - Compliance considerations

5. **Cost Management**
   - Understanding n8n pricing
   - AI model costs (local vs cloud)
   - Optimizing executions
   - Monitoring usage

**Hands-on**:
- Add error handling to workflows
- Implement monitoring
- Optimize slow workflows
- Secure sensitive workflows

---

## **Unit 10: Advanced Patterns**

### Week 10: Cutting-Edge Workflow Designs
**Learning Objectives**:
- Implement advanced reasoning
- Build self-improving workflows
- Create dynamic automation
- Explore innovative patterns

**Topics**:
1. **Advanced Reasoning Patterns**
   - Chain-of-thought (step-by-step thinking)
   - Self-reflection (AI critiques itself)
   - Multi-perspective analysis
   - Iterative improvement

2. **Dynamic Workflows**
   - AI generates next steps
   - Adaptive based on results
   - Self-modifying (with limits)

3. **Multi-Agent Collaboration**
   - Assembling specialist agents
   - Debate and consensus
   - Role-playing scenarios
   - Example: AI product team
     - PM agent → Designer agent → Developer agent → QA agent

4. **Emerging Patterns**
   - Vision + language workflows
   - Multimodal processing
   - Browser automation with AI
   - Code generation workflows (for tech team)

**Hands-on**:
- Build chain-of-thought workflow
- Create multi-agent debate system
- Implement self-improving content
- Experiment with multimodal workflows

---

## **Unit 11: Industry-Specific Applications**

### Week 11: Building for Your Domain
**Learning Objectives**:
- Apply concepts to your industry
- Build practical business workflows
- Solve real problems
- Create ROI-driven automation

**Topics**:
1. **Product Management Workflows**
   - User story generation from requirements
   - Feature idea analyzer
   - Competitive research automation
   - Customer feedback analyzer
   - Backlog prioritization assistant

2. **Project Management Workflows**
   - Sprint planning assistant
   - Stand-up notes summarizer
   - Risk analyzer
   - Status report generator
   - Resource allocation suggester

3. **Marketing and Content**
   - Content calendar automation
   - Social media post generator
   - Campaign ideation
   - Audience analyzer
   - Performance report creator

4. **Customer Success**
   - Sentiment analyzer
   - Churn prediction
   - Personalized outreach
   - Success plan generator
   - Escalation detector

5. **Cross-Functional Workflows**
   - Meeting minutes and action items
   - Decision logging
   - Knowledge base builder
   - Team communication enhancer

**Hands-on**:
- Build 3 workflows for your role
- Solve a real problem from your backlog
- Create a demo for your team
- Measure time savings

---

## **Unit 12: Capstone Project**

### Week 12: Build Your Own AI Solution
**Learning Objectives**:
- Design complete solution
- Implement end-to-end
- Present to stakeholders
- Plan for production deployment

**Project Requirements**:
1. **Core Components** (Mandatory):
   - Multi-step workflow with AI
   - Knowledge base or data source
   - At least 2 integrations (Slack, Email, etc.)
   - Memory/state management
   - Error handling

2. **Advanced Features** (Choose 2):
   - Multi-agent collaboration
   - Human approval workflow
   - Advanced search/RAG
   - Scheduled automation
   - Dashboard or reporting
   - Mobile notifications

3. **Documentation**:
   - Workflow diagram (visual from n8n)
   - Setup instructions
   - User guide
   - Business value / ROI estimate
   - Future enhancements

4. **Presentation**:
   - Live demo
   - Business case
   - Lessons learned
   - Next steps

**Project Ideas**:
1. **Product Discovery Assistant**
   - Gathers user feedback
   - Analyzes trends
   - Generates feature ideas
   - Prioritizes based on criteria

2. **Sprint Autopilot**
   - Prepares sprint planning
   - Tracks progress
   - Identifies blockers
   - Generates sprint reports

3. **Customer Champion Bot**
   - Monitors customer sentiment
   - Escalates issues
   - Suggests responses
   - Tracks success metrics

4. **Content Factory**
   - Generates marketing content
   - Adapts to brand voice
   - Multi-platform publishing
   - Performance tracking

5. **Research Automator**
   - Competitive analysis
   - Market research
   - Trend analysis
   - Report generation

---

## 📋 Course Comparison: Technical vs Non-Technical

| Aspect | Technical Track (Code) | Non-Technical Track (n8n) |
|--------|------------------------|---------------------------|
| **Tool** | Python, LangChain, LangGraph | n8n visual workflows |
| **Learning** | Write code | Drag and drop nodes |
| **Concepts** | Same (agents, tools, memory) | Same (agents, tools, memory) |
| **Outcomes** | Build from scratch | Build with visual tools |
| **Collaboration** | Understand each other's work | |
| **Time** | 8-12 weeks | 8-12 weeks |

---

## 🎯 Success Criteria

By the end, you should be able to:
- ✅ Design and build AI workflows independently
- ✅ Understand agent concepts deeply
- ✅ Communicate effectively with tech team
- ✅ Prototype AI solutions for business problems
- ✅ Evaluate AI feasibility for projects
- ✅ Contribute to AI product discussions

---

## 🛠️ Tools Required

### Must Have:
- **n8n** (desktop app or cloud account)
- **Ollama** (or use cloud AI - OpenAI, Anthropic)
- **Web browser**
- **Email account** (for testing)

### Nice to Have:
- **Slack workspace** (for testing bots)
- **Google Workspace** (for integrations)
- **Airtable/Notion** (for databases)

---

## 📚 Resources

### Official Documentation
- [n8n Documentation](https://docs.n8n.io/)
- [n8n Community](https://community.n8n.io/)
- [n8n Templates](https://n8n.io/workflows/)
- [N8n YouTube Channel](https://www.youtube.com/@n8n-io)

### Learning Resources
- n8n Academy
- Video tutorials
- Community workflows
- Template library

---

## 💡 Teaching Tips

### For Instructors Teaching Non-Technical Learners:
1. **Use Visuals** - Show, don't just tell
2. **Start Simple** - Build confidence gradually
3. **Relate to Business** - Use real scenarios they face
4. **Encourage Experimentation** - Breaking things is ok!
5. **Bridge to Technical Team** - Help them understand code concepts

### Common Challenges:
- Understanding AI limitations
- Overthinking workflow design
- Fear of "breaking" things
- Not testing enough

### Solutions:
- Lots of examples
- Encourage trial and error
- Show that workflows can be fixed
- Practice testing together

---

## 🚀 Getting Started

### Week 0: Pre-Course Setup
1. Install n8n desktop
2. Install Ollama
3. Test connection
4. Complete "Hello World" workflow
5. Join n8n community

---

**Next**: See detailed exercises and workflow templates in the exercises folder!

**Remember**: You don't need to code to build powerful AI agents. n8n makes it visual, intuitive, and accessible to everyone! 🎨🤖

---

**Version**: 1.0  
**Last Updated**: January 2026  
**Target**: Non-Technical Team Members  
**Parallel to**: Technical Curriculum
