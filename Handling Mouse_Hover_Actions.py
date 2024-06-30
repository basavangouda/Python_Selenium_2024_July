
#Example 1
"""import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.firstcry.com/")
driver.maximize_window()

time.sleep(5)
boy_fashion_ele=driver.find_element(By.XPATH,"//div[@class='menu-container']/ul/li[2]")

watches_ele=driver.find_element(By.XPATH,"//a[@href='https://www.firstcry.com/fashion-accessories/22/275?gender=boy,unisex&ref2=menu_dd_boy-fashion_watches_H']")

#Mouse Hover Action
act=ActionChains(driver)
act.move_to_element(boy_fashion_ele).move_to_element(watches_ele).click().perform()
time.sleep(5)
driver.close() """

"""
#Example 2
#We want to perform below actions on the website
#left Click ==>id="left-click"
#Right Click ==>id=right-click
#Double Click ==>id=double-click

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
driver.maximize_window()
time.sleep(5)
#left Click ==>id="left-click"
left_click=driver.find_element(By.ID,"left-click")
left_click.click()
time.sleep(5)
driver.switch_to.alert.accept()

#Right Click ==>id=right-click
right_click=driver.find_element(By.ID,"right-click")
act=ActionChains(driver)
act.context_click(right_click).perform()
time.sleep(5)
driver.switch_to.alert.accept()

#Double Click ==>id=double-click
double_click=driver.find_element(By.ID,"double-click")
act=ActionChains(driver)
act.double_click(double_click).perform()
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(5)
driver.close()
"""

"""
#Example 3:  Drag and Drop
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

source=driver.find_element(By.ID,"draggable")
target=driver.find_element(By.ID,"droppable")

act=ActionChains(driver)
act.drag_and_drop(source,target).perform()
time.sleep(5)
driver.close() """

"""
#Example 4 : Slider
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://jqueryui.com/slider/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.switch_to.frame(0)
min_slider=driver.find_element(By.XPATH,"//div[@id='slider']/span")
print(min_slider.location)

act=ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,200,200).perform()
time.sleep(5)
print(min_slider.location)
driver.close() """

#Scrolling the Page
"""
#Example 1 ==> Scroll by pixel 
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://jqueryui.com/slider/")
driver.maximize_window()
driver.implicitly_wait(10)

value=driver.execute_script("return window.pageYOffset;")
print("The scroll pixel initial value =",value)

#Scroll down the page by pixel
driver.execute_script("window.scrollBy(0,900)","")
time.sleep(5)

value=driver.execute_script("return window.pageYOffset;")
print("The Number of Pixel Moved =",value)
time.sleep(5)

driver.close()
"""

#Scrolling the Page
#Example 2 ==> Scroll till the element is visible
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.switch_to.frame("frame-one796456169")
submit_button=driver.find_element(By.XPATH,"//input[@name='Submit']")

driver.execute_script("arguments[0].scrollIntoView();",submit_button)
time.sleep(5)

value=driver.execute_script("return window.pageYOffset;")
print("The Number of Pixel Moved =",value)
driver.refresh()
time.sleep(5)

#Scroll till end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("The Number of Pixel Moved =",value)
time.sleep(5)

#Scroll to the Starting Position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("The Number of Pixel Moved =",value)
time.sleep(5)

driver.close()
