import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.hubspot.com/")
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//div[@id='hs-eu-opt-in-buttons']/button[2]").click()

#Capture the cookies from the browser
cookies=driver.get_cookies()
print("The Number of Cookies =",len(cookies))

for c in cookies:
    #print(c.get("key"))
    print(c.get('value'))

#Add cookies to browser
driver.add_cookie({"name":"1234","value":"mY qacIRCLE"})

print('******************Add cookies to browser*****************************************')
cookies=driver.get_cookies()
print("The Number of Cookies =",len(cookies))

for c in cookies:
    #print(c.get("key"))
    print(c.get('value'))

#Delete Specific cookies from browser
driver.delete_cookie("1234") # Here we have to pass name of the cookie

print('*********************elete Specific cookies from browser**************************************')
cookies=driver.get_cookies()
print("The Number of Cookies =",len(cookies))

for c in cookies:
    print(c.get('value'))

#Delete all the cookies
driver.delete_all_cookies()

print('******************Delete all the cookies ****************************************')
cookies=driver.get_cookies()
print("The Number of Cookies =",len(cookies))

for c in cookies:
    print(c.get('value'))


driver.quit()