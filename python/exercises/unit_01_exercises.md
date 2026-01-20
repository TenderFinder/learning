# Unit 1: Introduction to Agentic AI - Exercises

## Learning Objectives
By completing these exercises, you will:
- Understand basic agent components
- Work with local LLMs via Ollama
- Implement simple tools and memory
- Explore real-world agent patterns

---

## Exercise 1: Your First Ollama Interaction (Beginner)

**Objective**: Set up Ollama and interact with a local LLM.

**What You'll Build**:
A Python script that connects to your local Ollama instance and generates a response.

**Steps**:
1. **Verify Ollama**:
   - Open your terminal.
   - Run `ollama list` to check installed models.
   - Run `ollama pull llama3` if you haven't already.

2. **Setup Python Environment**:
   - Create a file named `ex1_ollama_setup.py`.
   - Import the necessary library:
     ```python
     from langchain_ollama import ChatOllama
     ```

3. **Initialize the Model**:
   - Create an instance of `ChatOllama`.
   - Set the `model` parameter to `"llama3"`.
   - Set `temperature` to `0.7` (balances creativity and focus).

4. **Generate Response**:
   - Call the `.invoke()` method with your prompt string.
   - Store the result in a variable.
   - Print `result.content` to see the output.

**Expected Output**:
```
Question: What are the three main components of an AI agent?
Response: [Model's explanation of agent components]
```

**Hints**:
- Use `langchain_ollama.ChatOllama` (install `langchain-ollama` package)
- The `.invoke()` method returns an `AIMessage` object; access content with `.content`.

---

## Exercise 2: Building Your First Tool (Intermediate)

**Objective**: Create custom tools that an agent can use.

**What You'll Build**:
A set of Python functions decorated as tools, ready for an agent to use.

**Steps**:
1. **Setup File**:
   - Create `ex2_custom_tools.py`.
   - Import the tool decorator: `from langchain_core.tools import tool`.

2. **Create Word Counter Tool**:
   - Define a function `word_counter(text: str) -> int`.
   - Add the `@tool` decorator.
   - Write a docstring: "Counts the number of words in the given text." (Crucial for the LLM!).
   - Implement the logic: `return len(text.split())`.

3. **Create Text Reverser Tool**:
   - Define `text_reverser(text: str) -> str`.
   - decorate with `@tool`.
   - Docstring: "Reverses the input text."
   - Logic: `return text[::-1]`.

4. **Create Sentiment Analyzer Tool**:
   - Define `sentiment_analyzer(text: str) -> str`.
   - Decorate and document.
   - detailed logic: simple keyword check (e.g., if "good" in text return "positive").

5. **Test Your Tools**:
   - Main execution block:
   - Call `word_counter.invoke("Hello world")`.
   - Print the name (`tool.name`) and description (`tool.description`) of each.

**Expected Output**:
```
Tool: word_counter
 Description: Counts the number of words in the given text
Testing with: "Hello world"
Result: 2
...
```

---

## Exercise 3: Conversation Memory Challenge (Intermediate)

**Objective**: Implement a chatbot with persistent conversation memory using modern production patterns.

**What You'll Build**:
A chatbot that uses a session ID to maintain separate conversation histories for different users.

**Steps**:
1. **Imports**:
   - From `langchain_ollama` import `ChatOllama`.
   - From `langchain_core.prompts` import `ChatPromptTemplate`, `MessagesPlaceholder`.
   - From `langchain_core.runnables.history` import `RunnableWithMessageHistory`.
   - From `langchain_core.chat_history` import `InMemoryChatMessageHistory`.

2. **Define the Chain**:
   - Create a `ChatPromptTemplate` with:
     - A system message ("You are a helpful assistant").
     - `MessagesPlaceholder(variable_name="history")`.
     - A human message template ("{input}").
   - Connect it to your LLM: `chain = prompt | llm`.

3. **Add Memory**:
   - Define a store dictionary: `store = {}`.
   - Create a `get_session_history` function that returns an `InMemoryChatMessageHistory` from the store based on a `session_id`.
   - Wrap your chain: `with_message_history = RunnableWithMessageHistory(chain, get_session_history, ...)`

