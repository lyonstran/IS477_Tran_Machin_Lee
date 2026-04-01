# Milestone 2: Project Plan 

## Overview

Public transit ridership reflects how people move through a city and can be influenced by a lot of external factors, including weather conditions and the cost of driving. The goal of this project is to analyze how daily CTA ridership changes over time and whether those changes are associated with weather patterns and gasoline prices in the Chicago area. We are interested in understanding whether unfavorable weather conditions, such as rain, snow, or extreme temperatures, correspond to lower ridership, and whether higher gasoline prices may be associated with greater CTA usage.

To answer these questions, we will combine three datasets: CTA Daily Boarding Totals, daily Chicago weather data, and average gasoline prices in the Chicago area. The CTA dataset will serve as our primary outcome variable as it records total daily boardings on Chicago transit. The weather dataset will provide daily environmental conditions such as precipitation, snowfall, and temperature that may affect how willing people are to use transit on a given day. The gasoline price dataset will provide economic context by measuring the cost of driving over time. Since the gas price data are less frequent than the daily ridership data, we will align the datasets by date and use appropriate aggregation or matching techniques as needed.

Our planned approach includes data cleaning and standardizing the datasets, merging them by time, exploring seasonal and day-to-day trends, and using visualizations and statistical analysis to identify which factors appear most strongly associated with ridership levels. Throughout the project, we hope to better understand the relationship between public transportation demand, environmental conditions, and driving costs in Chicago. 

## Team 
All team members will collaborate on all parts of the project, including planning, data cleaning, analysis, interpretation, and writing. To keep the project organized and ensure accountability, each team member will take on a primary team role while still contributing to all major deliverables. If needed, we can flex and/or switch roles and responsibilities as necessary. 

### Team members and their roles
**Project Manager** - Lyons Tran:
- Oversees the overall timeline and helps keep the team on schedule
- Coordinates task assignments and checks progress toward milestones
- Organizes GitHub submissions, release tags, and final deliverables
- Ensures that all required project components are completed

**Facilitator and Communication Lead** - Nathan Lee:
- Coordinates team meetings and discussions
- Helps the team make decisions about research questions, methods, and project
direction
- Keeps track of questions or issues that need clarification from course staff
- Supports collaboration and ensures contributions from all members are reflected in the project

**Analysis Lead** - Lucy Machin
- Takes primary responsibility for guiding the cleaning, merging, and validating processes 
- Helps guide exploratory analysis, visualization, and modeling decisions
- Documents assumptions, limitations, and technical choices made during the project
- Assists with interpreting findings and connecting results back to the research questions

Although each member has a primary role, all team members will contribute to data preparation, coding, interpretation, writing, and review, which can be expected to be reflected through the Git commit history. 

## Research Questions

This project is guided by the following research questions:

1. How does daily CTA ridership vary across time, including by month, season, and day type?
2. How are daily weather conditions (precipitation, snowfall, temperature) associated with CTA ridership?
3. Is there a relationship between average gasoline prices in Chicago and CTA ridership during 2024–2025?
4. Which of the factors appear to have the strongest association with daily ridership: weather conditions, gas prices, or seasonal/time-based patterns?

These questions are able to be answered using our selected datasets and allows us to investigate both short-term and broader time-based influences on transit demand.

## Datasets

We will use three datasets that complement one another and can be integrated using common time variables.

### 1. CTA - Ridership - Daily Boarding Totals

URL: https://data.cityofchicago.org/Transportation/CTA-Ridership-Daily-Boarding-Totals/6iiy-9s97/about_data

This dataset contains daily total CTA boardings from 2024-2025. This dataset will serve as the main outcome variable in our analysis. It records how many riders used CTA services on each day and includes the date and day type. This dataset is central to the project because it measures public transit demand over time.

**Contribution to project:**  
Provides the dependent variable for our analysis: daily CTA ridership.

**Key shared attribute for integration:**  
Date

### 2. Chicago Weather Dataset

URL used to request data: https://www.ncei.noaa.gov/access

We will use daily weather data for Chicago covering 2024–2025. The variables selected for this project include precipitation, snowfall, snow depth, average temperature, maximum temperature, minimum temperature, and weather-type indicators. These variables will help us measure how day-to-day weather conditions may affect ridership behavior.

**Contribution to project:**  
Provides daily environmental conditions that may influence whether people choose to use public transit.

**Key shared attribute for integration:**  
Date 

### 3. Average Price of Gasoline in Chicago

URL: https://fred.stlouisfed.org/series/APUS23A7471A

We will use a dataset containing average gasoline prices in the Chicago area for 2024–2025. Gas prices provide a useful economic signal because the cost of driving may affect whether people choose public transit instead of personal vehicles. If gas prices rise, transit may become relatively more attractive.

**Contribution to project:**  
Provides a broader economic factor that may be associated with changes in public transit use.

**Key shared attribute for integration:**  
Date or month/year, depending on the frequency of the gasoline dataset

### Dataset Integration
These datasets complement one another because they each contribute a different but related type of information. The CTA dataset tells us what happened in terms of transit demand. The weather dataset helps explain daily external conditions that may affect ridership. The gasoline price dataset adds economic context that may influence mode-of-transportation decisions.

The datasets can be integrated through shared time variables. CTA ridership and weather data are both daily and can be joined directly by date. Gasoline prices may need to be matched by month or aligned to daily observations using the reporting period of the price data. This integration will allow us to study how daily ridership responds to both short-term weather shocks and broader cost-related trends.


## Timeline (revise)
Below is a rough timeline we will refer to for completing the project:

1. Finalizing project plan (confirming topic, datasets, roles, and research questions) <- DONE

2. Collecting and inspecting data (downloading the CTA, weather, and gas price datasets and organizing into repository files) <- IN PROGRESS
  
3. Cleaning datasets (standardizing dates, removing columns not needed, choosing relevant variables, etc) <- NOT COMPLETE
  
4. Merging datasets, exploratory analysis, and modeling/analysis (Combining datasets, making summary statistics, potentially fitting models, running tests, visualizations, etc) <- NOT COMPLETE

5. Interpret findings (summarizing results and identifying the most important patterns) <- NOT COMPLETE

6. Drafting final submission/deliverables (reviewing project materials, cleaning code, finalizing submission) <- NOT COMPLETE

7. Revision and submission (final review and submission) <- END GOAL

This is just a rough anticipation of the workflow/timeline for our progression through the project. Every member will be involved in each step of the timeline, though some tasks will have certain members be more involed than the others given the nature of their roles. 

## Constraints
 
There are several constraints that may limit or challenge our work. One constraint may be that the CTA ridership and weather data are collected daily while gasoline price data are recorded monthly so we might have to adjust the time variables to match accordingly. 

Another limitation might be that the gasoline price data only has price and time variable and doesn't account for factors such as types of gasoline and which gas station. Another challenge that could present itself is that we do have a couple na values for the gasoline dataset which we would have to decide whether to remove, ignore, or fill in the missing data. A final limitation could be confounding variables that may affect our data such as major city events, transit disruptions, etc.

 ## Gaps

Although the datasets and reseach questions have been selected, there are some gaps or areas we may need additional input. One area we might need additional input is integrating the datasets together using proper time variables similar to each other. Although we may have planned how to align them together, further work may be needed to actually setting up and possibly converting the time variables with each other. 

Another gap we need additional input on is proper data quality. We have already pointed out several factors that we might need to check for our data but we may need to make sure that we have properly checked all of the data and its quality. Finally, an area we need additional input is proper data cleaning methods. Similar to the data quality, we have identified how we want to clean our data but may need more input on how to clean it properly without messing up our data values.

