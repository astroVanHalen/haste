import json
import argparse
from datetime import date
from pathlib import Path

from scenario_engine.constraints import TransactionConstraints
from scenario_engine.generator import TransactionGenerator


def main():
    parser = argparse.ArgumentParser(
        description="Generate AML training transactions and append to scenario JSON"
    )
    parser.add_argument(
        "scenario_json", help="Path to AI-authored scenario JSON (e.g. ALERT.raw.json)"
    )
    parser.add_argument(
        "--start-date",
        required=True,
        help="Start date for transaction generation (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--output", help="Optional output file path (defaults to *.generated.json)"
    )

    args = parser.parse_args()

    input_path = Path(args.scenario_json)

    if not input_path.exists():
        raise FileNotFoundError(f"Scenario file not found: {input_path}")

    # -------------------------------------------------
    # Load raw scenario JSON
    # -------------------------------------------------
    with input_path.open("r", encoding="utf-8") as f:
        scenario = json.load(f)

    # Guardrail: never generate on files that already contain transactions
    if "transactions" in scenario:
        raise RuntimeError(
            "Input scenario already contains transactions. "
            "Use the *.raw.json file as input."
        )

    tc_data = scenario["transaction_constraints"]

    # -------------------------------------------------
    # Build TransactionConstraints
    # -------------------------------------------------
    constraints = TransactionConstraints(
        time_horizon_days=tc_data["time_horizon_days"],
        avg_txns_per_day=tc_data["avg_txns_per_day"],
        transaction_types=tc_data["transaction_types"],
        amount_range=tuple(tc_data["amount_range"]),
        velocity_pattern=tc_data["velocity_pattern"],
        counterparty_behavior=tc_data["counterparty_behavior"],
        memo_style=tc_data["memo_style"],
        seasonality=tc_data.get("seasonality", "none"),
        primary_risk=scenario["primary_risk"],
        risk_signal_intent=tc_data["risk_signal_intent"],
        trainer_overrides=tc_data.get("trainer_overrides"),
        seed=tc_data.get("seed", 42),
        noise_level=tc_data.get("noise_level", 0.0),
        weekend_multiplier=tc_data.get("weekend_multiplier", 1.0),
    )

    # -------------------------------------------------
    # Generate transactions
    # -------------------------------------------------
    generator = TransactionGenerator(constraints)
    transactions = generator.generate(start_date=date.fromisoformat(args.start_date))

    # -------------------------------------------------
    # Append transactions to original scenario
    # -------------------------------------------------
    generated_scenario = {
        **scenario,
        "transactions": transactions,
    }

    # -------------------------------------------------
    # Determine output path
    # -------------------------------------------------
    if args.output:
        output_path = Path(args.output)
    else:
        # Default: ALERT.raw.json -> ALERT.generated.json
        output_path = (
            input_path.parent
            / "app/TestRuns"
            / input_path.with_name(
                input_path.name.replace(".raw.json", ".generated.json")
            )
        )

    # -------------------------------------------------
    # Write generated scenario
    # -------------------------------------------------
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(generated_scenario, f, indent=2)

    print(
        f"✅ Generated {len(transactions)} transactions\n"
        f"📄 Output written to: {output_path}"
    )


if __name__ == "__main__":
    main()
