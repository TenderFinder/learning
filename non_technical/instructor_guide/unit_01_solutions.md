# Unit 1: n8n Workflows - Instructor Guide & Solutions

## Overview
This guide provides complete solutions, teaching strategies, and troubleshooting tips for teaching non-technical learners to build AI agents with n8n.

---

## Teaching Approach for Non-Technical Learners

### Key Principles:
1. **Show First, Explain Later** - Build together, then discuss concepts
2. **Use Analogies** - Compare to familiar business processes
3. **Celebrate Small Wins** - Each working node is progress!
4. **Normalize Errors** - Breaking things is part of learning
5. **Connect to Their World** - Use examples from their daily work

### Common Fears to Address:
- "I can't code" → You don't need to!
- "I'll break something" → You can't break n8n, workflows are reversible
- "This is too technical" → We're just connecting boxes
- "I won't understand" → You understand business processes - this is the same

---

## Exercise 1: Your First n8n Workflow

### Complete Solution

**Workflow JSON**:
```json
{
  "name": "Hello World AI",
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "parameters": {
        "path": "hello",
        "method": "GET",
        "responseMode": "responseNode"
      }
    },
    {
      "name": "Ollama",
      "type": "n8n-nodes-base.ollama",
      "parameters": {
        "model": "llama3",
        "prompt": "={{ $json.query.text }}"
      }
    },
    {
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "parameters": {
        "respondWith": "text",
        "responseBody": "={{ $json.message }}"
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [[{"node": "Ollama"}]]
    },
    "Ollama": {
      "main": [[{"node": "Respond to Webhook"}]]
    }
  }
}
```

### Teaching Strategy

**Step 1: Show the End Result (5 min)**
- Demo a working workflow

- Let them see it in action
- Build excitement: "You'll build this in 10 minutes!"

**Step 2: Build Together (15 min)**
- Screen share or project
- Build node by node
- Explain each node as you add it:
  - Webhook: "This is how messages come in"
  - Ollama: "This is where the AI thinks"
  - Respond: "This is how we send the answer back"

**Step 3: Test Together (5 min)**
- Activate the workflow
- Test with simple questions
- Celebrate when it works!

**Step 4: Experiment (10 min)**
- Have them modify the prompt
- Try different questions
- Change parameters

### Common Issues & Solutions

**Issue 1**: "Webhook returns error 404"
```
Solution: 
1. Check workflow is activated (toggle in top right)
2. Verify URL is correct
3. Show them the test URL in n8n
```

**Issue 2**: "Ollama not responding"
```
Solution:
1. Check Ollama is running (get tech help if needed)
2. Test Ollama separately first
3. Try a simpler model (phi3)
```

**Issue 3**: "I don't see any output"
```
Solution:
1. Click on nodes to see data flowing
2. Use "Execute Workflow" button
3. Check execution log (bottom panel)
```

### Discussion Points

- ❓ "What is a webhook?" → A doorbell that triggers the workflow
- ❓ "Why Ollama?" → AI running on our computer, not the cloud
- ❓ "Can I change the AI's tone?" → Yes! Modify the prompt

### Extension Ideas
- Add a system prompt to give AI a personality
- Connect to Slack instead of webhook
- Add error handling
- Log questions to a Google Sheet

---

## Exercise 2: Simple Chatbot

### Complete Solution

**Key Nodes**:
1. **Chat Trigger**: Built-in chat interface
2. **Window Buffer Memory**: Remembers last 5 messages
3. **Ollama Chat Model**: llama3 model
4. **Respond to Chat**: Sends message back

**Critical Configuration**:
```
Chat Model Settings:
- Model: llama3
- System Message: "You are a helpful AI assistant who knows about product management and agile methodology."
- Temperature: 0.7
- Max Tokens: 500

Memory Settings:
- Context Window Size: 5
```

### Teaching Strategy

**Live Demonstration (10 min)**:
- Show n8n's chat interface
- Have a real conversation with the bot
- Highlight how it remembers context

**Build Together (20 min)**:
- Add Chat Trigger
- Configure Ollama Chat Model
- Add Memory node
- Connect everything
- Test immediately!

**Experimentation (15 min)**:
- Change system message (personality)
- Adjust temperature (creativity)
- Test memory limits

### Common Issues

**Issue**: "Bot doesn't remember previous messages"
```
Solution:
- Ensure Window Buffer Memory is connected
- Check memory is before the AI node
- Verify session ID is consistent
```

