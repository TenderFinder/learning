# n8n Workflow Templates - Unit 1

## Overview
These are sample n8n workflows that you can import directly into your n8n instance. Each workflow demonstrates key concepts from Unit 1.

---

## How to Import Workflows

1. **In n8n**:
   - Click on "Workflows" (top left)
   - Click "Import from File" or "Import from URL"
   - Select the JSON file
   - Click "Import"

2. **Configure**:
   - Review each node
   - Update credentials (if needed)
   - Test the workflow

3. **Activate**:
   - Toggle the switch in top right
   - Your workflow is live!

---

## Workflow 1: Hello World AI

**File**: `unit_01_hello_world.json`

### Description
Simple workflow that receives text and responds with AI.

### Nodes:
1. **Webhook** - Receives GET requests
2. **Ollama** - Processes with AI
3. **Respond to Webhook** - Sends response

### Configuration Needed:
- Ollama must be running
- Model: llama3

### Test:
```
GET http://localhost:5678/webhook/hello?text=What is AI?
```

### Example JSON (Simplified):
```json
{
  "name": "Hello World AI - Unit 1",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "GET",
        "path": "hello",
        "responseMode": "responseNode"
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [250, 300]
    },
    {
      "parameters": {
        "model": "llama3",
        "prompt": "={{ $json.query.text }}"
      },
      "name": "Ollama",
      "type": "n8n-nodes-base.ollama",
      "position": [450, 300]
    },
    {
      "parameters": {
        "respondWith": "text",
        "responseBody": "={{ $json.message }}"
      },
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [650, 300]
    }
  ],
  "connections": {
    "Webhook": {"main": [[{"node": "Ollama", "type": "main", "index": 0}]]},
    "Ollama": {"main": [[{"node": "Respond to Webhook", "type": "main", "index": 0}]]}
  }
}
```

---

## Workflow 2: Simple Chatbot with Memory

**File**: `unit_01_chatbot.json`

### Description
Conversational chatbot that remembers the last 5 messages.

### Nodes:
1. **Chat Trigger** - n8n's built-in chat interface
2. **Window Buffer Memory** - Remembers context
3. **Ollama Chat Model** - AI responses
4. **Respond to Chat** - Sends message

### Configuration Needed:
- Ollama running with llama3
- Memory window size: 5

### Test Conversation:
```
You: Hi, I'm Alex
Bot: Hello Alex! Nice to meet you.

You: What's my name?
Bot: Your name is Alex.  ✅ (remembers!)
```

### Key Settings:
```json
{
  "Ollama Chat Model": {
    "model": "llama3",
    "systemMessage": "You are a helpful assistant",
    "temperature": 0.7,
    "maxTokens": 500
  },
  "Memory": {
    "contextWindowLength": 5
  }
}
```

---

## Workflow 3: Calculator Agent (Tool Use)

**File**: `unit_01_calculator_agent.json`

### Description
AI agent that decides when to use a calculator tool vs regular chat.

### Nodes:
1. **Chat Trigger**
2. **AI Agent** - Decides which tool to use
3. **Calculator Tool** (Code node)
4. **Respond**

### How It Works:
- User asks: "What is 15 * 8?" → Uses calculator
- User asks: "Tell me about AI" → Just chats

### Calculator Code (JavaScript):
```javascript
// In Code node
const expression = $input.first().json.query;

try {
  // Safe eval for simple math
  const result = Function('"use strict"; return (' + expression + ')')();
  return [{ json: { result: result } }];
} catch (error) {
  return [{ json: { error: "Invalid expression" } }];
}
```

---

## Workflow 4: Multi-Step Content Generator

**File**: `unit_01_content_generator.json`

### Description
Creates blog content in multiple AI steps: title → outline → introduction.

### Nodes:
1. **Webhook** (receives topic)
2. **Ollama - Title** - Generates title
3. **Ollama - Outline** - Creates 3 subtopics
4. **Ollama - Introduction** - Writes intro paragraph
5. **Merge** - Combines all outputs
6. **Email** or **Respond** - Sends result

### Workflow Flow:
```
Topic: "AI in Product Management"
    ↓
Title: "How AI is Transforming Product Management"
    ↓
Outline: 1. User Research, 2. Prioritization, 3. Analytics
    ↓
Introduction: [Compelling paragraph]
    ↓
Final Output: Complete blog structure
```

### Prompts Used:
```javascript
// Title Generator
"Create a compelling blog post title about: {{topic}}"

// Outline Generator  
"For the blog post titled '{{title}}', list 3 main subtopics"

// Introduction Writer
"Write a 100-word introduction for '{{title}}' covering: {{outline}}"
```

---

## Workflow 5: Email Classifier

**File**: `unit_01_email_classifier.json`

### Description
Automatically classifies emails as urgent, question, newsletter, or other.

### Nodes:
1. **Email Trigger** (or Webhook for demo)
2. **Ollama - Classifier** - Determines category
3. **IF Node** - Routes based on category
4. **Different actions per category**:
   - Urgent → Slack notification
   - Question → Draft response
   - Newsletter → Archive
   - Other → Tag for review

