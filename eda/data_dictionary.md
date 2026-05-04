The dataset contains monthly CTA ridership, Chicago weather summaries, and average gasoline prices from January 2024 through November 2025. The final merged dataset contains 23 monthly observations and 25 variables.

# Variables
- `month`: Month and year of the observation. This variable was used as the merge key across the CTA ridership, weather, and gasoline price datasets. Source: created during cleaning.
- `bus`: Total CTA bus boardings for the month. Source: CTA Ridership.
- `rail_boardings`: Total CTA rail boardings for the month. Source: CTA Ridership.
- `total_rides`: Total CTA rides for the month, calculated as bus boardings plus rail boardings. Source: CTA Ridership.
- `total_saturdays`: Number of Saturdays in the month. Source: created from CTA day_type.
- `total_sunday_or_holiday`: Number of Sundays or holidays in the month. Source: created from CTA day_type.
- `total_weekdays`: Number of weekdays in the month. Source: created from CTA day_type.
- `PRCP`: Average monthly precipitation. Source: NOAA Weather.
- `SNOW`: Average monthly snowfall. Source: NOAA Weather.
- `SNWD`: Average monthly snow depth. Source: NOAA Weather.
- `TAVG`: Average monthly temperature. Source: NOAA Weather.
- `TMAX`: Average monthly maximum temperature. Source: NOAA Weather.
- `TMIN`: Average monthly minimum temperature. Source: NOAA Weather.
- `fog`: Monthly weather event indicator/count for fog. Source: NOAA Weather.
- `heavy_fog`: Monthly weather event indicator/count for heavy fog. Source: NOAA Weather.
- `thunder`: Monthly weather event indicator/count for thunder. Source: NOAA Weather.
- `ice_pellets_sleet_small_hail`: Monthly weather event indicator/count for ice pellets, sleet, or small hail. Source: NOAA Weather.
- `hail`: Monthly weather event indicator/count for hail. Source: NOAA Weather.
- `glaze_or_rime`: Monthly weather event indicator/count for glaze or rime. Source: NOAA Weather.
- `dust_volcanic_ash_blowing_dust_sand`: Monthly weather event indicator/count for dust, volcanic ash, blowing dust, or sand. Source: NOAA Weather.
- `smoke_or_haze`: Monthly weather event indicator/count for smoke or haze. Source: NOAA Weather.
- `blowing_or_drifting_snow`: Monthly weather event indicator/count for blowing or drifting snow. Source: NOAA Weather.
- `tornado_waterspout_funnel_cloud`: Monthly weather event indicator/count for tornado, waterspout, or funnel cloud. Source: NOAA Weather.
- `high_or_damaging_winds`: Monthly weather event indicator/count for high or damaging winds. Source: NOAA Weather.
- `avg_gas_price`: Average monthly gasoline price in Chicago. Source: FRED Gasoline Price Data.