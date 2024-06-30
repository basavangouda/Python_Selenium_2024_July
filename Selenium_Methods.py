"""
Selenium Methods
    1. Application Commands
    2. Conditional Commands
    3. Browser Commands
    4. Navigation Commands
    5. Wait commands

1. Application Commands

title ==> Used to get the title of the web page
current_url ==> Used to get the current URL of the web page
page_source ==> To Capture the Page Source of an application
get ===> To Open an application
"""
import time



# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://www.aha.video/")
# print(driver.title)
# print(driver.current_url)
# print(driver.page_source)
# driver.close()

"""
 2. Conditional Commands
 
 //div[@id='checkboxes']/descendant::input[@value='project-1']  
 //div[@id='checkboxes']/input[1]
 //input[@type='checkbox' and @value='project-1']
 
 1 . is_displayed()
 2.  is_enabled()
 3. is_selected()
 
"""
#Example 1
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://www.google.com/")
# driver.maximize_window()
# e=driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']/center/input[1]")
# print(e.is_displayed())
# time.sleep(5)
# print(driver.find_element(By.XPATH,"//textarea[@name='q']").is_enabled())
# driver.close()

#Example 2

# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://www.facebook.com/r.php")
# driver.maximize_window()
# print("*****find multiple elements (Multiple radio button)************")
# e=driver.find_elements(By.XPATH,"//input[@type='radio']")
# for i in e:
#     print(i.is_displayed())
# time.sleep(5)
# print("*******************Is Selected***************************")
# for i in e:
#     print(i.is_selected())
# time.sleep(5)
# print("******************Is Selected after clicking on element************************")
# for i in e:
#     i.click()
#     print(i.is_selected())
# time.sleep(5)
#
# print("******************Is enabled ************************")
# for i in e:
#     print(i.is_enabled())
# time.sleep(5)
#
# driver.close()
"""
Assignment 
Step 1 ==> Open the application : https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html
Step2 ==> Find all check boxes
Step 3 ==> check the status of all check boxes is selected
Step 4 ==> Select all check boxes
step 5 ==> check the status of all check boxes is selected
Step 6 ==> Deselect all check boxes 
Step 7 ==>check the status of all check boxes is selected or deselected.
"""


"""
3. Browser Commands

close()
quit()

"""
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://www.facebook.com/r.php")
# driver.maximize_window()
# driver.get("https://www.google.com/")
# driver.maximize_window()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# time.sleep(5)
# driver.get("https://www.firstcry.com/")
# driver.find_element(By.XPATH,"//span[text()='Track Order']").click()
# time.sleep(5)
# driver.close()
# time.sleep(5)
# driver.quit()

"""
4. Navigation Commands
    back() ====> driver.back() 
    refresh()===> driver.refresh()
    forward() ==>driver.forward()
    
"""
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver=webdriver.Chrome()
# time.sleep(5)
# driver.get("https://www.saucedemo.com/")
# driver.find_element(By.ID,"user-name").send_keys("standard_user")
# driver.find_element(By.ID,"password").send_keys("secret_sauce")
# driver.find_element(By.NAME,"login-button").click()
# time.sleep(5)
# driver.refresh()
# time.sleep(5)
# driver.back()
# time.sleep(5)
# driver.forward()
# time.sleep(5)
# driver.quit()

#Difference between text and get_attribute Method
"""
Both text and get_attribute() methods are used in selenium to extract the data from web pages.
But there are some key differences .
text =======>Return the visible text of any element , including sub element 
get_attribute() ==> Return the Value of specific attribute of an element.
"""
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.saucedemo.com/")
# Login_button=driver.find_element(By.NAME,"login-button")
# print(Login_button.text)
# time.sleep(5)
# print(Login_button.get_attribute('value'))
# print(Login_button.get_attribute("type"))
# driver.quit()

"""
5. Wait commands
"""
#Using time Module
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://www.google.com/")
# driver.maximize_window()
# search_box=driver.find_element(By.XPATH,"//textarea[@name='q']")
# time.sleep(5)
# search_box.send_keys("selenium")
# time.sleep(5)
# search_box.submit()
# time.sleep(5)
# driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
# time.sleep(5)
# driver.close()

#Use Implicit Wait
#Example 1
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://www.google.com/")
# driver.implicitly_wait(10)
# driver.maximize_window()
# search_box=driver.find_element(By.XPATH,"//textarea[@name='q']")
# search_box.send_keys("selenium")
# search_box.submit()
# driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
# driver.close()

#Example 2
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.find_element(By.ID,"dynamic_btn").click()
# time.sleep(5)
# driver.close()

#Explicit Wait
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait=WebDriverWait(driver,10,3)
dynamic_ele=wait.until(EC.element_to_be_clickable((By.ID,"dynamic_btn")))



"""
#Example 1:
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# driver.maximize_window()
# try:
#     wait=WebDriverWait(driver,10,3)
#     dynamic_ele=wait.until(EC.element_to_be_clickable((By.ID,"dynamic_btn")))
#
# except :
#     dynamic_ele.click()
#
# finally:
#     driver.close()

#example 2:
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import *
from selenium.common import *
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
driver.maximize_window()
try:
    wait=WebDriverWait(driver,10,3,(NoSuchElementException,StaleElementReferenceException,ElementNotVisibleException,Exception))
    dynamic_ele=wait.until(EC.element_to_be_clickable((By.ID,"dynamic_btn")))

except :
    dynamic_ele.click()

finally:
    driver.close()


#Type of Selenium exeptions :

