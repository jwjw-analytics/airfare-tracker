# Importing required packages and libraries
import os
import pyautogui
import win32com.client
import time
import datetime
from datetime import date, timedelta
import shutil

# Daily data update
yesterday = date.today() - timedelta(days=1)
date = yesterday.strftime('%m.%d')
xlapp = win32com.client.DispatchEx("Excel.Application")
wb = xlapp.Workbooks.Open(r'/Users/han.jw/Documents/Jae W. Han/MS Office/Project/Airfare Tracker/Airfare Tracker.xlsx')
wb.RefreshAll()
xlapp.CalculateUntilAsyncQueriesDone()
time.sleep(5)
wb.Save()
xlapp.Quit()
shutil.copy('/Users/han.jw/Documents/Jae W. Han/MS Office/Project/Airfare Tracker/Airfare Tracker ({date}).xlsx')