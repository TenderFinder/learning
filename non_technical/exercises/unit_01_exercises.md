# Unit 1: Introduction to Agentic AI - n8n Exercises

## Learning Objectives
By completing these exercises, you will:
- Understand AI agent concepts visually
- Build your first n8n workflows
- Connect to local AI (Ollama)
- Create simple chatbots and automation

---

## Exercise 1: Your First n8n Workflow (Beginner) ⭐

**Objective**: Create a simple "Hello World" AI workflow.

**What You'll Build**:
A workflow that takes any text input and gets a response from AI.

**Steps**:
1. Open n8n
2. Create a new workflow
3. Add these nodes:
   - **Webhook** node (trigger) - to receive input
   - **Ollama** node (or OpenAI) - for AI processing
   - **Respond to Webhook** node - to send response back

4. Configure:
   - Webhook: GET method, path `/hello`
   - Ollama: Model `llama3`, prompt from webhook data
   - Response: Return AI's response

5. Test:
   - Activate workflow
   - Send test: `http://localhost:5678/webhook/hello?text=What is AI?`
   - See AI response!

**Expected Result**:
```
Input: "What is AI?"
Output: [AI's explanation of artificial intelligence]
```

**Success Criteria**:
- ✅ Workflow runs without errors
- ✅ AI responds to your question
- ✅ You understand each node's purpose

**Bonus**: Try asking 3 different questions and observe different responses!

---

## Exercise 2: Build a Simple Chatbot (Beginner) ⭐

**Objective**: Create a chatbot that can have basic conversations.

**What You'll Build**:
A chatbot you can test through n8n's chat interface.

**Visual Workflow**:
```
Chat Message Trigger
       ↓
   Ollama AI
       ↓
  Send Response
```

**Steps**:
1. Use **Chat Trigger** node
2. Add **Ollama Chat Model** node:
   - Model: `llama3`
   - System Message: "You are a friendly AI assistant."
   - Temperature: 0.7 (for creative responses)
3. Add **Respond to Chat** node
4. Test in n8n's chat interface

**Conversation to Test**:
```
You: Hi! What's your name?
Bot: [Response]

You: Can you help me understand AI agents?
Bot: [Response]

You: Thank you!
Bot: [Response]
```

**Success Criteria**:
- ✅ Bot responds to greetings
- ✅ Bot can answer questions
- ✅ Responses make sense
- ✅ You can chat back and forth

**Bonus**: Change the system message to give the bot a different personality!

---

## Exercise 3: Understanding Tools - Build a Calculator Agent (Intermediate) ⭐⭐

**Objective**: Create an agent that can perform calculations.

**What You'll Build**:
An AI that knows when to use a calculator tool.

**Visual Workflow**:
```
User Question
     ↓
   AI Agent (decides if calculation needed)
     ↓
  [If YES] → Calculator Tool → AI (format answer)
  [If NO]  → AI responds directly
     ↓
   Response
```

