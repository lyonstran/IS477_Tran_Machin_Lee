import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# loading data
chicago_cta_daily_boarding = pd.read_csv("original_data\chicago_cta_daily_boarding.csv")
chicago_avg_price_gas = pd.read_csv("original_data\chicago_avg_price_gas.csv")
chicago_weather_2425 = pd.read_csv("original_data\chicago_weather_2425.csv")

# cleaning + prepared cta ridership data
chicago_cta_daily_boarding['service_date'] = pd.to_datetime(chicago_cta_daily_boarding['service_date'])
chicago_cta_daily_boarding = chicago_cta_daily_boarding.sort_values(by = 'service_date')
chicago_cta_daily_boarding = chicago_cta_daily_boarding[(chicago_cta_daily_boarding['service_date'].dt.year >= 2024) 
                                                        & (chicago_cta_daily_boarding['service_date'].dt.year <= 2026)]
chicago_cta_daily_boarding['month'] = chicago_cta_daily_boarding['service_date'].dt.to_period('M')

cta_monthly = chicago_cta_daily_boarding.groupby('month')[['bus', 'rail_boardings', 'total_rides']].sum().reset_index()
daytype_counts = pd.crosstab(chicago_cta_daily_boarding['service_date'].dt.to_period('M'),
                            chicago_cta_daily_boarding['day_type']).reset_index()
daytype_counts = daytype_counts.rename(columns = {'service_date' : 'month'})

chicago_cta_monthly_boarding = pd.merge(cta_monthly, daytype_counts, on = 'month')
chicago_cta_monthly_boarding = chicago_cta_monthly_boarding.rename(columns = {'A': 'total_saturdays', 
                                                                              'U' : 'total_sunday_or_holiday', 
                                                                              'W' : 'total_weekdays'})


# cleaning + preparing chicago gas price data
capg = chicago_avg_price_gas.rename(columns = {'observation_date' : 'month', 'APUS23A7471A' : 'avg_gas_price'})
capg['month'] = pd.to_datetime(capg['month']).dt.to_period('M')
capg = capg[capg['month'] <= '2025-11'] # because 2025-12 and 2026-01 don't exist in chicago_cta_monthly_boarding


# cleaning + preparing chicago weather data
chicago_weather_2425['DATE'] = pd.to_datetime(chicago_weather_2425['DATE'])
weather_small = chicago_weather_2425[['DATE', 'PRCP', 'SNOW', 'SNWD', 'TAVG', 'TMAX', 'TMIN',
                                      'WT01', 'WT02', 'WT03', 'WT04', 'WT05', 'WT06',
                                      'WT07', 'WT08', 'WT09', 'WT10', 'WT11']]

wt_cols = ['WT01', 'WT02', 'WT03', 'WT04', 'WT05', 'WT06',
           'WT07', 'WT08', 'WT09', 'WT10', 'WT11']
weather_small[wt_cols] = weather_small[wt_cols].fillna(0)

weather_daily = weather_small.groupby('DATE')[['PRCP', 'SNOW', 'SNWD', 'TAVG', 'TMAX', 'TMIN']].mean()
weather_events = weather_small.groupby('DATE')[['WT01', 'WT02', 'WT03', 'WT04', 'WT05', 'WT06',
                                                'WT07', 'WT08', 'WT09', 'WT10', 'WT11']].max()
weather_daily = pd.concat([weather_daily, weather_events], axis=1).reset_index()
weather_daily['month'] = weather_daily['DATE'].dt.to_period('M')

weather_monthly = weather_daily.groupby('month').agg({'PRCP': 'mean',
                                                    'SNOW': 'mean',
                                                    'SNWD': 'mean',
                                                    'TAVG': 'mean',
                                                    'TMAX': 'mean',
                                                    'TMIN': 'mean',
                                                    'WT01': 'sum',
                                                    'WT02': 'sum',
                                                    'WT03': 'sum',
                                                    'WT04': 'sum',
                                                    'WT05': 'sum',
                                                    'WT06': 'sum',
                                                    'WT07': 'sum',
                                                    'WT08': 'sum',
                                                    'WT09': 'sum',
                                                    'WT10': 'sum',
                                                    'WT11': 'sum'}).reset_index()
weather_monthly = weather_monthly[weather_monthly['month'] <= '2025-11']
weather_monthly = weather_monthly.rename(columns={'WT01': 'fog',
                                                  'WT02': 'heavy_fog',
                                                  'WT03': 'thunder',
                                                  'WT04': 'ice_pellets_sleet_small_hail',
                                                  'WT05': 'hail',
                                                  'WT06': 'glaze_or_rime',
                                                  'WT07': 'dust_volcanic_ash_blowing_dust_sand',
                                                  'WT08': 'smoke_or_haze',
                                                  'WT09': 'blowing_or_drifting_snow',
                                                  'WT10': 'tornado_waterspout_funnel_cloud',
                                                  'WT11': 'high_or_damaging_winds'})

# saving to csv
chicago_cta_monthly_boarding.to_csv("chicago_cta_monthly.csv", index = False)
capg.to_csv("chicago_avg_pg.csv", index = False)
weather_monthly.to_csv("chicago_weather_monthly.csv", index = False)