## Running the Generator via CLI

The command-line interface (CLI) is the **primary and supported way** to run `scenario_engine`.

The CLI consumes a **transaction constraints JSON file**, a **start date**, and produces a **transactions JSON file** suitable for merging into a full scenario prior to import into the training application.

---

### Basic CLI Usage

Run the CLI **from the project root directory** (the parent directory containing `scenario_engine`).

```bash
python -m scenario_engine.cli <path-to-constraints.json> --start-date YYYY-MM-DD --output <output-file>
```

---

### Example

```bash
python -m scenario_engine.cli scenarios/l2_undeclared_income/constraints.json --start-date 2026-01-01 --output scenarios/l2_undeclared_income/transactions.json
```

This command generates a `transactions.json` file containing all transactions derived from the supplied constraints.

---

### Output Format

The CLI always emits a single JSON object with this structure:

```json
{
  "transactions": [
    {
      "transaction_date": "2026-01-01",
      "transaction_type": "P2P Credit",
      "amount": 78.23,
      "description": "P2P Credit - Weekly help - Alex"
    }
  ]
}
```

This output is designed to be merged with a scenario JSON prior to running the scenario import command.

---

## Start Date vs Time Horizon

The generator does **not** assume the current date.

- `--start-date` determines **when generation begins**
- `time_horizon_days` in the constraints file determines **how long generation runs**

Example:

- Start date: `2026-01-01`
- Time horizon: `365`

This yields transactions dated:

```
2026-01-01 through 2026-12-31
```

No future-dated transactions are generated unless a future start date is explicitly provided.

---

## Behavior Plug-ins

Behavior plug-ins define **how patterns emerge** across the transaction timeline.

Examples include:

- Gradual velocity drift
- Recurring counterparty activity
- Near-threshold structuring behavior
- Layering or internal movement
- Dormant periods with no activity

Behavior characteristics:

- Modular
- Composable
- Selected by `risk_signal_intent`
- Applied deterministically when a seed is provided

---

### Adding a New Behavior

To add a behavior plug-in:

1. Create a new file in `scenario_engine/behaviors/`
2. Implement the `applies(context)` and `apply(txn, context)` methods
3. Register the behavior in `registry.py`

No changes to the core generator logic are required.

---

## Determinism and Seeds

Transaction generation is **deterministic by default**.

- Controlled by the `seed` field in the constraints file
- Identical constraints and seed values produce identical output
- Changing only the seed produces a controlled variation of the same scenario

This supports:

- Reproducibility
- Stable answer keys
- Consistency across training cohorts

---

## Using the Generator with Containers (Podman or Docker)

The CLI behaves identically inside containers.

```bash
python -m scenario_engine.cli scenarios/l2_undeclared_income/constraints.json --start-date 2026-01-01 --output scenarios/l2_undeclared_income/transactions.json
```

The generator is:

- Stateless
- File-based
- Safe to execute in Podman or Docker
- Independent of Django and database state

---

## Common Errors and Fixes

### ModuleNotFoundError: scenario_engine

Cause: Running the CLI from inside the `scenario_engine/` directory.

Fix:

- Run the command from the parent directory
- Ensure `scenario_engine/__init__.py` exists
- On Windows, ensure `PYTHONPATH=.` is set if needed

---

## Intended Usage Rules

- Do not generate raw transactions using AI
- Constraints describe behavior, not transaction data
- The generator is the only component that creates transactions
- The generator must remain independent of Django models
- Prefer multiple simple behaviors instead of complex monolithic logic

---

## Summary

The CLI forms the contract between **scenario intent** and **deterministic transaction data**.

Changing constraints changes behavior.
