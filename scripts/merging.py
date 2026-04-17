import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import os


input_dir = "cleaned_data"
output_dir = "eda"
os.makedirs(output_dir, exist_ok = True)

chicago_gas_price_monthly = pd.read_csv(os.path.join(input_dir, "chicago_avg_pg.csv"))
chicago_cta_monthly = pd.read_csv(os.path.join(input_dir, "chicago_cta_monthly.csv"))
chicago_weather_monthly = pd.read_csv(os.path.join(input_dir, "chicago_weather_monthly.csv"))

merged = chicago_cta_monthly.merge(chicago_weather_monthly, on = "month", how = "left")
merged = merged.merge(chicago_gas_price_monthly, on = "month", how = "left")

# save data to csv
merged.to_csv(os.path.join(output_dir, "merged_datasets.csv"), index = False)


