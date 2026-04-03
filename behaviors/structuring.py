import random
from scenario_engine.behaviors.base import Behavior

class StructuringBehavior(Behavior):
    def applies(self, context):
        return random.random() < 0.2

    def apply(self, txn, context):
        txn["amount"] = round(random.uniform(8800, 9900), 2)
