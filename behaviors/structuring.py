import random
from scenario_engine.behaviors.base import Behavior


class StructuringBehavior(Behavior):
    def __init__(self, constraints):
        super().__init__(constraints)

        min_amt, max_amt = constraints.amount_range

        # Validate scenario realism
        if max_amt < 5000:
            raise ValueError("StructuringBehavior requires realistic cash thresholds")

        self.band_min = constraints.trainer_overrides.get(
            "structuring_band_min", max(min_amt, 8500)
        )
        self.band_max = constraints.trainer_overrides.get(
            "structuring_band_max", min(max_amt, 9900)
        )

        self.max_occurrences = constraints.trainer_overrides.get(
            "max_structuring_occurrences", None
        )

        self._applied_count = 0

    def applies(self, context):
        # Stop if trainer-specified limit reached
        if self.max_occurrences is not None:
            if self._applied_count >= self.max_occurrences:
                return False

        # Default: probabilistic but subtle
        return random.random() < 0.15

    def apply(self, txn, context):
        self._applied_count += 1

        txn["amount"] = round(random.uniform(self.band_min, self.band_max), 2)
