============================================================
UNIT 1: Introduction to Agentic AI - Sample Code
============================================================

NOTE: Make sure Ollama is running and you have pulled the required models:
  ollama pull deepseek-r1:8b
  ollama pull llama2-uncensored
  ollama pull lama3-groq-tool-use3


============================================================
Example 1: Basic Ollama Interaction
============================================================
/Users/cnc/Documents/langgraph/python/sample_codes/unit_01_introduction.py:30: LangChainDeprecationWarning: The class `Ollama` was deprecated in LangChain 0.3.1 and will be removed in 1.0.0. An updated version of the class exists in the `langchain-ollama package and should be used instead. To use it run `pip install -U `langchain-ollama` and import as `from `langchain_ollama import OllamaLLM``.
  llm = Ollama(model="deepseek-r1:8b", temperature=0.7)

Prompt: Explain what an AI agent is in one sentence.

Response: An AI agent is a system that perceives its environment and takes optimal actions to achieve its goals.


============================================================
Example 2: Agent Tools
============================================================

Calculator Tool: The result is: 105
Date Tool: 2026-01-20 16:02:44


============================================================
Example 3: Memory System
============================================================
/Users/cnc/Documents/langgraph/python/sample_codes/unit_01_introduction.py:108: LangChainDeprecationWarning: Please see the migration guide at: https://python.langchain.com/docs/versions/migrating_memory/
  memory = ConversationBufferMemory()