### Classifier Prompt:
```
"Analyze this email and classify it as exactly ONE of:
- urgent
- question
- newsletter
- other

Email: {{email_content}}

Response format: Just the category, nothing else."
```

### Routing Logic:
```javascript
// In IF node
const category = $json.category.toLowerCase();

if (category.includes('urgent')) return 'urgent';
if (category.includes('question')) return 'question';
if (category.includes('newsletter')) return 'newsletter';
return 'other';
```

---

## Workflow 6: Meeting Notes Processor

**File**: `unit_01_meeting_notes.json`

### Description
Extracts summary, action items, decisions, and questions from meeting notes.

### Nodes:
1. **Webhook/Manual Trigger** (paste notes)
2. **Ollama - Analyzer** - Structured extraction
3. **Parse/Split** - Separate sections
4. **Multiple outputs**:
   - Slack summary
   - Create tasks in project tool
   - Save to database

### AI Prompt:
```
"Extract from these meeting notes:

SUMMARY: (2-3 sentences)
ACTION ITEMS: (list with owners)
DECISIONS: (key decisions made)
QUESTIONS: (open questions)

Meeting notes:
{{notes}}

Format output exactly as shown above."
```

### Output Structure:
```json
{
  "summary": "Discussion about...",
  "action_items": [
    "Alex: Create user stories by Friday",
    "Team: Review Ollama documentation"
  ],
  "decisions": [
    "Use n8n for automation"
  ],
  "questions": [
    "Which AI model for production?"
  ]
}
```

---

## Workflow 7: Self-Improving Content

**File**: `unit_01_self_improvement.json`

### Description
Generates content, critiques it, and improves iteratively.

### Nodes:
1. **Input** (topic)
2. **Generator AI** - Creates content
3. **Critic AI** - Rates quality (1-10)
4. **IF Node** - Check if good enough
5. **Improver AI** - Revises if needed
6. **Loop Logic** - Repeat up to 3 times

### Flow:
```
Topic: "Write haiku about AI"
    ↓
Generate: [First attempt]
    ↓
Critique: "6/10 - syllable count wrong"
    ↓
Improve: [Better version]
    ↓
Critique: "9/10 - excellent!"
    ↓
Output: Final haiku
```

### Implementation Note:
```
Use Loop node or manual counter:
- Start with iteration = 0
- Increment each loop
- Exit if score >= 8 OR iteration >= 3
```

---

## Workflow 8: Personal Assistant Starter

**File**: `unit_01_personal_assistant.json`

### Description
Multi-purpose assistant handling different request types.

### Capabilities:
- 📝 Create tasks
- ❓ Answer questions
- 📧 Send emails
- 🔍 Search knowledge base

### Architecture:
```
User Input
    ↓
Intent Classifier (AI)
    ↓
    ├─ [task] → Create in Airtable
    ├─ [question] → Search docs → AI answer
    ├─ [email] → Draft and send
    └─ [chat] → Conversational AI
    ↓
Update Memory
    ↓
Respond
```

### Intent Classification Prompt:
```
"Classify this request as:
- task (if creating/managing tasks)
- question (if asking for information)
- email (if sending communication)
- chat (if just conversing)

Request: {{user_input}}
Reply with just the category."
```

---

## Tips for Using These Templates

### 1. Start Simple
- Import Workflow 1 first
- Get it working
- Then try more complex ones

### 2. Customize
- Change prompts to your style
- Add your own integrations
- Modify to fit your needs

### 3. Learn by Doing
- Click on each node
- Read the configuration
- Understand the flow
- Modify and test

### 4. Troubleshooting
- Check execution logs
- Test nodes individually
- Verify credentials
- Ensure Ollama is running

---

## File Naming Convention

```
unit_XX_descriptive_name.json

Examples:
- unit_01_hello_world.json
- unit_01_chatbot.json
- unit_03_rag_system.json
```

---

## Creating Your Own Workflows

1. **Build in n8n**
2. **Test thoroughly**
3. **Export**:
   - Click "..." menu
   - "Download"
   - Save as JSON
4. **Share** with the team!

---

## Template Library

### Beginner Templates:
- ✅ Hello World AI
- ✅ Simple Chatbot
- ✅ Text Completion

### Intermediate Templates:
- ✅ Calculator Agent
- ✅ Email Classifier
- ✅ Content Generator

### Advanced Templates:
- ✅ Meeting Processor
- ✅ Self-Improving Content
- ✅ Personal Assistant

---

## Additional Resources

- **n8n Templates Library**: https://n8n.io/workflows/
- **Community Workflows**: https://community.n8n.io/
- **Documentation**: https://docs.n8n.io/

---

## Note About JSON Files

**Important**: The JSON examples above are simplified for readability. Full workflow exports include:
- Node positions
- Detailed parameters
- Credential references (you'll need to reconfigure)
- Version information

**Always test imported workflows before using in production!**

---

## Next Steps

1. Import a workflow
2. Study how it's built
3. Modify it
4. Create your own!

**Happy workflow building! 🎨🤖**
