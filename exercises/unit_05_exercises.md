# Unit 5: Advanced LangGraph Patterns - Exercises

## Learning Objectives
- Implement tool calling in LangGraph agents
- Build multi-agent collaborative systems
- Create human-in-the-loop workflows
- Add persistence and state management
- Handle errors gracefully

---

## Exercise 1: Tool-Enabled Agent (Intermediate) ⭐⭐

**Objective**: Build a LangGraph agent that can use multiple tools.

**Tasks**:
1. Create 3 tools:
   - `web_search(query: str)` - Simulated web search
   - `calculator(expression: str)` - Mathematical calculations
   - `get_weather(city: str)` - Simulated weather data

2. Build a LangGraph agent that:
   - Receives a question
   - Decides which tool(s) to use
   - Executes the tool
   - Formulates answer with tool results

**Test Questions**:
```python
questions = [
    "What is 15 * 24?",  # Should use calculator
    "What's the weather in Tokyo?",  # Should use weather
    "Search for information about LangGraph",  # Should use search
    "What is the square root of 144 plus the temperature in London?"  # Multiple tools!
]
```

**State Schema**:
```python
class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    question: str
    tool_calls: list
    final_answer: str
```

**Success Criteria**:
- ✅ Agent correctly chooses appropriate tools
- ✅ Handles single and multiple tool calls
- ✅ Provides coherent final answers
- ✅ Logs which tools were used

---

## Exercise 2: Multi-Agent Collaboration (Advanced) ⭐⭐⭐

**Objective**: Build a system where multiple specialized agents work together.

**Scenario**: Content Creation Team

**Agents to Build**:
1. **Researcher Agent** - Gathers information
2. **Writer Agent** - Creates content
3. **Editor Agent** - Reviews and improves
4. **Fact-Checker Agent** - Verifies accuracy

**Workflow**:
```
Topic Input
    ↓
Researcher (gathers facts)
    ↓
Writer (creates draft)
    ↓
Fact-Checker (verifies claims)
    ↓
[IF issues found] → Writer (revise) → Fact-Checker again
[IF no issues] → Editor (polish)
    ↓
Final Content
```

**Requirements**:
- Each agent has specific personality/instructions
- Agents pass work to each other
- Implement at least one feedback loop
- Track which agent did what

**Test Topic**: "The benefits of AI agents in software development"

---

## Exercise 3: Human-in-the-Loop Workflow (Advanced) ⭐⭐⭐

**Objective**: Implement approval workflows with human checkpoints.

**Scenario**: Social Media Post Approval System

**Workflow**:
```
Topic → Draft Post → [HUMAN APPROVAL] → Publish

If rejected:
→ Get Feedback → Revise → [HUMAN APPROVAL] again
```

**Implementation**:
1. Use LangGraph's interrupt capability
2. Create approval checkpoint
3. Handle approve/reject/request changes
4. Track revision history
5. Implement max 3 revision attempts

**State Schema**:
```python
class PostState(TypedDict):
    topic: str
    draft: str
    status: str  # draft, pending_approval, approved, rejected
    feedback: str
    revision_count: int
    history: Annotated[list, operator.add]
```

**Testing**:
- Simulate both approval and rejection scenarios
- Test multiple revision cycles
- Verify max attempts limit works

---

## Exercise 4: Persistent Agent State (Advanced) ⭐⭐⭐

**Objective**: Implement state persistence across sessions.

**Tasks**:
1. Build an agent that tracks conversation history
2. Use **SQLite** or **file-based** persistence
3. Implement:
   - Save state after each interaction
   - Load state when resuming
   - List all past conversations
   - Continue from specific conversation

**Features**:
```python
agent.start_conversation(user_id="alice")
agent.chat("Hello!")
agent.save_state()

# Later...
agent.load_state(user_id="alice")
agent.chat("Remember me?")  # Should remember previous context
```

**Bonus**: Implement state versioning (snapshots at key points)

---

## Exercise 5: ReAct Pattern Implementation (Advanced) ⭐⭐⭐

**Objective**: Build a proper ReAct (Reasoning + Acting) agent.

**The ReAct Loop**:
```
1. THOUGHT: "I need to find information about X"
2. ACTION: Use search tool
3. OBSERVATION: [Search results]
4. THOUGHT: "This answers part of it, but I need Y too"
5. ACTION: Use another tool
6. OBSERVATION: [More results]
7. THOUGHT: "Now I have enough to answer"
8. FINAL ANSWER: [Synthesized response]
```

**Implementation**:
- Agent thinks before each action
- Logs reasoning steps
- Can chain multiple actions
- Knows when to stop (has enough info)

**Test Scenario**:
```
Question: "What's the weather in the capital of France, and is it a good day for tourism?"

Expected Flow:
1. THOUGHT: "Need to know capital of France"
2. ACTION: Search "capital of France"
3. OBSERVATION: "Paris"
4. THOUGHT: "Now need weather in Paris"
5. ACTION: Get weather for Paris
6. OBSERVATION: "22°C, sunny"
7. THOUGHT: "This is good tourism weather"
8. FINAL: "Paris is 22°C and sunny - excellent for tourism!"
```

---

## Exercise 6: Error Handling and Recovery (Intermediate) ⭐⭐

**Objective**: Build robust agents that handle failures gracefully.

**Scenarios to Handle**:
1. Tool execution fails
2. LLM returns invalid format
3. Network timeout
4. Resource not available
5. Max retries exceeded

