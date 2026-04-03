from scenario_engine.behaviors.base import Behavior

class VelocityDrift(Behavior):
    def apply(self, txn, context):
        day = context["day_index"]
        total = context["total_days"]
        multiplier = 1 + (0.35 * (day / total))
        txn["amount"] = round(txn["amount"] * multiplier, 2)
