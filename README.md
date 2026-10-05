# Risk-Based White-Box Testing of Online Payment Processing System

## Project Overview

This project implements an online payment processing module with a configurable risk engine.

The system analyzes transaction amount, card validity, fraud status, and configurable risk parameters to determine the payment decision.

## Payment Decisions

The system can produce:

- Payment Successful
- Manual Verification Required
- Transaction Blocked
- Invalid Amount
- Card Declined

## Technologies Used

- Python
- PyTest
- Radon
- Coverage.py

## Terminal Implementation

### Run the tests

```bash
pytest -v