import streamlit as st

# calc logics
from calculate import calculate

# ui comps
from components.sidebar import show_sidebar
from components.days_card import render_days_card
from components.cost_card import render_cost_card
 
# page setting up 
st.set_page_config(page_title="WaterPulse Nilgiris",layout="wide",initial_sidebar_state="expanded")

#dark background set up
st.markdown("""
<style>
.stApp { background-color: #080c12; color: #e8eef8; }
[data-testid="stSidebar"] { background-color: #0e1520; }
.block-container { padding-top: 1.2rem; padding-bottom: 2rem; }
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# side bar inputs dispaly
with st.sidebar:
    inputs, month = show_sidebar()

# calulation 
results=calculate(inputs, month)

# header part styling
st.markdown("""
<h2 style="font-family:Georgia; font-weight:900;">
Water<span style="color:#4db8ff;">Pulse</span>
<span style="color:rgba(180,210,255,0.3); font-size:16px;"> Nilgiris</span>
</h2>
<p style="font-size:12px; color:rgba(150,180,220,0.3);">
Hotel Water Storage Simulator · Coonoor / Ooty
</p>
""", unsafe_allow_html=True)

st.divider()

#ouput cards display
render_days_card(results, month)
render_cost_card(results, month)

# bottom styling
st.markdown("""
<div style="text-align:center; font-size:11px; color:rgba(120,150,200,0.3);">
WaterPulse Nilgiris · IMD Verified Rainfall Data · Python + Streamlit
</div>
""", unsafe_allow_html=True)
