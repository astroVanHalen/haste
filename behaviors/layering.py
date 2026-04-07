import random
from scenario_engine.behaviors.base import Behavior


class LayeringBehavior(Behavior):
    def __init__(self, constraints):
        super().__init__(constraints)

        overrides = constraints.trainer_overrides or {}

        self.cluster_probability = overrides.get("layering_cluster_probability", 0.25)
        self.max_clusters = overrides.get("layering_max_clusters", 2)
        self.cluster_gap_days = overrides.get("layering_cluster_gap_days", 1)

        self._clusters_created = 0
        self._last_cluster_day = None

    def applies(self, context):
        day = context["day_index"]

        if self._clusters_created >= self.max_clusters:
            return False

        if self._last_cluster_day is not None:
            if day - self._last_cluster_day <= self.cluster_gap_days:
                return True

        return random.random() < self.cluster_probability

    def apply(self, txn, context):
        day = context["day_index"]

        self._clusters_created += 1
        self._last_cluster_day = day

        # IMPORTANT: Do NOT hardcode laundering labels
        # Only subtly change description / semantics
        txn["description"] = txn.get("description", "") or "Account activity"

        # Optional subtle type shift ONLY if allowed
        if "Internal Transfer" in self.constraints.transaction_types:
            txn["transaction_type"] = "Internal Transfer"