**Issue**: "Responses are too long/short"
```
Solution:
- Adjust Max Tokens setting
- Modify system prompt to request brevity
```

### Real-World Applications
- Internal Q&A bot
- First-line customer support
- Meeting assistant
- Onboarding buddy

### Assessment Criteria
- ✅ Bot responds to messages
- ✅ Maintains context for 3+ turns
- ✅ System message affects behavior
- ✅ Student understands each component

---

## Exercise 3: Calculator Agent (Tools Concept)

### Complete Solution

**Workflow Structure**:
```
Chat Trigger
    ↓
AI Agent (decides: math or chat?)
    ↓
   [IF MATH] → Execute Calculator → Format Response
   [IF OTHER] → Direct Response
```

**Calculator Tool Code** (Simple n8n Function):
```javascript
// Simple calculator in Code node
const expression = $input.first().json.expression;

try {
  // Safely evaluate math expressions
  const result = eval(expression);
  return { result };
} catch (error) {
  return { error: "Invalid calculation" };
}
```

### Teaching Strategy

**Concept Introduction (10 min)**:
- Explain: "Tools are like giving AI hands to do things"
- Analogy: "You have a brain (AI) and hands (tools)"
- Examples: Calculator, search, email, database

**Visual Mapping (5 min)**:
- Draw on whiteboard:
  - Question → AI thinks → Decides if tool needed → Uses tool → Formats answer

**Build Together (25 min)**:
- Start with simple chat
- Add AI Agent node
- Create calculator as a tool
- Configure agent to use it
- Test with math and non-math questions

**Key Learning Moment**:
- Show AI deciding when to use calculator
- THIS is what makes it "intelligent"!

### Common Challenges

**Challenge**: "How does AI know when to use the calculator?"
```
Answer:
1. AI Agent node has tool descriptions
2. AI reads the question
3. AI thinks: "This needs math" → Uses calculator
4. AI thinks: "This is just chat" → Responds directly
```

**Challenge**: "My agent always/never uses the calculator"
```
Solutions:
- Check tool description is clear
- Ensure tool name is descriptive
- Test with obvious math questions first
- Review AI agent configuration
```

### Discussion: Real Tools in Business
- Email sender (for notifications)
- Database lookup (for customer info)
- Google Sheets (for data)
- Slack (for messages)
- Calendar (for scheduling)

**Exercise**: "What tools would YOUR perfect assistant have?"

---

## Exercise 4: Memory Implementation

### Complete Solution

**Memory Types to Demonstrate**:

1. **Buffer Memory** (Remembers everything)
2. **Window Memory** (Last N messages)
3. **Summary Memory** (Condenses old messages)

**Configuration**:
```
Window Buffer Memory:
- Context Window Size: 5
- Memory Key: "chat_history"

For Airtable Persistent Memory:
- Create table: user_id, message, timestamp, role
- Query before AI to get history
- Save after AI response
```

### Teaching Strategy

**Start with a Story (5 min)**:
```
"Imagine meeting someone who forgets everything after 5 minutes.
That's AI without memory. Now imagine someone who remembers 
everything you've ever said. That's buffer memory. 
A good assistant remembers important stuff - that's smart memory!"
```

**Demo All Three Types (15 min)**:
- Show workflow with NO memory
- Add buffer memory - see improvement
- Add window memory - explain trade-offs
- Show summary memory (optional, advanced)

**Build Exercise (20 min)**:
- Start with simple chat
- Add window buffer memory
- Test the test conversation from exercise
- Observe memory in action

### Common Issues

**Issue**: "Memory doesn't persist across browser refreshes"
```
Solution:
- Explain: Window memory is session-based
- For persistent: Use Airtable/Notion
- Show how to implement database memory
```

**Issue**: "Agent remembers too much / too little"
```
Solution:
- Adjust window size
- Explain context window limits
- Discuss when to summarize
```

### Real-World Memory Examples
- Customer history in support
- User preferences in shopping
- Previous conversations with clients
- Project context in meetings

---

## Exercise 5: Multi-Step Content Generator

### Complete Solution

**Full Workflow visual**:
```
Webhook (topic)
    ↓
AI #1: Title Generator
    ↓
AI #2: Subtopic Generator (uses title)
    ↓
AI #3: Introduction Writer (uses title + subtopics)
    ↓
Merge node (combines all)
    ↓
Email OR Google Docs
```

