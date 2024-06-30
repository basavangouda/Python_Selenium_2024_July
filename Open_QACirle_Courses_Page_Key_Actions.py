import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://qacircle.com/")
driver.maximize_window()
time.sleep(5)
#Case 1 (By Selenum Actions)
driver.find_element(By.LINK_TEXT,"COURSES").click()
time.sleep(5)
driver.back()
time.sleep(5)

#Case 2
Course_link=Keys.CONTROL+Keys.ENTER
driver.find_element(By.LINK_TEXT,"COURSES").send_keys(Course_link)
time.sleep(5)

"""
Note : In this case selenium is focusing on parent tab,if i want to switch to
child tab , we have to use window handles method
"""

#Case 3
#Selenium 4 have new method to open it in new tab
driver.switch_to.new_window('tab')
driver.get("https://qacircle.in")
time.sleep(5)

#case 4
driver.switch_to.new_window('window')
driver.get("https://google.com")
time.sleep(5)
driver.close()