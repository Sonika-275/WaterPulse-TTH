#inputs from the hotel owners
import streamlit as st
from constants import hotel,months,rainfall_mm,monsoon_months,tourist_months

def show_sidebar():
    #header
    st.markdown(
        """
          <h3 style="color:#4db8ff;
                     font-family:Georgia, serif;
                     margin-bottom:2px;">
                     Your Hotel
          </h3>
          <p style="
            color:rgba(150,175,210,0.4);
            font-size:11px;
            margin-top:0;">
            4 fields. That is all.
           </p>
        """,unsafe_allow_html=True,)

    st.divider()

    # hotel details
    st.markdown(
        """
        <p style="font-size:11px;
                  font-weight:700;
                  letter-spacing:2px;
                  text-transform:uppercase;
                  color:rgba(150,175,210,0.4);
                  margin-bottom:4px">
                  Hotel Details
        </p>
        """,
        unsafe_allow_html=True,
    )

    rooms= st.number_input("no.of rooms",
                           min_value=1, max_value=300, value=hotel["rooms"],
                           step=1)
    
    occupancy= st.slider("room occupancy in % this month",
                           min_value=10, max_value=100, value=hotel["occupancy"],
                           step=5)
    
    st.divider()
    

   # water system
    st.markdown(
         """
        <p style="font-size:11px;
                  font-weight:700;
                  letter-spacing:2px;
                  text-transform:uppercase;
                  color:rgba(150,175,210,0.4);
                  margin-bottom:4px">
                  Water System
        </p>
        """,unsafe_allow_html=True,)
    
    storage = st.number_input("Tank capacity (litres)",
        min_value=1_000,max_value=1_000_000,value=hotel["storage"],
        step=5_000)

    st.divider()

    # month selection simulation
    st.markdown(
        """
        <p style="font-size:11px;
                  font-weight:700;
                  letter-spacing:2px;
                  text-transform:uppercase;
                  color:rgba(150,175,210,0.4);
                  margin-bottom:4px">
                  Simulate Month
        </p>
        """,unsafe_allow_html=True,) 
    
    def format_month(index: int) -> str:
        """month label to give"""
        if index in monsoon_months:
            return f" {months[index]}"
        elif index in tourist_months:
            return f" {months[index]}"
        return f" {months[index]}"

    month=st.selectbox("Select month",
                       options=range(12),
                       format_func=format_month,
                       index=4,  # may month is set as default (critical period)
                       label_visibility="collapsed")

    # rainfall and demand details

    rainfall=rainfall_mm[month]

    if months in monsoon_months:
         accent_color = "#00c878"
         note = "Monsoon period — needed strong rainwater recharge"
    elif months in tourist_months :
        accent_color = "#ff6b6b"
        note = "Peak tourist season — demand multiplier applied"
    else:
        accent_color = "#7a93b8"
        note = "Moderate transition month"

  
    st.markdown(f"""
        <div style="background:rgba(255,255,255,0.03);
                  border-left:3px solid {accent_color};
                    border-radius:6px;
                     padding:8px 12px;
                    margin-top:8px;">
            
            <span style="color:{accent_color};
                       font-weight:700;
                        font-family:monospace;
                        font-size:15px;">
                         {rainfall} mm
            </span>
            
            <span style="color:rgba(140,165,200,0.45);
                        font-size:11px;
                        margin-left:8px;">
                       IMD Coonoor average · {note}
            </span>
        </div>
        """,unsafe_allow_html=True,)

    #return 
    inputs = {
        "rooms": int(rooms),
        "occupancy": int(occupancy),
        "storage": int(storage),
    }

    month_name = st.selectbox("Select Month", months)
    month_index = months.index(month_name)

    return inputs, month_index
   
