from constants import (rainfall_mm,days_in_month,tourist_months,usage,runoff_eff,roof_area_std,emergency_rate,advance_rate,tanker_size,fill_by_month)

def calculate(inputs, month):
    # month details
    days = days_in_month[month]
    fill = fill_by_month[month]
    is_tourist_month = month in tourist_months
    demand_multiplier = 1.7 if is_tourist_month else 1.0
    
    # formula 1: deamand calc
    occupied_rooms = inputs["rooms"]*(inputs["occupancy"] / 100)

    daily_demand = (occupied_rooms*usage*demand_multiplier)

    monthly_demand = daily_demand * days


    #formula 2: rainwater collected calc
    rainfall = rainfall_mm[month]

    rainwater_collected = (rainfall*roof_area_std*runoff_eff)

    daily_rain_input = rainwater_collected / days

    #formula 3: storage and shortage risk 
    current_storage = (inputs["storage"]*(fill / 100))

    net_daily_drain = daily_demand - daily_rain_input

    if net_daily_drain <= 0:
        days_to_zero = float("inf")
    else:
        days_to_zero = int(current_storage / net_daily_drain)

    total_available = current_storage + rainwater_collected

    deficit = max(0.0, monthly_demand - total_available)
    surplus = max(0.0, total_available - monthly_demand)

    # tanker cost purchase comparison
    if deficit > 0:
        tankers_needed = -(-int(deficit) // tanker_size)
    else:
        tankers_needed = 0

    emergency_monthly_cost = tankers_needed * emergency_rate
    advance_monthly_cost   = tankers_needed * advance_rate

    emergency_annual_cost = emergency_monthly_cost * 4
    advance_annual_cost   = advance_monthly_cost * 4

    monthly_saving = emergency_monthly_cost - advance_monthly_cost
    annual_saving  = emergency_annual_cost  - advance_annual_cost

    # return 
    return {
        # Water data
        "daily_demand": daily_demand,
        "monthly_demand": monthly_demand,
        "rain_collected": rainwater_collected,
        "current_storage": current_storage,
        "total_available": total_available,
        "deficit": deficit,
        "surplus": surplus,
        "fill_percentage": fill,

        # Risk indicator
        "days_to_zero": days_to_zero,
        "days_in_month": days_in_month,
        "tourist_surge_applied": is_tourist_month,

        # Financial data
        "tankers_needed": tankers_needed,
        "emergency_monthly_cost": emergency_monthly_cost,
        "emergency_annual_cost": emergency_annual_cost,
        "advance_monthly_cost": advance_monthly_cost,
        "advance_annual_cost": advance_annual_cost,
        "monthly_saving": monthly_saving,
        "annual_saving": annual_saving,
    }