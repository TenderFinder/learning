# Unit 3: LangChain Fundamentals - Exercises

## Learning Objectives
- Master prompt templates and engineering
- Build and compose chains
- Implement different memory strategies
- Use LCEL (LangChain Expression Language)

---

## Exercise 1: Advanced Prompt Templates (Intermediate)

**Objective**: Create sophisticated prompt templates for different scenarios.

**Tasks**:
1. Create a few-shot prompt template for classifying programming languages
2. Use at least 5 examples in the template
3. Test with 3 new inputs

**Example Format**:
```
Language: Python, Type: interpreted, Use Case: data science
Language: C++, Type: compiled, Use Case: systems programming
...
Language: [NEW], Type: ?, Use Case: ?
```

**Requirements**:
- Use `FewShotPromptTemplate`
- Include proper prefix and suffix
- Test classification accuracy

---

## Exercise 2: Chain Composition Challenge (Advanced)

**Objective**: Build a multi-step content creation pipeline.

**Tasks**:
Create a sequential chain that:
1. Takes a broad topic as input
2. Generates 3 specific subtopics
3. For the first subtopic, creates:
   - A title
   - An outline (3 points)
   - An introduction paragraph
4. Returns all components

**Example**:
```
Input: "Cloud Computing"

Output:
  Subtopics:
    1. Serverless Architecture
    2. Container Orchestration
    3. Cloud Security

  Title: "Understanding Serverless Architecture"
  Outline:
    - What is serverless?
    - Benefits and use cases
    - Popular platforms
  Introduction: [generated paragraph]
```

---

## Exercise 3: Memory Systems Comparison (Intermediate)

**Objective**: Compare different memory types in action.

**Tasks**:
1. Implement the same 10-turn conversation with:
   - ConversationBufferMemory
   - ConversationBufferWindowMemory (k=3)
   - ConversationSummaryMemory
2. Compare memory usage and effectiveness
3. Document trade-offs

**Conversation Script**:
```
1. User introduces themselves (name, profession, hobbies)
2-4. Discuss a technical topic
5-7. Switch to a different topic
8. Ask about something from turn 1
9. Ask about something from turn 4
10. Ask for overall summary
```

**Deliverable**: A comparison table with findings.

---

## Exercise 4: Build a Code Review Assistant (Advanced)

**Objective**: Create a practical chain-based application.

**Tasks**:
Build an assistant that:
1. Takes code as input
2. Analyzes it for:
   - Code quality issues
   - Potential bugs
   - Performance concerns
3. Suggests improvements
4. Generates a formatted review

**Requirements**:
- Use appropriate prompt templates
- Implement memory (remember previous reviews)
- Use chain composition
- Handle multiple programming languages

**Test with code samples in**: Python, JavaScript, and one other language

---

## Exercise 5: LCEL Pipeline Construction (Advanced)

**Objective**: Master LangChain Expression Language.

**Tasks**:
Create a pipeline using LCEL that:
1. Takes a research question
2. Breaks it into 3 sub-questions
3. Answers each sub-question
4. Synthesizes a final answer

**Requirements**:
- Use pipe operators (`|`)
- Include output parsers
- Handle errors gracefully
- Make it reusable

---

## Exercise 6: Streaming Responses (Intermediate)

**Objective**: Implement streaming for better UX.

**Tasks**:
1. Create a storytelling application that streams responses
2. Show progress indicators
3. Handle interruption
4. Calculate and display:
   - Tokens per second
   - Time to first token
   - Total time

---

## Challenge Project: Interactive Learning Tutor

**Objective**: Build a complete tutoring application.

**Requirements**:
Your tutor should:
1. Ask about student's level (beginner/intermediate/advanced)
2. Adapt explanations based on level
3. Remember topics covered
4. Provide examples and practice problems
5. Track student progress across sessions
6. Save and load conversation history

**Features**:
- Multiple subjects support
- Progress tracking
- Personalized recommendations
- Export learning summary

---

**Estimated Time**: 8-10 hours
**Prerequisites**: Unit 1 and 2 completed
