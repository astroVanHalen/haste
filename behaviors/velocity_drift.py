from scenario_engine.behaviors.base import Behavior


class VelocityDrift(Behavior):
    def __init__(self, constraints):
        super().__init__(constraints)

        overrides = constraints.trainer_overrides or {}

        # When does the velocity ramp begin?
        self.ramp_start_day = overrides.get("velocity_ramp_start_day", 0)

        # Maximum total multiplier applied by the end
        self.max_multiplier = overrides.get("velocity_max_multiplier", 1.35)

        # Optional cap on how many txns per day this applies to
        self.max_daily_txns = overrides.get("velocity_max_daily_txns", None)

        self._daily_count = {}

    def applies(self, context):
        day = context["day_index"]

        if day < self.ramp_start_day:
            return False

        if self.max_daily_txns is not None:
            date = context["date"]
            self._daily_count.setdefault(date, 0)
            if self._daily_count[date] >= self.max_daily_txns:
                return False

            self._daily_count[date] += 1

        return True

    def apply(self, txn, context):
        day = context["day_index"]
        total = context["total_days"]

        effective_days = max(total - self.ramp_start_day, 1)
        relative_day = max(day - self.ramp_start_day, 0)

        multiplier = 1 + ((self.max_multiplier - 1) * (relative_day / effective_days))

        txn["amount"] = round(txn["amount"] * multiplier, 2)
