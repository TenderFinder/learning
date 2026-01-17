# Unit 2: Environment Setup & n8n Mastery - n8n Exercises

## Learning Objectives
- Master n8n interface and features
- Connect to multiple AI providers
- Test and debug workflows effectively
- Understand n8n best practices
- Build reusable workflow components

---

## Exercise 1: n8n Interface Mastery (Beginner) ⭐

**Objective**: Become proficient with n8n's interface and features.

**Tasks**:
1. **Workflow Organization**:
   - Create 3 folders: "Learning", "Production", "Templates"
   - Build a simple workflow in each
   - Practice moving workflows between folders

2. **Node Exploration**:
   - Try 5 different trigger nodes
   - Try 5 different action nodes
   - Document what each does

3. **Execution Understanding**:
   - Run a workflow manually
   - View execution history
   - Understand execution logs
   - Identify errors in logs

**Deliverable**: Screenshot documentation of your explorations

---

## Exercise 2: Multi-Provider AI Setup (Intermediate) ⭐⭐

**Objective**: Connect to multiple AI providers and compare them.

**Providers to Setup**:
1. **Ollama** (local - llama3)
2. **OpenAI** (cloud - if available)
3. **Anthropic/Claude** (cloud - if available)

**Tasks**:
1. Create credentials for each provider
2. Build identical workflows using each
3. Test with same prompts
4. Compare:
   - Response quality
   - Speed
   - Cost (if applicable)
   - Best use cases

**Test Workflow**:
```
Webhook Input (text)
    ↓
AI Provider (configurable)
    ↓
Response
```

**Questions to Answer**:
- Which is fastest?
- Which gives best responses?
- When would you use each?

---

## Exercise 3: Building Reusable Sub-Workflows (Intermediate) ⭐⭐

**Objective**: Create modular, reusable workflow components.

**Sub-Workflows to Create**:
1. **Email Validator**
   - Input: Email address
   - Output: Valid/Invalid + reason

2. **Text Summarizer**
   - Input: Long text
   - Output: 2-sentence summary

3. **Sentiment Analyzer**
   - Input: Text
   - Output: Positive/Negative/Neutral + score

**Then**: Build a main workflow that uses all three!

**Main Workflow Example**:
```
Process Customer Feedback
    ↓
Validate Email (sub-workflow)
    ↓
Analyze Sentiment (sub-workflow)
    ↓
Summarize (sub-workflow)
    ↓
Save to Database
```

---

## Exercise 4: Error Handling Mastery (Advanced) ⭐⭐⭐

**Objective**: Build bulletproof workflows with comprehensive error handling.

**Workflow to Build**: Email Processing with Full Error Handling

**Requirements**:
1. **Try-Catch Pattern**:
   - Wrap risky operations
   - Catch specific errors
   - Log errors properly

2. **Retry Logic**:
   - Auto-retry failed operations
   - Maximum 3 attempts
   - Exponential backoff

3. **Fallback Strategies**:
   - If AI fails → Use template response
   - If email fails → Save to queue
   - If database fails → Log to file

4. **Notifications**:
   - Alert on critical errors
   - Daily error summary

**Test Scenarios**:
- Simulate AI timeout
- Simulate invalid email
- Simulate database connection failure

---

## Exercise 5: Workflow Testing Framework (Advanced) ⭐⭐⭐

**Objective**: Create a systematic way to test workflows.

**Build**:
1. **Test Data Generator**
   - Creates varied test inputs
   - Edge cases included
   - Invalid data for error testing

2. **Automated Test Suite**
   - Runs multiple test cases
   - Checks expected outputs
   - Reports pass/fail

3. **Test Documentation**:
   - What's being tested
   - Expected results
   - Actual results
   - Pass/fail status

**Example Test Suite**:
```
Workflow: Email Classifier

Test Cases:
1. Urgent email → Should route to "urgent" path ✅
2. Question email → Should draft response ✅
3. Newsletter → Should archive ✅
4. Invalid format → Should handle error ✅
5. Empty email → Should reject gracefully ✅

Results: 5/5 passed
```

---

## Exercise 6: Integration Exploration (Intermediate) ⭐⭐

**Objective**: Connect n8n to real business tools.

**Integrations to Setup** (choose 3):
- Slack / Discord
- Google Sheets / Excel
- Email (Gmail / Outlook)
- Airtable / Notion
- Calendar (Google / Outlook)
- GitHub / GitLab

**For Each Integration**:
1. Set up credentials
2. Build a simple workflow
3. Test thoroughly
4. Document setup steps

