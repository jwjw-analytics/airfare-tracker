# Web Scraping Flight Price Data with Selenium and BeautifulSoup Python Packages
# Google Flights: From Abroad to Korea, One-way Ticket Price

# Importing required packages and libraries
from urllib.error import HTTPError
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
import datetime
import time
import calendar
from multiprocessing import Pool
import pandas as pd

# Creating variable 'date' which stores data capturing date
now = datetime.datetime.now()
date = now.strftime('%Y-%m-%d')

# Defining target and output data path
target_file_path = '/Users/han.jw/Documents/Jae W. Han/Python/Project/Airfare Tracker/index/'
output_file_path = '/Users/han.jw/Documents/Jae W. Han/Python/Project/Airfare Tracker/output/'

# Chromedriver which enables robotic process of capturing the data
chrome_driver_path = '/Users/han.jw/Documents/Jae W. Han/Python/chromedriver'

# Chromedriver settings
options = Options()
options.add_argument('--window-size=1200,800')
options.add_argument('headless')
options.add_argument("disable-gpu")

# Storing scraped data in result dataframe with following columns
result = pd.DataFrame(columns=['Capture Date', 'Data Source', 'Departure Date', 'Traffic Pattern',
                               'Departure Airport', 'Arrival Airport', 'Number of Stops',
                               'Marketing Carrier', 'Fare', 'Currency', 'Fare Condition', 'Fare Type',
                               'Travel Days', 'Travel Type'])

# Storing target route into the target dataframe
target = pd.read_excel(target_file_path + 'target.xlsx', sheet_name='4TF')

# Convert data into list datatype
departure_list = target.orig.tolist()
arrival_list = target.dest.tolist()
merge_list = list(zip(departure_list,arrival_list))

# Sending queries to website automatically via Selenium package (next 90 days)
def make_request(ODI):

    A = ODI[0]
    B = ODI[1]

    try:
        driver = webdriver.Chrome(chrome_driver_path, options=options)

        for day_offset in range(0,2):
            dep_date = (now + datetime.timedelta(days=day_offset)).strftime('%Y-%m-%d')
            url = 'https://www.google.com/flights?hl=ko&gl=us&curr=USD#flt={ORIG}.{DEST}.{dep_d};c:USD;e:1;s:2;sd:1;t:f;tt:o'.format(
                ORIG=A, DEST=B, dep_d=dep_date)
            driver.get(url)
            time.sleep(3)
            print("Capturing " + dep_date + "_" + A+'ICN')
            crawling(driver, A, B, dep_date)
            time.sleep(2)

        time.sleep(2)
        print("Saving " + A + B)
        result.to_excel(output_file_path + 'GGL' + '_OW_' + A + B +'_'+ date + '.xlsx')
        result.drop(result.index[0:], inplace=True)
        driver.close()
        # driver.quit()

    except HTTPError as e:
        return None

# Web crawling via BeautifulSoup package
def crawling(driver, depa, arr, dep_date):

    try:
        soup = bs(driver.page_source, 'html.parser')
        rows = soup.find_all(class_='OgQvJf nKlB3b')
        ota = "Google"
        trfc = "4TF"
        badge = ""
        price_type = "성인"
        currency = "USD"
        triptype = "OW"
        traveldays = 0
        for row in rows:
            airline = row.find(class_='TQqf0e sSHqwe tPgKwe ogfYpf').get_text('@').strip().replace(",","&").replace(" ","")
            airlinetext = airline.split("@")
            air = airlinetext[0]
            if air == "함께예약된다구간항공권":
                airlines = airlinetext[3]
            else:
                airlines = airlinetext[0]
            price = row.find(class_='FpEdX').get_text().strip().replace("US$","").replace(",","").replace("    왕복","")
            # price = price.replace("가격 확인가격을 확인할 수 없습니다.", "9999999").replace("예약이 불가능합니다.", "9999999")
            via = row.find(class_='pIgMWd ogfYpf').get_text().strip().replace("경유 ","").replace("회","").replace("직항","0")
            result.loc[len(result)+1] = [date, ota, dep_date, trfc, depa, arr, via, airlines, int(price), currency, price_type, badge, traveldays, triptype]

        time.sleep(0.5)
        print(result)

    except:
        return None

# Main function
if __name__ == '__main__':
     start_time = time.time()
     pool = Pool(processes=5)
     pool.map(make_request, merge_list)
     print("실행 시간(초) : %s" % (time.time() - start_time))
 