**Steps**:
1. Create Chat Trigger
2. Add **AI Agent** node
3. Add **Code** node as calculator tool:
   - Name it "Calculator"
   - Add simple calculation logic (use n8n's built-in functions)
4. Configure agent to use calculator when needed
5. Test with:
   - "What is 25 * 16?" (should use calculator)
   - "What is AI?" (should not use calculator)

**Test Cases**:
```
✅ "Calculate 144 divided by 12" → Uses calculator
✅ "What's 2 + 2?" → Uses calculator
❌ "Tell me about AI" → Doesn't use calculator
```

**Success Criteria**:
- ✅ Agent uses calculator for math questions
- ✅ Agent responds normally for non-math questions
- ✅ Calculations are correct

**Learning Point**: This demonstrates how agents decide which tools to use!

---

## Exercise 4: Adding Memory to Your Chatbot (Intermediate) ⭐⭐

**Objective**: Build a chatbot that remembers the conversation.

**What You'll Build**:
A chatbot that recalls what you told it earlier.

**Visual Workflow**:
```
Chat Message
     ↓
Load Previous Messages (Memory)
     ↓
AI + Context
     ↓
Save to Memory
     ↓
Respond
```

**Steps**:
1. Add **Window Buffer Memory** node (remembers last 5 messages)
2. Connect to your AI agent
3. Test memory:
   - Turn 1: "My name is Alex"
   - Turn 2: "I work in product management"
   - Turn 3: "What's my name?" (should remember!)
   - Turn 4: "What do I do?" (should remember!)

**Advanced Version**:
- Use **Airtable** or **Notion** to store long-term memory
- Remember user preferences across sessions

**Success Criteria**:
- ✅ Bot remembers your name
- ✅ Bot recalls previous topics
- ✅ Conversation feels contextual

**Bonus**: Clear memory and see the difference!

---

## Exercise 5: Multi-Step Workflow - Content Generator (Intermediate) ⭐⭐

**Objective**: Build a workflow that performs multiple AI tasks in sequence.

**What You'll Build**:
A blog post outline generator that works in steps.

**Visual Workflow**:
```
Topic Input
    ↓
Generate Title (AI #1)
    ↓
Generate 3 Subtopics (AI #2)
    ↓
Write Introduction (AI #3)
    ↓
Combine & Format
    ↓
Email Result or Save to Google Docs
```

**Steps**:
1. **Webhook** to receive topic
2. **Ollama #1**: Generate catchy title
   - Prompt: "Create a blog post title about: {{topic}}"
3. **Ollama #2**: Generate subtopics
   - Prompt: "List 3 subtopics for: {{title}}"
4. **Ollama #3**: Write intro
   - Prompt: "Write introduction for: {{title}} covering {{subtopics}}"
5. **Format node**: Combine all outputs
6. **Email** or **Google Docs** node to save result

**Test Topic**: "AI in Product Management"

**Expected Output**:
```
Title: "How AI is Revolutionizing Product Management in 2026"

Subtopics:
1. AI-Powered User Research
2. Data-Driven Backlog Prioritization  
3. Automated Feature Validation

Introduction:
[Generated paragraph]
```

**Success Criteria**:
- ✅ All steps execute in order
- ✅ Output is coherent and useful
- ✅ Result is saved/emailed
- ✅ You understand each step's purpose

---

## Exercise 6: Conditional Workflow - Email Classifier (Advanced) ⭐⭐⭐

**Objective**: Build an intelligent email routing system.

**What You'll Build**:
A workflow that classifies emails and routes them differently.

**Visual Workflow**:
```
New Email
    ↓
AI Classifier
    ↓
  [IF Urgent] → Send to Slack + Mark Important
  [IF Question] → Draft Response → Ask for approval
  [IF Newsletter] → Archive
  [IF Other] → Tag "Review Later"
```

**Steps**:
1. **Email Trigger** (or use webhook to simulate)
2. **AI Classifier**: 
   - Prompt: "Classify this email as: urgent, question, newsletter, or other"
   - Extract category from response
3. **IF node** to route based on classification
4. Different paths for each category:
   - Urgent: Slack notification
   - Question: Generate draft response
   - Newsletter: Move to folder
   - Other: Add tag

**Test Emails**:
```
1. "URGENT: Server is down!"
2. "Can you explain the new feature?"
3. "Newsletter: Latest updates"
4. "FYI: Meeting moved to 3pm"
```

**Success Criteria**:
- ✅ Correctly classifies 4/4 test emails
- ✅ Routes to correct action
- ✅ You understand conditional logic

**Real-World Use**: Automate your inbox!

---

## Exercise 7: Real-World Scenario - Meeting Assistant (Advanced) ⭐⭐⭐

**Objective**: Build a practical workflow you can use daily.

**What You'll Build**:
An assistant that processes meeting notes into action items.

**Visual Workflow**:
```
Meeting Notes (Google Docs or paste)
    ↓
AI Analysis
    ↓
Extract: Summary, Action Items, Decisions, Questions
    ↓
Format into Template
    ↓
Send to Slack + Create Jira/Trello cards
    ↓
Save to Notion/Airtable
```

**Steps**:
1. **Trigger**: Google Docs webhook or manual input
2. **AI Processor**:
   - Prompt: "Extract from these notes:
     1. Summary (2-3 sentences)
     2. Action items with owners
     3. Key decisions made
     4. Open questions"
3. **Parser node**: Structure the AI output
4. **Multiple outputs**:
   - Slack message with summary
   - Create tasks in Jira/Trello
   - Save structured data to database

**Test Notes**:
```
Meeting: Sprint Planning
- Discussed new features for Q1
- Alex will create user stories by Friday
- Decided to use n8n for automation
- Question: Which AI model to use?
- Sarah suggested checking Ollama
```

**Expected Output**:
```
Summary: Sprint planning covered Q1 features and automation decisions.

Action Items:
- [ ] Alex: Create user stories (Due: Friday)
- [ ] Team: Evaluate Ollama vs alternatives

Decisions:
- Use n8n for automation

Open Questions:
- Which AI model to use?
```

**Success Criteria**:
- ✅ Accurately extracts all sections
- ✅ Notifies team on Slack
- ✅ Creates actual tasks
- ✅ Saves for future reference

---

## Exercise 8: Understanding Agent Loops (Advanced) ⭐⭐⭐

**Objective**: Build a self-improving content workflow.

**What You'll Build**:
An AI that generates content, critiques it, and improves it.

**Visual Workflow**:
```
Topic
  ↓
Generate Content (AI #1)
  ↓
Self-Critique (AI #2)
  ↓
[IF Good] → Output
[IF Needs Work] → Improve (AI #3) → Loop back to Critique
  ↓
Final Content
```

**Steps**:
1. **Input**: Receive topic
2. **Generator AI**: Create initial haiku/text
3. **Critic AI**: Review quality
   - Prompt: "Rate this content 1-10 and explain issues"
4. **IF node**: Check if score >= 8
5. **Improver AI**: Revise based on feedback
6. **Loop Logic**: Max 3 iterations
7. **Output**: Best version

**Test**: "Write a haiku about AI agents"

**Expected Flow**:
```
Iteration 1:
Generated: [haiku - may not be perfect]
Critique: "6/10 - syllable count is off"

Iteration 2:
Improved: [better haiku]
Critique: "8/10 - good!"
→ Output final version
```

**Success Criteria**:
- ✅ Generates initial content
- ✅ Critiques objectively
- ✅ Improves based on feedback
- ✅ Stops after good result or 3 tries

**Learning**: This is how AI agents improve through iteration!

---

## Challenge Project: Personal AI Assistant (Advanced) ⭐⭐⭐⭐

**Objective**: Build a complete, useful AI assistant for yourself.

**Requirements**:
Your assistant should handle:
1. **Task Management**
   - Create tasks from chat
   - List today's tasks
   - Mark tasks complete

2. **Information Lookup**
   - Answer questions from your knowledge base
   - Remember preferences you tell it

3. **Automation**
   - Send reminders
   - Daily summaries
   - Quick actions ("Send status to team")

4. **Memory**
   - Remember your name, role, preferences
   - Track conversation history
   - Learn over time

**Visual Architecture**:
```
Chat Interface
      ↓
Intent Classifier (AI)
      ↓
   [Task] → Task Management System
   [Question] → Knowledge Base Search
   [Automation] → Execute Action
   [General] → Conversational AI
      ↓
   Response + Update Memory
```

**Suggested Integrations**:
- Slack/Discord for interface
- Airtable for tasks and memory
- Google Calendar for scheduling
- Email for notifications

**Test Scenarios**:
```
"Remember that I prefer morning meetings"
→ Saves to preferences

"Add task: Review sprint backlog"
→ Creates task in Airtable

"What are my tasks for today?"
→ Lists from database

"Send a message to the team that I'll be 5 min late"
→ Sends to Slack

"What time do I prefer meetings?"
→ Recalls from memory: "mornings"
```

**Success Criteria**:
- ✅ Handles all 4 types of requests
- ✅ Maintains consistent memory
- ✅ Provides helpful responses
- ✅ Actually useful in daily work!

**Bonus Features**:
- Voice input (if possible)
- Mobile notifications
- Weekly summaries
- Suggest task prioritization

---

## Submission Guidelines

For each exercise:
1. **Screenshots**:
   - Workflow canvas (visual diagram)
   - Successful execution logs
   - Sample outputs

2. **Workflow Export**:
   - Export as JSON from n8n
   - Include in submission

3. **Documentation**:
   - Brief description of what it does
   - How to use it
   - Any gotchas or special setup

4. **Demo Video** (for challenge project):
   - 2-3 minute walkthrough
   - Show it working in real-time

---

## Evaluation Criteria

- **Functionality**: Does it work as specified?
- **Understanding**: Do you understand what each node does?
- **Creativity**: Did you add interesting improvements?
- **Practicality**: Could this be used in real work?
- **Documentation**: Can someone else understand and use it?

---

## Tips for Success

### General n8n Tips:
- 💡 Test each node individually before connecting
- 💡 Use the "Execute Workflow" button liberally
- 💡 Check execution logs when something fails
- 💡 Start simple, add complexity gradually
- 💡 Save frequently!

### Debugging:
- ❓ Not working? Check credentials first
- ❓ AI not responding? Verify Ollama is running
- ❓ Wrong output? Look at the data between nodes
- ❓ Confused? Simplify and build back up

### Learning:
- 📚 Use n8n templates for inspiration
- 📚 Join n8n community for help
- 📚 Watch tutorial videos
- 📚 Experiment fearlessly!

---

## Resources

- **n8n Documentation**: https://docs.n8n.io/
- **Templates**: https://n8n.io/workflows/
- **Community**: https://community.n8n.io/
- **YouTube**: Search "n8n AI workflows"
- **Your Tech Team**: They can help with Ollama setup!

---

## Next Steps

After completing these exercises:
1. Move to Unit 2 exercises (environment mastery)
2. Share your workflows with the team
3. Identify real problems to solve
4. Build your portfolio of workflows

---

**Estimated Time**: 8-12 hours for all exercises  
**Difficulty**: Progressive (beginner → advanced)  
**Prerequisites**: n8n installed, Ollama running  

**Remember**: The goal isn't perfection—it's understanding! Experiment, break things, learn, and have fun! 🎨🤖