**Example Workflows**:
- **Slack**: Bot that responds to mentions
- **Google Sheets**: Auto-update from AI analysis
- **Email**: Auto-categorize and respond
- **Airtable**: AI-powered data entry
- **Calendar**: Smart meeting scheduler

---

## Exercise 7: Performance Optimization (Advanced) ⭐⭐⭐

**Objective**: Make workflows faster and more efficient.

**Workflow to Optimize**: Multi-step content analyzer
```
Input: 10 articles
Process: Summarize + Extract keywords + Sentiment analysis
Output: Structured data
```

**Optimization Tasks**:
1. **Baseline Measurement**:
   - Time total execution
   - Note bottlenecks

2. **Parallel Processing**:
   - Process articles simultaneously
   - Measure improvement

3. **Caching**:
   - Cache AI responses
   - Reuse repeated operations

4. **Batch Operations**:
   - Group similar tasks
   - Reduce API calls

**Goal**: 50%+ speed improvement

**Document**:
- Before: X seconds
- After: Y seconds
- Techniques used
- Trade-offs made

---

## Exercise 8: Production Readiness Checklist (Advanced) ⭐⭐⭐

**Objective**: Prepare workflows for real-world use.

**Take ANY workflow and make it production-ready**:

**Checklist**:
- [ ] Error handling on all nodes
- [ ] Retry logic where needed
- [ ] Proper logging
- [ ] Clear node naming
- [ ] Workflow documentation
- [ ] Test coverage
- [ ] Performance optimized
- [ ] Security reviewed (credentials, sensitive data)
- [ ] Monitoring/alerts configured
- [ ] Backup/recovery plan
- [ ] Team documentation (how to use)
- [ ] Deployment plan

**Deliverable**: Before/after comparison showing improvements

---

## Challenge Project: n8n Workflow Library (Expert) ⭐⭐⭐⭐

**Objective**: Build a personal library of reusable workflows.

**Create**:
1. **Template Workflows** (5+):
   - Chatbot template
   - Email processor template
   - Data analyzer template
   - Content generator template
   - API integration template

2. **Component Library**:
   - Custom error handler
   - Standard logger
   - AI wrapper (works with multiple providers)
   - Data validator
   - Response formatter

3. **Documentation**:
   - Setup guide for each
   - customization instructions
   - Best practices
   - Example use cases

4. **Sharing**:
   - Export as JSON
   - Create README for each
   - Share with team
   - Contribute to n8n community!

**Bonus**:
- Create video tutorials
- Write blog posts about your workflows
- Present to team

---

## Real-World Scenarios

### Scenario 1: Onboarding Automation
Build complete employee onboarding workflow:
- Email welcome message
- Create accounts (simulated)
- Send calendar invites
- Add to Slack channels
- Track completion

### Scenario 2: Daily Standup Bot
Automate standup collection:
- Daily Slack message to team
- Collect responses
- Summarize with AI
- Post summary to channel
- Track over time

### Scenario 3: Content Pipeline
Automate content creation:
- Generate topic ideas
- Research each topic
- Create outline
- Draft content
- Review with AI
- Schedule for publishing

**Choose one and build it fully!**

---

## Submission Guidelines

For each exercise:
1. **Workflow Export**: JSON file
2. **Screenshots**: Show working execution
3. **Documentation**:
   - What it does
   - How to set it up
   - How to use it
   - Troubleshooting tips
4. **Demo Video** (for challenge project)

---

## Evaluation Criteria

- **Functionality**: Does it work reliably?
- **Error Handling**: Handles edge cases?
- **Documentation**: Clear and complete?
- **Reusability**: Can others use it?
- **Creativity**: Innovative solutions?

---

## Tips for Success

### n8n Best Practices:
1. **Name Everything Clearly**: "Send Email" not "HTTP Request 3"
2. **Test Incrementally**: Test each node before adding next
3. **Use Sticky Notes**: Document complex logic
4. **Version Control**: Export backups regularly
5. **Start Simple**: Add complexity gradually

### Debugging:
- Click on nodes to see data flow
- Check execution logs
- Test with simple data first
- Use "Execute Workflow" liberally

### Learning:
- Browse n8n templates for ideas
- Join community forum
- Watch tutorial videos
- Experiment fearlessly!

---

**Estimated Time**: 10-12 hours for all exercises  
**Prerequisites**: Unit 1 completed, n8n installed  
**Resources**: n8n.io/workflows, community.n8n.io

**Master n8n and unlock visual AI superpowers! 🎨🚀**
