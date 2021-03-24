# Airfare Tracker: Web Scraping and Visualizing the Flight Price Data

Do you need price benchmarks data as an airline pricing analyst or travel agent? Are you a travler looking for the cheapest flight and the best date to fly to your destination? This project will guide you through the entire process of building your own price monitoring tool by web scraping the data with Python and visualizing it with Tableau and Excel.

The dashboard you create can be updated on daily basis applying RPA (Robotic Process Automation) with Python. It will enable you to promptly response to the market. This business intelligence will be an arsenal for your strategic decision making.

Note: The data you collect must be public data. Depending on the website and the country, web scraping may cause legal issues. Please examine commercial law and terms of the website.

See examples of the final dashboard in the link below.

[Tableau Dashboard](https://public.tableau.com/views/AirfareTracker/Dashboard?:language=ko&:retry=yes&:display_count=y&:origin=viz_share_link)

<p align="center">
  <img width="1110" alt="스크린샷 2021-03-24 오후 9 30 05" src="https://user-images.githubusercontent.com/44926255/112310642-2a01e280-8ce8-11eb-8682-f9dc9d5a67e3.png">
</p>

[Excel Dashboard](link)

<p align="center">
  <img width="1155" alt="스크린샷 2021-03-25 오전 1 28 59" src="https://user-images.githubusercontent.com/44926255/112346995-da341300-8d09-11eb-89a0-11a0e8816fdd.png">
</p>

## Methodology

The process can be divded into four main steps as following.

<p align="center">
  <img width="1132" alt="스크린샷 2021-03-12 오후 6 24 37" src="https://user-images.githubusercontent.com/44926255/110920030-41dc7c80-8360-11eb-8cf6-5f46055dc7ef.png">
</p>

### Requirements

[Python IDE with Python 3](https://www.jetbrains.com/pycharm/)\
[Microsoft Excel (2010 or later)](https://support.microsoft.com/en-us/office/start-the-power-pivot-add-in-for-excel-a891a66d-36e3-43fc-81e8-fc4798f39ea8)\
[Tableau Desktop](https://www.tableau.com/products/desktop/download)

### Libraries

Here are the Python packages used for this project:

[Selenium](https://pypi.org/project/selenium/)\
[BeautifulSoup](https://pypi.org/project/beautifulsoup4/)\
[Pandas](https://pypi.org/project/pandas/)\
[PyAutoGUI](https://pypi.org/project/PyAutoGUI/)\
[win32com.client](https://pbpython.com/windows-com.html)

## Data Preparation

The focus of this project is placed on economy seats and frequent flight routes from Seoul to abroad and from abroad to Seoul, Korea. This is just an example. Target routes can be modified to which you have interest in.

[target.xlsx](link)

<p align="center">
  <img width="1047" alt="스크린샷 2021-03-12 오후 6 59 54" src="https://user-images.githubusercontent.com/44926255/110924242-29bb2c00-8365-11eb-8b6f-48a6e6e4c000.png">
</p>

### Web Scraping

There are many travel metasearch engine (e.g., Skyscanner, Kayak, Expedia, etc.). For this project, the data were web-scraped from Google Flights and Interpark Ticket. Choose the metasearch engine which best suits your needs.

[googleflights_oneway.py](link)\
[googleflights_roundtrip.py](link)\
[interpark_oneway.py](link)\
[interpark_roundtrip.py](link)

Selenium package is used to automate web browser, and BeautifulSoup package extracts the data out of HTML and XML files. Both packages in action are shown below.

<p align="center">
  <img width="956" alt="스크린샷 2021-03-24 오후 9 58 39" src="https://user-images.githubusercontent.com/44926255/112314231-1fe1e300-8cec-11eb-91c7-30fbea36dcc0.png">
</p>

Once scraping for each route is completed, the data are saved in excel file. Number of output excel files should be same as number of target routes you have specified in target.xlsx.

### Data Wrangling

The data which have been scraped must be integrated as one file for the further analysis or visualization. The following Python code will perform the data merging.

[merged_data.py](link)\
[price_20210115.xlsx](link)

<p align="center">
  <img width="1365" alt="스크린샷 2021-03-22 오후 6 12 04" src="https://user-images.githubusercontent.com/44926255/111966339-26c8f400-8b3a-11eb-9720-c3662bc5fd7c.png">
</p>

## Visualization

Tableau and Excel were used for data visualization. Map chart is also available on Excel depending on the version.

[Airfare Tracker.twb](link)\
[Aifrare Tracker.xlsx](link)

## Data Update

Daily data update is achievable. In order to web-scrape flight price data automatically on daily basis, make batch files for each Python code that you have created. Then schedule to run the batch files using Task Scheduler (Windows) or Automator (Mac). This will able you to obtain raw data automatically.

[Windows Task Scheduler](https://www.thewindowsclub.com/how-to-schedule-batch-file-run-automatically-windows-7)\
[Macintosh Automator](https://support.apple.com/en-eg/guide/automator/welcome/mac)
