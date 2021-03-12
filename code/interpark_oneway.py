# Web Scraping Flight Price Data with Selenium and BeautifulSoup Python Packages
# Interpark Ticket: From Korea to Abroad, One-way Ticket Price

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
options.add_argument('--window-size=1800,700')
options.add_argument('headless')
options.add_argument("disable-gpu")

# Storing scraped data in result dataframe with following columns
result = pd.DataFrame(columns=['Capture Date', 'Data Source', 'Departure Date', 'Traffic Pattern',
                               'Departure Airport', 'Arrival Airport', 'Number of Stops',
                               'Marketing Carrier', 'Fare', 'Currency', 'Fare Condition', 'Fare Type',
                               'Travel Days', 'Travel Type'])

# Storing target route into the target dataframe
target = pd.read_excel(target_file_path + 'target.xlsx', sheet_name='3TF')

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

        for day_offset in range(0, 90):
            dep_date = (now + datetime.timedelta(days=day_offset)).strftime('%Y%m%d')
            dep_date2 = (now + datetime.timedelta(days=day_offset)).strftime('%Y-%m-%d')
            url = 'https://fly.interpark.com/booking/mainFlights.do?tripType=OW&sdate0={dep_d}&sdate1=&sdate2=&dep0={orig}&arr0={dest}&dep1=&arr1=&dep2=&arr2=&adt=1&chd=0&inf=0&comp=Y&val=#list'.format(
                orig = A, dest = B, dep_d=dep_date)
            driver.get(url)
            print("Capturing " + dep_date + "_" + "SEL" + B)
            wait = WebDriverWait(driver, 80).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="dBodyContent"]/div[1]/div[2]')))
            # time.sleep(5)
            crawling(driver, A, B, dep_date2)

        print("Saving " + "SEL" + B)
        result.to_excel(output_file_path + 'INP' + "_OW_" + A + B + '_' + date + '.xlsx')
        result.drop(result.index[0:], inplace=True)
        driver.close()
        # driver.quit()

    except HTTPError as e:
        return None

# Web crawling via BeautifulSoup package
def crawling(driver, departure, destination, dep_date2):
    try:

        # Crawl
        soup = bs(driver.page_source, 'html.parser')
        rows = soup.find('ul', id='schedule0List').find_all('li', recursive=False)
        currency = "KRW"
        ota = "Interpark"
        trfc = "3TF"
        traveldays = 0
        triptype = "OW"

        for row in rows:
            via = row.find(class_='t4').get_text().strip().replace("회 경유", "").replace("                중간경유          주유 공급과 항공기 정비를 위해           기착지 대기 후 다음 목적지로 이동합니다.", "").replace("직항","0")
            airline = row.find(class_='airportName').get_text().strip()
            fares = row.find(class_='charge-select-list').find_all('li')
            badge = row.find(class_='best-group').get_text().strip()
            for fare in fares:
                price = fare.find(class_='charge-detail').get_text().strip().replace("원", "").replace(",", "").replace("~", "")
                price_type = fare.label.get_text().strip().replace("결제조건", "")
                result.loc[len(result) + 1] = [date, ota, dep_date2, trfc, departure, destination, via, airline, int(price), currency, price_type, badge, traveldays, triptype]

        time.sleep(0.5)
        print(result)

    except:
        return None

# Main function
if __name__ == '__main__':
   start_time = time.time()
   pool = Pool(processes=4)
   pool.map(make_request, merge_list)
   print("실행 시간(초) : %s" % (time.time() - start_time))