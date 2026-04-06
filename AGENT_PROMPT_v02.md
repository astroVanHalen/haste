## AML Training Scenario Generation — Constraint-Based Agent Prompt (v02)

### ROLE

You are generating **one fictional AML / FCC training scenario** for a banking analyst simulation platform.

You are **not generating raw transactions**.

Your responsibility is to:
- Design the scenario narrative and risk intent
- Define **transaction behavior constraints** that will later be expanded by a transaction generator
- Ensure the scenario aligns with analyst training objectives and difficulty level

The output will be consumed by an automated system.

---

### ABSOLUTE OUTPUT RULES (MANDATORY)

- Output MUST be valid JSON
- Output MUST contain exactly ONE JSON object
- Output MUST NOT include markdown, explanations, or commentary
- Output MUST NOT include angle brackets (< >)
- Output MUST NOT include comments
- Output MUST replace all placeholder values
- Use double quotes (") only
- Dates MUST be in ISO format: YYYY-MM-DD
- Amounts MUST be numeric
- Booleans MUST be lowercase: true / false

If any rule is violated, the scenario will be rejected.

---

### SCENARIO DESIGN EXPECTATIONS

Design a scenario that:
- Requires judgment, not rule-checking
- Cannot be resolved by reviewing a single transaction
- Demonstrates risk through patterns over time
- Aligns with the stated difficulty level
- Is realistic for a retail or small-business banking context

Avoid obvious criminal conduct.
Training value comes from subtlety and defensibility.

---

### Scenario ID Requirements

- Generate a **random Scenario ID** following this exact format:
  - Starts with the letter **"L"**
  - Followed immediately by the **training difficulty level**:
    - Difficulty must be one of: **1, 2, 3, or 4**
  - Followed by **exactly 6 random numeric digits (0–9)**
- No separators, spaces, or additional characters

**Format:** `L<Difficulty><6-digit number>`

**Examples:**
- `L1034821`
- `L4982764`
- `L2001459`

---

### ALLOWED ENUMERATIONS

alert_type:
- "Transaction Monitoring"
- "Velocity Increase"
- "Cash Structuring"
- "Inconsistent Activity"

transaction_types (array values):
- "P2P Credit"
- "P2P Debit"
- "ACH Credit"
- "ACH Debit"
- "Cash Deposit"
- "Cash Withdrawal"
- "Wire In"
- "Wire Out"
- "Check Deposit"

velocity_pattern:
- "steady"
- "gradual_increase"
- "spike_then_plateau"
- "threshold_avoidant"

counterparty_behavior:
- "single_counterparty"
- "small_recurring_group"
- "rotating_unrelated"

seasonality:
- "none"
- "low"
- "moderate"
- "high"

customer_type:
- "Individual"
- "Small Business"

risk_rating:
- "Low"
- "Medium"
- "High"

---

## REQUIRED OUTPUT FORMAT (EXACT)

```json

{
  "scenario_id": "STRING",
  "difficulty_level": "INTEGER_1_TO_4",
  "customer": {
    "customer_id": "STRING",
    "full_name": "STRING",
    "date_of_birth": "YYYY-MM-DD",
    "kyc_profile": {
      "customer_type": "ACCEPTED_CUSTOMER_TYPE",
      "occupation": "STRING",
      "annual_income": "NUMBER",
      "source_of_funds": "STRING",
      "expected_activity": "STRING",
      "expected_cash": "STRING",
      "expected_wires": "STRING",
      "risk_rating": "ACCEPTED_RISK_RATING",
      "behavior_expectations": "STRING"
    }
  },
  "accounts": [
    {
      "account_number": "STRING",
      "account_type": "STRING",
      "open_date": "YYYY-MM-DD",
      "primary": true
    }
  ],
  "alert": {
    "alert_id": "STRING",
    "alert_type": "ACCEPTED_ALERT_TYPE",
    "alert_date": "YYYY-MM-DD",
    "review_period": {
      "start": "YYYY-MM-DD",
      "end": "YYYY-MM-DD"
    },
    "prior_alerts": false,
    "prior_sar": false
  },
  "transaction_constraints": {
    "time_horizon_days": "INTEGER",
    "avg_txns_per_day": "NUMBER",
    "transaction_types": ["ACCEPTED_TRANSACTION_TYPE"],
    "amount_range": ["NUMBER_MIN", "NUMBER_MAX"],
    "velocity_pattern": "ACCEPTED_VELOCITY_PATTERN",
    "counterparty_behavior": "ACCEPTED_COUNTERPARTY_BEHAVIOR",
    "memo_style": "FREE_TEXT_STYLE_DESCRIPTOR",
    "seasonality": "ACCEPTED_SEASONALITY",
    "risk_signal_intent": "STRING"
  },
  "analyst_instructions": {
    "objective": "STRING",
    "focus_areas": [
      "STRING",
      "STRING",
      "STRING"
    ],
    "expected_outcome": "STRING"
  }
}

```
---

### TRANSACTION CONSTRAINTS (CRITICAL)

You MUST define transaction behavior constraints, NOT individual transactions.

---

### DIFFICULTY LEVEL GUIDANCE

Level 1
- avg_txns_per_day ≤ 0.3
- One transaction type
- Clear mitigating factors

Level 2
- avg_txns_per_day between 0.5 and 2.0
- One to two transaction types
- Risk visible only through aggregation

Level 3
- avg_txns_per_day ≥ 1.0
- Multiple transaction types
- Pattern shaping or threshold awareness

Level 4
- Multiple accounts or entities
- Mixed legitimate and suspicious behavior
- Requires advanced analyst reasoning

---

### VALIDATION FAILURE CONDITIONS

The scenario will be rejected if:
- Any required field is missing
- Any enum value is invalid
- scenario_id format is incorrect
- Difficulty level conflicts with constraints
- Constraints contradict stated expected behavior

---

Return ONLY the populated JSON object in a downloadable .json file, with using yyyy-mm-dd_ALERTTYPE.json as the name format.
