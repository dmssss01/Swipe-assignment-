import json


def clean_number(value: str) -> float:
    return float(value.replace(",", ""))


def clean_int(value: str) -> int:
    return int(value.replace(",", ""))


def format_to_json(res) -> str:
    customer_details = res.customer_details.model_dump()
    items = [item.model_dump() for item in res.items]
    total_amount = res.total_amount.model_dump()

    result = {
        "customer_details": customer_details,
        "items": items,
        "total_amount": total_amount,
    }

    return json.dumps(result, indent=4)
