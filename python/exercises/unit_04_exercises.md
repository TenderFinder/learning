# Unit 4: Introduction to LangGraph - Exercises

## Learning Objectives
- Build stateful workflows with LangGraph
- Implement conditional routing
- Create cyclic graphs
- Integrate LLMs in graph nodes

---

## Exercise 1: Simple State Machine (Beginner)

**Objective**: Create your first LangGraph state machine.

**What You'll Build**:
A linear workflow tracking an order status with timestamps.

**Steps**:
1. **Define State**:
   - `class OrderState(TypedDict)`:
     - `order_id`: str
     - `status`: str
     - `timestamps`: Annotated[list, operator.add]
     - `messages`: Annotated[list, add_messages]

2. **Define Nodes**:
   - Python functions that take `OrderState` and return a dictionary of updates.
   - `received(state)`: returns `{"status": "Received", "timestamps": [now()]}`.
   - `validated(state)`: returns `{"status": "Validated", ...}`.
   - `processed(state)`: ...
   - `shipped(state)`: ...

3. **Build Graph**:
   - `builder = StateGraph(OrderState)`
   - `builder.add_node("received", received)`
   - ... repeat for all.

4. **Add Edges**:
   - `builder.set_entry_point("received")`
   - `builder.add_edge("received", "validated")`
   - `builder.add_edge("validated", "processed")`
   - ...
   - `builder.add_edge("shipped", END)`

5. **Run**:
   - `graph = builder.compile()`
   - `graph.invoke({"order_id": "123", "timestamps": [], "messages": []})`

**Expected Output**:
```
Order #12345 Processing:
  [10:00:00] Received
  [10:00:01] Validated
  ...
Status: Complete
```

---

## Exercise 2: Conditional Routing Challenge (Intermediate)

**Objective**: Implement complex conditional logic.

**What You'll Build**:
A content moderation workflow that routes inputs based on content analysis.

**Steps**:
1. **Define State**:
   - `content`: str
   - `classification`: str
   - `status`: str

2. **Define Nodes**:
   - `classify_content(state)`: Returns `{"classification": "spam" | "explicit" | "clean"}`.
   - `human_review_node(state)`: Returns `{"status": "approved" | "rejected"}`.
   - `publish_node(state)`: Returns `{"status": "published"}`.

3. **Define Router**:
   - Function `route_content(state)`:
     - if classification == "clean" return "publish"
     - else return "review"

4. **Build Graph**:
   - Add nodes: `classify`, `review`, `publish`.
   - Entry: `classify`.
   - Conditional Edge:
     - `builder.add_conditional_edges("classify", route_content, {"publish": "publish", "review": "review"})`.
   - Normal Edges:
     - `review` -> END (or publish).
     - `publish` -> END.

5. **Test**:
   - Input: "Buy cheap meds now!" -> Should go to review.
   - Input: "Hello world" -> Should go to publish.

---

## Exercise 3: Loop-Based Iteration (Intermediate)

**Objective**: Build a graph with controlled loops.

**What You'll Build**:
A math tutor that gives you 3 tries to solve a problem.

**Steps**:
1. **Define State**:
   - `problem`: str
   - `answer`: str
   - `attempts`: int
   - `solved`: bool

2. **Nodes**:
   - `present_problem`: Prints problem (if attempts==0).
   - `evaluate_answer`: Checks answer. Returns `{"solved": True/False, "attempts": state["attempts"] + 1}`.

3. **Router**:
   - `check_progress(state)`:
     - If `solved`: return "end"
     - If `attempts` >= 3: return "end" (failed)
     - Else: return "retry"

4. **Graph Construction**:
   - Nodes: `ask` (Entry), `evaluate`.
   - Edge: `ask` -> `evaluate`.
   - Conditional Edge from `evaluate`:
     - `check_progress` -> {"retry": "ask", "end": END}.

5. **Execution**:
   - Manually simulate "user input" inside the `evaluate` node for this exercise (or use `input()` function).

**Expected Output**:
```
Problem: 7 * 8?
Attempt 1: 54 (Wrong)
Attempt 2: 56 (Correct)
Transitions: ask -> eval -> ask -> eval -> END.
```

---

## Exercise 4: Multi-Step Reasoning Graph (Advanced)

**Objective**: Build a sophisticated reasoning workflow.

**What You'll Build**:
A "Plan-and-Execute" style agent that researches complex topics.

**Steps**:
1. **State**:
   - `question`: str
   - `plan`: list[str] (steps)
   - `current_step`: int
   - `findings`: list[str]

2. **Planner Node**:
   - Uses LLM to generate a list of steps for the `question`.
   - Update `plan` in state.

3. **Executor Node**:
   - Takes `plan[current_step]`.
   - Simulates research (or uses a tool).
   - Updates `findings`.
   - Increments `current_step`.