**Implementation**:
```python
class RobustAgentState(TypedDict):
    task: str
    attempts: int
    max_attempts: int
    errors: Annotated[list, operator.add]
    fallback_used: bool
    result: str
```

**Requirements**:
- Try-catch in tool nodes
- Retry logic (exponential backoff)
- Fallback strategies
- Error logging
- Graceful degradation

**Test**:
- Intentionally fail tools
- Verify retry mechanism
- Check fallback is used
- Ensure errors are logged

---

## Exercise 7: Dynamic Workflow Generation (Expert) ⭐⭐⭐⭐

**Objective**: Build an agent that creates its own workflow based on the task.

**Concept**:
```
Complex Task → AI Plans Steps → AI Generates Workflow → Execute
```

**Example**:
```
Task: "Analyze competitor websites and create a report"

AI Planning:
1. Determine which competitors
2. Visit each website
3. Extract key information
4. Compare features
5. Generate report

AI generates and executes this workflow dynamically!
```

**Implementation Hints**:
- Use LLM to generate step list
- Dynamically create graph nodes
- Execute generated workflow
- Handle variable number of steps

---

## Exercise 8: Supervisor Pattern (Advanced) ⭐⭐⭐

**Objective**: Implement a supervisor agent that delegates to worker agents.

**Architecture**:
```
User Request
    ↓
Supervisor Agent (decides which worker to use)
    ↓
  ├─ Worker Agent 1 (Code tasks)
  ├─ Worker Agent 2 (Writing tasks)
  ├─ Worker Agent 3 (Data tasks)
  └─ Worker Agent 4 (Research tasks)
    ↓
Supervisor (aggregates results)
    ↓
Final Response
```

**Requirements**:
- Supervisor analyzes request
- Routes to appropriate worker(s)
- Can use multiple workers
- Synthesizes results
- Returns cohesive answer

**Test Requests**:
```
1. "Write a Python function to calculate fibonacci"  → Code worker
2. "Research the history of AI"  → Research worker
3. "Analyze this dataset and write a summary"  → Data + Writing workers
```

---

## Challenge Project: Autonomous Research Agent (Expert) ⭐⭐⭐⭐

**Objective**: Build a fully autonomous research agent.

**Capabilities**:
1. **Self-Planning**: Creates own research plan
2. **Tool Selection**: Chooses appropriate tools
3. **Iterative Research**: Keeps searching until satisfied
4. **Self-Evaluation**: Checks if answer is complete
5. **Source Citation**: Tracks all sources used
6. **Report Generation**: Creates formatted report

**Workflow**:
```
Research Question
    ↓
Plan Research Steps
    ↓
Execute Step 1 → Evaluate (enough?) → [NO] → Execute Step 2 → ...
            ↓ [YES]
    Synthesize Findings
            ↓
    Verify Completeness
            ↓
    Generate Report with Citations
```

**Requirements**:
- At least 3 research tools (search, scrape, database)
- Maximum 5 research iterations
- Quality threshold for completion
- Structured output format
- Full source attribution

**Test Question**:
"What are the key differences between LangChain and LangGraph, and when should each be used?"

**Expected Output**:
```markdown
# Research Report: LangChain vs LangGraph

## Summary
[2-3 sentence overview]

## Key Differences
1. [Difference with source]
2. [Difference with source]
...

## Use Cases
LangChain: [scenarios with sources]
LangGraph: [scenarios with sources]

## Recommendations
[When to use each]

## Sources
1. [URL/Source 1]
2. [URL/Source 2]
...

## Research Process
- Iterations: 3
- Tools used: search (2x), documentation_lookup (3x)
- Confidence: High
```

---

## Submission Guidelines

For each exercise:
1. **Code**: Complete, working implementation
2. **Tests**: Demonstrate all requirements
3. **Documentation**: 
   - How to run
   - Example outputs
   - Design decisions
4. **Reflection**:
   - What was challenging?
   - What did you learn?
   - How could it be improved?

---

## Evaluation Criteria

| Criteria | Weight | Description |
|----------|--------|-------------|
| **Functionality** | 40% | Does it work as specified? |
| **Code Quality** | 20% | Clean, readable, well-structured? |
| **Error Handling** | 15% | Robust and graceful? |
| **Documentation** | 10% | Clear and complete? |
| **Creativity** | 15% | Interesting extensions? |

---

## Common Challenges & Tips

### Challenge 1: Tool Calling Complexity
**Tip**: Start with one tool, test thoroughly, then add more

### Challenge 2: State Management
**Tip**: Keep state schema simple, add complexity gradually

### Challenge 3: Human-in-the-Loop
**Tip**: Use `interrupt` carefully, test resume logic

### Challenge 4: Multi-Agent Coordination
**Tip**: Define clear handoff points, log all transitions

### Challenge 5: Error Handling
**Tip**: Think about failure modes upfront, test them explicitly

---

## Resources

- **LangGraph Docs**: https://langchain-ai.github.io/langgraph/
- **ReAct Paper**: https://arxiv.org/abs/2210.03629
- **Multi-Agent Examples**: LangGraph documentation
- **Persistence Guide**: LangGraph checkpointing docs

---

**Estimated Time**: 15-20 hours for all exercises  
**Difficulty**: Intermediate to Expert  
**Prerequisites**: Units 1-4 completed, solid LangGraph understanding

**This is where it gets really interesting! 🚀**
