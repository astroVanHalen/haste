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
    "undeclared_secondary_income": [VelocityDrift, CounterpartyReuse],
    "structuring_near_threshold": [StructuringBehavior],
    "layering_behavior": [VelocityDrift, LayeringBehavior],
}


def load_behaviors(constraints):
    """
    Instantiate only the behaviors relevant to the scenario's primary risk.
    """
    behaviors = []

    risk_key = constraints.primary_risk

    behavior_classes = BEHAVIOR_MAP.get(risk_key, [])

    for behavior_cls in behavior_classes:
        if "constraints" not in behavior_cls.__init__.__code__.co_varnames:
            raise RuntimeError(
                f"{behavior_cls.__name__} does not accept `constraints` in __init__"
            )
        behaviors.append(behavior_cls(constraints))

    return behaviors
