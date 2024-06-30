
"""
In selenium, we can handle dropdown with the help of select class

Multiple options to handle dropdown
1. select_by_index(int index)
2. select_by_value(String value)
3. select_by_visible_text(String text)


"""
#Example 1
# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# driver.maximize_window()
# drop_down_ele=driver.find_element(By.ID,"projectName")
# drop_down=Select(drop_down_ele)
# drop_down.select_by_value("Project-4")
# time.sleep(5)
# drop_down.select_by_visible_text("Project-1")
# time.sleep(5)
# drop_down.select_by_index(5)
# time.sleep(5)
# driver.close()

#Example 2
# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# drop_down=Select(driver.find_element(By.ID,"country"))
# all_options=drop_down.options
# #get the text of all the elements
# for option in all_options:
#     print(option.text)
# time.sleep(5)
# drop_down.select_by_visible_text("India")
# time.sleep(5)
# #Deselect option only possible in multi select drop down
# #drop_down.deselect_by_value("India") ==> This code will not work here
# driver.close()


#How to handle multi select dropdown
#Example 3
# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# mul_sel_drop_down=Select(driver.find_element(By.ID,"colors"))
# print(mul_sel_drop_down.is_multiple)
# mul_sel_drop_down.select_by_value("yellow")
# time.sleep(5)
# mul_sel_drop_down.select_by_visible_text("Green")
# time.sleep(5)
# mul_sel_drop_down.select_by_index(1)
# time.sleep(5)
# # mul_sel_drop_down.deselect_by_value("yellow")
# # time.sleep(5)
# # mul_sel_drop_down.deselect_by_index(1)
# # time.sleep(5)
# #first selected option to get text
# print(mul_sel_drop_down.first_selected_option.text)
#
# #all selected options to get text
# all_selected=mul_sel_drop_down.all_selected_options
# for x in all_selected:
#     print(x.text)
# time.sleep(5)
# mul_sel_drop_down.deselect_all()
# time.sleep(5)
# driver.close()

#We can handle dropdown without using select class
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
dropdownlist=driver.find_elements(By.ID,"colors")

for x in dropdownlist:
    print(x.text)
    x.click()
    time.sleep(2)

time.sleep(5)
driver.close()






