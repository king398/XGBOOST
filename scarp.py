import investpy
import time
from nsetools import Nse
import numpy as np
from datetime import datetime
import random

CODE = ["BAJFINANCE", "SBIN"]
nse = Nse()
end_dict = {}
for n in range(1):
	technical = []
	prices = []
	for i in CODE:
		search_result = investpy.search_quotes(text=i, products=['stocks'],
		                                       countries=['india'], n_results=1)
		technical_indicators = search_result.retrieve_technical_indicators(interval='1min')
		technical_indicators["value"] = technical_indicators["value"].astype(np.float)
		technical.append(technical_indicators["value"].values)

	time.sleep(10)
	for p in CODE:
		q = nse.get_quote(p)
		prices.append(float(q.get("averagePrice")))
	for a, b in zip(list(technical), prices):
		now = datetime.now()
		a = a.tolist()
		current_time = now.strftime("%H:%M:%S")
		a.append(b)
		end_dict.update({random.randint(0, 100000000000000000000000): a})
print(end_dict)
