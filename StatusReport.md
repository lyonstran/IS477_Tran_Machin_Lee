 ## Updates

Since the initial project plan, we've done the following:
- small corrections to the ProjectPlan.md file based off of feedback from Canvas
- Collected and inspected data
- Cleaned the datasets as necessary

Overall, some substantial changes  is the inclusion of more definitive tasks for group members to be responsible for. A member with "Primary responsibility" is the person designated with main oversight on the task itself, whether that be independent completion and having other members check and revise, or guide the other members to complete the task in a timely manner, depending on that persons said experience with the task and comfortability. In this status report, we've also added file format and data documentation information, as well as licensing/terms of use information. 

(section to provide updates on data collection and cleaning, as well as section to include links to specific artifacts in our repo like scripts, datasets, workflows, diagrams, flowcharts, etc if applicable)

Aside from finishing data inspection, cleaning, and merging, full and deeper EDA is expected to be done in parallel with the revised timeline below: 

## Revised Timeline
Below is the full updated timeline for completing the project to target dates for when we want things to be done by. This timeline includes the current status of each task, the target completion date, and the team members primarily responsible. Although each task has a primary lead, all team members will contribute throughout the project.

**Corrections to project plan**
- Description: Confirm topic, datasets, team roles, research questions, and project scope
- Status: Done
- Target date: March 31, 2026
- Primary responsibility: Lyons Tran, with contributions from all members

**Collecting and inspecting data**
- Description: Download CTA ridership, Chicago weather, and Chicago gasoline price datasets; organize files in repository; review variable definitions and formats
- Status: Done
- Target date: April 2, 2026
- Primary responsibility: Lucy Machin for dataset review and structure, Lyons Tran for repository organization, Nathan Lee for coordination and documentation

**Cleaning datasets**
- Description: Standardize dates, remove unnecessary columns, choose relevant weather variables, check missing values, and prepare each dataset for integration
- Status: Done
- Target date: April 4, 2026
- Primary responsibility: Lucy Machin, with support from Lyons Tran and Nathan Lee

**Preparing interim status report**
- Description: Write StatusReport.md, summarize progress on each planned task, reference repository artifacts, document challenges, and add individual contribution summaries
- Status: In progress
- Target date: April 5, 2026
- Primary responsibility: Nathan Lee, with all members writing and committing their own contribution summaries

**Merging datasets**
- Description: Join CTA ridership, weather, and gasoline data into a single analysis-ready dataset using date and aligned time periods
- Status: Not complete
- Target date: April 8, 2026
- Primary responsibility: Lyons Tran, with supervision from Lucy Machin and Nathan Lee

**Exploratory analysis**
- Description: Produce summary statistics, trend plots, and initial visualizations to identify ridership patterns and possible relationships with weather and gas prices
- Status: Not complete
- Target date: April 12, 2026
- Primary responsibility: Nathan Lee, with Lyons Tran and Lucy Machin supporting interpretation and discussion

**Modeling and deeper analysis**
- Description: Fit statistical models or other analytical methods to evaluate the relationship between ridership, weather, and gasoline prices
- Status: Not complete
- Target date: April 17, 2026
- Primary responsibility: Lucy Machin, with feedback from Lyons Tran and Nathan Lee

**Interpreting findings**
- Description: Summarize key results, identify important patterns, and connect findings back to the project research questions
- Status: Not complete
- Target date: April 21, 2026
- Primary responsibility: Nathan Lee, with contributions from all members

**Drafting final deliverables**
- Description: Prepare final report materials, organize code and figures, review repository contents, and polish presentation of results
- Status: Not complete
- Target date: April 25, 2026
- Primary responsibility: Lyons Tran, with contributions from all members

**Revision and final submission**
- Description: Conduct final review, make revisions, ensure the GitHub repository is complete, create the final release/tag if needed, and submit final materials
- Status: Not complete
- Target date: April 29, 2026
- Primary responsibility: Lyons Tran, with all members reviewing final materials

## File Format Details
All three datasets were retrieved in the `.csv` format. Links to the documentation, as well as brief overview of attributes featured in datasets are below:

**CTA Ridership - Daily Boarding Totals Dataset Documentation:**
https://data.cityofchicago.org/Transportation/CTA-Ridership-Daily-Boarding-Totals/6iiy-9s97/about_data

The `chicago_cta_daily_boarding.csv` dataset features only 5 attributes:
- `service_date`: date of service
- `day_type`:
  - W = Weekday 
  - A = Saturday
  - U = Sunday/Holiday
- `bus`: total number of bus boardings on that particular `service_date` 
- `rail_boardings`: total number of train boardings on that particular `service_date`
- `total_rides`: sum of `bus` and `rail_boardings`

**Chicago Weather Dataset Dataset Documentation:**
https://www.ncei.noaa.gov/pub/data/cdo/documentation/GHCND_documentation.pdf

The main attributes in `chicago_weather_2425.csv` are:

- `STATION`: station identification code for the reporting weather station  
- `DATE`: date of observation  
- `PRCP`: daily precipitation amount  
- `SNOW`: daily snowfall amount  
- `SNWD`: daily snow depth  
- `TMAX`: maximum daily temperature  
- `TMIN`: minimum daily temperature  
- `WT01`-`WT11`: indicators for specific weather conditions such as fog, thunder, hail, smoke/haze, snow, tornadoes, and high winds  

**Average Price of Gasoline in Chiago Dataset Documentation:**

An official/explicit link to documentation was not found for the `chicago_avg_price_gas.csv`. However, it is quite self-explanatory as the dataset only features two attributes:
- `observation_date` : date of recorded average price of gasoline in Chicago, and increments by months
- `APUS23A7471A` : represents average dollar amount


## Data licenses and Terms of Use
**CTA Ridership - Daily Boarding Totals:** This dataset is publicly available through the City of Chicago and is governed by the City’s Data Terms of Use. The City provides the data “as is,” and makes no gurantees regarding accuracy/completeness, and disclaims liability for use of the data.  
- Link(s):
  - https://www.chicago.gov/city/en/narr/foia/data_disclaimer.html
  - https://www.transitchicago.com/terms/
  - https://www.transitchicago.com/developers/terms/

**Average Price of Gasoline in Chicago (FRED):** This dataset is accessed through FRED and is subject to FRED’s legal terms. Use is generally permitted for educational and non-commercial purposes, with appropriate citation to FRED and the original data source.  
- Link: https://fred.stlouisfed.org/legal/

**Chicago Weather Dataset (NOAA):** NOAA states that information on its websites is generally public information and may be copied or distributed unless otherwise specified. NOAA requests attribution when the data are used.  
- Link: https://data.ngdc.noaa.gov/ngdcinfo/privacy.html

## Challenges and Obstacles 

Some challenges/obstacles we met were...

## Team Member Contribution Summaries

**Lyons**: ...

**Lucy**:  ...
 
**Nathan**:    ...

