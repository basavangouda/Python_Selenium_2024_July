"""
#Case 1
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

#Switching to the frame
driver.switch_to.frame(0)
year="2025"
month='January'
date='31'

#Find the date text filed and click on it
date_text_field=driver.find_element(By.ID,"datepicker")
date_text_field.click()
#send_keys method it will not work here
#date_text_field.send_keys("31/01/2025")

while True:
    Month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    Year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if Month==month and Year==year:
        print(Month,Year)
        break
    else:
        right_Arro=driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']")
        right_Arro.click()

#Select the date
dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for Date in dates:
    #print(Date.text)
    if Date.text==date:
        Date.click()
        break

time.sleep(5)
driver.close()
"""

#Case 2
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

#Switching to the frame
driver.switch_to.frame(0)
year="1994"
month='June'
date='8'

#Find the date text filed and click on it
date_text_field=driver.find_element(By.ID,"datepicker")
date_text_field.click()
#send_keys method it will not work here
#date_text_field.send_keys("31/01/2025")

while True:
    Month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    Year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if Month==month and Year==year:
        print(Month,Year)
        break
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()


#Select the date
dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for Date in dates:
    #print(Date.text)
    if Date.text==date:
        Date.click()
        break

time.sleep(5)
driver.close()
