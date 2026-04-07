
# TRAINER_OVERRIDE_CHEATSHEET.md

Trainer overrides adjust difficulty WITHOUT revealing answers.

---

STRUCTURING OVERRIDES

structuring_band_min       → Lower bound for near-threshold amounts
structuring_band_max       → Upper bound for near-threshold amounts
max_structuring_occurrences → Max number of such events

Example:
"structuring_band_min": 9000
"structuring_band_max": 9800
"max_structuring_occurrences": 2

---

VELOCITY OVERRIDES

velocity_ramp_start_day    → Day index when increase begins
velocity_max_multiplier   → Max total drift
velocity_max_daily_txns   → Cap per day

---

DORMANCY OVERRIDES

dormancy_start_day         → First quiet day
dormancy_end_day           → Last quiet day
dormancy_probability       → Random quiet days

---

COUNTERPARTY OVERRIDES

counterparty_pool          → Allowed names/accounts

---

RULES

✅ Overrides LIMIT behavior
❌ Overrides must NEVER force conclusions
❌ Overrides must NEVER label risk

---

If analysts can guess the answer from data alone, tone it down.
