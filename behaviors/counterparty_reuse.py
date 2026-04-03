import random
from scenario_engine.behaviors.base import Behavior

class CounterpartyReuse(Behavior):
    def __init__(self):
        self.counterparties = ["Alex", "Jamie", "Riley", "Morgan", "Taylor"]

    def apply(self, txn, context):
        name = random.choice(self.counterparties)
        txn["description"] += f" - {name}"