/Users/cnc/Documents/langgraph/python/sample_codes/unit_01_introduction.py:109: LangChainDeprecationWarning: The class `ConversationChain` was deprecated in LangChain 0.2.7 and will be removed in 1.0. Use `langchain_core.runnables.history.RunnableWithMessageHistory` instead.
  conversation = ConversationChain(

--- First Interaction ---


> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:

Human: My name is Alice and I'm learning about AI agents.
AI:

> Finished chain.
Response: Hi Alice! That's a fascinating field to be diving into. AI agents are a really exciting area — they're essentially systems that can perceive their environment and take actions to achieve specific goals, often autonomously.

Think of them as software entities that can act on your behalf or in their own interest, using artificial intelligence to make decisions and interact with the world (or a simulation of it).

We can talk about different types of AI agents, like:

*   **Reactive agents:** That just respond to stimuli in their environment.
*   **Deliberative agents:** That plan and reason about actions.
*   **Hybrid agents:** Combining reactive and deliberative approaches, which is common for more complex AI.
*   **Autonomous agents:** Capable of independent action and planning.

They're used in lots of places: recommendation systems, chatbots, game characters, robotics, automated trading, and even scientific research simulations.

I'm really excited to help you learn about them. What specific aspects of AI agents are you most interested in exploring right now?


--- Second Interaction ---


> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
Human: My name is Alice and I'm learning about AI agents.
AI: Hi Alice! That's a fascinating field to be diving into. AI agents are a really exciting area — they're essentially systems that can perceive their environment and take actions to achieve specific goals, often autonomously.

Think of them as software entities that can act on your behalf or in their own interest, using artificial intelligence to make decisions and interact with the world (or a simulation of it).

We can talk about different types of AI agents, like:

*   **Reactive agents:** That just respond to stimuli in their environment.
*   **Deliberative agents:** That plan and reason about actions.
*   **Hybrid agents:** Combining reactive and deliberative approaches, which is common for more complex AI.
*   **Autonomous agents:** Capable of independent action and planning.

They're used in lots of places: recommendation systems, chatbots, game characters, robotics, automated trading, and even scientific research simulations.

I'm really excited to help you learn about them. What specific aspects of AI agents are you most interested in exploring right now?
Human: What's my name?
AI:

> Finished chain.
Response: Your name is Alice. 😊


--- Conversation History ---
Human: My name is Alice and I'm learning about AI agents.
AI: Hi Alice! That's a fascinating field to be diving into. AI agents are a really exciting area — they're essentially systems that can perceive their environment and take actions to achieve specific goals, often autonomously.

Think of them as software entities that can act on your behalf or in their own interest, using artificial intelligence to make decisions and interact with the world (or a simulation of it).

We can talk about different types of AI agents, like:

*   **Reactive agents:** That just respond to stimuli in their environment.
*   **Deliberative agents:** That plan and reason about actions.
*   **Hybrid agents:** Combining reactive and deliberative approaches, which is common for more complex AI.
*   **Autonomous agents:** Capable of independent action and planning.

They're used in lots of places: recommendation systems, chatbots, game characters, robotics, automated trading, and even scientific research simulations.

I'm really excited to help you learn about them. What specific aspects of AI agents are you most interested in exploring right now?
Human: What's my name?
AI: Your name is Alice. 😊


============================================================
Example 4: Agent Reasoning Loop
============================================================

Task: What is 25 * 4?

--- Agent Loop ---

1. THINK:
To solve the task "What is 25 * 4?", I need to perform multiplication. Here's my step-by-step reasoning:

1. Multiplication is a mathematical operation that combines two numbers to find their product. In this case, I'm multiplying 25 by 4.
2. I can think of this as adding 25 four times: 25 + 25 + 25 + 25.
   - 25 + 25 = 50
   - 50 + 25 = 75
   - 75 + 25 = 100
   So, the result is 100.
3. Alternatively, I can break it down using the distributive property: 25 * 4 = (20 + 5) * 4 = (20 * 4) + (5 * 4) = 80 + 20 = 100.
4. I can also recall that 25 * 4 is a basic multiplication fact, and it equals 100.

No special tool is needed for this calculation, as it can be done mentally or with basic arithmetic skills. If a tool were required, a calculator could be used, but it's unnecessary for such a simple operation. The answer is 100.

2. ACT (using calculator):
The result is: 100

3. OBSERVE & RESPOND:
Based on the calculator's response of "The result is: 100", which aligns with the calculation of 25 * 4, the final answer is 100.


============================================================
Example 5: Agent Use Case Patterns
============================================================

--- Use Case 1: Customer Service ---
Agent Response:
Oh no! I'm so sorry to hear that you're having trouble logging into your account. It can be frustrating when you're unable to access something important.

To help you get back in, here are a few things you might try:

1. **Reset Your Password Again:** Sometimes multiple attempts are needed. Make sure you're using the correct email address associated with your account, and check your inbox (including your spam folder) for the reset link.

2. **Check Your Security Questions or Backup Methods:** If you've set up security questions or added a backup email or phone number, you might be able to use one of those to regain access.

3. **Contact Our Support Team:** If you're still having trouble, our support team is here to help. Could you please provide more details about the error message you're seeing or the device you're using? This will help us assist you better.

I'm here to help you resolve this as quickly as possible. Let me know how else I can assist!


--- Use Case 2: Research Assistant ---
Agent Response:
Okay, as a research assistant, I would approach the task of analyzing the question "What are the key differences between LangChain and LangGraph?" by following these steps:

## Research Outline: Analyzing Differences between LangChain and LangGraph

1.  **Define the Terms and Context:**
    *   **Clarify LangChain:** Confirm LangChain is the established framework (e.g., `langchain.com`, GitHub repository). Understand its core purpose: providing tools and abstractions for building applications with Large Language Models (LLMs), focusing on components like LLMs, prompts, chains, agents, memory, tools, etc.
    *   **Clarify LangGraph:** This is the crucial step. "LangGraph" isn't a universally recognized, distinct framework like LangChain. I need to determine its exact nature:
        *   Is it a *new, separate framework*? (Search GitHub, Hugging Face, arXiv, developer blogs for a framework explicitly named "LangGraph" released recently).
        *   Is it a *component or sub-project* within LangChain? (Check the LangChain GitHub repository, official documentation, changelogs. LangChain does have a `langgraph` module/alpha feature for state management using graphs).
        *   Is it a *project with a similar name* but unrelated? (Search for projects using "Graph" for LLM workflows that aren't part of LangChain).
        *   *Action:* Perform initial searches on platforms like GitHub, Hugging Face, Google Scholar, and developer forums (e.g., Reddit r/LocalLLaMA, Hugging Face Discuss) to identify what "LangGraph" refers to in the current context. This is vital as the comparison changes drastically based on this finding.

2.  **Identify the Core Components and Concepts:**
    *   For **LangChain**: List its key components (LLM, PromptTemplate, LLMChain, Agent, Tool, Memory, Embeddings, VectorStore, etc.).
    *   For **LangGraph** (based on Step 1's findings):
        *   If it's part of LangChain: Identify the specific module/feature (e.g., the `langgraph` alpha package for state graphs). Understand its purpose – likely to manage complex, multi-step conversations or workflows using a graph structure (nodes for steps, edges for transitions).
        *   If it's a separate framework: Identify its core components and architecture. What does it offer? (e.g., graph-based state management, specific API wrappers, knowledge graph integration, etc.?)

3.  **Compare Architectures and Design Philosophy:**
    *   How does LangChain structure its components? (Modular, composable chains/agents).
    *   How does LangGraph structure its components? (Graph-based, nodes/states, transitions?).
    *   What is the primary goal or philosophy behind each? (LangChain: general-purpose LLM application building. LangGraph: potentially more specialized, graph-centric workflows?).

4.  **Compare Key Features and Capabilities:**
    *   **State Management/Memory:** This is a critical area.
        *   LangChain: Offers various memory types (Simple, Conversation, Vector stores). State management can sometimes become complex in long, branching conversations.
        *   LangGraph (if it's the graph module): Specifically designed for managing complex, multi-step, conditional conversations or workflows using a graph structure. Provides more explicit control over state transitions.
        *   LangGraph (if it's a separate framework): Likely focuses heavily on graph-based state management.
    *   **Workflow Composition:** How easily can complex tasks be broken down and chained together?
        *   LangChain: Uses `LLMChain`, `Agent`, `Router`, etc.
        *   LangGraph: Uses graph structures (nodes, edges, execution) for workflow definition.
    *   **Complexity Handling:** How well do they handle very complex, branching, or conditional logic in LLM applications?
    *   **Integration Points:** What external libraries or APIs do they integrate well with? (LLM providers, vector databases, etc.)
    *   **Performance:** Are there known performance differences, especially for very large or complex graphs/workflows? (This might be hard to find concrete comparisons).

5.  **Compare Use Cases and Target Applications:**
    *   **LangChain:** General-purpose LLM apps, chatbots, assistants, summarization, Q&A systems, document processing, agents, etc.
    *   **LangGraph**:
        *   If part of LangChain: More suitable for complex, long-form conversations, intricate decision-making processes, multi-agent systems with defined interactions.
        *   If separate: Potentially for building applications heavily reliant on graph structures (e.g., knowledge bases, recommendation systems, complex workflows, specific types of dialogue management).

6.  **Evaluate Maturity, Community, and Documentation:**
    *   How established is LangGraph? (Check release dates, number of stars on GitHub, activity level).
    *   Is LangGraph actively maintained? (Check commit frequency, issue resolution speed).
    *   Compare the documentation quality and accessibility for both LangChain and LangGraph.
    *   Compare the community support size and activity.

7.  **Identify Limitations and Downsides:**
    *   What are the known limitations of LangChain (e.g., complexity of state management, potential cost, specific agent limitations)?
    *   What are the known limitations of LangGraph (e.g., smaller feature set, less mature, niche application, potential overhead for simple tasks)?

8.  **Synthesize Findings and Formulate Key Differences:**
    *   Based on the research, summarize the core differences. Focus on:
        *   **Architecture:** Component-based chains vs. Graph-based state/workflow management.
        *   **Primary Strength:** General-purpose application building vs. Handling complex, conditional, graph-based workflows.
        *   **Complexity:** How each handles increasing complexity.
        *   **Niche:** LangChain for broader applications; LangGraph potentially for a specific subset of complex interactions (depending on its nature).

9.  **Outline Findings:**
    *   Structure the answer clearly, presenting the key differences identified in Step 8. Ensure clarity on what LangGraph is (crucial point). Provide examples where applicable.


--- Use Case 3: Code Debugging ---
Agent Response:
The issue occurs when the `calculate_average` function is called with an empty list (`[]`), leading to division by zero. This is because `len(numbers)` returns 0 for an empty list, and dividing by zero raises a `ZeroDivisionError`.

**Fix:** Add a check to handle empty lists explicitly.

```python
def calculate_average(numbers):
    if not numbers:  # Check if the list is empty
        return None  # Or raise a custom exception, or return 0, but None is clear here
    return sum(numbers) / len(numbers)
```

This fix prevents the division by zero error by returning `None` (or another appropriate value/error) for empty lists.



Attempting model comparison (skip if models not available)...
============================================================
Example 6: Model Comparison
============================================================

--- LLAMA2-UNCENSORED ---
Response: Agent autonomy refers to a computer system's ability to make decisions without human intervention, based on predefined rules and algorithms.

--- DEEPSEEK-R1:8B ---
Response: An agent acts independently, pursues its own goals, and makes its own decisions without direct human control.

--- LLAMA3-GROQ-TOOL-USE ---
Response: Agent autonomy refers to an agent's ability to make decisions and take actions without explicit instructions from its creator.


============================================================
Example 7: Agent Planning
============================================================

Task: Plan a birthday party for 20 people this weekend.

--- Agent's Plan ---
Here’s a numbered list of sub-tasks to help you plan a birthday party for 20 people this weekend. This breakdown covers the key aspects of party planning, from initial setup to execution and cleanup. Each sub-task is designed to be actionable and can be tackled in a logical order, keeping in mind the time-sensitive nature of planning for this weekend.

1. **Define the party details**: Determine the birthday person's preferences, the party theme (e.g., birthday boy/girl's interests), and the overall vibe (e.g., casual, formal, kids-focused). This will guide all other decisions.

2. **Set a budget**: Establish a budget for the party, including costs for food, decorations, venue, entertainment, and any other expenses. Allocate funds for unexpected costs.

3. **Choose a date and time**: Since the task specifies "this weekend," select a specific date and time slot (e.g., Saturday afternoon or Sunday evening) that works for the birthday person and most guests.

4. **Select a venue or location**: Decide where the party will take place (e.g., home, backyard, rented space, or a public venue). Consider factors like capacity (for 20 people), accessibility, and any necessary permits.

5. **Create a guest list**: Compile a list of exactly 20 people to invite, ensuring it includes close friends and family. Consider any dietary restrictions or special needs.

6. **Send out invitations**: Design and distribute invitations (e.g., digital or physical) with the date, time, location, and RSVP deadline. Use a tool like Google Forms for easy responses.

7. **Plan the menu and food arrangements**: Decide on food options (e.g., potluck, catering, or DIY) and ensure there's something for all guests. Budget for drinks and snacks, and assign any cooking or serving responsibilities.

8. **Arrange entertainment**: Choose activities to keep guests engaged, such as music (e.g., playlist or DJ), games, a photo booth, or a birthday activity. If needed, book a performer or rent equipment.

9. **Handle decorations and supplies**: Select a theme and gather or order decorations, party supplies (e.g., balloons, tableware), and any necessary items for the venue setup.

10. **Coordinate helpers or vendors**: If needed, enlist friends or family to assist with setup, serving, or cleanup. Research and book any external vendors (e.g., caterers, florists) if required.

11. **Plan party favors or gifts**: Consider small tokens to give guests (e.g., goody bags or personalized items) to enhance the celebration.

12. **Manage RSVPs and confirm attendance**: Track responses to the invitations and follow up with guests who haven't replied. Adjust plans based on the expected number of attendees.

13. **Set up a timeline for weekend preparations**: Create a schedule for tasks, such as shopping on Friday morning, setting up the venue on the day of the party, and hosting in the evening.

14. **Plan for logistics and contingencies**: Organize seating, transportation for guests if needed, and a backup plan for bad weather (if outdoors). Also, arrange for party cleanup supplies and post-party tasks.

15. **Review and finalize preparations**: A day or two before the party, double-check all details, including food, decorations, and guest lists, to ensure everything is on track.

This list provides a structured approach to planning. Since the party is this weekend, prioritize tasks that can be done quickly, like sending invitations and confirming details, to avoid last-minute stress. If you need help with specific sub-tasks, such as generating ideas for a theme or estimating costs, let me know!


============================================================
Example 8: Feedback and Self-Correction
============================================================

--- Initial Attempt ---
Agent's First Attempt:
Learning, evolving,
Dreaming, designing,
Changing us all.

--- Self-Critique ---
Self-Critique:
Okay, let's break down the syllable count:

*   **Learning, evolving:** 2 + 3 = **5** syllables (correct).
*   **Dreaming, designing:** 2 + 3 = **5** syllables (This line is **too short**; it needs 7 syllables).
*   **Changing us all:** 2 + 1 + 1 = **4** syllables (This line is **too short**; it needs 7 syllables).

**Critique:**

The haiku **does not follow the standard 5-7-5 syllable pattern**.

*   The first line has 5 syllables, which is correct.
*   The second line has only 5 syllables, but requires 7.
*   The third line has only 4 syllables, but requires 5.

The syllable count is the primary failing here. While the content touches on themes of growth ("Learning, evolving") and change ("Changing us all"), the structure doesn't meet the technical requirements of a traditional haiku.

--- Improved Version ---
Improved Haiku:
Okay, here is an improved haiku strictly adhering to the 5-7-5 syllable count, addressing potential issues like clarity and focus:

**Silicon heart**
With no beating pulse
But endless thought.



============================================================
All examples completed successfully!
============================================================