import random
from datetime import date


def seed_random(seed: int):
    """
    Seed Python's random module to ensure deterministic output.
    This guarantees reproducibility for the same constraints + seed.
    """
    random.seed(seed)


def is_weekend(d: date) -> bool:
    """
    Returns True if the given date is a Saturday or Sunday.
    Useful for applying weekend-specific behavior or multipliers.
    """
    return d.weekday() >= 5


def clamp(value: float, min_value: float, max_value: float) -> float:
    """
    Clamp a numeric value between min_value and max_value.
    Prevents runaway amounts when multiple behaviors stack.
    """
    return max(min_value, min(value, max_value))


def apply_noise(
    base_value: float,
    noise_level: float = 0.0
) -> float:
    """
    Apply controlled stochastic noise to a number.
    noise_level is expressed as a percentage (e.g., 0.15 = ±15%).
    """
    if noise_level <= 0:
        return base_value

    multiplier = random.uniform(
        1 - noise_level,
        1 + noise_level
    )
    return round(base_value * multiplier, 2)
