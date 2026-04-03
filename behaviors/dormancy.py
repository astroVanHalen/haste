import random
from scenario_engine.behaviors.base import Behavior

class DormancyInjection(Behavior):
    def applies(self, context):
        return random.random() < 0.05

    def apply(self, txn, context):
        txn.clear()
