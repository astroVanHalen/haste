# AML Training Scenario Design Guide (Trainer Reference)

## PURPOSE
This document explains how AML training scenarios are structured, what information matters, and how to request scenarios from an AI agent or provide test cases.

You do NOT need to understand JSON deeply to use this system successfully.

---

## WHAT A SCENARIO REPRESENTS

Each scenario simulates:
- One real-world customer
- One AML alert
- One set of transactions that triggered the alert

Analysts will review these scenarios to:
- Compare activity to expected behavior
- Identify red flags
- Consider mitigating factors
- Decide whether to close or escalate the alert

---

## SCENARIO COMPONENTS (CONCEPTUAL)

### Customer
Represents who the person or business is:
- Identity details
- Occupation or industry
- Risk rating
- Expected financial behavior

### Accounts
Represents how the customer banks:
- Checking, savings, business accounts
- One account is marked as primary
- Open dates must be realistic

### Alert
Represents why the analyst is reviewing activity:
- Alert type (e.g., Structuring, Wire Activity)
- Review period (what time window matters)
- Prior alert/SAR history

### Transactions
Represents what actually happened:
- Cash deposits
- Wires
- ACH transfers
- Must align with the alert type and customer profile

### Analyst Instructions
Guides what the trainee should focus on:
- Why the scenario exists
- What red flags to identify
- What a reasonable conclusion might be

---

## HOW TRAINERS SHOULD REQUEST SCENARIOS

When asking an AI to generate scenarios, specify:

- Alert Type  
  (e.g., Incoming Cash Structuring)

- Customer Type  
  (Individual, Sole Proprietor, Business)

- Risk Level  
  (Low, Medium, High)

- Red Flags  
  (e.g., cash just below $10k, foreign wires)

- Mitigating Factors  
  (e.g., cash-intensive business)

- Training Objective  
  (What skill the analyst should practice)

Example request:
> “Generate a medium-risk cash structuring scenario for a sole proprietor with mitigating factors, suitable for junior analysts.”

---

## IMPORTANT RULES FOR TRAINERS

- One file = one scenario
- Scenarios should be realistic, not extreme
- Red flags should require judgment, not be obvious
- Mitigating factors should be plausible, not exculpatory
- Analysts should reasonably debate the outcome

---

## WHAT TRAINERS SHOULD NOT DO

- Do not edit scenario JSON in Excel
- Do not manually change field names
- Do not include commentary inside scenario files
- Do not create multiple alerts in one scenario

---

## QUALITY CHECK QUESTIONS

Before approving a scenario, ask:
- Does the activity make sense for this customer?
- Are the red flags subtle but detectable?
- Is the outcome arguable, not obvious?
- Would this be confusing for a new analyst?

If yes, it is a good training scenario.

---

## HOW SCENARIOS ARE USED

Scenarios are:
- Loaded into the system via JSON import
- Presented to analysts through the dashboard
- Reviewed using the alert workbench
- Used to practice investigative judgment

Trainers do NOT need to interact with the backend after import.

---

## SUMMARY

- Trainers define *learning goals*
- AI generates *structured scenarios*
- The system enforces *data integrity*
- Analysts practice *realistic decision-making*

This separation allows scalable, consistent, and high-quality AML training.
