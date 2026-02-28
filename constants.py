# rainfall pattern data , month divisions , tank options data , emergency tanker service revenue data, hotel demo data
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
days_in_month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# coonoor monthly  avg rainfall patterns ( fro IMD records)
rainfall_mm=[18, 15, 22, 45, 120, 280, 380, 320, 210, 180, 95, 30]

# Touristers peak months 
tourist_months=[2,3,4,9,10] # mar,apr,may,oct,nov
# Heavy monsoon months
monsoon_months=[5, 6, 7, 8] # jun,jul,aug,sept

# tanker pricing 
tanker_size=12000 # liters per tanker
emergency_rate=4000 # Rs per trip on crises day
advance_rate=3000  # Rs per trip on prev booking

#approx usage of water per room in the hotel
usage=300 # in litres (includes bathroom,laundery,kitchen,cleaning0

#percent of rainfall thats collectable
runoff_eff=0.7 # in percent (30% assumed loss)

#30 room coonoor hotel sample deafault data 
roof_area_std=600 # in m2
hotel={ "rooms": 30,"avg_occ": 80,"occupancy": 70,"storage":80000}

#water tank fill %
fill_by_month = {
    0: 35,   # Jan
    1: 25,   # Feb
    2: 15,   # Mar — tourist season starting
    3: 10,   # Apr — near critical
    4: 5,    # May — worst month
    5: 40,   # Jun — monsoon starts
    6: 75,   # Jul — filling fast
    7: 90,   # Aug — peak fill
    8: 85,   # Sep — still high
    9: 70,   # Oct — drawdown begins
    10: 55,  # Nov
    11: 45,  # Dec
} 
