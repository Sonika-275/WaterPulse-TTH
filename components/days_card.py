import streamlit as st
from constants import months, rainfall_mm

def format_litres(value: float) -> str:
    if value >= 100_000:
        return f"{value / 100_000:.1f} Lakh L"
    if value >= 1_000:
        return f"{value / 1_000:.1f} kL"
    return f"{int(value)} L"


def render_days_card(results: dict, month: int):

    days_to_zero = results["days_to_zero"]
    month_name = months[month]

    # status logic
    if days_to_zero == float("inf"):
        st.success(f"✅ Safe Month — No water crisis in {month_name}")
        st.write(f"Surplus: {format_litres(results['surplus'])}")
        st.write(f"Rain collected: {format_litres(results['rain_collected'])}")
        return

    elif days_to_zero == 0:
        st.error("🚨 Tank is already empty")

    elif days_to_zero <= 7:
        st.error(f"🚨 Critical — Water ends in {days_to_zero} days")

    elif days_to_zero <= 20:
        st.warning(f"⚠️ Warning — {days_to_zero} days left")

    else:
        st.info(f"ℹ️ {days_to_zero} days remaining")

    # metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("Days Left", days_to_zero)
    col2.metric("Daily Usage", format_litres(results["daily_demand"]))
    col3.metric("Current Storage", format_litres(results["current_storage"]))

    coverage_pct = min(
        int(results["total_available"] / max(results["monthly_demand"], 1) * 100),
        100
    )

    st.progress(coverage_pct)
    st.caption(f"Monthly coverage: {coverage_pct}%")
