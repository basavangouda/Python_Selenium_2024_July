
#Chrome Browser
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

ops=webdriver.ChromeOptions()
ops.add_argument("--headless=new")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=ops)

driver.get("https://www.qacircle.in/")
driver.implicitly_wait(10)
driver.maximize_window()
print("The Title of the page =",driver.title)
print(driver.current_url)
driver.close()

#Microsoft edge browser
def headless_edge():
    from selenium import webdriver
    from selenium.webdriver.edge.service import Service as edgeservice
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    ops=webdriver.EdgeOptions()
    ops.add_argument("--headless=new")
    driver=webdriver.Edge(service=edgeservice(EdgeChromiumDriverManager().install()),options=ops)
    return driver

driver=headless_edge()
driver.get("https://www.google.com/")
driver.maximize_window()
print("The Title of the page =",driver.title)
print(driver.current_url)
driver.close()

#Firefox Browser
def headless_firefox1():
    from selenium import webdriver
    from selenium.webdriver.firefox.service import Service as firefoxservice
    from webdriver_manager.firefox import GeckoDriverManager
    ops=webdriver.FirefoxOptions()
    ops.add_argument("--headless")
    driver=webdriver.Firefox(service=firefoxservice(GeckoDriverManager().install()),options=ops)
    return driver

driver=headless_firefox1()
driver.get("https://www.google.com/")
driver.maximize_window()
print("The Title of the page =",driver.title)
print(driver.current_url)
driver.close()


def headless_firefox2():
    from selenium import webdriver
    from selenium.webdriver.firefox.service import Service as firefoxservice
    from webdriver_manager.firefox import GeckoDriverManager
    from selenium.webdriver.firefox.options import Options
    ops=Options()
    ops.add_argument("--headless")
    driver=webdriver.Firefox(service=firefoxservice(GeckoDriverManager().install()),options=ops)
    return driver

driver=headless_firefox2()
driver.get("https://www.google.com/")
driver.maximize_window()
print("The Title of the page =",driver.title)
print(driver.current_url)
driver.close()