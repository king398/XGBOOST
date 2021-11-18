import investpy
import time
from nsetools import Nse

nse = Nse()
for i in range(10):
	search_result = investpy.search_quotes(text='SBIN', products=['stocks'],
	                                       countries=['india'], n_results=1)
	technical_indicators = search_result.retrieve_technical_indicators(interval='1min')
	print(technical_indicators.head())

	time.sleep(300)
	q = nse.get_quote("SBIN")
	print(q.get("averagePrice"))
