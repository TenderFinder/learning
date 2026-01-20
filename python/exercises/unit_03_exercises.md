# Unit 3: LangChain Fundamentals - Exercises

## Learning Objectives
- Master prompt templates and engineering
- Build and compose chains
- Implement different memory strategies
- Use LCEL (LangChain Expression Language)

---

## Exercise 1: Advanced Prompt Templates (Intermediate)

**Objective**: Create sophisticated prompt templates for different scenarios.

**What You'll Build**:
A few-shot classification system that learns from examples in the prompt itself.

**Steps**:
1. **Define Examples**:
   - Create a list of dictionaries:
     ```python
     examples = [
       {"input": "Python", "output": "Type: Interpreted, Use Case: Data Science"},
       {"input": "Rust", "output": "Type: Compiled, Use Case: Systems Programming"},
       ...
     ]
     ```

2. **Create Example Formatter**:
   - Use `PromptTemplate.from_template("Language: {input}\n{output}")`.

3. **Create FewShot Template**:
   - Use `FewShotPromptTemplate`:
     - `examples=examples`
     - `example_prompt=example_prompt`
     - `prefix="Classify the following programming languages based on the examples below:\n"`
     - `suffix="\nLanguage: {input}\nType:"`

4. **Test**:
   - Format with `input="JavaScript"`.
   - Verify the output string contains the examples and the new query.

5. **Connect to LLM**:
   - Chain: `few_shot_prompt | llm`.
   - Invoke with `{"input": "Kotlin"}`.

**Expected Output**:
```
Classify the following...
Language: Python...
...
Language: JavaScript
Type: Interpreted, Use Case: Web Development
```

---

## Exercise 2: Chain Composition Challenge (Advanced)

**Objective**: Build a multi-step content creation pipeline.

**What You'll Build**:
A blog post generator that plans, outlines, and writes in sequence.

**Steps**:
1. **Chain 1: Planner**:
   - Prompt: "Generate 3 subtopics for blog post about {topic}."
   - LLM: `ChatOllama`.
   - JSON Parser: `JsonOutputParser`.

2. **Chain 2: Writer (Branching)**:
   - Create a function `write_section(subtopic)`.
   - Inside: Prompt "Write a paragraph about {subtopic}".
   - Return string.

3. **Main Pipeline (LCEL)**:
   - `full_chain = (planner_chain | (lambda x: x['subtopics'][0]) | writer_chain)` (Simplified for exercise).
   - *Better approach*: Use `RunnableParallel` to write all 3 sections at once.

4. **Implementation**:
   - Input: "Cloud Computing".
   - Step A: Get subtopics ["Serverless", "Security", "AI"].
   - Step B: Generate title for "Serverless".
   - Step C: Generate outline for "Serverless".
   - Step D: Write intro.

**Expected Output**:
```
Topic: Cloud Computing
Subtopic Selected: Serverless Architecture
Title: "Going Serverless: A Guide"
Introduction: [LLM generated text...]
```

---

## Exercise 3: Memory Management Strategies (Intermediate)

**Objective**: Compare different memory management approaches using modern patterns.

**What You'll Build**:
Three different chatbots with unique memory behaviors.

**Steps**:
1. **Setup Core Chain**:
   - `prompt = ChatPromptTemplate.from_messages(...)` (System, History Placeholder, Human).
   - `runnable = prompt | llm`.

2. **Strategy 1: Full History**:
   - Wrap `runnable` with `RunnableWithMessageHistory`.
   - `get_session_history` returns a standard `InMemoryChatMessageHistory`.

3. **Strategy 2: Sliding Window (Trim)**:
   - Import `trim_messages` from `langchain_core.messages`.
   - Create a trimmer: `trimmer = trim_messages(strategy="last", token_limit=100, ...)`
   - Add to chain: `runnable_with_trim = (RunnablePassthrough.assign(history=itemgetter("history") | trimmer) | prompt | llm)`.

4. **Strategy 3: Summary Memory (Advanced)**:
   - Create a side-chain that takes `history` and produces a summary string.
   - Inject verification step: If history > 5 messages, summarize and replace older messages. (Complex logic, often done via LangGraph, but simulate here).

