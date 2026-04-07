import random

MEMO_LIBRARY = {
    "casual_service_like": [
        "Thanks",
        "Weekly help",
        "Session",
        "Consult",
        "Support",
        "Appreciate it",
    ],
    "casual_personal": ["Dinner", "Help", "Gift", "Reimbursement"],
}


def apply_memo(txn, context):
    style = context["constraints"].memo_style
    if style not in MEMO_LIBRARY:
        style = "casual_service_like"

    memo = random.choice(MEMO_LIBRARY[style])

    # Only apply memo if not already set by a behavior
    if not txn.get("description"):
        txn["description"] = f"{txn['transaction_type']} - {memo}"
