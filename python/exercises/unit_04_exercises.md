# Unit 4: Introduction to LangGraph - Exercises

## Learning Objectives
- Build stateful workflows with LangGraph
- Implement conditional routing
- Create cyclic graphs
- Integrate LLMs in graph nodes

---

## Exercise 1: Simple State Machine (Beginner)

**Objective**: Create your first LangGraph state machine.

**Tasks**:
Build a simple order processing workflow:
1. States: received → validated → processed → shipped
2. Each state updates a status message
3. Track timestamps for each state

**State Schema**:
```python
class OrderState(TypedDict):
    order_id: str
    status: str
    timestamps: Annotated[list, operator.add]
    messages: Annotated[list, operator.add]
```

**Expected Output**:
```
Order #12345 Processing:
  [10:00:00] Received
  [10:00:01] Validated
  [10:00:02] Processed
  [10:00:03] Shipped
Status: Complete
```

---

## Exercise 2: Conditional Routing Challenge (Intermediate)

**Objective**: Implement complex conditional logic.

**Tasks**:
Build a content moderation system:
1. Input: user-generated content
2. Check for:
   - Explicit language → flag_explicit
   - Spam patterns → flag_spam
   - Normal content → approve
3. Flagged content goes through review
4. Approved content is published

**Routing Logic**:
```
check_content → (explicit | spam | clean)
  ├─ explicit → review → (approve | reject)
  ├─ spam → review → (approve | reject)
  └─ clean → publish
```

---

## Exercise 3: Loop-Based Iteration (Intermediate)

**Objective**: Build a graph with controlled loops.

**Tasks**:
Create a "learning loop" that:
1. Presents a problem
2. Gets student answer
3. Checks if correct
4. If wrong, provides hint and loops back (max 3 attempts)
5. If correct or max attempts reached, moves to next problem

**Test with math problems**:
```
Problem 1: What is 7 * 8?
Problem 2: What is sqrt(144)?
Problem 3: What is 15 + 27?
```

---

## Exercise 4: Multi-Step Reasoning Graph (Advanced)

**Objective**: Build a sophisticated reasoning workflow.

**Tasks**:
Create a research assistant that:
1. Takes a complex question
2. Breaks it into sub-questions (planning)
3. Researches each sub-question
4. Checks if answer is sufficient
   - If yes → synthesize final answer
   - If no → generate more sub-questions (loop)
5. Returns comprehensive answer with sources

**Max iterations**: 3 research loops

---

## Exercise 5: Parallel Execution (Advanced)

**Objective**: Implement parallel node execution.

**Tasks**:
Build a document analyzer that processes a document through parallel paths:
1. Branch into 3 parallel analyses:
   - Sentiment analysis
   - Key entity extraction
   - Summary generation
2. Merge results
3. Generate final report

**Hint**: Use `add_edge` from multiple nodes to a merger node

---

## Exercise 6: Human-in-the-Loop Workflow (Advanced)

**Objective**: Implement approval workflows.

**Tasks**:
Create an email drafting assistant:
1. Generate email draft based on user intent
2. **Interrupt** for user review
3. User can:
   - Approve → send (simulate)
   - Request changes → regenerate with feedback
   - Reject → abort
4. Track revision history

**Bonus**: Implement multi-step approval (manager + legal team)

---

## Exercise 7: Error Handling and Recovery (Advanced)

**Objective**: Build robust graphs with error handling.

**Tasks**:
1. Create a workflow that can fail at any node
2. Implement:
   - Try-catch in nodes
   - Retry logic (max 3 retries)
   - Fallback paths
   - Error logging
3. Test with intentionally failing nodes

**Scenario**: API call workflow that might timeout

---

## Challenge Project: Multi-Agent Task Planner

**Objective**: Build a complete task planning and execution system.

**Requirements**:
Create a system that:
1. Takes a complex project task (e.g., "Plan a conference")
2. Breaks it into subtasks
3. Assigns each subtask to a specialized "agent" (node)
4. Routes based on task type:
   - Budget tasks → budget_planner
   - Scheduling → schedule_manager
   - Communications → communication_agent
5. Tracks completion status
6. Handles dependencies (task B needs task A completed)
7. Generates progress reports
8. Allows re-planning if tasks fail

**State Schema**:
```python
class ProjectState(TypedDict):
    project_name: str
    tasks: list[Task]
    completed_tasks: list[str]
    current_task: Optional[Task]
    status: str
    messages: Annotated[list, operator.add]
```

**Testing**:
- Test with multi-step projects
- Simulate task failures
- Test dependency handling

**Bonus Features**:
- Visual graph representation (use mermaid or graphviz)
- Persistence (save/load state)
- Time estimation for tasks
- Resource allocation

---

## Debugging Exercise: Fix the Broken Graph

**Objective**: Debug common LangGraph issues.

**Provided**: A broken graph with multiple issues:
- Infinite loops
- Missing state updates
- Incorrect edge conditions
- State type mismatches

**Tasks**:
1. Identify all issues
2. Fix them
3. Add proper validation
4. Explain what was wrong

---

## Performance Exercise: Graph Optimization

**Objective**: Optimize graph execution.

**Tasks**:
1. Create a graph with 10+ nodes
2. Profile execution time
3. Identify bottlenecks
4. Optimize by:
   - Parallelizing independent nodes
   - Caching results
   - Reducing LLM calls
5. Measure improvement

**Goal**: 50%+ performance improvement

---

**Estimated Time**: 10-12 hours
**Prerequisites**: Units 1-3 completed  
**Key Concepts**: States, Nodes, Edges, Conditionals, Loops