**Prompts**:
```
Title Generator:
"Create a compelling, SEO-friendly blog post title about: {{topic}}.
Make it under 60 characters."

Subtopic Generator:
"For this blog post: {{title}}
List exactly 3 main subtopics to cover. Format as numbered list."

Introduction Writer:
"Write an engaging 100-word introduction for:
Title: {{title}}
Subtopics: {{subtopics}}
Make it conversational and hook the reader."
```

###Teaching Strategy

**Visual First (10 min)**:
- Draw the workflow on whiteboard
- Show how data flows
- Explain " chaining" concept
- Relate to assembly line

**Build Step-by-Step (30 min)**:
- Node 1: Get input
- Test it
- Node 2: Generate title
- Test it (see the title!)
- Node 3: Generate subtopics
- Test it (see them appear!)
- Node 4: Write intro
- Test it
- Finally: Merge and send

**Key Teaching Point**:
"Each step uses the output from previous steps.
That's chaining! This is how complex AI workflows work."

### Common Issues

**Issue**: "AI #2 doesn't see the title from AI #1"
```
Solution:
- Show the expression: {{ $("Title Generator").first().json.output }}
- Explain: This references previous node's output
- Practice selecting data from previous nodes
```

**Issue**: "The final output is messy"
```
Solution:
- Add a "Format" node (Set node)
- Create a structured output template
- Show markdown formatting
```

### Extension Ideas
- Add image generation
- Include SEO keywords
- Create multiple versions
- A/B test titles
- Auto-publish to WordPress

---

## General Teaching Tips

### For Different Learning Styles:

**Visual Learners**:
- Use lots of diagrams
- Draw workflows before building
- Use colors for different node types

**Auditory Learners**:
- Explain concepts verbally first
- Have them explain back to you
- Discuss analogies

**Kinesthetic Learners**:
- Let them build ASAP
- Encourage experimentation
- "Break it and fix it" exercises

### Pacing

**Too Fast**: Students look confused, not clicking along
**Too Slow**: Students look bored, building ahead
**Just Right**: Nodding, asking questions, building together

### Assessment Without Pressure

Instead of "Did you finish?":
- "What did you learn?"
- "What was surprising?"
- "What would you change?"
- "How could you use this at work?"

### Building Confidence

Celebrate:
- ✅ First node added
- ✅ First connection made
- ✅ First workflow executed
- ✅ First error resolved
- ✅ First creative modification

### Red Flags (Students Struggling)

- Not clicking along
- Lots of "uh-huh" without understanding
- Rushing without testing
- Getting frustrated

**Interventions**:
- Slow down
- Check screen share is clear
- Pair them with confident peer
- One-on-one breakout

---

## Bridging to Technical Team

Help them understand code concepts:
- **Nodes** = Functions in code
- **Connections** = Data flow in code
- **Expressions** = Variables in code
- **Workflows** = Programs/scripts

Encourage collaboration:
- "Your n8n workflow IS a spec for developers!"
- "You can prototype, they can optimize"
- "Same concepts, different tools"

---

## Success Metrics

By end of Unit 1, students should:
- ✅ Build simple workflows independently
- ✅ Connect 3+ nodes together
- ✅ Test and debug basic issues
- ✅ Explain what agents, tools, and memory are
- ✅ Feel confident to experiment

---

## Resources for Instructors

**Prepared Materials Needed**:
- [ ] n8n instance ready for demo
- [ ] Ollama running and tested
- [ ] Example workflows loaded
- [ ] Test accounts (Slack, email, etc.)
- [ ] Troubleshooting cheat sheet

**Backup Plans**:
- If Ollama fails: Use OpenAI temporarily
- If n8n cloud is down: Use desktop version
- If internet is slow: Prepare offline examples

---

**Estimated Teaching Time**: 
- Lecture: 2 hours
- Hands-on: 4-6 hours
- Q&A: 1 hour
- Total: ~8 hours for Unit 1

**Recommended Class Size**: 5-15 students
**Ideal Format**: Hybrid (some together, some practice alone)

---

## Appendix: Example Workflows

### Example 1: Complete Chatbot with Memory
[Detailed JSON export would go here]

### Example 2: Email Classifier
[Detailed JSON export would go here]

### Example 3: Meeting Notes Processor
[Detailed JSON export would go here]

---

**Next**: Progress to Unit 2 (Environment Mastery)

**Remember**: The goal is confidence and understanding, not perfection. Non-technical doesn't mean non-capable! 🎨🤖
