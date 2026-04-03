import random
from scenario_engine.engines.frequency import should_generate
from scenario_engine.engines.memo import apply_memo
from scenario_engine.engines.seasonality import apply_seasonality
from scenario_engine.registry import load_behaviors
from scenario_engine.utils import seed_random

class TransactionGenerator:
    def __init__(self, constraints):
        self.constraints = constraints
        seed_random(constraints.seed)
        self.behaviors = load_behaviors(constraints)

    def generate(self, start_date):
        transactions = []

        for day in range(self.constraints.time_horizon_days):
            context = self.constraints.context(
                day,
                self.constraints.time_horizon_days,
                start_date
            )

            if not should_generate(context):
                continue

            min_amt, max_amt = self.constraints.amount_range
            amount = round(random.uniform(min_amt, max_amt), 2)

            txn = {
                "transaction_date": context["date"].isoformat(),
                "transaction_type": random.choice(
                    self.constraints.transaction_types
                ),
                "amount": amount,
                "description": ""
            }

            for behavior in self.behaviors:
                if behavior.applies(context):
                    behavior.apply(txn, context)

            if not txn:
                continue

            txn["amount"] = apply_seasonality(txn["amount"], context)
            apply_memo(txn, context)
            transactions.append(txn)

        return transactions
