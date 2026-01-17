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

**Tasks**:
1. Make sure Ollama is installed and running
2. Pull the `llama3` model
3. Create a Python script that:
   - Connects to Ollama
   - Asks the model: "What are the three main components of an AI agent?"
   - Prints the response

**Expected Output**:
```
Question: What are the three main components of an AI agent?
Response: [Model's explanation of agent components]
```

**Hints**:
- Use `langchain_community.llms.Ollama`
- Set temperature to 0.7 for creative responses

---

## Exercise 2: Building Your First Tool (Intermediate)

**Objective**: Create custom tools that an agent can use.

**Tasks**:
1. Create three custom tools:
   - `word_counter(text: str)` - counts words in text
   - `text_reverser(text: str)` - reverses the text
   - `sentiment_analyzer(text: str)` - returns "positive", "negative", or "neutral"
2. Test each tool with sample inputs
3. Print the tool descriptions

**Expected Output**:
```
Tool: word_counter
 Description: Counts the number of words in the given text
Testing with: "Hello world"
Result: 2 words

Tool: text_reverser
Description: Reverses the input text
Testing with: "Hello"
Result: "olleH"
```

**Hints**:
- Use the `@tool` decorator from `langchain.agents`
- Add descriptive docstrings
- For sentiment, use simple keyword matching (don't use external libraries)

---

## Exercise 3: Conversation Memory Challenge (Intermediate)

**Objective**: Implement a chatbot that remembers conversation context.

**Tasks**:
1. Create a chatbot using `ConversationChain`
2. Implement `ConversationBufferMemory`
3. Have a conversation with at least 5 turns
4. The conversation should include:
   - User introduces themselves (name, profession)
   - User asks about a topic
   - User asks a follow-up question
   - User asks "What's my name?"
   - User asks "What did we discuss?"
5. Print the conversation history at the end

**Expected Behavior**:
- The chatbot should correctly recall the user's name
- The chatbot should reference earlier parts of the conversation

**Bonus**: Try using `ConversationBufferWindowMemory` with `k=2` and observe the difference.

---

## Exercise 4: Agent Loop Simulator (Advanced)

**Objective**: Simulate the Think-Act-Observe-Respond loop of an agent.

**Tasks**:
1. Given this task: "Calculate the square root of 144 and then add 5 to it"
2. Create a function that simulates each step:
   - **Think**: Use LLM to break down the task
   - **Act**: Call appropriate tool (create a `calculator` tool)
   - **Observe**: Get the result from the tool
   - **Respond**: Use LLM to formulate final answer
3. Print each step clearly

**Expected Output**:
```
=== Agent Loop Simulation ===
Task: Calculate the square root of 144 and then add 5 to it

Step 1 - THINK:
[LLM's breakdown of the task]

Step 2 - ACT:
Using calculator tool: sqrt(144)
Result: 12

Step 3 - ACT:
Using calculator tool: 12 + 5
Result: 17

Step 4 - OBSERVE & RESPOND:
[LLM's final formatted answer]
```

**Hints**:
- You'll need to create a `calculator` tool that can handle `sqrt`, `+`, `-`, `*`, `/`
- You may need to call the tool multiple times
- Use clear prompts for the LLM

---

## Exercise 5: Multi-Model Comparison (Intermediate)

**Objective**: Compare responses from different models.

**Tasks**:
1. Pull at least 3 different models from Ollama (e.g., llama3, mistral, phi3)
2. Create a function that:
   - Takes a prompt as input
   - Queries all three models
   - Compares their responses
3. Test with this prompt: "Explain what an AI agent is in exactly 15 words."
4. Display responses side-by-side
5. Measure and compare response times

**Expected Output**:
```
Prompt: Explain what an AI agent is in exactly 15 words.

----------------------------------------
MODEL: llama3
Time: 1.23s
Response: [15-word response]

MODEL: mistral
Time: 0.95s
Response: [15-word response]

MODEL: phi3
Time: 0.87s
Response: [15-word response]

Fastest Model: phi3 (0.87s)
```

---

## Exercise 6: Use Case Implementation (Advanced)

**Objective**: Implement a complete use case for an AI agent.

**Choose ONE of the following**:

### Option A: Code Debugger Agent
Create an agent that:
- Takes buggy code as input
- Identifies the bug
- Suggests a fix
- Explains why it works

### Option B: Meeting Summarizer Agent
Create an agent that:
- Takes meeting notes/transcript as input
- Extracts key points
- Identifies action items
- Creates a summary

### Option C: Learning Assistant Agent
Create an agent that:
- Takes a complex topic as input
- Breaks it down into subtopics
- Explains each subtopic
- Suggests related resources

**Requirements**:
- Use appropriate prompt engineering
- Handle edge cases
- Provide clear, structured output
- Include at least 2 working examples

---

## Exercise 7: Feedback and Self-Improvement (Advanced)

**Objective**: Create an agent that can critque and improve its own output.

**Tasks**:
1. Create a two-step workflow:
   - Step 1: Generate a haiku about "artificial intelligence"
   - Step 2: Critique the haiku (check 5-7-5 syllable pattern)
   - Step 3: If critique finds issues, generate an improved version
2. Repeat until a valid haiku is produced (max 3 iterations)
3. Show all iterations and critiques

**Expected Output**:
```
=== Iteration 1 ===
Haiku: [First attempt]
Critique: [Issues found]

=== Iteration 2 ===
Haiku: [Second attempt]
Critique: [Issues found or "Valid!"]

Final Haiku: [Best version]
```

**Bonus**: Extend this to other forms (sonnets, limericks) or other validation criteria.

---

## Exercise 8: Tool Composition Challenge (Advanced)

**Objective**: Create complex tools by composing simpler ones.

**Tasks**:
1. Create these basic tools:
   - `fetch_random_word()` - returns a random word
   - `count_vowels(word)` - counts vowels in a word
   - `reverse_word(word)` - reverses a word
2. Create a composite workflow that:
   - Fetches 3 random words
   - Counts vowels in each
   - Reverses words with >2 vowels
   - Reports results
3. Use an LLM to provide commentary on the results

**Example workflow**:
```
Word 1: "automation" (5 vowels) -> Reversed: "noitamotua"
Word 2: "code" (2 vowels) -> Not reversed
Word 3: "intelligent" (5 vowels) -> Reversed: "tnegillentni"
```

---

## Challenge Project: Personal Assistant Agent

**Objective**: Build a complete personal assistant with multiple capabilities.

**Requirements**:
Your assistant should be able to:
1. Maintain conversation memory
2. Use at least 3 different tools:
   - Calculator
   - Date/time getter
   - Note taker (saves to file)
3. Respond to these types of requests:
   - Calculations: "What's 25 * 16?"
   - Time queries: "What time is it?"
   - Note-taking: "Remember that my meeting is tomorrow at 3pm"
   - Recall: "What meetings do I have?"
4. Have a friendly, helpful personality

**Bonus Features**:
- Save conversation history to file
- Load previous conversations on startup
- Add more tools (weather, reminders, etc.)
- Implement a simple CLI interface

**Testing Scenarios**:
```
User: Hi! My name is Alex.
Assistant: Hello Alex! How can I help you today?

User: What's 144 divided by 12?
Assistant: [Uses calculator] That's 12!

User: Remember that I have a dentist appointment on Friday
Assistant: [Saves note] Got it! I've noted your dentist appointment on Friday.

User: What was my name again?
Assistant: Your name is Alex!
```

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
