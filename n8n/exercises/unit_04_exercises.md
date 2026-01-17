# Unit 4: Building Stateful Agents (Visual State Machines) - n8n Exercises

## Learning Objectives
- Build state-based workflows
- Implement decision trees visually
- Create loops and iterations
- Track workflow state
- Build multi-step reasoning flows

---

## Exercise 1: Order Processing State Machine (Intermediate) ⭐⭐

**Objective**: Create a complete order processing workflow with states.

**States**:
- New → Validated → Payment → Fulfilled → Completed
- Can also go to: Cancelled, Refunded, Error

**Visual Workflow**:
```
Order Received
    ↓
Validate Order
    ├─ [Valid] → Process Payment
    └─ [Invalid] → Cancel → Notify Customer
Process Payment
    ├─ [Success] → Fulfill Order
    └─ [Failed] → Retry (3x) → Cancel if still fails
Fulfill Order
    → Mark Complete → Send Confirmation
```

**Data to Track**:
```javascript
{
  order_id: string,
  status: string,
  created_at: timestamp,
  updated_at: timestamp,
  history: [array of state changes],
  retry_count: number
}
```

**Test with 5 different order scenarios**

---

## Exercise 2: Decision Tree Builder (Intermediate) ⭐⭐

**Objective**: Create complex branching logic.

**Scenario**: Product Recommendation Engine

**Decision Tree**:
```
Customer Profile
    ↓
Budget Level?
  ├─ Low → Category A products
  ├─ Medium → Category B products
  └─ High → Category C products
       ↓
Previous Purchases?
  ├─ Yes → Similar items
  └─ No → Trending items
       ↓
Location?
  ├─ US → US inventory
  ├─ EU → EU inventory
  └─ Other → International options
```

**Requirements**:
- At least 3 decision levels
- 8+ possible end paths
- Track decision path taken
- Generate personalized recommendations

---

## Exercise 3: Iterative Loop Workflow (Advanced) ⭐⭐⭐

**Objective**: Build workflow with controlled loops.

**Scenario**: Research Question Answerer

**Workflow**:
```
Question Input
    ↓
Search for Information (iteration 1)
    ↓
Check: Is answer complete?
  ├─ [Yes, confidence > 80%] → Generate Final Answer
  └─ [No] → Refine search query → Search again
       ↓
Max 5 iterations
If not complete after 5 → Best effort answer
```

**State Tracking**:
- Current iteration
- Sources found
- Confidence level
- Search queries used

**Test Questions**:
- "What is LangGraph?"
- "How does photosynthesis work?"
- "Explain quantum computing"

---

## Exercise 4: Multi-Step Approval Workflow (Advanced) ⭐⭐⭐

**Objective**: Implement approval chain with states.

**Scenario**: Expense Report Approval

**States & Flow**:
```
Submitted
    ↓
Manager Review
  ├─ [Approve, <$1000] → Approved → Process Payment
  ├─ [Approve, >=$1000] → Director Review
  └─ [Reject] → Rejected → Notify Submitter
       ↓
Director Review
  ├─ [Approve] → Approved → Process Payment
  └─ [Reject] → Rejected → Notify All
```

**Features**:
- Email notifications at each step
- Deadline tracking (escalate if overdue)
- Comments at each approval level
- Complete audit trail

---

## Exercise 5: Session-Based Chatbot (Advanced) ⭐⭐⭐

**Objective**: Build stateful conversational agent.

**Features**:
```
State Management:
- Session ID tracking
- Conversation history (last 10 messages)
- User preferences
- Current context

Workflow States:
- Greeting → Understanding Intent → Executing Action → Confirming
```

**Capabilities**:
- Remember user name
- Track conversation topics
- Provide context-aware responses
- Handle topic switches

