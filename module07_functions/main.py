from business_rules import (
    calculate_total,
    requires_review,
    get_approval_tier,
    apply_discount,
)


price, qty = 450.00, 3
total = calculate_total(price, qty)


print(f"Total: ${total:.2f}")
print(f"Requires review:{requires_review(total)}")
print(f"Approval tier: {get_approval_tier(total)}")
print(f"10% discount applied: ${apply_discount(price, 10):.2f}")
