# CTA Ridership, Weather, and Gas Prices in Chicago

### Table of Contents

1. [Project Team Members and Contributions](#project-team-members-and-contributions)
2. [Summary](#summary)
3. [Data Profile](#data-profile)
    - [CTA Ridership Daily Boarding Totals](#cta-ridership-daily-boarding-totals)
    - [Chicago Weather Data](#chicago-weather-data)
    - [Gasoline Price Data](#gasoline-price-data)
    - [Data Licenses and Terms of Use](#data-licenses-and-terms-of-use)
    - [Integrated Dataset](#integrated-dataset)
4. [Data Quality](#data-quality)
5. [Data Cleaning](#data-cleaning)
6. [Findings](#findings)
7. [Future Work](#future-work)
8. [Challenges](#challenges)
9. [Reproducing](#reproducing)
10. [References](#references)


## Project Team Members and Contributions

**Lyons Tran**: contributed heavily to project coordination, repository organization, integration, workflow setup, and final submission preparation. Early in the project, created and organized the GitHub repository structure, added initial project planning materials, formatted project documents, and helped revise the project plan and status report. Organized the raw and cleaned data folders, helped add the original CSV files, and made several file location adjustments so the project structure was easier to follow. Also led the dataset merging stage by creating and revising the merging workflow, saving the merged dataset to `eda/merged_datasets.csv`, and adjusting the gasoline dataset after the team identified issues with the original gas price series. Also updated scripts to use `os` for more reliable file loading and saving across folders. During the final stage, organized the repository, revised code, updated the README structure, added project details, and prepared the final report and release materials.

**Lucy Machin**: Led much of the dataset cleaning and standardization work. She helped inspect the structure and variables of the CTA ridership, Chicago weather, and gasoline price datasets. Created and revised the cleaning process used to prepare the datasets for integration. For the CTA ridership data, she converted dates, sorted records, filtered the data to the project period, aggregated daily records to monthly totals, and added counts of weekdays, Saturdays, and Sundays/holidays. For the gasoline data, she standardized the date column, renamed the gas price variable, and helped align the dataset with the shared monthly time period. For the weather data, she selected relevant variables, converted dates, collapsed multiple station observations into daily records, aggregated weather values to the monthly level, handled missing weather-event indicators, and renamed technical weather variables into readable names. Also contributed to project plan revisions, status report edits, and the deeper modeling stage, including the statistical analysis used to evaluate relationships between ridership, weather, and gas prices.

**Nathan Lee**: Contributed strongly to documentation, project coordination, exploratory analysis, and interpretation of results. Helped coordinate the dataset review and project timeline, contributed to the status report, and finalized portions of `StatusReport.md`. He was primarily responsible for preparing the interim status report and documenting progress, challenges, and contribution summaries. Also led the exploratory analysis stage by helping produce and interpret summary statistics, trend plots, and initial visualizations related to CTA ridership, weather, and gas prices. In the final analysis stage, contributed to interpreting the visualizations, correlation results, and regression output. He helped connect the results back to the project’s research questions, especially the finding that weather and seasonal patterns appeared more strongly associated with ridership than gasoline prices.

Although each task had a primary lead, all team members contributed feedback, review, interpretation, and revisions throughout the project. Some commits were pushed through one member’s account even when the work reflected group discussion or shared editing.

## Summary

This project investigates the relationship between Chicago Transit Authority (CTA) ridership, weather conditions, and gasoline prices in Chicago from January 2024 through November 2025. The motivation for this project is that public transportation use is influenced by many external factors beyond transit service alone. Weather can affect how comfortable or safe it is to walk to a bus stop or train station, while gasoline prices can affect the cost of driving. By combining CTA ridership data with weather and gasoline price data, this project aims to better understand which factors are most strongly associated with changes in CTA ridership.

This project is guided by four main research questions. First, how does monthly CTA ridership vary across time, including by month and season? Second, how are monthly weather conditions, including precipitation, snowfall, snow depth, and temperature, associated with CTA ridership? Third, is there a relationship between average gasoline prices in Chicago and CTA ridership during 2024–2025? Fourth, which factors appear to have the strongest association with CTA ridership: weather conditions, gas prices, or seasonal/time-based patterns?

We used three in this project. The first dataset is CTA Ridership Daily Boarding Totals, which includes daily bus boardings, rail boardings, total rides, and day type. The second dataset is Chicago weather data from NOAA, which includes daily measurements such as precipitation, snow, snow depth, average temperature, maximum temperature, minimum temperature, and weather event indicators. The third dataset is average gasoline price data for Chicago. Since CTA and weather data were daily but gasoline price data was monthly, the final analysis was conducted at the monthly level. CTA and weather data were aggregated by month and then merged with monthly gas prices using a shared `month` variable.

The final merged dataset contains 23 monthly observations and 25 variables. The analysis uses summary statistics, visualizations, correlation analysis, and an ordinary least squares regression model. The visualizations include monthly total ridership, bus versus rail ridership, ridership versus gas prices, ridership versus average temperature, ridership versus snow, and a correlation heatmap.

The results suggest that CTA ridership follows seasonal patterns. Average monthly total ridership was 26,316,123 rides. The lowest monthly total ridership occurred in January 2024, with 21,435,348 rides, while the highest monthly total ridership occurred in October 2025, with 30,451,035 rides. Temperature variables had strong positive correlations with total rides, including maximum temperature at 0.788, average temperature at 0.772, and minimum temperature at 0.749. Snow-related variables were negatively correlated with ridership, including snow at -0.652 and snow depth at -0.626. Gas prices had a weaker positive correlation with total rides at 0.263.

The OLS regression model used total monthly ridership as the dependent variable and average gas price, average temperature, precipitation, snow, and snow depth as predictors. The model had an R-squared value of 0.723, suggesting that these variables explained about 72.3% of the variation in monthly ridership. However, average temperature was the only statistically significant predictor in the model. Overall, the findings suggest that weather and seasonality were more strongly associated with CTA ridership than gasoline prices during the study period.

## Data Profile
### CTA Ridership Daily Boarding Totals

The CTA ridership dataset is stored in the project repository at `original_data/chicago_cta_daily_boarding.csv`. The cleaned monthly version is stored at `cleaned_data/chicago_cta_monthly.csv`. This dataset comes from the City of Chicago Data Portal and contains daily boarding totals for CTA bus and rail service.

The original dataset includes five main attributes: `service_date`, `day_type`, `bus`, `rail_boardings`, and `total_rides`. The `service_date` column identifies the date of service. The `day_type` column classifies each date as a weekday, Saturday, or Sunday/holiday. The `bus` column contains the number of bus boardings on that date. The `rail_boardings` column contains the number of rail boardings on that date. The `total_rides` column is the combined number of bus and rail boardings.

This dataset is central to the project because it provides the main outcome variable: CTA ridership. The project used the total ridership to evaluate overall transit use while also keeping bus and rail ridership as separate variables for comparison. Since the other datasets were integrated at the monthly level, the daily CTA data was aggregated by month. The monthly cleaned dataset includes total monthly bus ridership, total monthly rail ridership, total monthly rides, and counts of weekdays, Saturdays, and Sundays/holidays within each month.

The CTA data is public government data. Ethical concerns are limited because the dataset is aggregated and does not contain personally identifiable information about individual riders. However, the data still needs to be used according to the City of Chicago’s data terms and disclaimers. 

### Chicago Weather Data

The Chicago weather dataset is stored in the project repository at `original_data/chicago_weather_2425.csv`. The cleaned monthly version is stored at `cleaned_data/chicago_weather_monthly.csv`. This dataset comes from a query on NOAA weather records, which includes daily weather observations for Chicago.

The weather dataset contains daily weather measurements such as `PRCP`, `SNOW`, `SNWD`, `TAVG`, `TMAX`, and `TMIN`. These represent precipitation, snowfall, snow depth, average temperature, maximum temperature, and minimum temperature. The dataset also includes weather event variables that were renamed to be more readable, such as `fog`, `heavy_fog`, `thunder`, `ice_pellets_sleet_small_hail`, `hail`, `glaze_or_rime`, `smoke_or_haze`, `blowing_or_drifting_snow`, `tornado_waterspout_funnel_cloud`, and `high_or_damaging_winds`.

The weather data is important because weather conditions may affect transit ridership. For example, extremely cold temperatures, snow, or icy conditions may discourage travel or make it harder for riders to reach transit stops. Warmer weather may be associated with more regular travel activity. By integrating weather data with CTA ridership, this project can evaluate whether ridership patterns appear to be associated with seasonal weather conditions.

The weather dataset was originally daily, so we aggregated it to the monthly level. Numeric weather measurements were summarized by month. Weather event variables were also summarized so that they could be compared with monthly ridership. The final cleaned weather dataset was then joined to the CTA ridership data using the `month` column.

The NOAA weather data is public and does not contain personally identifiable information. Ethical concerns are limited, but the data should be used with proper attribution and in accordance with NOAA documentation and data policies. One limitation is that weather data may come from specific stations and may not perfectly represent conditions experienced by all CTA riders across the entire city.

### Gasoline Price Data

The gasoline price dataset is stored in the project repository at `original_data/chicago_avg_price_gas.csv`. The cleaned version is stored at `cleaned_data/chicago_avg_pg.csv`. This dataset contains average monthly gasoline prices in Chicago.

The main variables in this dataset are `month` and `avg_gas_price`. The `month` column identifies the month of the observation, and `avg_gas_price` gives the average gasoline price for that month. This dataset was already monthly, which determined the final time scale of the project analysis.

Gasoline prices are relevant because it represents the cost of driving. If gasoline becomes more expensive, some people may be more likely to consider public transit as a better alternative. However, the relationship between gasoline prices and transit use is not simple. Ridership may also depend on job schedules, remote work, income, service availability, weather, safety, and many other factors.

The project originally considered using an all-types gasoline price series, but that source had a missing value for October 2025. The project instead used a more complete unleaded gasoline price series because unleaded gasoline is more relevant to the average consumer and avoided the missing-value issue. This decision improved the completeness of the final merged dataset. 

Since the dataset is aggregated at the city/month level, it does not contain personal information and raises minimal privacy concerns.

The original datasets can be found in the [original data folder](./original_data/). The cleaned datasets can be found in the [cleaned data folder](./cleaned_data/).

### Data Licenses and Terms of Use

The CTA Ridership - Daily Boarding Totals dataset is publicly available through the City of Chicago Data Portal. The data is governed by the City of Chicago’s Data Terms of Use. The City provides the data “as is”. It does not guarantee the accuracy, completeness, or timeliness of the data, and disclaims liability for uses of the data. Because the dataset contains aggregated daily ridership totals and does not include individual rider records, there are no major privacy concerns for this project. However, the dataset still requires proper citation and proper usage.

Relevant CTA and City of Chicago terms:

- City of Chicago Data Terms of Use: https://www.chicago.gov/city/en/narr/foia/data_disclaimer.html
- CTA Terms of Use: https://www.transitchicago.com/terms/
- CTA Developer Terms of Use: https://www.transitchicago.com/developers/terms/

The Average Price of Gasoline in Chicago dataset is accessed through FRED and is subject to FRED’s legal terms. FRED allows use of its data for educational and non-commercial purposes with appropriate citation to FRED and the original source. Since the gasoline price data is an economic time series and does not contain personal information, it does not raise privacy concerns. The main requirement is to cite FRED and follow its legal terms.

Relevant FRED terms:

- FRED Legal Terms: https://fred.stlouisfed.org/legal/

The Chicago weather dataset comes from NOAA. NOAA states that information on its websites is generally public information and may be copied or distributed unless otherwise specified. NOAA requests attribution when its data are used. The weather dataset does not contain personal information, so there are no major privacy concerns. The main requirement is to cite NOAA.

Relevant NOAA terms:

- NOAA Privacy, Copyright, and Disclaimer Information: https://data.ngdc.noaa.gov/ngdcinfo/privacy.html

The full comprehensive list of licenses/terms of use can be found in the [Referencecs section](#references). 

### Integrated Dataset

The final merged dataset is stored at `eda/merged_datasets.csv`. It contains 23 monthly observations from January 2024 through November 2025 and 25 variables. This dataset combines monthly CTA ridership, monthly weather summaries, and monthly gasoline prices.

The integration key was the `month` variable. CTA ridership was used as the base dataset, and weather and gasoline price data were joined to it. This integrated dataset allows the project to compare monthly ridership with weather and gasoline price variables during the same time period.

## Data Quality

The final merged dataset contains 23 monthly observations and 25 variables. It covers January 2024 through November 2025. After cleaning and merging, there were no missing values in the final merged dataset. This made the dataset suitable for exploratory analysis, correlation analysis, visualization, and regression modeling without requiring additional imputation at the final analysis stage.

One major data quality issue was that the datasets used different time scales. CTA ridership and weather data were originally daily, while gasoline price data was monthly. These datasets could not be directly joined in their raw form because daily observations do not match one-to-one with monthly observations. To address this issue, CTA ridership and weather data were aggregated to the monthly level. This created a common `month` variable that could be used as the integration key across the three datasets.

A second data quality issue involved date formatting. The original datasets represented time using different date columns and formats. CTA data used a service date, weather data used a date field, and gasoline data used monthly dates. During cleaning, these date fields were converted into consistent monthly values, a step that was necessary in order to prevent merge errors and to make sure that observations from the same month were correctly aligned across datasets.

A third issue involved missingness and completeness. Weather data can contain missing values because not all stations or variables are reported every day. This of course is reflected in the original/unclean version of the weather data. These variables were carefully  cleaned before the monthly aggregation. In the final merged dataset, there were no missing values remaining. The gasoline price data also presented a completeness issue because the original all-types gasoline price series had a missing value for October 2025. Instead of manually filling this value, the project used a more complete unleaded gasoline price series. This made the final dataset more complete and better matched typical consumer gasoline use.

A fourth issue involved interpretability. NOAA weather variables used short technical codes that are difficult to understand without documentation. To improve interpretability, several weather event variables were renamed using clearer labels, such as `fog`, `thunder`, `hail`, `glaze_or_rime`, and `high_or_damaging_winds`. This made the cleaned dataset easier to understand and made the final report more readable.

A fifth issue involved the limitations of monthly aggregation. Aggregating daily data to the monthly level made integration possible, but it also reduced the amount of detail in the data. Daily ridership changes, short weather events, holidays, and temporary service disruptions may be hidden when data is summarized by month. For example, a snowstorm on one day may affect daily ridership strongly but appear only as part of a monthly average. This means the final analysis is a lot more useful for broad seasonal patterns but not so much for detailed daily ridership behavior.

Another data quality limitation is that the regression model is based on only 23 monthly observations. This is a small sample size for statistical modeling. The regression results are useful as an exploratory tool, but they should not be interpreted as strong causal evidence. The OLS output also reported a high condition number, which may indicate multicollinearity or numerical issues. This is reasonable because several weather variables are related to each other.

Overall, the cleaned and merged dataset was complete, consistently formatted, and appropriate for exploratory data analysis. The main limitations are the small number of monthly observations, loss of daily detail from aggregation, and the observational nature of the data.

## Data Cleaning

The data cleaning process was completed using Python scripts stored in the `scripts/` folder. The main cleaning script is `scripts/cleaning.py`. The integration script is `scripts/merging.py`, and the analysis script is `scripts/analysis.py`.

For the CTA ridership dataset, the `service_date` column was converted into a date format. A new `month` variable was created from the service date. The data was then grouped by month. Monthly totals were calculated for bus ridership, rail boardings, and total rides. The `day_type` variable was also summarized into monthly counts. These counts became `total_weekdays`, `total_saturdays`, and `total_sunday_or_holiday`. This was done because months can contain different numbers of weekdays, Saturdays, and Sundays/holidays, which may affect ridership totals.

For the weather dataset, date values were converted into a consistent date format and then transformed into a monthly variable. Weather variables were cleaned and aggregated to the monthly level. Numeric measurements such as precipitation, snowfall, snow depth, average temperature, maximum temperature, and minimum temperature were summarized by month. Weather event variables were also cleaned and renamed to make them easier to understand. For example, technical weather event columns were converted into descriptive columns such as `fog`, `heavy_fog`, `thunder`, `hail`, and `high_or_damaging_winds`.

For the gasoline price dataset, the date variable was converted into a monthly format. The gas price column was cleaned and retained as `avg_gas_price`. The project originally considered using a gasoline dataset for all gasoline types, but that dataset had a missing value for October 2025. The project instead used a complete unleaded gasoline price dataset because it was more relevant to typical consumer driving costs and avoided manual imputation.

After the individual datasets were cleaned, they were merged in `scripts/merging.py`. The merge used the `month` column as the common key. The CTA monthly dataset was used as the base dataset because ridership was the main outcome of interest. The weather and gasoline price datasets were then joined to the CTA data. The final merged dataset was saved as `eda/merged_datasets.csv`.

The final analysis was performed in `scripts/analysis.py`. This script created summary statistics, a correlation table, correlations with total rides, visualizations, and an OLS regression model. Output tables were saved in the `results/` folder, and visualizations were saved in the `figures/` folder. These cleaning operations addressed the main data quality issues by standardizing dates, aligning datasets to the same monthly level, handling completeness issues, improving column readability, and producing a final integrated dataset that could be used for analysis.

A full data dictionary which describes the final merged datasets attributes used for analysis can be found [here](./eda/data_dictionary.md). The scripts mentioned above can be found in the [sciprts folder](./scripts/).

## Findings

The final merged dataset contains 23 monthly observations from January 2024 through November 2025 and 25 variables. Across this period, CTA averaged 26,316,123 total rides per month. The lowest monthly ridership occurred in January 2024, with 21,435,348 total rides, while the highest monthly ridership occurred in October 2025, with 30,451,035 total rides. Average monthly bus ridership was 15,317,668 rides, while average monthly rail ridership was 10,998,455 rides. Average gasoline price during the study period was $3.595, with a minimum of $3.223 and a maximum of $4.133.

The monthly ridership plots show that CTA ridership followed a seasonal pattern. Ridership was generally lower during winter months and higher during warmer months. This pattern appears in both the total ridership plot and the bus versus rail ridership plot. Bus ridership was consistently higher than rail ridership, but both modes moved in similar directions over time. This suggests that overall CTA ridership changes were not isolated to only one mode of transit.

The correlation results show that temperature variables had some of the strongest positive relationships with total rides. Maximum temperature had a correlation of 0.788 with total rides, average temperature had a correlation of 0.772, and minimum temperature had a correlation of 0.749. These results suggest that ridership tended to be higher during warmer months. Thunder also had a moderate positive correlation with total rides at 0.423, though this may reflect seasonal patterns because thunder is more common in warmer months.

Snow and winter-weather variables were negatively associated with total ridership. Glaze or rime had the strongest negative correlation with total rides at -0.734. Average snow had a correlation of -0.652, snow depth had a correlation of -0.626, heavy fog had a correlation of -0.576, blowing or drifting snow had a correlation of -0.535, and ice pellets, sleet, or small hail had a correlation of -0.511. These results suggest that harsher winter weather conditions were associated with lower CTA ridership.

Gasoline prices had a weaker relationship with total ridership than the weather variables. The correlation between average gas price and total rides was 0.263. This is a weak positive association, meaning that months with higher gas prices sometimes had higher ridership, but the relationship was not very strong. The gas price scatterplot also did not show as clear of a pattern as the temperature and snow plots.

To further evaluate these relationships, an ordinary least squares regression model was fit using average gas price, average temperature, precipitation, snow, and snow depth as predictors of monthly total rides. The model had an R-squared value of 0.723 and an adjusted R-squared value of 0.641, meaning that the model explained about 72.3% of the variation in monthly total ridership, or about 64.1% after adjusting for the number of predictors. The overall model was statistically significant, with a Prob(F-statistic) value of 0.000274.

In the regression model, average temperature was the only statistically significant predictor. Its coefficient was approximately 111,900, with a p-value of 0.001. This means that, holding gas price, precipitation, snow, and snow depth constant, a one-degree increase in average monthly temperature was associated with about 111,900 additional monthly CTA rides. Average gas price was not statistically significant in the regression model. Its coefficient was negative, approximately -2,436,000, with a p-value of 0.123. This means there was not enough evidence in this model to conclude that gas prices had a clear relationship with monthly CTA ridership after accounting for weather variables.

Precipitation, snow, and snow depth were also not statistically significant in the regression model. Their p-values were 0.573, 0.476, and 0.615, respectively. Although snow and snow depth had negative correlations with ridership, they were not significant in the regression model once average temperature and the other variables were included. This may be because winter weather variables are related to each other, making it harder to separate their individual effects.

Overall, the findings suggest that CTA ridership during 2024–2025 was more strongly associated with weather and seasonal patterns than with gasoline prices. Temperature showed the clearest relationship with ridership. Snow-related variables were negatively associated with ridership in the correlation analysis, while gasoline prices showed only a weak relationship. Because this analysis is based on observational monthly data with only 23 observations, the results should be interpreted as exploratory associations rather than causal effects.

These findings can be found in the [results folder](./results/). The generated figures can be found in the [figures folder](./figures/).

## Future Work

Future work could improve this project in several ways. First, the project could include more years of data. The current analysis only covers January 2024 through November 2025, which gives 23 monthly observations. This is enough for exploratory analysis, but it is limited for statistical modeling. A longer time period would make the regression model more reliable and would allow stronger conclusions about seasonal patterns.

Second, future work could analyze ridership at the daily level instead of the monthly level. The original CTA and weather datasets were daily, but the final analysis was monthly because gasoline prices were monthly. Daily analysis would preserve more detail and allow the project to study short-term effects of weather events, such as snowstorms, heavy precipitation, or extreme temperatures. A future version could keep CTA and weather data daily while joining gasoline prices as a monthly contextual variable.

Third, future analysis could include additional variables that affect ridership. CTA ridership is likely influenced by factors such as service frequency, delays, fare changes, employment patterns, remote work, holidays, school schedules, special events, and safety perceptions. These variables were not included in the current model, which means that some potentially more important explanations for ridership changes may be missing.

Fourth, future work could model bus and rail ridership separately. This project focused mainly on total ridership, but bus and rail may respond differently to weather and gasoline prices. For example, bus riders can be more exposed to outdoor conditions while waiting, while rail ridership may be more strongly connected to commuting patterns. Separate models could identify whether weather or gas prices affect one mode more than the other.

Fifth, future work could use more advanced statistical methods. The current project uses correlation analysis and an ordinary least squares regression model. Future versions could use time-series models, or nonlinear models. Lagged gasoline prices may be useful because changes in gas prices may not affect transit behavior immediately.

Overall, this project provides a useful starting point for understanding relationships between CTA ridership, weather, and gas prices. Future work can build on this by using more data, more detailed time scales, and stronger statistical modeling.

## Challenges

One major challenge was that the datasets used different time scales. CTA ridership and weather data were originally daily, while gasoline price data was monthly. To integrate the datasets, CTA and weather data had to be aggregated to the monthly level. This made the merge possible, but it also removed daily-level detail from the analysis.

A second challenge was deciding how to handle gasoline price data. The original all-types gasoline price dataset had a missing value for October 2025. Instead of manually filling that value from another source, the project used an unleaded gasoline price series because it was more complete and more relevant to average consumer driving costs. This decision improved the final dataset, but it also required revising the project documentation.

A third challenge was interpreting the statistical model. The OLS regression model explained a meaningful amount of variation in monthly ridership, but the dataset only includes 23 observations. This means the model should be treated as exploratory rather than causal. The model also reported a high condition number, which may indicate multicollinearity or numerical issues. This makes sense because several weather variables are related to each other.

A fourth challenge was maintaining reproducibility. The project includes raw data, cleaned data, merged data, scripts, results, figures, and documentation. To make the workflow easier to reproduce, the repository was organized into separate folders, and a `run_all.py` script was created to run the cleaning, merging, and analysis steps.

## Reproducing

To reproduce this project, please follow these steps:

1. Clone the project repository in the terminal

    - `git clone "repository url"`
    - `cd "repository-folder"`

2. Make sure that Python is installed and running on Python 

3. Install the required packages in the terminal. Required packages are listed in `/requirements.txt`

    - `pip install -r requirements.txt`

4. Make sure that the original data files are stored in the original_data/ folder

    - [chicago_cta_boarding.csv](./original_data/chicago_cta_daily_boarding.csv)
    - [chicago_weather_2425.csv](./original_data/chicago_weather_2425.csv)
    - [chciago_avg_price_gas.csv](./original_data/chicago_avg_price_gas.csv)

5. Run the full workflow from the root of the project using the terminal 

    - `python scripts/run_all.py`

6. Confirm that the cleaned datasets are created in the `cleaned_data` folder

    - [chicago_cta_monthly.csv](./cleaned_data/chicago_cta_monthly.csv)
    - [chicago_weather_monthly.csv](./cleaned_data/chicago_weather_monthly.csv)
    - [chicago_avg_pg.csv](./cleaned_data/chicago_avg_pg.csv)

7. Confirm that the merged dataset is created in the `eda/` folder

    - [merged_datasets.csv](./eda/merged_datasets.csv)

8. Confirm that the analysis outputs are created in the   `results/` folder

    - [summary_statistics.csv](./results/summary_statistics.csv)
    - [correlation_table.csv](./results/correlation_table.csv)
    - [correlations_with_total_rides.csv](./results/correlations_with_total_rides.csv)
    - [linear_regression_results.txt](./results/linear_regression_results.txt)
    - [analysis_summary.txt](./results/analysis_summary.txt)

9. Confirm that the visualizations are created in the `figures/` folder

    - [monthly_total_rides.png](./figures/monthly_total_rides.png)
    - [bus_vs_rail_rides.png](./figures/bus_vs_rail_rides.png)
    - [ridership_vs_gas_price.png](./figures/ridership_vs_gas_price.png)
    - [ridership_vs_temperature.png](./figures/ridership_vs_temperature.png)
    - [ridership_vs_snow.png](./figures/ridership_vs_snow.png)
    - [average_day_type_counts.png](./figures/average_day_type_counts.png)
    - [correlation_heatmap.png](./figures/correlation_heatmap.png)

## References

Chicago Data Portal. CTA Ridership - Daily Boarding Totals. City of Chicago.  
https://data.cityofchicago.org/Transportation/CTA-Ridership-Daily-Boarding-Totals/6iiy-9s97

City of Chicago. Data Terms of Use and Disclaimer.  
https://www.chicago.gov/city/en/narr/foia/data_disclaimer.html

Chicago Transit Authority. Terms of Use.  
https://www.transitchicago.com/terms/

Chicago Transit Authority. Developer Terms of Use.  
https://www.transitchicago.com/developers/terms/

Federal Reserve Economic Data. Average Price of Gasoline Data. Federal Reserve Bank of St. Louis.  
https://fred.stlouisfed.org/

Federal Reserve Economic Data. Legal Terms. Federal Reserve Bank of St. Louis.  
https://fred.stlouisfed.org/legal/

National Oceanic and Atmospheric Administration. Global Historical Climatology Network Daily Documentation.  
https://www.ncei.noaa.gov/pub/data/cdo/documentation/GHCND_documentation.pdf

NOAA National Centers for Environmental Information. Privacy, Copyright, and Disclaimer Information.  
https://data.ngdc.noaa.gov/ngdcinfo/privacy.html

