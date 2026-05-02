import os
import pandas as pd
import matplotlib.pyplot as plt

def make_folder(folder_name):
    if (not os.path.exists(folder_name)):
        os.makedirs(folder_name)

input_file = os.path.join("eda", "merged_datasets.csv")
figures_folder = "figures"
results_folder = "results"

make_folder(figures_folder)
make_folder(results_folder)
df = pd.read_csv(input_file)

# additional conversion for month column to datetime for plotting
df["month"] = pd.to_datetime(df["month"])

# summary stats. 
numeric_df = df.select_dtypes(include = "number")
summary_stats = numeric_df.describe().T # .T transposes df so that it's easier to read and make sense of results 
summary_stats.to_csv(os.path.join(results_folder, "summary_statistics.csv"))

correlation_table = numeric_df.corr()
correlation_table.to_csv(os.path.join(results_folder, "correlation_table.csv"))

# corr. with total ridership
total_rides_corr = correlation_table["total_rides"].sort_values(ascending = False)
total_rides_corr.to_csv(os.path.join(results_folder, "correlations_with_total_rides.csv"))

# simple linear regression model for "modeling and deeper analysis section"
# checks how gas price and weather variables are associated with total ridership

import statsmodels.api as sm
model_data = df[["total_rides", "avg_gas_price", "TAVG", "PRCP", "SNOW", "SNWD"]].dropna()
y = model_data["total_rides"]
x = model_data[["avg_gas_price", "TAVG", "PRCP", "SNOW", "SNWD"]]
x = sm.add_constant(x)
ols_model = sm.OLS(y, x).fit()
with open(os.path.join(results_folder, "linear_regression_results.txt"), "w") as file:
    file.write(ols_model.summary().as_text())

# first plot shows monthly total ridership 
plt.figure(figsize = (11, 8))
plt.plot(df["month"], df["total_rides"], marker = "o")
plt.title("Monthly CTA Total Ridership")
plt.xlabel("Month")
plt.ylabel("Total Rides")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.savefig(os.path.join(figures_folder, "monthly_total_rides.png"), dpi = 300)
plt.close()

# second plot shows relationship between bus v rail ridership 
plt.figure(figsize=(11, 8))
plt.plot(df["month"], df["bus"], marker = "o", label = "Bus")
plt.plot(df["month"], df["rail_boardings"], marker = "o", label = "Rail")
plt.title("Monthly CTA Bus and Rail Ridership")
plt.xlabel("Month")
plt.ylabel("Monthly Rides")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(figures_folder, "bus_vs_rail_rides.png"), dpi = 300)
plt.close()

# third plot shows ridership v gas prices
plt.figure(figsize = (9, 7))
plt.scatter(df["avg_gas_price"], df["total_rides"])
plt.title("CTA Ridership vs. Gas Price")
plt.xlabel("Average Gas Price")
plt.ylabel("Total Rides")
plt.tight_layout()
plt.savefig(os.path.join(figures_folder, "ridership_vs_gas_price.png"), dpi = 300)
plt.close()

# fourth plot shows ridership v avg temps 
plt.figure(figsize = (10, 8))
plt.scatter(df["TAVG"], df["total_rides"])
plt.title("CTA Ridership vs. Average Temperature")
plt.xlabel("Average Temperature")
plt.ylabel("Total Rides")
plt.tight_layout()
plt.savefig(os.path.join(figures_folder, "ridership_vs_temperature.png"), dpi = 300)
plt.close()

# fifth plot shows riderships v snow Plot
plt.figure(figsize = (10, 8))
plt.scatter(df["SNOW"], df["total_rides"])
plt.title("CTA Ridership vs. Snow")
plt.xlabel("Average Snow")
plt.ylabel("Total Rides")
plt.tight_layout()
plt.savefig(os.path.join(figures_folder, "ridership_vs_snow.png"), dpi = 300)
plt.close()

# sixth plot is corr. heatmap 
plt.figure(figsize = (11, 9))
plt.imshow(correlation_table)
plt.colorbar(label="Correlation")
plt.xticks(range(len(correlation_table.columns)), correlation_table.columns, rotation = 90)
plt.yticks(range(len(correlation_table.columns)), correlation_table.columns)
plt.title("Correlation Heatmap of Numeric Variables")
plt.tight_layout()
plt.savefig(os.path.join(figures_folder, "correlation_heatmap.png"), dpi = 300)
plt.close()

# code to generate anaylsis summary 
summary_text = []
summary_text.append("Analysis Summary\n")
summary_text.append("================\n\n")
summary_text.append(f"Number of monthly observations: {len(df)}\n")
summary_text.append(f"Number of variables: {len(df.columns)}\n")

# https://www.geeksforgeeks.org/python/python-strftime-function/
# <- docu. for strftime()
summary_text.append(f"Date range: {df['month'].min().strftime('%Y-%m')} to {df['month'].max().strftime('%Y-%m')}\n\n")

average_total_rides = round(df["total_rides"].mean())
minimum_total_rides = round(df["total_rides"].min())
maximum_total_rides = round(df["total_rides"].max())

average_bus_rides = round(df["bus"].mean())
average_rail_rides = round(df["rail_boardings"].mean())

average_gas_price = round(df["avg_gas_price"].mean(), 3)
minimum_gas_price = round(df["avg_gas_price"].min(), 3)
maximum_gas_price = round(df["avg_gas_price"].max(), 3)

summary_text.append("Average monthly total rides: " + str(average_total_rides) + "\n")
summary_text.append("Minimum monthly total rides: " + str(minimum_total_rides) + "\n")
summary_text.append("Maximum monthly total rides: " + str(maximum_total_rides) + "\n\n")

summary_text.append("Average monthly bus rides: " + str(average_bus_rides) + "\n")
summary_text.append("Average monthly rail boardings: " + str(average_rail_rides) + "\n\n")

summary_text.append("Average gas price: $" + str(average_gas_price) + "\n")
summary_text.append("Minimum gas price: $" + str(minimum_gas_price) + "\n")
summary_text.append("Maximum gas price: $" + str(maximum_gas_price) + "\n\n")

summary_text.append("Correlations with total rides:\n")

for variable, value in total_rides_corr.items():
    if variable != "total_rides":
        rounded_value = round(value, 3)
        summary_text.append(variable + ": " + str(rounded_value) + "\n")

# save files to respective locations in the repo 
with open(os.path.join(results_folder, "analysis_summary.txt"), "w") as file:
    file.writelines(summary_text)

# should display if no errors occur when running code
print("analysis finished successfully.")
print("Figures saved in figures/")
print("Results saved in results/")