4. **Router**:
   - If `current_step` < `len(plan)`: return "continue".
   - Else: return "synthesize".

5. **Synthesizer Node**:
   - Uses LLM to combine `findings` into final answer.

6. **Graph**:
   - `planner` -> `executor` -> (conditional) -> `synthesizer` -> END.
   - The conditional edge loops back to `executor` if "continue".

**Result**: A powerful agent that breaks down "Who is the CEO of the company that made ChatGPT?" into [Find Company -> OpenAI, Find CEO -> Sam Altman].

---

## Exercise 5: Parallel Execution (Advanced)

**Objective**: Implement parallel node execution.

**What You'll Build**:
A document analyzer that processes text through 3 independent paths simultaneously.

**Steps**:
1. **State**: `doc_text`, `sentiment`, `entities`, `summary`.
2. **Nodes**:
   - `analyze_sentiment`: Updates `sentiment` key.
   - `extract_entities`: Updates `entities` key.
   - `summarize_text`: Updates `summary` key.
3. **Graph Construction**:
   - `builder.add_node("sentiment", analyze_sentiment)`
   - `builder.add_node("entities", extract_entities)`
   - `builder.add_node("summary", summarize_text)`
   - Entry point: A dummy start node or directly branch from start?
   - *Better pattern*: Start node -> (Fan out) -> all 3 nodes.
   - Edges: `start` -> `sentiment`, `start` -> `entities`, `start` -> `summary`.
   - All 3 nodes -> `end_node` (Fan in).
4. **Execution**:
   - Verify that all 3 keys in state are populated after run.
   - Note: LangGraph executes parallel branches automatically.

**Expected Output**:
```
Running parallel nodes...
Validating state:
 - Sentiment: Positive
 - Entities: [Google, AI]
 - Summary: "The text discusses..."
Success!
```

---

## Exercise 6: Human-in-the-Loop Workflow (Advanced)

**Objective**: Integrate human approval steps.

**What You'll Build**:
A tweet generator that requires human approval before "posting".

**Steps**:
1. **State**: `topic`, `tweet_draft`, `feedback`.
2. **Nodes**:
   - `generate_tweet`: LLM writes draft.
   - `human_approval`: (No-op node, or just the checkpointer boundary).
   - `post_tweet`: Print "Posted!".

3. **Graph with Checkpoint**:
   - Enable checkpointing: `memory = MemorySaver()`.
   - `graph = builder.compile(checkpointer=memory, interrupt_before=["post_tweet"])`.

4. **Execution Flow**:
   - Run graph with configuration `{"configurable": {"thread_id": "1"}}`.
   - It stops before `post_tweet`.
   - **User Action**: Inspect state `graph.get_state(config)`.
   - **Decision**:
     - If approving: `graph.invoke(None, config)` to continue.
     - If rejecting: `graph.update_state(config, {"feedback": "Too long!"})` then invoke to rerun generation.

**visualize**:
- Use `print(graph.get_graph().draw_ascii())`.

---

## Challenge Project: Build an RPG Game Engine

**Objective**: Create a text-based RPG using a State Graph.

**What You'll Build**:
A dungeon crawler where each room is a node and player choices determine the path.

**Steps**:
1. **State**:
   - `player_hp`: int
   - `inventory`: list
   - `location`: str
   - `last_message`: str

2. **Room Nodes**:
   - Define functions for `entrance`, `hallway`, `treasure_room`, `monster_room`.
   - Each node should return a description and update state (e.g., add item).

3. **Conditional Logic (The Map)**:
   - Create a router function `parse_command(state)` that looks at `last_message` (user input).
   - Map: "north" -> `hallway`, "fight" -> `combat_graph`.

4. **Combat Subgraph** (Bonus):
   - A separate graph for fighting logic (Player Attack -> Enemy Attack -> Loop).
   - Call this subgraph from the `monster_room`.

5. **Loop**:
   - Use a `while` loop in Python to take `input()` and update the state, driving the graph forward 1 step at a time.

**Success Criteria**:
- ✅ Player can move between rooms (Graph traversal).
- ✅ State persists (Inventory items kept).
- ✅ Game logic handles "Game Over" (HP <= 0).

---

## Debugging Exercise: Fix the Broken Graph

**Objective**: Debug common LangGraph issues.

**Provided**: A broken graph script (you create it) with:
- An infinite loop (Node A -> Node B -> Node A).
- A state value that gets overwritten incorrectly.

**Tasks**:
1. Run the graph and observe the `RecursionLimitError`.
2. Fix the loop by adding a logic check or max steps.
3. Fix the state overwrites by changing the reducer to `add_messages` or `operator.add`? (Depends on intent). (Hint: If it's a list, use a reducer!).

---

**Estimated Time**: 10-12 hours
**Prerequisites**: Units 1-3 completed
**Key Concepts**: States, Nodes, Edges, Conditionals, Loops, Checkpointing
