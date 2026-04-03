import random

def should_generate(context):
    avg = context["constraints"].avg_txns_per_day
    if avg >= 1:
        return True
    return random.random() < avg
