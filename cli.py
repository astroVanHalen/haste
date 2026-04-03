import json
import argparse
from datetime import date
from scenario_engine.constraints import TransactionConstraints
from scenario_engine.generator import TransactionGenerator

def main():
    parser = argparse.ArgumentParser(
        description="Generate AML training transactions from constraints"
    )
    parser.add_argument("constraint_json")
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--output", default="transactions.json")

    args = parser.parse_args()

    with open(args.constraint_json, "r") as f:
        data = json.load(f)

    tc_data = data["transaction_constraints"]

    constraints = TransactionConstraints(
        time_horizon_days=tc_data["time_horizon_days"],
        avg_txns_per_day=tc_data["avg_txns_per_day"],
        transaction_types=tc_data["transaction_types"],
        amount_range=tuple(tc_data["amount_range"]),
        velocity_pattern=tc_data["velocity_pattern"],
        counterparty_behavior=tc_data["counterparty_behavior"],
        memo_style=tc_data["memo_style"],
        seasonality=tc_data.get("seasonality", "none"),
        risk_signal_intent=tc_data["risk_signal_intent"],
        seed=tc_data.get("seed", 42)
    )

    generator = TransactionGenerator(constraints)
    transactions = generator.generate(
        start_date=date.fromisoformat(args.start_date)
    )

    with open(args.output, "w") as f:
        json.dump({"transactions": transactions}, f, indent=2)

    print(f"✅ Generated {len(transactions)} transactions")

if __name__ == "__main__":
    main()
