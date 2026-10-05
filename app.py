import streamlit as st
from payment import process_payment


st.set_page_config(
    page_title="Advanced Payment Processing Dashboard",
    page_icon="💳",
    layout="wide"
)


# =========================================================
# SESSION STATE
# =========================================================

if "transaction_history" not in st.session_state:
    st.session_state.transaction_history = []


# =========================================================
# TITLE
# =========================================================

st.title("💳 Advanced Payment Processing Dashboard")
st.subheader("White-Box Testing Demonstration with Risk Engine")


# =========================================================
# COLUMNS
# =========================================================

left_col, right_col = st.columns([1, 2])


# =========================================================
# LEFT SIDE - INPUTS
# =========================================================

with left_col:

    st.header("Transaction Input")

    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )

    card_valid = st.checkbox(
        "Card Valid",
        value=True
    )

    fraud_flag = st.checkbox(
        "Fraud Suspected",
        value=False
    )

    st.subheader("⚙️ Risk Configuration")

    fraud_weight = st.slider(
        "Fraud Weight",
        min_value=0,
        max_value=100,
        value=70
    )

    high_value_weight = st.slider(
        "High Value Weight",
        min_value=0,
        max_value=100,
        value=30
    )

    block_threshold = st.slider(
        "Block Threshold",
        min_value=0,
        max_value=100,
        value=70
    )

    manual_threshold = st.slider(
        "Manual Threshold",
        min_value=0,
        max_value=100,
        value=30
    )

    process_button = st.button("Process Payment")


# =========================================================
# RIGHT SIDE - RESULTS
# =========================================================

with right_col:

    st.header("Transaction Status")

    if process_button:

        decision, risk_score = process_payment(
            amount,
            card_valid,
            fraud_flag,
            fraud_weight,
            high_value_weight,
            block_threshold,
            manual_threshold,
            return_score=True
        )

        # -----------------------------
        # Transaction Status
        # -----------------------------

        if decision == "Payment Successful":
            st.success(decision)

        elif decision == "Manual Verification Required":
            st.warning(decision)

        elif decision == "Transaction Blocked":
            st.error(decision)

        else:
            st.error(decision)

        # -----------------------------
        # Risk Score
        # -----------------------------

        st.subheader("Risk Score")

        st.metric(
            label="Final Risk Score",
            value=risk_score
        )

        # -----------------------------
        # Execution Trace
        # -----------------------------

        st.subheader("Execution Trace (White-Box View)")

        st.write("• Base Risk Score: 0")

        if amount <= 0:

            st.write("• Invalid transaction amount detected")

        elif not card_valid:

            st.write("• Card validation failed")

        else:

            if fraud_flag:
                st.write(
                    f"• Fraud detected → Risk +{fraud_weight}"
                )
            else:
                st.write(
                    "• Fraud check → No fraud detected"
                )

            if amount > 10000:
                st.write(
                    f"• High-value transaction → Risk +{high_value_weight}"
                )
            else:
                st.write(
                    "• High-value check → Normal transaction amount"
                )

            st.write(
                f"• Final Risk Score: {risk_score}"
            )

            st.write(
                f"• Block Threshold: {block_threshold}"
            )

            st.write(
                f"• Manual Threshold: {manual_threshold}"
            )

            if risk_score >= block_threshold:
                st.write("• Decision: Transaction Blocked")

            elif risk_score >= manual_threshold:
                st.write("• Decision: Manual Verification Required")

            else:
                st.write("• Decision: Payment Successful")

        # =================================================
        # SAVE TRANSACTION
        # =================================================

        transaction = {
            "Amount": amount,
            "Card": "Valid" if card_valid else "Invalid",
            "Fraud": "Yes" if fraud_flag else "No",
            "Risk Score": risk_score,
            "Decision": decision
        }

        st.session_state.transaction_history.append(transaction)

    else:

        st.info(
            "Enter transaction details and click Process Payment."
        )


# =========================================================
# TRANSACTION HISTORY
# =========================================================

st.divider()

st.header("📊 Transaction History")

if st.session_state.transaction_history:

    st.dataframe(
        st.session_state.transaction_history,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No transactions processed yet.")

# =========================================================
# WHITE-BOX TESTING ANALYSIS
# =========================================================

st.divider()

st.header("🔬 White-Box Testing Analysis")

st.write(
    "Run the automated white-box analysis to verify "
    "complexity, test execution, and code coverage."
)

if st.button("Run White-Box Analysis"):

    import subprocess
    import sys
    import re

    # -----------------------------------------------------
    # 1. Run PyTest
    # -----------------------------------------------------

    pytest_result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "-q"
        ],
        capture_output=True,
        text=True
    )

    pytest_output = pytest_result.stdout + pytest_result.stderr

    # Extract number of passed tests
    passed_match = re.search(
        r"(\d+)\s+passed",
        pytest_output
    )

    passed_tests = (
        int(passed_match.group(1))
        if passed_match
        else 0
    )

    # -----------------------------------------------------
    # 2. Run Radon
    # -----------------------------------------------------

    radon_result = subprocess.run(
        [
            "radon",
            "cc",
            "payment.py",
            "-s"
        ],
        capture_output=True,
        text=True
    )

    radon_output = radon_result.stdout + radon_result.stderr

    # Extract complexity
    complexity_match = re.search(
        r"\((\d+)\)",
        radon_output
    )

    complexity = (
        int(complexity_match.group(1))
        if complexity_match
        else 0
    )

    # -----------------------------------------------------
    # 3. Run Coverage
    # -----------------------------------------------------

    coverage_run = subprocess.run(
        [
            sys.executable,
            "-m",
            "coverage",
            "run",
            "-m",
            "pytest",
            "-q"
        ],
        capture_output=True,
        text=True
    )

    coverage_result = subprocess.run(
        [
            sys.executable,
            "-m",
            "coverage",
            "report"
        ],
        capture_output=True,
        text=True
    )

    coverage_output = (
        coverage_result.stdout
        + coverage_result.stderr
    )

    # Extract payment.py coverage
    coverage_match = re.search(
        r"payment\.py\s+\d+\s+\d+\s+(\d+)%",
        coverage_output
    )

    coverage_percentage = (
        int(coverage_match.group(1))
        if coverage_match
        else 0
    )

    # -----------------------------------------------------
    # 4. Display Results
    # -----------------------------------------------------

    st.subheader("Analysis Results")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Cyclomatic Complexity",
            complexity
        )

    with col2:
        st.metric(
            "Independent Paths",
            complexity
        )

    with col3:
        st.metric(
            "Tests Passed",
            passed_tests
        )

    with col4:
        st.metric(
            "Statement Coverage",
            f"{coverage_percentage}%"
        )

    # -----------------------------------------------------
    # 5. Detailed Results
    # -----------------------------------------------------

    st.subheader("PyTest Result")

    if passed_tests > 0:
        st.success(
            f"{passed_tests} test cases passed successfully."
        )
    else:
        st.error("PyTest execution failed.")

    st.subheader("Radon Complexity Result")

    st.code(
        radon_output,
        language="text"
    )

    st.subheader("Coverage Result")

    st.code(
        coverage_output,
        language="text"
    )