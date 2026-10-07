# Author: Brenden Canale
# Business_Rules.py

APPROVAL_LIMIT = 1000


def calculate_total(amount: float, quantity: int) -> float:
    """Return total cost including 7% tax"""
    return amount * quantity * 1.07


def requires_review(amount: float) -> bool:
    """Reutrn True if amount exceeds the approval limit"""
    return amount > 1000


def get_approval_tier(amount: float) -> str:
    """Return approval routing tier for a given amount."""
    if amount <= 500:
        return "auto"
    elif amount <= 2000:
        return "manager"
    else:
        return "director"


def apply_discount(amount: float, pct: float) -> float:
    """Return price after discount. pct is 0-100."""
    return amount * (1 - pct / 100)
