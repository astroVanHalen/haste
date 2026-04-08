"""
TransactionConstraints is not a config file, a rule engine, or a generator.
It is a formal declaration of behavioral intent, frozen at import time.
"""

from dataclasses import dataclass
from datetime import date, timedelta
from typing import List, Tuple, Dict, Any, Optional


@dataclass
class TransactionConstraints:
    """
    Canonical constraint object emitted by the AI agent
    and consumed by the transaction generator.

    This class defines WHAT behavior should exist,
    not HOW it is implemented.
    """

    # --- Time & volume ---
    time_horizon_days: int
    avg_txns_per_day: float

    # --- Transaction makeup ---
    transaction_types: List[str]
    amount_range: Tuple[float, float]

    # --- Behavioral patterns ---
    velocity_pattern: str  # e.g. flat, gradual_increase
    counterparty_behavior: str  # e.g. small_recurring_group
    memo_style: str  # e.g. casual_service_like
    seasonality: str  # none, moderate, strong

    # --- Risk classification (scenario-level) ---
    primary_risk: str  # e.g. "cash_structuring"

    # --- Risk intent ---
    risk_signal_intent: List[str]  # e.g. ["undeclared_secondary_income"]

    # --- Trainer overrides (optional fine-tuning) ---
    trainer_overrides: Optional[Dict[str, Any]] = None
    # --- Reproducibility ---
    seed: int = 42

    # --- Optional noise / tuning ---
    noise_level: float = 0.0  # ± percentage variance (e.g. 0.15 = ±15%)
    weekend_multiplier: float = 1.0  # Adjust amounts on weekends if desired

    def context(
        self, day_index: int, total_days: int, start_date: date
    ) -> Dict[str, Any]:
        """
        Build a context dictionary for a single simulation day.
        This context is passed to all engines and behaviors.

        NOTHING in behaviors should need direct access to raw JSON.
        """

        current_date = start_date + timedelta(days=day_index)

        return {
            "day_index": day_index,
            "total_days": total_days,
            "date": current_date,
            "is_weekend": current_date.weekday() >= 5,
            "constraints": self,
        }

    def base_transaction_template(self, txn_type: str) -> Dict[str, Any]:
        """
        Produce the minimal transaction skeleton
        that behaviors will mutate.

        No behavior logic belongs here.
        """

        return {
            "transaction_date": None,  # Filled by generator
            "transaction_type": txn_type,
            "amount": 0.00,
            "description": "",
        }