4. **Simulate Conversation**:
   - Define a `session_id` (e.g., "user_123").
   - Invoke the chain multiple times with the same config: `config={"configurable": {"session_id": "user_123"}}`.
   - Turn 1: "Hi, I'm Bob."
   - Turn 2: "What is my name?" (Verify it remembers).

5. **Verify Isolation**:
   - Change `session_id` to "user_456".
   - Ask "What is my name?" (Should NOT know Bob).

**Expected Behavior**:
- The chatbot correctly identifies "Bob" in the first session.
- The chatbot does not know "Bob" in the second session.

---

## Exercise 4: Agent Loop Simulator (Advanced)

**Objective**: Simulate the Think-Act-Observe-Respond loop of an agent.

**What You'll Build**:
A script that manually executes the steps an agent takes, helping you understand the internal loop.

**Steps**:
1. **Define the Task**:
   - "Calculate the square root of 144 and then add 5 to it".

2. **Step 1: THINK**:
   - Prompt the LLM: "Break down this task into steps: [Task]".
   - Print the plan.

3. **Step 2: ACT (Simulation)**:
   - Create a python function `calculator(op, val1, val2=None)`.
   - "Manually" call this function based on the plan (e.g., `calculator('sqrt', 144)`).
   - Print "Using tool: calculator..."

4. **Step 3: OBSERVE**:
   - Capture the return value of your function (e.g., `12`).
   - Print "Observation: 12".

5. **Step 4: ACT (Simulation - Part 2)**:
   - Use the previous result.
   - Call calculator: `12 + 5`.
   - Print "Observation: 17".

6. **Step 5: RESPOND**:
   - Prompt LLM: "The user asked [Task]. The tool results were 12 and 17. Formulate a final answer."
   - Print the final response.

**Expected Output**:
```
=== Agent Loop Simulation ===
Task: Calculate...
...
Step 2 - ACT:
Using calculator tool: sqrt(144)
Result: 12
...
```

---

## Exercise 5: Multi-Model Comparison (Intermediate)

**Objective**: Compare responses from different models.

**What You'll Build**:
A benchmarking script that runs the same prompt against multiple local LLMs.

**Steps**:
1. **Setup List of Models**:
   - Define a list: `["llama3", "mistral", "phi3"]`. (Ensure you have pulled them all).

2. **Define Test Function**:
   - Create `test_model(model_name, prompt)`.
   - Initialize `ChatOllama` with the specific `model_name`.
   - Start a timer (`time.time()`).
   - Invoke the model.
   - Stop timer.
   - Return response content and duration.

3. **Execution Loop**:
   - Prompt: "Explain what an AI agent is in exactly 15 words."
   - Loop through your model list.
   - Print results in a formatted table.

4. **Compare**:
   - Identify the fastest model.
   - Subjectively judge the best quality response.

**Expected Output**:
```
MODEL: llama3 | Time: 1.23s | Response: ...
MODEL: phi3   | Time: 0.87s | Response: ...
...
Fastest: phi3
```

---

## Exercise 6: Use Case Implementation (Advanced)

**Objective**: Implement a complete use case for an AI agent.

**Choose ONE Option**:

**Option A: Code Debugger**
**Steps**:
1. Define a Prompt that asks the LLM to act as a senior developer.
2. Input: A python string containing a deliberate bug (e.g., `print "hello"` in Python 3).
3. Chain: Pass code to LLM.
4. Output: specific "Bug Analysis" and "Fixed Code" sections.

**Option B: Meeting Summarizer**
**Steps**:
1. Create a dummy meeting transcript text file.
2. Define a Prompt: "Extract action items and summary from this text."
3. Chain: Load file -> Pass to LLM -> Parse output.
4. Output: Bulleted list of action items.

**Option C: Learning Assistant**
**Steps**:
1. Inputs: Topic (e.g., "Quantum Computing") and Level (e.g., "5 year old").
2. Prompt: "Explain {topic} to a {level}."
3. Chain: Inputs -> Prompt -> LLM.
4. Output: Simple explanation.

---

## Exercise 7: Feedback and Self-Improvement (Advanced)

