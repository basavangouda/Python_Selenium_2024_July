

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.ID,"select2-billing_country-container").click()
time.sleep(5)

countries=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(countries))

for country in countries:
    if country.text=='India':
        print(country.text)
        country.click()
        break

time.sleep(5)

driver.close()