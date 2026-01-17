# Unit 3: Building Workflows (Visual Chains) - n8n Exercises

## Learning Objectives
- Build multi-step visual workflows
- Master prompt engineering in n8n
- Implement conditional logic
- Create reusable templates
- Handle data transformation

---

## Exercise 1: Multi-Step Content Pipeline (Intermediate) ⭐⭐

**Objective**: Build a 5-step content creation workflow.

**Workflow**:
```
Topic Input
    ↓
Generate Title (AI)
    ↓
Create Outline (AI)
    ↓
Write Introduction (AI)
    ↓  
Generate Keywords (AI)
    ↓
Format & Output (Markdown)
```

**Requirements**:
- Each AI step uses output from previous step
- Final output is well-formatted markdown
- Include metadata (word count, keywords)
- Save to Google Docs or send via email

**Test Topics**:
- "AI in Healthcare"
- "Remote Work Productivity"
- "Sustainable Technology"

**Success Criteria**:
- ✅ All 5 steps execute in sequence
- ✅ Each step builds on previous
- ✅ Final output is coherent
- ✅ Can run with different topics

---

## Exercise 2: Conditional Routing Mastery (Intermediate) ⭐⭐

**Objective**: Build intelligent routing based on AI decisions.

**Scenario**: Customer Inquiry Router

**Workflow**:
```
Customer Message
    ↓
AI Classifier (determines type)
    ↓
    ├─ [Complaint] → Escalate to Manager + Log
    ├─ [Question] → Search FAQ → Draft Response
    ├─ [Order Status] → Check Database → Provide Update
    └─ [Feedback] → Thank & Save to Airtable
```

**Requirements**:
- 4 different paths
- Each path has 2-3 steps
- All paths log to central database
- Send different notifications per path

**Test Messages**:
```
1. "I'm very unhappy with my recent purchase!"
2. "How do I reset my password?"
3. "Where is my order #12345?"
4. "Your product is amazing, thank you!"
```

**Success Criteria**:
- ✅ Correctly routes all 4 message types
- ✅ Each path executes properly
- ✅ All interactions logged
- ✅ Appropriate notifications sent

---

## Exercise 3: Prompt Template Library (Intermediate) ⭐⭐

**Objective**: Create reusable, customized prompt templates.

**Templates to Build**:

1. **Blog Post Generator**
```
System: You are a professional content writer.
Template: Write a {tone} blog post about {topic} for {audience}.
Include: {requirements}
Length: {word_count} words
```

2. **Email Responder**
```
System: You are a customer service representative.
Template: Respond to this {email_type} email professionally.
Tone: {tone}
Context: {customer_history}
Include: {required_elements}
```

3. **Data Analyzer**
```
System: You are a data analyst.
Template: Analyze this {data_type} and provide {analysis_type}.
Focus on: {key_metrics}
Format: {output_format}
```

**Tasks**:
- Create n8n workflows for each template
- Make all variables configurable
- Test with different inputs
- Document usage for each

**Bonus**: Create a "Template Manager" workflow that lets you choose which template to use

---

## Exercise 4: Few-Shot Learning Implementation (Advanced) ⭐⭐⭐

**Objective**: Use examples to teach AI specific formats.

**Scenario**: Product Description Generator

**Few-Shot Examples**:
```
Example 1:
Input: "Wireless Mouse"
Output: "Experience precision and freedom with our ergonomic wireless mouse. Features: 2.4GHz connectivity, 6-month battery life, DPI adjustment. Perfect for: Office work, gaming, productivity."

Example 2:
Input: "Yoga Mat"
Output: "Transform your practice with our premium yoga mat. Features: Non-slip surface, 6mm thickness, eco-friendly material. Perfect for: Yoga, Pilates, stretching."

Example 3:
Input: "Coffee Maker"
Output: "Brew barista-quality coffee at home. Features: 12-cup capacity, programmable timer, auto-shutoff. Perfect for: Busy mornings, coffee enthusiasts, offices."
```

**Your Task**:
- Build workflow that includes these examples
- Test with new products
- AI should follow same format
- Compare with/without examples

**Test Products**:
- Bluetooth Speaker
- Standing Desk
- Water Bottle

---

## Exercise 5: Data Transformation Pipeline (Advanced) ⭐⭐⭐

**Objective**: Process and transform data through multiple steps.

**Scenario**: Survey Response Analyzer

**Input**: Raw survey responses (10-20 responses)

**Workflow**:
```
Raw Responses
    ↓
Clean Data (remove duplicates, fix formatting)
    ↓
Categorize Responses (AI)
    ↓
Extract Key Themes (AI)
    ↓
Sentiment Analysis (AI)
    ↓
Generate Summary Report (AI)
    ↓
Create Visualizations (charts/graphs)
    ↓
Email Report to Stakeholders
```

**Requirements**:
- Handle messy input data
- Use AI for analysis steps
- Create structured output
- Generate actual visual charts (Chart.js or similar)

**Sample Data**: Create 15+ fake survey responses about product satisfaction

---

## Exercise 6: Iterative Improvement Loop (Advanced) ⭐⭐⭐

**Objective**: Build self-improving content workflow.

**Scenario**: Essay Writer with Quality Control