**Objective**: Create an agent that can critique and improve its own output.

**What You'll Build**:
A loop where the AI writes a haiku, checks its syllable count (simulated or real), and rewrites it if wrong.

**Steps**:
1. **Generator Chain**:
   - Prompt: "Write a haiku about AI."
   - LLM generates 3 lines.

2. **Critique Chain**:
   - Take the generated haiku.
   - Prompt: "Check if this poem follows the 5-7-5 syllable structure. Return YES or NO and explain."

3. **Python Control Logic**:
   - Run Generator.
   - Run Critique on the output.
   - **While** Critique says "NO" (and attempts < 3):
     - Run Generator again, feeding it the Critique's explanation ("Try again, previous was wrong because...").

4. **Final Output**:
   - Print the final successful haiku and number of retries.

**Expected Output**:
```
Attempt 1: ... (Critique: Syllable count wrong)
Attempt 2: ... (Critique: Valid)
Final Haiku: ...
```

---

## Exercise 8: Tool Composition Challenge (Advanced)

**Objective**: Create complex tools by composing simpler ones.

**What You'll Build**:
A workflow that strings together multiple custom tools using LCEL.

**Steps**:
1. **Tool 1**: `fetch_random_word` (Simulate by returning a random word from a list).
2. **Tool 2**: `reverse_word(word)`.
3. **LCEL Composition**:
   - Create a RunnableLambda for tool 1.
   - Create a RunnableLambda for tool 2.
   - Chain them: `chain = tool_1 | tool_2`.
4. **Execution**:
   - Run the chain.
   - Verify the output is the reversed version of a random word.
5. **Add LLM**:
   - `full_chain = tool_1 | tool_2 | llm_commentary`.
   - Prompt: "Make a joke about this reversed word: {input}".

**Result**: A random word, reversed, and then joked about by the AI.

**Hints**:
- Use LCEL (`chain = tool_1 | tool_2`) for clean composition
- Define a `TypedDict` for passing state between tools like a pro

---

## Challenge Project: Personal Assistant Agent

**Objective**: Build a complete personal assistant with multiple capabilities.

**What You'll Build**:
A console-based assistant that remembers you, uses tools, and chatting.

**Steps**:
1. **Setup Tools**:
   - `calculator`: Python function using `eval` (safety warning!) or specific math logic.
   - `save_note`: Appends text to a `notes.txt` file.
   - `get_time`: Returns `datetime.now()`.
   - Bind these to your LLM using `.bind_tools()`.

2. **Setup Memory**:
   - Use the `RunnableWithMessageHistory` pattern from Exercise 3.

3. **The Agent Loop**:
   - **Input**: specific user query.
   - **LLM Call**: Agent decides if it needs a tool.
   - **Tool Execution**: If tool call detected, run the Python function.
   - **Response**: Feed tool output back to LLM to generate final answer.

4. **Interactive Mode**:
   - Wrap it in a `while True:` loop.
   - `input("You: ")`.
   - Print `Assistant: ...`.

5. **Test**:
   - "Hi, I'm [Name]."
   - "What is 25 * 50?"
   - "Save a note that I need milk."
   - "What time is it?"
   - "What is my name?"

**Success**: The agent handles all requests gracefully and remembers context.


---

## Submission Guidelines

For each exercise:
1. Create a Python file named `ex<number>_<description>.py`
2. Include comments explaining your approach
3. Add a docstring at the top with:
   - Your name
   - Exercise number and title
   - Brief description
4. Include example usage at the bottom of the file

## Evaluation Criteria

- **Correctness**: Does the code work as specified?
- **Code Quality**: Is it well-organized and readable?
- **Completeness**: Are all requirements met?
- **Creativity**: Did you add interesting extras?
- **Error Handling**: Does it handle edge cases?

## Additional Resources

- LangChain Documentation: https://python.langchain.com/docs/
- Ollama Documentation: https://ollama.ai/docs
- Python Typing Guide: https://docs.python.org/3/library/typing.html

---

**Estimated Time**: 6-8 hours for all exercises
**Difficulty Progression**: Beginner → Intermediate → Advanced
