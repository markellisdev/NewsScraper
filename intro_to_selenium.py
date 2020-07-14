# Import Relevant Packages
import json
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
webdriver_path = r'./chromedriver'

# Path to webdriver
browser = webdriver.Chrome(webdriver_path)

# URL to scrape
browser.get("https://www.marketwatch.com/markets?mod=breadcrumb")

# Get positive stocks 
indicators = browser.find_elements_by_xpath('//bg-quote[@class="positive"]')

# Get list of indicators
indicators_list = []
for ind in range(len(indicators)):
    indicators_list.append(indicators[ind].text)

# Search 
# indicators.send_keys('selenium python API' + Keys.RETURN)
# assert "No results found." not in browser.page_source
print(indicators_list)

# Quit
browser.close()