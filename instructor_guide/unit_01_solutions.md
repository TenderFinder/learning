# Unit 1: Introduction to Agentic AI - Instructor Guide & Solutions

## Overview
This guide provides complete solutions, teaching tips, and common pitfalls for Unit 1 exercises.

---

## Exercise 1: Your First Ollama Interaction

### Solution
```python
"""
Exercise 1: First Ollama Interaction
Student Name: [Instructor Example]
"""

from langchain_community.llms import Ollama

def main():
    # Initialize Ollama with llama3
    llm = Ollama(model="llama3", temperature=0.7)
    
    # Ask the question
    question = "What are the three main components of an AI agent?"
    print(f"Question: {question}\n")
    
    # Get response
    response = llm.invoke(question)
    print(f"Response: {response}")

if __name__ == "__main__":
    main()
```

### Teaching Tips
- **Common Issue**: Students forget to start Ollama server
  - Solution: Show them `ollama serve` and how to check if it's running
- **Common Issue**: Model not pulled
  - Solution: Demonstrate `ollama list` and `ollama pull llama3`
- **Discussion Point**: Ask students about the `temperature` parameter
  - Higher temp = more creative, lower temp = more deterministic

### Expected Student Challenges
1. ImportError for langchain_community
   - Solution: `pip install langchain-community`
2. Connection refused error
   - Solution: Ollama not running - start it
3. Slow first response
   - Explanation: Model loading into memory (normal)

### Extension Ideas
- Try different temperature values and compare
- Try different models (mistral, phi3)
- Format the output more nicely

---

## Exercise 2: Building Your First Tool

### Solution
```python
"""
Exercise 2: Building Custom Tools
Student Name: [Instructor Example]
"""

from langchain.agents import tool

@tool
def word_counter(text: str) -> int:
    """Counts the number of words in the given text."""
    words = text.split()
    return len(words)

@tool
def text_reverser(text: str) -> str:
    """Reverses the input text character by character."""
    return text[::-1]

@tool
def sentiment_analyzer(text: str) -> str:
    """Analyzes sentiment of text and returns positive, negative, or neutral."""
    text_lower = text.lower()
    
    positive_words = ['good', 'great', 'excellent', 'happy', 'love', 'wonderful', 'fantastic']
    negative_words = ['bad', 'terrible', 'awful', 'hate', 'horrible', 'poor', 'worst']
    
    positive_count = sum(1 for word in positive_words if word in text_lower)
    negative_count = sum(1 for word in negative_words if word in text_lower)
    
    if positive_count > negative_count:
        return "positive"
    elif negative_count > positive_count:
        return "negative"
    else:
        return "neutral"

def main():
    # Test all tools
    tools = [word_counter, text_reverser, sentiment_analyzer]
    
    test_cases = {
        word_counter: ["Hello world", "The quick brown fox jumps"],
        text_reverser: ["Hello", "Python"],
        sentiment_analyzer: ["This is great!", "This is terrible", "The sky is blue"]
    }
    
    for tool in tools:
        print(f"\n{'='*60}")
        print(f"Tool: {tool.name}")
        print(f"Description: {tool.description}")
        print(f"{'='*60}")
        
        for test_input in test_cases[tool]:
            result = tool.invoke({"text": test_input})
            print(f"\nInput: '{test_input}'")
            print(f"Output: {result}")

if __name__ == "__main__":
    main()
```

### Teaching Tips
- **Key Concept**: Tools are how agents interact with the world
- **Show them**: How to inspect tool.name and tool.description
- **Emphasize**: Importance of good docstrings (they become tool descriptions)

### Common Student Mistakes
1. Forgetting the `@tool` decorator
2. Not providing type hints (str, int, etc.)
3. Missing docstrings
4. Incorrect function signature (missing parameter)

### Grading Rubric
- ✅ All three tools implemented (60%)
- ✅ Proper @tool decorators (10%)
- ✅ Clear docstrings (10%)
- ✅ Type hints included (10%)
- ✅ Tested with examples (10%)

### Extension Ideas
- Add more sophisticated sentiment analysis
- Create a tool that chains other tools
- Add error handling for edge cases

---

## Exercise 3: Conversation Memory Challenge

