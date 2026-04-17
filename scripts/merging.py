import pandas as pd

# loads dataset, then merges the datasets on the 'month' attribute. 
chicago_gas_price_monthly = pd.read_csv("cleaned_data\chicago_avg_pg.csv")
chicago_cta_monthly = pd.read_csv("cleaned_data\chicago_cta_monthly.csv")
chicago_weather_monthly = pd.read_csv("cleaned_data\chicago_weather_monthly.csv")

merged = chicago_cta_monthly.merge(chicago_weather_monthly, on = "month", how = "left")
merged = merged.merge(chicago_gas_price_monthly, on = "month", how = "left")

# save data to csv
merged.to_csv("merged_datasets.csv", index = False)


