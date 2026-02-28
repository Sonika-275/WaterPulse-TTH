
#  WaterPulse – Tanker Cost Intelligence for Hotels

##  Problem Statement

Hotels in the Nilgiris depend heavily on water tankers due to erratic rainfall and limited municipal supply.


* Tourism is the **second highest revenue generator** in the district after tea.
* Local authorities have proposed restricting tanker supply to prioritize residents.
* Emergency tanker pricing increases by **25–40%** during crisis situations.

Most hotel owners order tankers only when water runs out — leading to panic pricing and higher expenses.

---

##  Solution

**WaterPulse** helps hotel owners make smart water planning decisions.

Users enter 4 inputs and instantly see:

* When water will run out
* What tanker cost will be after water hits zero
* What tanker cost would be if ordered in advance
* Exact yearly savings by planning early

The goal is simple:

> Show the financial impact of panic ordering vs planned ordering.

---

##  How It Works

### Inputs (4 Fields)

| Input              | Purpose                                             |
| ------------------ | --------------------------------------------------- |
| Number of Rooms    | Drives daily water consumption                      |
| Occupancy %        | Determines actual water usage                       |
| Tank Size (Liters) | Current water storage capacity                      |
| Month              | Auto-loads rainfall data + tourist surge multiplier |

---

###  Outputs (2 Results)

####  Days to Zero

* Calculates the exact day water supply runs out.
* Example:

  > "4 days. Taps run dry on May 4th."

---

####  Cost Comparison

Shows two scenarios:

### After Zero (Emergency Ordering)

* Tankers ordered in panic
* Higher cost due to emergency premium
* Example:

  * 23 tankers
  * ₹92,000 this month
  * ₹3,68,000 per year

###  Before Zero (Planned Ordering)

* Tankers ordered in advance
* Normal tanker rate
* Example:

  * Same 23 tankers
  * ₹69,000 this month
  * ₹2,76,000 per year
  * Saves ₹92,000 annually

---

##  The insight:
> Planning 3 weeks early saves lakhs — without reducing water usage.

---

## Project Structure

```
WaterPulse-TTH/
│
├── app.py                → Main application (~70 lines)
├── constants.py           → IMD data, rates, defaults
├── calculate.py           → Core mathematical formulas
│
└── components/
    ├── __init__.py        → Empty file
    ├── sidebar.py          → 4 input fields
    ├── days_card.py        → Days to zero output
    └── cost_card.py        → Cost comparison output
```

---

##  Tech Stack

* Python
* Streamlit / Web Framework (depending on implementation)
* Pure mathematical computation
* Modular architecture


