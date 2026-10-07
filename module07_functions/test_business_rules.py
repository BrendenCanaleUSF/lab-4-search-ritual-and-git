from business_rules import (
    requires_review,
    calculate_total,
    requires_review,
    get_approval_tier,
    apply_discount,
)


def test_requires_review_over():
    assert requires_review(1500) is True


def test_requires_review_under():
    assert requires_review(500) is False


def test_boundary_at_limit():
    assert requires_review(1000) is False


def test_total_includes_tax():
    assert round(calculate_total(100.0, 2), 2) == 214.00


def test_tier_auto():
    assert get_approval_tier(400) == "auto"


def test_tier_boundary_500():
    assert get_approval_tier(500) == "auto"


def test_tier_manager():
    assert get_approval_tier(1500) == "manager"


def test_discount_ten():
    assert apply_discount(100.00, 10) == 90.0
