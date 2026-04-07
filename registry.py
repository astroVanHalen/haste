"""
This is where we convert risk intent into runtime behavior
Risk ≠ behavior
Risk is abstract.
Behavior is observable.
"""

from scenario_engine.behaviors.velocity_drift import VelocityDrift
from scenario_engine.behaviors.counterparty_reuse import CounterpartyReuse
from scenario_engine.behaviors.structuring import StructuringBehavior
from scenario_engine.behaviors.layering import LayeringBehavior

BEHAVIOR_MAP = {
    "undeclared_secondary_income": [VelocityDrift(), CounterpartyReuse()],
    "structuring_near_threshold": [StructuringBehavior()],
    "layering_behavior": [VelocityDrift(), LayeringBehavior()],
}


def load_behaviors(constraints):
    behaviors = []
    for intent in constraints.risk_signal_intent:
        for behavior_cls in BEHAVIOR_MAP.get(intent, []):
            behaviors.append(behavior_cls(constraints))
    return behaviors
