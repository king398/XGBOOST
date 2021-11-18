import investpy
import time
from nsetools import Nse
import numpy as np
from datetime import datetime
import random
import pandas as pd
from tqdm import tqdm

comp = pd.read_csv("F:\Pycharm_projects\XGBOOST\data\ind_nifty50list.csv")
CODE = comp["Symbol"].values
CODE = CODE.tolist()
nse = Nse()
end_dict = {}
for n in range(10):
	technical = []
	prices = []
	for i in tqdm(CODE):
		try:
			search_result = investpy.search_quotes(text=i, products=['stocks'],
			                                       countries=['india'], n_results=1)
			technical_indicators = search_result.retrieve_technical_indicators(interval='1min')

			technical_indicators["value"] = technical_indicators["value"].astype(np.float)
			technical.append(technical_indicators["value"].values)
		except:
			CODE.remove(i)
			print(i)


	time.sleep(1)
	for p in CODE:
		q = nse.get_quote(str(p))
		prices.append(float(q.get("averagePrice")))
	for a, b in zip(list(technical), prices):
		now = datetime.now()
		a = a.tolist()
		current_time = now.strftime("%H:%M:%S")
		a.append(b)
		end_dict.update({random.randint(0, 100000000000000000000000): a})
print(end_dict)

result = pd.DataFrame.from_dict(data=end_dict, orient="index")
result.to_csv(r"F:\Pycharm_projects\XGBOOST\data\formodel.csv", index=True)
