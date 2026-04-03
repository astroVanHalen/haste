SEASONALITY = {
    1: 0.9,
    2: 0.95,
    3: 1.0,
    4: 1.05,
    5: 1.1,
    6: 1.15,
    7: 1.2,
    8: 1.15,
    9: 1.1,
    10: 1.05,
    11: 1.0,
    12: 0.95
}

def apply_seasonality(amount, context):
    month = context["date"].month
    return round(amount * SEASONALITY.get(month, 1.0), 2)
