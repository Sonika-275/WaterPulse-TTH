import streamlit as st
from constants import months

def format_rupees(amount: float) -> str:
    if amount >= 100_000:
        return f"₹{amount / 100_000:.1f}L"
    if amount >= 1_000:
        return f"₹{int(amount / 1_000)}K"
    return f"₹{int(amount)}"


def render_cost_card(results: dict, month: int):

    month_name = months[month]

    if results["deficit"] == 0:
        st.success(f"✅ No tankers needed in {month_name}")
        return

    tankers = results["tankers_needed"]

    st.subheader(f"💰 Tanker Cost Comparison — {month_name}")

    col1, col2 = st.columns(2)

    # AFTER (panic)
    with col1:
        st.error("After Zero (Panic)")
        st.write(f"Water shortage: {results['deficit']}")
        st.write(f"Tankers: {tankers}")
        st.metric("Monthly Cost", format_rupees(results["advance_monthly_cost"]))
        st.metric("Annual Cost", format_rupees(results["advance_annual_cost"]))

    # BEFORE (planned)
    with col2:
        st.info("Before Zero (Planned)")
        st.write(f"Water shortage: {results['deficit']}")
        st.write(f"Tankers: {tankers}")
        st.metric("Monthly Cost", format_rupees(results["emergency_monthly_cost"]))
        st.metric("Annual Cost", format_rupees(results["emergency_annual_cost"]))

    # savings
    st.success(
        f"💡 Save {format_rupees(results['monthly_saving'])}/month "
        f"({format_rupees(results['annual_saving'])}/year)"
    )
