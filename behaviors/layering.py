import random
from scenario_engine.behaviors.base import Behavior

class LayeringBehavior(Behavior):
    def applies(self, context):
        return random.random() < 0.3

    def apply(self, txn, context):
        txn["transaction_type"] = "Internal Transfer"
        txn["description"] = "Account movement"