**Test Conversation**:
```
User: Hi, I'm Alex
Bot: [Saves name] Hello Alex!

User: I need help with my order
Bot: [Sets context: order_help] I can help with that...

User: Also, what's your return policy?
Bot: [Switches context] Our return policy...

User: Thanks! What was my first question?
Bot: [Recalls from history] You asked about your order.
```

---

## Exercise 6: Progress Tracking System (Advanced) ⭐⭐⭐

**Objective**: Build workflow that tracks multi-step progress.

**Scenario**: Onboarding Checklist

**Steps to Track**:
1. Account created
2. Profile completed
3. First product added
4. Payment method set up
5. First order placed
6. Email confirmed

**Workflow**:
- Update progress on each action
- Send reminders for incomplete steps
- Celebrate milestones
- Generate completion report

**State Schema**:
```javascript
{
  user_id: string,
  started_at: timestamp,
  progress: {
    step1: {completed: bool, timestamp: date},
    step2: {completed: bool, timestamp: date},
    ...
  },
  completion_percentage: number,
  current_step: string
}
```

---

## Exercise 7: Dynamic State Router (Expert) ⭐⭐⭐⭐

**Objective**: Build workflow that changes behavior based on accumulated state.

**Scenario**: Intelligent Customer Support Bot

**State Evolution**:
```
New User State → Regular User → VIP User → At-Risk User

State determines:
- Response priority
- Features available
- Support level
- Routing destination
```

**State Transitions**:
- New → Regular: After 3 interactions
- Regular → VIP: If lifetime value > $1000  
- Any → At-Risk: If negative sentiment detected
- At-Risk → Regular: If issue resolved

**Workflow adapts based on current state!**

---

## Exercise 8: Parallel State Management (Expert) ⭐⭐⭐⭐

**Objective**: Manage multiple concurrent states.

**Scenario**: Project Management System

**Parallel States**:
```
Project Status: Planning / In Progress / Review / Complete
Budget Status: Under / On Track / Over
Timeline Status: Ahead / On Time / Delayed
Quality Status: Needs Work / Acceptable / Excellent
```

**All states tracked simultaneously**

**Workflow**:
- Update any state independently
- Overall project health = combination of all states
- Trigger alerts based on state combinations
- Generate status reports

**Example Combinations**:
- In Progress + Over Budget + Delayed = HIGH ALERT
- Review + On Track + Acceptable = NORMAL
- Complete + Under Budget + Ahead = SUCCESS

---

## Challenge Project: Workflow Orchestration Engine (Expert) ⭐⭐⭐⭐

**Objective**: Build meta-workflow that manages other workflows.

**Features**:

1. **Workflow Registry**:
   - Store available workflows
   - Track versions
   - Record dependencies

2. **Dynamic Execution**:
   - Choose workflow based on input
   - Pass state between workflows
   - Handle workflow failures

3. **State Persistence**:
   - Save state to database
   - Resume from any point
   - Audit complete history

4. **Monitoring**:
   - Track all executions
   - Performance metrics
   - Error rates
   - Success rates

**Example Use Case**:
```
Customer Request arrives
    ↓
Orchestrator analyzes request
    ↓
Routes to appropriate workflow:
  - "Order Status" workflow
  - "Return Request" workflow
  - "Product Question" workflow
    ↓
Tracks execution state
    ↓
Aggregates results
    ↓
Responds to customer
```

---

## Submission Requirements

1. **Workflow exports** (JSON)
2. **State diagrams** (visual documentation)
3. **Test scenarios** with results
4. **State transition logs**
5. **Performance metrics**

---

## Evaluation Criteria

- **State Management** (40%): Proper state tracking
- **Logic Flow** (25%): Correct transitions
- **Error Handling** (20%): Edge cases covered
- **Documentation** (15%): Clear and complete

---

**Estimated Time**: 15-18 hours  
**Prerequisites**: Units 1-3 completed  
**Focus**: State machines, decisions, loops

**Build intelligent, stateful workflows! 🎯🔄**
