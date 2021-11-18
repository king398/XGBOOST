import investpy

search_result = investpy.search_quotes(text='reliance', products=['stocks'],
                                       countries=['india'], n_results=1)
technical_indicators = search_result.retrieve_technical_indicators(interval='1min')
print(technical_indicators.head())
