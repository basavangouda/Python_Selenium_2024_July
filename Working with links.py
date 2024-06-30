#internal links
#External links
#broken links ===> No target is associated.

#//a ===>It will highlight the list of links which are present on the webpage
# href ==>hyperlink reference.
#Write a program to print the total number of links present on webpage
# and print name of each link
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://qacircle.in")
# driver.maximize_window()
# links=driver.find_elements(By.TAG_NAME,'a')
# print("Total number of links =",len(links))
#
# #Print the all links name
# for link in links:
#     print(link.text)
#
# time.sleep(5)
# driver.quit()

#broken links ===> No target is associated.
#Example 1
# import time
# import requests
# count=0
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://bstackdemo.com/")
# driver.maximize_window()
# links=driver.find_elements(By.TAG_NAME,'a')
# for link in links:
#     url=link.get_attribute('href')
#     res=requests.head(url)
#     if res.status_code>=400:
#         print(url," It is broken ")
#         count=count+1
#
# time.sleep(5)
# print("The total number of broken links =",count)
# driver.quit()

#Example 2 :
import time
import requests
count=0
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
links=driver.find_elements(By.TAG_NAME,'a')
for link in links:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
        if res.status_code>=400:
            print(url," It is broken ")
            count=count+1
    except Exception:
        print("No Exception")
time.sleep(5)
print("The total number of broken links =",count)
driver.quit()