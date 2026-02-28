import streamlit as st
from constants import months

# fromatting
def format_rupees(amount: float) -> str:
    if amount >= 100_000:
        return f"₹{amount / 100_000:.1f}L"
    if amount >= 1_000:
        return f"₹{int(amount / 1_000)}K"
    return f"₹{int(amount)}"


def format_litres(value: float) -> str:
    if value >= 100_000:
        return f"{value / 100_000:.1f} Lakh L"
    if value >= 1_000:
        return f"{value / 1_000:.0f} kL"
    return f"{int(value)} L"


# comparison
def build_row(label: str, value: str, color: str, highlight: bool = False) -> str:
    font_weight = "700" if highlight else "500"
    background  = "rgba(255,255,255,0.05)" if highlight else "transparent"

    return f"""
    <div style="
        display:flex;
        justify-content:space-between;
        padding:8px 12px;
        background:{background};
        border-radius:8px;
        margin-bottom:4px;
    ">
        <span style="font-size:12px;opacity:0.6">{label}</span>
        <span style="font-weight:{font_weight};
                     color:{color};
                     font-family:monospace">
            {value}
        </span>
    </div>
    """


# cost compoarison details
def render_cost_card(results: dict, month: int):

    month_name = months[month]

    #no shortage
    if results["deficit"] == 0:
        st.success(f"No tankers needed in {month_name}. Rain + storage fully cover demand.")
        return

    tankers = results["tankers_needed"]

    #after zero days hitting
    after_section = (
        build_row("Water shortage", format_litres(results["deficit"]), "#ff6b6b") +
        build_row("Tankers needed", f"{tankers} trips", "#ff6b6b") +
        build_row("Rate (panic)", "₹4,000 per trip", "#ff4444") +
        build_row("Monthly cost", format_rupees(results["advance_monthly_cost"]), "#ff4444", True) +
        build_row("Annual cost", format_rupees(results["advance_annual_cost"]), "#ff3333", True)
    )

    #before zero days hitting
    before_section = (
        build_row("Water shortage", format_litres(results["deficit"]), "#4db8ff") +
        build_row("Tankers needed", f"{tankers} trips", "#4db8ff") +
        build_row("Rate (advance)", "₹3,000 per trip", "#4db8ff") +
        build_row("Monthly cost", format_rupees(results["emergency_monthly_cost"]), "#4db8ff", True) +
        build_row("Annual cost", format_rupees(results["emergency_annual_cost"]), "#3ab0ff", True)
    )

    #render card
    st.markdown(f"""
    <div style="background:#0a0f1a;padding:24px;border-radius:16px">

        <h3>Tanker Cost Comparison — {month_name}</h3>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">

            <div>
                <h4 style="color:#ff4444">After Zero (Panic)</h4>
                {after_section}
            </div>

            <div>
                <h4 style="color:#4db8ff">Before Zero (Planned)</h4>
                {before_section}
            </div>

        </div>

        <div style="
            margin-top:20px;
            padding:16px;
            background:rgba(0,200,120,0.08);
            border-radius:12px;
        ">
            <strong>Savings from planning:</strong><br>
            {format_rupees(results["monthly_saving"])} per month<br>
            {format_rupees(results["annual_saving"])} per year
        </div>

    </div>
    """, unsafe_allow_html=True)