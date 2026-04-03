import random

MEMO_LIBRARY = {
    "casual_service_like": [
        "Thanks",
        "Weekly help",
        "Session",
        "Consult",
        "Support",
        "Appreciate it"
    ],
    "casual_personal": [
        "Dinner",
        "Help",
        "Gift",
        "Reimbursement"
    ]
}

def apply_memo(txn, context):
    style = context["constraints"].memo_style
    memo = random.choice(MEMO_LIBRARY.get(style, ["Transfer"]))
    txn["description"] = f"{txn['transaction_type']} - {memo}"