5. **Evaluation**:
   - Run 10 turns of conversation.
   - Check `len(history.messages)` for each strategy.

**Deliverable**:
A table showing "Messages Stored" vs "Context Recall Quality".

---

## Exercise 4: Build a Code Review Assistant (Advanced)

**Objective**: Create a practical chain-based application.

**What You'll Build**:
An automated code reviewer that outputs structured markdown.

**Steps**:
1. **Define Input Schema**:
   - `code`: The source code string.
   - `language`: "Python" / "JS".

2. **System Prompt**:
   - "You are a senior engineer. Review the following code for: 1. Bugs, 2. Performance, 3. Style."

3. **Output Structure**:
   - Define a Pydantic object `CodeReview` with fields: `bugs: list[str]`, `rating: int`, `summary: str`.
   - Use `.with_structured_output(CodeReview)`.

4. **Chain Construction**:
   - `review_chain = prompt | llm.with_structured_output(CodeReview)`.

5. **Testing**:
   - Pass in a simple buggy Python script.
   - Verify the output is a valid JSON/Object, not free text.

**Expected Output**:
```json
{
  "rating": 3,
  "bugs": ["Infinite loop in while condition", "Variable 'x' undefined"],
  "summary": "Critical issues found. Do not merge."
}
```

---

## Exercise 5: LCEL Pipeline Construction (Advanced)

**Objective**: Master LangChain Expression Language.

**What You'll Build**:
A complex pipeline using `RunnableParallel`, `RunnablePassthrough` and `RunnableLambda`.

**Steps**:
1. **Step 1**: Define a simple chain `joke_chain` ("Tell a joke about {topic}").
2. **Step 2**: Define a simple chain `fact_chain` ("Tell a fact about {topic}").
3. **Step 3**: Compose parallel execution:
   - `map_chain = RunnableParallel(joke=joke_chain, fact=fact_chain)`.
4. **Step 4**: Add a synthesis step:
   - `final_chain = map_chain | RunnableLambda(lambda x: f"Joke: {x['joke']}\nFact: {x['fact']}")`.

5. **Execute**:
   - `final_chain.invoke({"topic": "bears"})`.

**Expected Output**:
```
Joke: Why did the bear dissolve? It was polar!
Fact: Bears have excellent sense of smell.
```

---

## Exercise 6: Streaming Responses (Intermediate)

**Objective**: Implement streaming for better UX.

**What You'll Build**:
A console application that types out the AI response character-by-character.

**Steps**:
1. **Setup Chain**: Standard `prompt | llm` (do NOT use output parser for raw chunks).
2. **Stream Loop**:
   ```python
   print("AI:", end="", flush=True)
   for chunk in chain.stream({"input": "Tell me a long story"}):
       print(chunk.content, end="", flush=True)
   ```
3. **Metrics**:
   - Record `start_time`.
   - Increment `token_count` inside loop.
   - At end, print `Total Time` and `Tokens/Sec`.

**Success Criteria**:
- ✅ Text appears immediately (low Time To First Token).
- ✅ Output flows smoothly.

---

## Challenge Project: Interactive Learning Tutor

**Objective**: Build a complete tutoring application.

**What You'll Build**:
An adaptive tutor that assesses your level and teaches accordingly.

**Steps**:
1. **Assessment Phase**:
   - Ask user concepts about a topic (e.g., "What is recursion?").
   - AI evaluates answer (Beginner/Intermediate/Advanced).
   - Store level in memory.

2. **Teaching Phase**:
   - Loop:
     - AI explains a concept based on `user_level`.
     - AI asks a checking question.
     - User answers.
     - AI evaluates. If correct -> Next concept. If wrong -> Explain simpler.

3. **Architecture**:
   - Use `RunnableWithMessageHistory` to track the whole session.
   - Use distinct prompts for "Evaluator" and "Teacher" personas.

4. **Persistence**:
   - Save the conversation history to a JSON file at the end using `json.dump`.

**Example Session**:
```
Bot: Topic is Python. What is a list comprehension?
User: It's a way to make lists in one line.
Bot: Good! I'd rate you as Intermediate. Let's discuss Generators...
```

---

**Estimated Time**: 8-10 hours
**Prerequisites**: Unit 1 and 2 completed
