import pandas as pd
import datetime
import pywhatkit

pd = pd.read_csv(r"F:\Pycharm_projects\XGBOOST\data\BSE500Daily.csv")
date_object = str(datetime.date.today())
print(date_object)
today = pd[date_object].values
company_name = pd["Company_Name"].values
yestarday = pd["2021-11-15"].values


def get_change(current, previous):
	if current == previous:
		return 100.0
	try:
		return ((current - previous) / previous) * 100.0
	except ZeroDivisionError:
		return 0


i = 0
message = ""
for t, y, c in zip(today, yestarday, company_name):
	diff = get_change(t, y)
	if diff >= 300 or diff <= -75:
		temp_message = f" {c}:{round(diff, 2)} \n"
		message += temp_message
		i += 1
print(i)
pywhatkit.sendwhatmsg("+919422878112", message, 16, 44)
