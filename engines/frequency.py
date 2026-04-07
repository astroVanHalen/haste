import random


def should_generate(context):
    constraints = context["constraints"]
    overrides = constraints.trainer_overrides or {}
    day = context["day_index"]

    # ------------------------------------
    # Dormancy window (explicit, highest priority)
    # ------------------------------------
    dormancy_start = overrides.get("dormancy_start_day")
    dormancy_end = overrides.get("dormancy_end_day")

    if dormancy_start is not None and dormancy_end is not None:
        if dormancy_start <= day <= dormancy_end:
            return False

    # ------------------------------------
    # Probabilistic dormancy (secondary)
    # ------------------------------------
    dormancy_prob = overrides.get("dormancy_probability", 0.0)
    if dormancy_prob > 0 and random.random() < dormancy_prob:
        return False

    # ------------------------------------
    # Base frequency logic
    # ------------------------------------
    avg = max(0.0, min(1.0, constraints.avg_txns_per_day))
    return random.random() < avg
