import pandas as pd
df = pd.read_csv("F:\Pycharm_projects\XGBOOST\data\Reliance_data.csv")
target_sensor = "Austin"
features = list(df.columns.difference([target_sensor]))

forecast_lead = 15
target = f"{target_sensor}_lead{forecast_lead}"

df[target] = df[target_sensor].shift(-forecast_lead)
df = df.iloc[:-forecast_lead]
