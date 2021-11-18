from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from tqdm import tqdm

code = input("enter code: ")
driver = webdriver.Chrome('F:\Pycharm_projects\XGBOOST\data\chromedriver.exe')
driver.get("https://www.bseindia.com/corporates/Comp_Resultsnew.aspx")
select = Select(driver.find_element_by_id('ContentPlaceHolder1_broadcastdd'))
select.select_by_value("6")
inputElement = driver.find_element_by_id("ContentPlaceHolder1_SmartSearch_smartSearch")
inputElement.send_keys(code)
inputElement.send_keys(Keys.ENTER)
search_press = driver.find_elements_by_name("ctl00$ContentPlaceHolder1$btnSubmit")[0].click()
results = driver.find_elements_by_class_name("tdcolumn")
links = []
quarters = []
for x, i in enumerate(results[3:]):
	result = i.find_elements_by_tag_name("a")

	if x % 7 == 0:
		link = result[0].get_attribute("href")
		links.append(link)
		quarters.append(i.text)
dict = {}
len(links)
for x, i in tqdm(enumerate(links)):
	i = i.replace("'", '')
	driver.execute_script(f"window.open('about:blank', 'tab{x}');")
	driver.switch_to.window(f"tab{x}")

	driver.get(i)
	finc = []
	numbers = driver.find_elements_by_class_name("TTRow_right")
	for num in numbers:
		try:
			txt = num.text
			txt = txt.replace(",", "")
			finc.append((float(txt)))
			print(int(txt))
		except:
			finc.append(num.text)

	real_finc = []
	for z, i in enumerate(finc):
		if z % 2 == 0:
			real_finc.append(i)
	dict.update({quarters[x]: real_finc})

columns = ['Net Sales', 'Other Income', 'Total Income', 'Expenditure', 'Cost of Materials Consumed', 'Finance Costs',
           'Other Expenses', 'Purchases of stock-in-trade',
           'Changes in inventories of finished goods, work-in-progress and stock-in-trade', 'Employee benefit expense',
           'Depreciation and amortisation expense', 'vehicle/dies for own use',
           'Profit (+)/ Loss (-) from Ordinary Activities before Tax', 'Tax',
           'Net Profit (+)/ Loss (-) from Ordinary Activities after Tax', 'Net Profit', 'Current tax', 'Deferred tax',
           'Minority Interest', 'Share of Profit & Loss of Asso', 'Net Profit after Mino Inter & Share of P & L',
           'Any Other', 'Income Attributable to Consolidated Group', 'EPS after Extraordinary items (in Rs)',
           'Exceptional Item', 'Profit after Interest but before Exceptional Items',
           'Net Profit Loss for the period from continuing operations',
           'Profit (loss) from discontinuing operations before tax', 'Tax expense of discontinuing operations',
           'Net profit (loss) from discontinuing operation after tax', 'Other Comprehensive Income Net of Taxes',
           'Any Other Comprehensive Item', 'Total Comprehensive Income for the Period',
           'Total Amount of items that will not be reclassified to profit and loss',
           'Income tax relating to items that will not be reclassified to profit or loss',
           'Total Amount of items that will be reclassified to profit and loss',
           'Income tax relating to items that will be reclassified to profit or loss',
           'Net movement in regulatory deferral account balances',
           'Share of profit(loss) of associates and joint ventures', 'Basic EPS for continuing operation',
           'Diluted EPS for continuing operation', 'Basic for discontinued & continuing operation',
           'Diluted for discontinued & continuing operation']

driver.quit()
print(dict)
import pandas as pd

result = pd.DataFrame.from_dict(data=dict, orient="index", columns=columns)
result.to_csv(r"F:\Pycharm_projects\XGBOOST\data\Reliance.csv", index=True)
