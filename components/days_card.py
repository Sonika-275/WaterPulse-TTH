import streamlit as st
from constants import months,rainfall_mm

# formatting litres as readable
def format_litres(value: float) -> str:
    if value >= 100_000:
        return f"{value / 100_000:.1f} Lakh L"
    if value >= 1_000:
        return f"{value / 1_000:.1f} kL"
    return f"{int(value)} L"

#output 1: days to zero card
def render_days_card(results: dict, month: int):

    days_to_zero = results["days_to_zero"]
    month_name = months[month]

    if days_to_zero == float("inf"):
        state = {"number": "∞",
                 "color": "#00c878",
                "badge": "SAFE MONTH",
                "headline": f"No water crisis in {month_name}",
                "detail": (
                    f"Rain fully covers demand. "
                    f"Surplus: {format_litres(results['surplus'])}. "
                    f"Rain collected: {format_litres(results['rain_collected'])} "
                    f"from {rainfall_mm[month]} mm rainfall." )
        }

    elif days_to_zero == 0:
        state = {
            "number": "0",
            "color": "#ff2222",
            "badge": "ALREADY EMPTY",
            "headline": "Tank is dry right now",
            "detail": (
                f"Daily usage: {format_litres(results['daily_demand'])}. "
                f"No storage remaining."
            )
        }

    elif days_to_zero <= 7:
        state = {
            "number": str(days_to_zero),
            "color": "#ff4444",
            "badge": "CRITICAL",
            "headline": f"Taps run dry in {days_to_zero} days",
            "detail": (
                f"{format_litres(results['current_storage'])} left. "
                f"Using {format_litres(results['daily_demand'])}/day."
            )
        }

    elif days_to_zero <= 20:
        state = {
            "number": str(days_to_zero),
            "color": "#f59e0b",
            "badge": "WARNING",
            "headline": f"{days_to_zero} days of water left",
            "detail": (
                f"Plan tanker booking soon. "
                f"Daily demand: {format_litres(results['daily_demand'])}."
            )
        }

    else:
        state = {
            "number": str(days_to_zero),
            "color": "#4db8ff",
            "badge": "MONITOR",
            "headline": f"{days_to_zero} days remaining",
            "detail": (
                f"In tank: {format_litres(results['cur_storage'])}. "
                f"Using {format_litres(results['daily_demand'])}/day."
            )
        }

    # coverage in %
    coverage_pct = min(
        int(results["total_available"] / max(results["monthly_demand"], 1) * 100),
        100
    )

    #  Render Card
    st.markdown(f"""
    <div style="
        background:#0e1520;
        border-left:4px solid {state['color']};
        border-radius:16px;
        padding:26px;
        margin-bottom:16px;
    ">
        <div style="font-size:12px;opacity:0.6;">
            OUTPUT 1 — DAYS TO ZERO
        </div>

        <div style="font-size:72px;
                    font-weight:900;
                    color:{state['color']};
                    margin:10px 0;">
            {state['number']}
        </div>

        <div style="font-weight:700;">
            {state['badge']}
        </div>

        <div style="margin-top:8px;">
            <strong>{state['headline']}</strong><br>
            {state['detail']}
        </div>

        <div style="margin-top:14px;">
            Monthly coverage: {coverage_pct}%
        </div>
    </div>
    """, unsafe_allow_html=True)