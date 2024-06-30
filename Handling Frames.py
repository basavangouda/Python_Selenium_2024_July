
"""
===>Whenever we want to find an element which are present inside a iframe , we have to
switch to that particular frame and find the element . 

===>Directly we can't find an element

#Switching to the particular frame
driver.switch_to.frame(name of the frame)
driver.switch_to.frame(id of the frame)
driver.switch_to.frame(web element)

#Switching back to the parent window
driver.switch_to.default_content()
driver.switch_to.parent_frame()

"""
#Write a selenium script to find total number of frames present inside webpage
# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# URL="file:///D:/Python_SDET_March-2024-Batch/HTML/Handling%20frames.html"
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get(URL)
# driver.maximize_window()
# time.sleep(5)
# list_of_frames=driver.find_elements(By.TAG_NAME,"iframe")
# print(len(list_of_frames))
# time.sleep(5)
# driver.close()

#Write a selenium script to find total number of frames present in webpage
# and switch to each frame and print one statement

# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# driver.maximize_window()
# time.sleep(5)
# list_of_frames=driver.find_elements(By.TAG_NAME,"iframe")
# print(len(list_of_frames))
#
# frame1=driver.find_element(By.XPATH,"//iframe[@name='test-iframe']")
# frame2=driver.find_element(By.XPATH,"//iframe[@src='droppable.html']")
# frame3=driver.find_element(By.XPATH,"//iframe[@src='menu.html']")
# frame4=driver.find_element(By.XPATH,"//iframe[@src='tooltip.html']")
#
# #Switch to frame 1 and print I am in frame one
# driver.switch_to.frame(frame1)
# print("I am in frame1")
#
# driver.switch_to.default_content()
# #Switch to frame 2 and print I am in frame two
# driver.switch_to.frame(frame2)
# print("I am in frame2")
#
# driver.switch_to.default_content()
# #Switch to frame 3 and print I am in frame three
# driver.switch_to.frame(frame3)
# print("I am in frame3")
#
# driver.switch_to.default_content()
# #Switch to frame 4 and print I am in frame four
# driver.switch_to.frame(frame4)
# print("I am in frame4")
#
# driver.switch_to.default_content()
# driver.find_element(By.XPATH,"//button[@name='submit_button']").click()
# driver.switch_to.alert.accept()
# time.sleep(5)
# driver.close()

#Write a selenium script to find a submit button present inside iframe element , perform click action
#and handle the alert window
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
driver.maximize_window()
time.sleep(5)
frame1=driver.find_element(By.NAME,"test-iframe")

#Switch to frame 1 and print I am in frame one
driver.switch_to.frame(frame1)
driver.find_element(By.NAME,'frame_submit_button').click()
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(5)

driver.switch_to.parent_frame()
#switch to frame 3 and get the text of books element.
frame_3=driver.find_element(By.XPATH,"//iframe[@src='menu.html']")
driver.switch_to.frame(frame_3)
print(driver.find_element(By.XPATH,"//ul[@id='menu']/li[2]").text)
time.sleep(5)
driver.close()