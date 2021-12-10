from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from tqdm import tqdm
from datetime import datetime

driver = webdriver.Chrome('F:\Pycharm_projects\XGBOOST\data\chromedriver.exe')
driver.get('https://www.moneycontrol.com/india/stockmarket/stock-deliverables/marketstatistics/indices/cnx-200.html')
salaries = driver.find_elements_by_xpath('//td[@class="brdrgtgry"]')
salaries_list = []
for s in tqdm(range(len(salaries))):
	salaries_list.append(salaries[s].text)
print(len(salaries_list))
driver.quit()
Company_Name = []
Last_Price = []
Chg = []
Chg_percent = []
Dely_percent = []
five_Day_Avg_Del_percent = []
delivery_volumens = []
five_Day_avg_deliverable = []
Traded_volumes = []
id = 0
non_usefull = []
for count, i in enumerate(salaries_list):
	if count % 10 == 0:
		Company_Name.append(i)
		non_usefull.append(count)

print(Company_Name)
for count, i in enumerate(salaries_list[6:]):
	if count % 10 == 0:
		delivery_volumens.append(int(i.replace(',', '')))

print(delivery_volumens)
dict = {"Company_Name": Company_Name, "delivery_volumens": delivery_volumens}
df = pd.read_csv("F:\Pycharm_projects\XGBOOST\data\Reliance_data.csv")
df.to_csv(fr"F:\Pycharm_projects\XGBOOST\data\Reliance_data.csv")
