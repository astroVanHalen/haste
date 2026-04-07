import random
from scenario_engine.behaviors.base import Behavior


class CounterpartyReuse(Behavior):
    def __init__(self, constraints):
        super().__init__(constraints)

        # Default name pool
        self.counterparties = ["Alex", "Jamie", "Riley", "Morgan", "Taylor"]

        # Optional trainer override
        overrides = getattr(constraints, "trainer_overrides", {}) or {}

        if "counterparty_pool" in overrides:
            self.counterparties = overrides["counterparty_pool"]

        if not self.counterparties:
            raise ValueError("CounterpartyReuse requires at least one counterparty")

    def apply(self, txn, context):
        name = random.choice(self.counterparties)
        txn["description"] += f" - {name}"