### Solution
```python
"""
Exercise 3: Conversation Memory
Student Name: [Instructor Example]
"""

from langchain_community.llms import Ollama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory

def main():
    # Setup
    llm = Ollama(model="llama3", temperature=0.7)
    memory = ConversationBufferMemory()
    
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=False  # Set to True to see prompts
    )
    
    # Conversation turns
    print("="*60)
    print("Conversation with Memory")
    print("="*60)
    
    turns = [
        "Hi! My name is Sarah and I'm a data scientist.",
        "I'm interested in learning about LangGraph for building AI agents.",
        "Can you explain what makes LangGraph different from LangChain?",
        "What was my name again?",
        "What topics did we discuss so far?"
    ]
    
    for i, user_input in enumerate(turns, 1):
        print(f"\n--- Turn {i} ---")
        print(f"User: {user_input}")
        response = conversation.predict(input=user_input)
        print(f"Assistant: {response}")
    
    # Show memory
    print("\n" + "="*60)
    print("Conversation History")
    print("="*60)
    print(memory.buffer)
    
    # Bonus: Window Memory
    print("\n\n" + "="*60)
    print("Bonus: Window Memory (k=2)")
    print("="*60)
    
    window_memory = ConversationBufferWindowMemory(k=2)
    window_conversation = ConversationChain(
        llm=llm,
        memory=window_memory,
        verbose=False
    )
    
    print("\nSame conversation with window memory...")
    for i, user_input in enumerate(turns, 1):
        print(f"\nTurn {i}: {user_input[:50]}...")
        window_conversation.predict(input=user_input)
    
    print("\n--- Window Memory (only last 2 turns) ---")
    print(window_memory.buffer)

if __name__ == "__main__":
    main()
```

### Teaching Tips
- **Key Concept**: Memory is crucial for context-aware conversations
- **Demonstrate**: The difference between BufferMemory and WindowMemory
- **Discussion Point**: When to use each type of memory
  - Buffer: Small conversations, important context
  - Window: Long conversations, recent context matters most
  - Summary: Very long conversations, need condensed history

### Expected Observations
- With BufferMemory: Agent remembers everything
- With WindowMemory: Agent forgets early turns
- The assistant should correctly recall the name in turn 4

### Common Issues
1. Agent doesn't remember name
   - Likely: Model didn't parse the introduction correctly
   - Solution: More explicit prompt or different model
2. Verbose=True shows too much
   - Explain: This is good for debugging
3. Memory growing too large
   - Introduce: Summary memory as next step

### Assessment Criteria
- ✅ Uses ConversationChain correctly (20%)
- ✅ Minimum 5 conversation turns (20%)
- ✅ Includes self-introduction (20%)
- ✅ Agent recalls information correctly (20%)
- ✅ Prints conversation history (10%)
- ✅ Bonus: Window memory comparison (10%)

---

## Exercise 4: Agent Loop Simulator

### Solution
```python
"""
Exercise 4: Agent Loop Simulator
Student Name: [Instructor Example]
"""

from langchain_community.llms import Ollama
from langchain.agents import tool
import math

@tool
def calculator(expression: str) -> str:
    """
    Evaluates mathematical expressions including sqrt, +, -, *, /.
    Examples: 'sqrt(144)', '5 + 3', '10 * 2'
    """
    try:
        # Add support for sqrt
        expression = expression.replace('sqrt', 'math.sqrt')
        result = eval(expression, {"__builtins__": {}, "math": math})
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

def agent_loop(task: str):
    """Simulate Think-Act-Observe-Respond loop."""
    
    llm = Ollama(model="llama3", temperature=0.3)
    
    print("=" * 70)
    print("AGENT LOOP SIMULATION")
    print("=" * 70)
    print(f"\nTask: {task}\n")
    
    # Step 1: THINK
    print("--- Step 1: THINK ---")
    think_prompt = f"""You are an AI agent solving this task: "{task}"

Break down this task into steps. What calculations do you need to perform?
List them clearly."""
    
    thinking = llm.invoke(think_prompt)
    print(f"{thinking}\n")
    
    # Step 2: ACT (first calculation)
    print("--- Step 2: ACT (Calculate sqrt(144)) ---")
    result1 = calculator.invoke({"expression": "math.sqrt(144)"})
    print(f"Tool: calculator")
    print(f"Input: math.sqrt(144)")
    print(f"Output: {result1}\n")
    
    # Step 3: ACT (second calculation)
    print("--- Step 3: ACT (Add 5) ---")
    result2 = calculator.invoke({"expression": f"{result1} + 5"})
    print(f"Tool: calculator")
    print(f"Input: {result1} + 5")
    print(f"Output: {result2}\n")
    
    # Step 4: OBSERVE & RESPOND
    print("--- Step 4: OBSERVE & RESPOND ---")
    observe_prompt = f"""Task was: {task}

We performed these calculations:
1. sqrt(144) = {result1}
2. {result1} + 5 = {result2}

Provide a clear, final answer to the task."""
    
    final_response = llm.invoke(observe_prompt)
    print(f"{final_response}\n")
    
    print("=" * 70)
    print(f"FINAL ANSWER: {result2}")
    print("=" * 70)

def main():
    task = "Calculate the square root of 144 and then add 5 to it"
    agent_loop(task)

if __name__ == "__main__":
    main()
```

