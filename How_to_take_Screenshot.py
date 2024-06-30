import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
driver.maximize_window()

#Case 1
#Save Screenshot at the specific location using .png file name
driver.save_screenshot("C:\\Users\\dell\\Downloads\\qacircle.png")
driver.save_screenshot("C:/Users/dell/Downloads/BG.png")

#Case 2
#Save Screenshot at the specific location using .png file name using OS module
driver.save_screenshot(os.getcwd()+"python.png")

#Case 3
driver.get_screenshot_as_file(os.getcwd()+" Homepage.png")
time.sleep(5)
driver.close()