**Workflow**:
```
Topic + Requirements
    ↓
Generate Essay (AI #1)
    ↓
Quality Checker (AI #2):
  - Grammar: Pass/Fail
  - Structure: Pass/Fail
  - Arguments: Pass/Fail
  - Length: Pass/Fail
    ↓
[IF all pass] → Final Output
[IF any fail] → Improver (AI #3) → Loop back to Quality Checker
    ↓
Max 3 iterations
```

**State Tracking**:
- Current iteration count
- Which checks passed/failed
- Improvement history
- Final quality score

**Test Requirements**:
```
Topic: "Impact of AI on Education"
Requirements:
- 500 words
- 3 main arguments
- Introduction and conclusion
- Academic tone
```

---

## Exercise 7: Dynamic Workflow Builder (Expert) ⭐⭐⭐⭐

**Objective**: Build a workflow that adapts based on input.

**Scenario**: Flexible Content Generator

**Concept**:
```
Input: 
  - Content type (blog, email, social post)
  - Number of variants (1-5)
  - Additional parameters

Workflow DYNAMICALLY:
  - Adjusts prompts based on content type
  - Creates parallel branches for variants
  - Applies appropriate formatting
  - Routes to correct output channel
```

**Implementation**:
- Use Switch node extensively
- Create modular sub-workflows
- Handle variable number of outputs
- Merge results intelligently

**Test Cases**:
1. Blog post, 1 variant
2. Social media, 3 variants (Twitter, LinkedIn, Instagram)
3. Email campaign, 2 variants (A/B test)

---

## Exercise 8: Workflow Optimization Challenge (Advanced) ⭐⭐⭐

**Objective**: Make a slow workflow significantly faster.

**Given**: A workflow that processes 10 customer inquiries (sequential, ~60 seconds total)

**Your Tasks**:
1. **Baseline**: Measure current performance
2. **Parallelize**: Process inquiries simultaneously
3. **Cache**: Store repeated AI responses
4. **Batch**: Group similar operations
5. **Optimize Prompts**: Reduce token usage
6. **Measure**: Compare before/after

**Goal**: 50%+ improvement

**Requirements**:
- Document all optimization techniques
- Show metrics (before/after)
- Explain trade-offs
- Ensure quality doesn't degrade

---

## Challenge Project: Intelligent Content Factory (Expert) ⭐⭐⭐⭐

**Objective**: Build a complete, production-ready content generation system.

**System Features**:

1. **Content Planning**:
   - AI generates content calendar
   - Suggests topics based on trends
   - Schedules posts

2. **Multi-Format Generation**:
   - Blog posts (long-form)
   - Social media posts (short-form)
   - Email newsletters
   - Video scripts

3. **Quality Control**:
   - AI proofreading
   - Fact-checking
   - Brand voice consistency
   - SEO optimization

4. **Distribution**:
   - Posts to WordPress
   - Schedules to Buffer/Hootsuite
   - Sends to email list
   - Archives to Drive

5. **Analytics**:
   - Tracks performance
   - A/B test results
   - Optimization suggestions

**Requirements**:
- At least 5 integrated tools
- Complete error handling
- Scheduling capabilities
- Dashboard/reporting
- User-friendly interface

**Deliverables**:
- Working n8n workflows (exportable)
- Documentation
- Video demo
- Performance metrics

---

## Real-World Scenarios

### Scenario A: Meeting Notes Processor
**Build**:
- Input: Raw meeting transcript
- Extract: Decisions, action items, attendees
- Assign: Tasks in project management tool
- Send: Summary to participants
- Archive: In knowledge base

### Scenario B: Customer Feedback Loop
**Build**:
- Collect: Feedback from multiple channels
- Analyze: Sentiment and themes
- Categorize: By product/feature
- Route: Urgent issues to team immediately
- Report: Weekly summary to stakeholders

### Scenario C: Social Media Manager
**Build**:
- Generate: Post ideas
- Create: Multiple variants
- Schedule: Across platforms
- Monitor: Engagement
- Learn: From performance data

**Choose one and build completely!**

---

## Submission Guidelines

For each exercise:
1. **Workflow Export** (JSON)
2. **Screenshots** showing:
   - Workflow canvas
   - Successful execution
   - Sample outputs
3. **Documentation**:
   - Setup instructions
   - Configuration options
   - How to customize
4. **Test Results** with various inputs

---

## Evaluation Criteria

- **Functionality** (35%): Works correctly
- **Design** (20%): Well-structured workflow
- **Reusability** (15%): Can be adapted easily
- **Error Handling** (15%): Handles edge cases
- **Documentation** (15%): Clear and complete

---

## Tips for Success

### Prompt Engineering:
- Be specific and clear
- Use examples when possible
- Specify output format
- Test and iterate

### Workflow Design:
- Keep nodes organized
- Use descriptive names
- Add sticky notes for complex logic
- Test each step individually

### Debugging:
- Check data between nodes
- Use execution logs
- Test with simple data first
- Add error logging

---

**Estimated Time**: 12-15 hours  
**Prerequisites**: Units 1-2 completed  
**Focus**: Multi-step workflows, prompts, logic

**Master the art of visual workflow design! 🎨✨**
