import pandas as pd
import matplotlib.pyplot as plt

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
df.to_csv("F:\Pycharm_projects\XGBOOST\data/New stock id/reliance.csv", index=False)

target_mean = df[target].mean()
target_stdev = df[target].std()

for c in df.columns:
	mean = df[c].mean()
	stdev = df[c].std()

	df[c] = (df[c] - mean) / stdev
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = "plotly_white"

plot_template = dict(
	layout=go.Layout({
		"font_size": 18,
		"xaxis_title_font_size": 24,
		"yaxis_title_font_size": 24})
)

fig = px.line(df, labels=dict(
	created_at="Date", value="Indicators variance", variable="Sensor"
))
fig.update_layout(
	template=plot_template, legend=dict(orientation='h', y=1.02, title_text="")
)
fig.show()