### Teaching Tips
- **Key Concept**: This is how real agents work (ReAct pattern)
- **Emphasize**: The cycle can repeat multiple times
- **Show**: How tools bridge the gap between reasoning and action
- **Discuss**: Why we need lower temperature here (0.3 vs 0.7)

### Advanced Discussion Points
1. **Why simulate when we have actual agents?**
   - Understanding the pattern helps debug real agents
   - Shows what happens "under the hood"
   
2. **Real-world complexity**
   - Multiple tool calls
   - Failed tool calls (retry logic)
   - Choosing between multiple tools

3. **ReAct Pattern**
   - This is a simplified version
   - Real ReAct has more sophisticated reasoning

### Common Challenges
1. Calculator tool not handling sqrt
   - Solution provided uses math module
2. String vs numeric operations
   - Need to convert tool outputs appropriately
3. Prompt engineering
   - Students may struggle with clear prompts

### Extension Activities
- Add more mathematical operations
- Handle failed calculations gracefully
- Let LLM decide which tools to use
- Add visualization of the loop

---

## Exercise 5: Multi-Model Comparison

### Solution
```python
"""
Exercise 5: Multi-Model Comparison
Student Name: [Instructor Example]
"""

from langchain_community.llms import Ollama
import time

def compare_models(prompt: str, models: list[str]):
    """Compare responses from multiple models."""
    
    print("=" * 70)
    print("MULTI-MODEL COMPARISON")
    print("=" * 70)
    print(f"\nPrompt: {prompt}\n")
    print("-" * 70)
    
    results = []
    
    for model_name in models:
        try:
            print(f"\nMODEL: {model_name}")
            llm = Ollama(model=model_name, temperature=0.5)
            
            start_time = time.time()
            response = llm.invoke(prompt)
            end_time = time.time()
            
            elapsed = end_time - start_time
            
            print(f"Time: {elapsed:.2f}s")
            print(f"Response: {response}")
            
            results.append({
                'model': model_name,
                'time': elapsed,
                'response': response
            })
            
        except Exception as e:
            print(f"Error: {e}")
            print(f"Make sure to pull the model: ollama pull {model_name}")
    
    # Find fastest
    if results:
        print("\n" + "=" * 70)
        fastest = min(results, key=lambda x: x['time'])
        print(f"Fastest Model: {fastest['model']} ({fastest['time']:.2f}s)")
        print("=" * 70)
    
    return results

def main():
    prompt = "Explain what an AI agent is in exactly 15 words."
    models = ["llama3", "mistral", "phi3"]
    
    results = compare_models(prompt, models)
    
    # Verify word count
    print("\n\n" + "=" * 70)
    print("Word Count Verification")
    print("=" * 70)
    
    for result in results:
        word_count = len(result['response'].split())
        match = "✅" if word_count == 15 else "❌"
        print(f"\n{result['model']}: {word_count} words {match}")

if __name__ == "__main__":
    main()
```

### Teaching Tips
- **Show**: How different models have different "personalities"
- **Discuss**: Speed vs quality trade-offs
- **Point out**: Models may not follow "exactly 15 words" instruction perfectly
  - This shows limitations of LLMs
  - Opportunity to discuss prompt engineering

### Discussion Questions
1. Which model gave the best response? Why?
2. Is the fastest model always the best choice?
3. How would you choose a model for production?

### Common Observations
- llama3: Usually good balance
- mistral: Often faster, different style
- phi3: Very fast, sometimes less detailed

---

## General Teaching Strategies for Unit 1

### Day 1: Introduction
-Start with why agents matter
- Show impressive demos
- Get students excited

### Day 2-3: Hands-on Basics
- Exercises 1-3
- Emphasize getting things working
- Troubleshoot together

### Day 4: Advanced Concepts
- Exercises 4-5
- Discuss patterns and best practices

### Day 5: Project Work
- Exercises 6-8 or Challenge Project
- Peer code reviews
- Share solutions

### Assessment Approach
- Focus on understanding over perfection
- Reward creativity and experimentation
- Provide detailed feedback on code quality
- Encourage iteration and improvement

### Common Pitfalls to Watch For
1. **Setup Issues** (60% of early problems)
   - Have a "setup party" session
   - Create a troubleshooting doc

2. **Prompt Engineering** (novice students struggle)
   - Provide templates
   - Show examples of good vs bad prompts

3. **Async Confusion** (tool calling)
   - Keep it synchronous initially
   - Introduce async later

### Success Metrics
By end of Unit 1, students should be able to:
- ✅ Connect to Ollama independently
- ✅ Create simple tools
- ✅ Implement basic memory
- ✅ Understand agent loop concept
- ✅ Debug common issues

---

**Estimated Teaching Time**: 8-10 hours (including lab time)
**Recommended Group Size**: 2-3 students per group for projects
**Prerequisites**: Basic Python knowledge
