"""
Alert is not a web element, we can't inspect. it's a special object we have to handle differently

Types of Alerts
1. simple alert
2. Prompt alert
3. Confirmation alert

"""
# Example 1 ==> Simple Alert
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# driver.maximize_window()
# driver.find_element(By.ID,"test-alert").click()
# time.sleep(5)
# alert_window=driver.switch_to.alert
# time.sleep(5)
# print(alert_window.text)
# alert_window.accept()
# time.sleep(5)
# driver.close()

# Example 2 ==> Simple Alert
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
# time.sleep(5)
# driver.switch_to.alert.accept()
# time.sleep(5)
# driver.close()

# Example 3 ==> Confirmation Alert
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
# time.sleep(5)
# driver.switch_to.alert.accept()
# exp_res='You clicked: Ok'
# assert exp_res==driver.find_element(By.ID,"result").text
# time.sleep(5)
# driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
# time.sleep(5)
# driver.switch_to.alert.dismiss()
# exp_result="You clicked: Cancel"
# assert exp_result==driver.find_element(By.ID,"result").text
# time.sleep(5)
# driver.close()

# Example 4 ==> Prompt Alert
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
# time.sleep(5)
# window_ele=driver.switch_to.alert
# window_ele.send_keys("QACircle Software Training Academy")
# window_ele.accept()
# exp_result="You entered: QACircle Software Training Academy"
# assert exp_result==driver.find_element(By.ID,"result").text,"Both element texts are different"
# time.sleep(5)
# driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
# time.sleep(5)
# window_ele=driver.switch_to.alert
# window_ele.send_keys("QACircle Software Training Academy")
# window_ele.dismiss()
# exp_re="You entered: null"
# assert exp_re==driver.find_element(By.ID,"result").text
# driver.close()

# Authenication popup
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# #Syntax ==> https://username:password@url of the application
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
# driver.maximize_window()
# time.sleep(5)
# driver.close()

# Handling notification popups
"""
1. We can disable this kind of popups from the browser by passing parameters
2. For this we need to create chrome options
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=ops)
driver.get("https://whatmylocation.com/")
driver.maximize_window()
time.sleep(5)
driver.close()
