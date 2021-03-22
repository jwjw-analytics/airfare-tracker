# Airfare Tracker: Web Scraping and Visualizing the Flight Price Data

## Introduction

Do you need price benchmarks data as an airline pricing analyst or travel agent? Are you a travler looking for the cheapest flight and the best date to fly to your destination? This project will guide you through the entire process of building your own price monitoring tool by web scraping the data with Python and visualizing it with Tableau and Excel.

The dashboard you create can be updated on daily basis applying RPA (Robotic Process Automation) with Python. It will enable you to promptly response to the market. This business intelligence will be an arsenal for your strategic decision making.

Note: The data you collect must be public data. Depending on the website and the country, web scraping may cause legal issues. Please examine commercial law and terms of the website such as robots.txt.

See examples of the final dashboard in the link below.

[Tableau Dashboard](https://public.tableau.com/views/AirfareTracker/Dashboard?:language=ko&:retry=yes&:display_count=y&:origin=viz_share_link)

<img width="1030" alt="스크린샷 2021-03-11 오후 11 23 53" src="https://user-images.githubusercontent.com/44926255/110801765-e60ee680-82c0-11eb-88ea-9a8f8be29922.png">

[Excel Dashboard](link)

image

## Methodology

The process can be divded into four main steps as following.

<img width="1132" alt="스크린샷 2021-03-12 오후 6 24 37" src="https://user-images.githubusercontent.com/44926255/110920030-41dc7c80-8360-11eb-8cf6-5f46055dc7ef.png">

### Requirements

[Python IDE with Python 3](https://www.jetbrains.com/pycharm/)\
[Microsoft Excel (2010 or later)](https://support.microsoft.com/en-us/office/start-the-power-pivot-add-in-for-excel-a891a66d-36e3-43fc-81e8-fc4798f39ea8)\
[Tableau Desktop](https://www.tableau.com/products/desktop/download)

### Libraries

Here are the Python packages used for the project:

[Selenium](https://pypi.org/project/selenium/)\
[BeautifulSoup](https://pypi.org/project/beautifulsoup4/)\
[Pandas](https://pypi.org/project/pandas/)\
[PyAutoGUI](https://pypi.org/project/PyAutoGUI/)\
[win32com.client](https://pbpython.com/windows-com.html)

## Data Preparation

The focus of this project is placed on economy seats and frequent flight routes from Seoul to abroad and from abroad to Seoul, Korea. This is just an example. Target routes can be modified to which you have interest in.

[target.xlsx](link)

<img width="1047" alt="스크린샷 2021-03-12 오후 6 59 54" src="https://user-images.githubusercontent.com/44926255/110924242-29bb2c00-8365-11eb-8b6f-48a6e6e4c000.png">

### Web Scraping

There are many travel metasearch engine (e.g., Skyscanner, Kayak, Expedia, etc.). For this project, the data was web-scraped from Google Flights and Interpark Ticket. Choose the metasearch engine which best suits your needs.

[googleflights_oneway.py](link)\
[googleflights_roundtrip.py](link)\
[interpark_oneway.py](link)\
[interpark_roundtrip.py](link)

Selenium package is used to automate web browser and BeautifulSoup package extracts the data out of HTML and XML files. Both package in action are shown below.

<img width="907" alt="스크린샷 2021-03-22 오후 5 07 28" src="https://user-images.githubusercontent.com/44926255/111959304-9be3fb80-8b31-11eb-9afe-484b77840959.png">

output files.xlsx

### Wrangligh the Data (Data Cleansing)

merge.py
mergedoutput.xlsx

## Visualization
Visualization is important

## Dynamic Data Update
you need to see dynamic data

## Final Deliverables
After completion
