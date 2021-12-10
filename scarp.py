import investpy
import time
from nsetools import Nse
import numpy as np
from datetime import datetime
from yahoo_fin import stock_info as si
from tqdm import tqdm
from nsetools import Nse
import pandas as pd
import urllib.request
import json


class GoogleFinanceAPI:
	def __init__(self):
		self.prefix = "https://www.google.com/finance"

	def get(self, symbol, exchange):
		url = self.prefix + "%s:%s" % (exchange, symbol)
		u = urllib.request.urlopen(url)
		content = u.read().decode('utf-8')
		obj = json.loads(content[3:])
		return obj[0]


import yfinance as yf

for i in range(5):
	nse = Nse()
	prices = []
	stock = "RELIANCE"
	feat = ["timestamp", "RSI", "STOCH", "STOCHRSI", "MACD", "ADX", "Williams", "CCI", "ATR", "HighsLows",
	        "Ultimate Oscillator", "ROC", "Bull/Bear Power", "Price"]
	technical = [str(datetime.now())]
	for i in tqdm(range(1)):
		search_result = investpy.search_quotes(text=stock, products=['stocks'],
		                                       countries=['india'], n_results=1)
		technical_indicators = search_result.retrieve_technical_indicators(interval='1min')

		technical_indicators["value"] = technical_indicators["value"].astype(np.float)
		technical.extend(technical_indicators["value"].values)
	msft = yf.Ticker("RELIANCE.NS")
	technical.append(msft.info["currentPrice"])
	dict = {"timestamp": str(datetime.now())}
	for i, x in zip(technical, feat):
		dict.update({x: i})

	df = pd.read_csv("F:\Pycharm_projects\XGBOOST\data\Reliance_data.csv")
	new_df = df.append(dict,
	                   ignore_index=True)
	new_df.to_csv(fr"F:\Pycharm_projects\XGBOOST\data\Reliance_data.csv", index=False)
	print(new_df.head())
	for i in tqdm(range(400)):
		time.sleep(1)

