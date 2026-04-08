
# SCENARIO_AGENT.md

## Purpose

This document is the minimal contract provided to AI systems (Copilot / LLMs) to generate **valid AML training scenarios**.

The AI's role is to describe **intent and structure**, never transactions.

---

## AI Responsibilities (Hard Rules)

The AI MUST:
- Output **valid JSON only**
- Match the required schema exactly
- Describe intent, constraints, and narrative only

The AI MUST NOT:
- Create individual transactions
- Encode conclusions (e.g., "this is structuring")
- Guess schema fields
- Add commentary outside JSON

---

## Required JSON Sections

The AI must populate:

- `scenario_id`
- `difficulty_level`
- `customer`
- `accounts`
- `alert`
- `transaction_constraints`
- `analyst_instructions`

No other top-level keys are permitted.

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

## Transaction Constraints

`transaction_constraints` describe **how transactions behave**, not what happened.

Required fields:
- time_horizon_days
- avg_txns_per_day
- transaction_types
- amount_range
- velocity_pattern
- counterparty_behavior
- memo_style
- seasonality
- risk_signal_intent

Optional:
- trainer_overrides (leave empty unless instructed)

---

## Analyst Instructions

Instructions must:
- Frame analysis objectives
- Identify focus areas
- Describe what a good narrative looks like

They must NOT:
- State conclusions
- Explain generator mechanics
- Reveal risk type as fact

---

## Output Rules

✅ Return JSON only
✅ No markdown
✅ No explanations
✅ No comments

Invalid output should be regenerated.

---
