
# SCENARIO_TRAINER_GUIDE.md

## Purpose

This guide explains how non-technical trainers use AI-generated scenarios safely and correctly in the AML training platform.

You do **not** need to write code.

---

## High-Level Workflow

1. Ask AI to create a scenario (intent only)
2. Validate the JSON structure
3. (Optional) Add trainer overrides
4. Import the scenario into the app
5. Analysts perform the review

---

## Step-by-Step Instructions

### Step 1 — Ask AI for a Scenario

Use this exact prompt format:

```
Using the SCENARIO_AI_CONTRACT, generate a complete AML training scenario.

Requirements:
- Medium difficulty
- Cash-intensive small business
- Ambiguous activity with mitigating factors

Do NOT create transactions.
Return JSON only.
```

✅ Copy the JSON exactly as returned.

---

### Step 2 — Validate the Scenario

The system uses a schema to ensure scenarios are valid.

If validation fails:
- Do **not** fix it by hand
- Re-run the AI with the error message

---

### Step 3 — (Optional) Add Trainer Overrides

Trainer overrides refine *how the data behaves*, not the conclusion.

Common examples:

```json
"trainer_overrides": {
  "structuring_band_min": 9000,
  "structuring_band_max": 9850,
  "max_structuring_occurrences": 2,
  "dormancy_start_day": 10,
  "dormancy_end_day": 18
}
```

Overrides MUST:
- Limit frequency or magnitude
- Never state or force conclusions

---

### Step 4 — Import the Scenario

Use the import command provided by the app:

```
python manage.py import_scenario_json path/to/scenario.json
```

The system will:
- Generate transactions deterministically
- Reset analyst state if the scenario already exists

---

### Step 5 — Review With Analysts

Analysts will:
- See the customer profile
- Review generated activity
- Write their own narrative
- Reach their own conclusion

There is **no single correct answer**.

---

## Things Trainers Must Never Do

🚫 Write transaction rows
🚫 Label behavior as suspicious
🚫 Edit generated transactions
🚫 Encode the “right” answer

---

## Trainer Mindset (Important)

Your job is to shape **ambiguity**, not clarity.

If analysts can spot the answer quickly, the scenario is too strong.

---

## Summary

- AI writes intent
- Engine writes data
- Trainers guide difficulty
- Analysts supply judgment

This separation keeps training realistic and fair.

