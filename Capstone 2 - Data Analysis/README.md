# Capstone Module 2 - New York TLC Trip Analysis

## Project Overview
Taxis are a major mode of commuting in New York City, and the TLC trip dataset provides detailed records of taxi rides. Analyzing this data helps understand travel demand, commuting behavior, and operational variations, which is valuable for the New York City Taxi and Limousine Commission (TLC) in regulating taxis and overseeing vendors. 
Problems & Objectives:
- Trip Patterns: Identify peak and low demand hours, days, and day periods to optimize taxi supply and distribution.
- Area Distribution: Identify key pickup and drop-off areas to allocate taxis more effectively based on demand.
- Pricing Patterns: Analyze fare amount trends per hour to optimize pricing and manage demand effectively, with tipping behavior included as optional insight for drivers or platforms collaborating with NYC TLC.
- Congestion Surcharge: Determine when and where congestion surcharges should be applied to better manage traffic and passenger demand.
- Vendor Performance: Evaluate operators to ensure reliable service quality.
    
## Data Sources
- New York City TLC Trip Record – Contains detailed trip-level data

| Feature               | Description |
|-----------------------|-------------|
| VendorID              | Code for LPEP provider. 1 = Creative Mobile Technologies, LLC; 2 = VeriFone Inc. |
| lpep_pickup_datetime  | Date and time when meter was engaged. |
| lpep_dropoff_datetime | Date and time when meter was disengaged. |
| Passenger_count       | Number of passengers (driver-entered). |
| Trip_distance         | Trip distance in miles by the taximeter. |
| PULocationID          | TLC Taxi Zone of pickup. |
| DOLocationID          | TLC Taxi Zone of drop-off. |
| RateCodeID            | Rate code at trip end. 1 = Standard, 2 = JFK, 3 = Newark, 4 = Nassau/Westchester, 5 = Negotiated, 6 = Group ride |
| Store_and_fwd_flag    | Indicates if trip was stored in vehicle before sending. Y = yes, N = no |
| Payment_type          | Payment method. 1 = Credit card, 2 = Cash, 3 = No charge, 4 = Dispute, 5 = Unknown, 6 = Voided |
| Fare_amount           | Meter-calculated fare including minor extras ($0.50/$1 rush/overnight). |
| MTA_tax               | $0.50 MTA tax triggered automatically. |
| Improvement_surcharge | $0.30 surcharge on hailed trips at flag drop (since 2015). |
| Tip_amount            | Credit card tips only; cash not included. |
| Tolls_amount          | Total tolls paid. |
| Total_amount          | Total fare charged (excluding cash tips). |
| Trip_type             | Trip type: 1 = Street-hail, 2 = Dispatch. |
| congestion_surcharge  | Extra fee in peak traffic areas/times (e.g., Manhattan). |

- [Taxi Zone Lookup Table](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) - Contains trip area information

| Feature       | Description |
|---------------|-------------|
| LocationID    | Unique ID for each TLC taxi zone. |
| Borough       | Borough where the taxi zone is located (e.g., Manhattan, Brooklyn). |
| Zone          | Name of the specific taxi zone within the borough. |
| service_zone  | Category of service area: e.g., Yellow, Green, or Other regulated zones. |

  
## Technologies Used
- **Programming Language:** Python  
- **Analysis & Manipulation:** pandas & SciPy  
- **Visualization:** Matplotlib, Seaborn  
- **Interactive Dashboard:** [Tableau](https://public.tableau.com/views/NewYorkTLCTripAnalysis/Dashboard?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
  *Note: For the best experience, please download and open the dashboard in Tableau Desktop, as the Tableau Public preview does not match the original sheet size.*
- **Development Environment:** Jupyter Notebook

## Summary of Finding
  ### Business Insight
- Trip Patterns: Taxi demand rises steadily from 1–6 PM, peaking at 6 PM. Tuesday records the most trips, followed by Thursday and Friday, while weekends see fewer rides. Night hours (1–5 AM) still have demand but limited supply.
- Area Distribution: Manhattan dominates trips, especially East Harlem North & South. Brooklyn and Queens peak in the evening, while the Bronx has more morning trips.
- Pricing Patterns: Fares are highest around 5 AM when supply is low. Tipping peaks on Sundays, followed by Thursdays and Saturdays, often linked to long or evening trips.
- Congestion Patterns: The $2.75 surcharge peaks at 6 PM, aligning with rush hours, while the $2.50 surcharge is highest at midday (12 PM).
- Vendor Performance: Vendor 2 (VeriFone) is more reliable with real-time records, higher revenue, and fewer disputes, while Vendor 1 (CMT) is more Manhattan-focused with shorter trips and more disputes.
  
  ### Recommendation
- Taxi Supply: Increase supply between 1–6 PM on weekdays (focus on Tuesday) and in the evenings from Wednesday to Friday. Add more taxis at night (1–5 AM), especially on weekends.
- Area Allocation: Boost availability in Manhattan during afternoons, in Brooklyn/Queens during evenings (commuting, airports, nightlife), and in the Bronx during mornings for commuters.
- Pricing & Incentives: Monitor early morning fares to ensure fairness. Share tipping trends (Sundays, Thursday evenings) with drivers to guide shift choices. Consider flat fare pilots in Bronx, Staten Island, and EWR to stimulate demand.
- Congestion Management: Apply stronger surcharges in Manhattan during morning/afternoon (esp. East Harlem, Upper East Side). Extend evening surcharges to Queens/Brooklyn and morning adjustments in the Bronx.
- Vendor Performance: Encourage Vendor 1 to reduce disputes, minimize delays, and expand beyond Manhattan. Maintain and support Vendor 2’s reliable coverage, especially for airports and outer-borough trips.

## Contact
Linkedin: https://www.linkedin.com/in/fatimahzhra
