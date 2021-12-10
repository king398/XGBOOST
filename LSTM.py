import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df = pd.read_csv("F:\Pycharm_projects\XGBOOST\data\Reliance_data.csv")
del df['timestamp']
target_sensor = "Price"
features = list(df.columns.difference([target_sensor]))

forecast_lead = 2
target = f"{target_sensor}_lead{forecast_lead}"

df[target] = df[target_sensor].shift(-forecast_lead)
df = df.iloc[:-forecast_lead]
display(df)
