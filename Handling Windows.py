
#Example 1
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
current_window_id=driver.current_window_handle
print(current_window_id)
time.sleep(5)

driver.find_element(By.XPATH,"//a[@href='http://www.orangehrm.com']").click()
time.sleep(5)

#Find the Number of Browser Tabs
windows=driver.window_handles
print(len(windows))
for i in windows:
    print(i)

print("***********************************")
print("Parent window ID =",windows[0])
print("Child window ID =",windows[1])


# Get the title of the Tabs
# print(driver.title)
# driver.switch_to.window(windows[1])
# print(driver.title)
# driver.close()
#
# time.sleep(5)
# driver.switch_to.window(windows[0])
# print(driver.title)
# time.sleep(5)
# driver.close()

#Use for loop for closing tabs
for window in windows:
    driver.switch_to.window(window)
    if driver.title=="Human Resources Management Software | OrangeHRM" or "OrangeHRM":
        time.sleep(5)
        driver.close()

"""
#Example 2
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[text()='New Window']").click()
time.sleep(5)

window_ids=driver.window_handles
for window in window_ids:
    print(window)

print("Parent Window Id", window_ids[0])
print("child Window Id", window_ids[1])

print(driver.title)
driver.switch_to.window(window_ids[1])
print(driver.title)


for window in window_ids:
    driver.switch_to.window(window)
    if driver.title=="QACircle Software Training Academy":
        driver.close()

driver.switch_to.window(window_ids[0])
time.sleep(5)
driver.close()