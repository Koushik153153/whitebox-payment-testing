from payment import process_payment


def test_invalid_amount():
    assert process_payment(-100, True, False) == "Invalid Amount"


def test_card_declined():
    assert process_payment(500, False, False) == "Card Declined"


def test_fraud_only():
    assert process_payment(500, True, True) == "Transaction Blocked"


def test_high_value_only():
    assert process_payment(15000, True, False) == "Manual Verification Required"


def test_fraud_and_high_value():
    assert process_payment(15000, True, True) == "Transaction Blocked"


def test_normal_transaction():
    assert process_payment(500, True, False) == "Payment Successful"


def test_boundary_value():
    assert process_payment(10000, True, False) == "Payment Successful"


def test_return_score_feature():
    decision, score = process_payment(
        500,
        True,
        True,
        return_score=True
    )

    assert decision == "Transaction Blocked"
    assert score == 70