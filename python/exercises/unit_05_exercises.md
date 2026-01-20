# Unit 5: Advanced LangGraph Patterns - Exercises

## Learning Objectives
- Implement tool calling in LangGraph agents
- Build multi-agent collaborative systems
- Create human-in-the-loop workflows with state modification
- Add persistence and state management
- Handle errors gracefully

---

## Exercise 1: Tool-Enabled Agent (Intermediate)

**Objective**: Build a LangGraph agent that can use multiple tools.

**What You'll Build**:
A "ReAct" style agent using LangGraph's prebuilt components or custom logic.

**Steps**:
1. **Define Tools**:
   - Create `def calculator(query: str)` decorated with `@tool`.
   - Create `def weather(city: str)` decorated with `@tool`.
   - Bind them to the model: `model.bind_tools([calculator, weather])`.

2. **Define State**:
   - `class AgentState(TypedDict):`
     - `messages`: Annotated[list, add_messages] (Import `add_messages` from `langgraph.graph.message`)

3. **Define Nodes**:
   - `agent_node(state)`: Calls `model.invoke(state["messages"])`.
   - `tool_node`: Use the prebuilt `ToolNode` from `langgraph.prebuilt`.
     - `tools = [calculator, weather]`
     - `tool_node = ToolNode(tools)`

4. **Define Router**:
   - Use `tools_condition` from `langgraph.prebuilt`.
   - This checks if the last message has `tool_calls`.

5. **Build Graph**:
   - `builder.add_node("agent", agent_node)`
   - `builder.add_node("tools", tool_node)`
   - Edges:
     - `agent` -> (conditional `tools_condition`) -> `tools` OR END.
     - `tools` -> `agent` (Loop back to reason about the result).

6. **Test**:
   - "What is 123 * 45?" (Should call calc).
   - "Hi" (Should just answer).

**Expected Output**:
```
User: Calculate 5 * 5
Agent: [Call: calculator(5*5)]
Tool: 25
Agent: The result is 25.
```

---

## Exercise 2: Multi-Agent Collaboration (Advanced)

**Objective**: Build a system where multiple specialized agents work together.

**What You'll Build**:
A research team consisting of a "Researcher" and a "Writer".

**Steps**:
1. **Define Agents**:
   - Create a helper function `create_agent(llm, tools, system_prompt)`.
   - It returns a node that calls the LLM and formats the output.

2. **Define State**:
   - `messages`: Annotated[list, add_messages]
   - `next`: str (Tracks who speaks next)

3. **Researcher Node**:
   - Has `Tavily` or `simulated_search` tool.
   - System Prompt: "You are a researcher. Search for facts. If done, say 'FINISHED'."

4. **Writer Node**:
   - Has no tools.
   - System Prompt: "You are a writer. Summarize the researcher's findings."

5. **Supervisor / Router**:
   - Or use a "hand-off" pattern:
     - If Researcher says "FINISHED", route to Writer.
     - If Writer says "FINISHED", route to END.
     - Else, route back to same agent (or tool).

6. **Build Graph**:
   - `builder.add_node("researcher", researcher_agent)`
   - `builder.add_node("writer", writer_agent)`
   - Logic: `entry` -> `researcher`.

**Expected Flow**:
```
User: Research "LangGraph"
Researcher: [Tool Call: Search]
Tool: [Results...]
Researcher: I found these facts... FINISHED.
Writer: Here is a summary article...
```

---

## Exercise 3: Dynamic State Modification (Advanced)

**Objective**: Allow a human to "rewrite" the memory of an agent.

**What You'll Build**:
An interview coach that simulates a conversation, but you can "rewind and fix" your answers.

**Steps**:
1. **Setup**: Simple Chat Agent (Interviewer).
2. **Checkpointing**: Use `MemorySaver`.
3. **Execution**:
   - User: "I am ready."
   - Bot: "Tell me about yourself."
   - User: "I like python." (Wait, that was weak).
4. **Modifying State**:
   - Get the current state config.
   - Use `graph.update_state(config, {"messages": [HumanMessage("I am a Senior Python Engineer...")]})`.
     - *Crucial*: To "overwrite" or "insert", you might need to treat the state update carefully (e.g., matching IDs if you want to replace, or appending if you want to add).
   - In LangGraph, `update_state` acts as if that new message simulateously happened.
5. **Replay**:
   - Invoke graph again. The Bot should respond to the *new* message.

---

## Exercise 4: Subgraphs and Hierarchical Teams (Advanced)

**Objective**: Nest a graph inside another graph.

**What You'll Build**:
A "Dev Team" graph (Coder + Tester) that is treated as a single node in a larger "Company" graph.

**Steps**:
1. **Build Subgraph (Dev Team)**:
   - Nodes: `coder`, `tester`.
   - Flow: `coder` -> `tester`. If test fails -> `coder`. If pass -> END.
   - Compile this: `dev_graph = dev_builder.compile()`.

2. **Build Parent Graph (Company)**:
   - Node: `product_manager` (LLM).
   - Node: `dev_team` (This is the `dev_graph`!).
     - *Key*: You can add a compiled graph as a node: `builder.add_node("dev_team", dev_graph)`.

3. **Execution**:
   - PM passes specs to `dev_team`.
   - `dev_team` runs its internal loop until finished.
   - Control returns to PM.

**Success**: You see the "inner loop" logs happening inside the "outer loop".

---

## Exercise 5: Persistence with Database (Advanced)

**Objective**: detailed exploration of long-term memory.

**What You'll Build**:
An agent that remembers you across server restarts using a SQLite checkpointer.

**Steps**:
1. **Setup Checkpointer**:
   - `from langgraph.checkpoint.sqlite import SqliteSaver`.
   - `conn = sqlite3.connect("memory.db", check_same_thread=False)`.
   - `memory = SqliteSaver(conn)`.

2. **Compile**:
   - `graph = builder.compile(checkpointer=memory)`.

3. **Run Session A**:
   - Config: `thread_id="session1"`.
   - "My name is Alice".

4. **Restart Script**:
   - Stop the python script.
   - Run a new script connecting to the *same* `memory.db`.
   - Use `thread_id="session1"`.
   - Ask "What is my name?".

**Expected**: It answers "Alice" because the state was loaded from SQLite.

---

## Challenge Project: Specialized Support Center

**Objective**: Build a full enterprise routing system.

**Requirements**:
1. **Triage Agent**: Classifies tickets (Billing, Tech Support, General).
2. **Billing Subgraph**:
   - Handles refunds, invoices.
   - Uses `refund_tool`.
3. **Tech Support Subgraph**:
   - Troubleshoots issues.
   - Uses `search_docs_tool`.
4. **Escalation**:
   - If Tech Support fails -> Route to "Human Manager" (HIL).
5. **Persistence**:
   - Store all tickets in SQLite.

**Deliverable**:
A working script where you can input different ticket types and see them routed and processed by the correct sub-teams.

---

**Estimated Time**: 15-20 hours for all exercises  
**Difficulty**: Intermediate to Expert  
**Prerequisites**: Units 1-4 completed, solid LangGraph understanding
