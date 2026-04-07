
# ENUM_TIGHTENING_NOTES.md

The following fields should ONLY accept enumerated values.

velocity_pattern:
- flat
- gradual_increase
- threshold_avoidant

seasonality:
- none
- moderate
- strong

memo_style:
- casual_service_like
- casual_personal

counterparty_behavior:
- single_counterparty
- small_recurring_group

Any other value must be rejected by schema or validation.
