def process_payment(
    amount,
    card_valid,
    fraud_flag,
    fraud_weight=70,
    high_value_weight=30,
    block_threshold=70,
    manual_threshold=30,
    return_score=False
):

    risk_score = 0

    if amount <= 0:
        return "Invalid Amount"

    if not card_valid:
        return "Card Declined"

    if fraud_flag:
        risk_score += fraud_weight

    if amount > 10000:
        risk_score += high_value_weight

    if risk_score >= block_threshold:
        decision = "Transaction Blocked"

    elif risk_score >= manual_threshold:
        decision = "Manual Verification Required"

    else:
        decision = "Payment Successful"

    if return_score:
        return decision, risk_score

    return decision