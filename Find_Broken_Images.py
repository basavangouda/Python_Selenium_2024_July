import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Initialize WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#https://www.nykaa.com/ ==> We will get no broken images
#https://www.hubspot.com/ ==> We will get 3 broken images

# Navigate to a webpage
driver.get('https://www.hubspot.com/')
driver.maximize_window()


# Find all image elements
images = driver.find_elements(By.TAG_NAME, "img")
print(len(images))

# Check each image
broken_images = []
for image in images:
    src = image.get_attribute("src")
    try:
        response = requests.get(src,timeout=5) #time out optional
        if response.status_code != 200:
            broken_images.append(src)
    except requests.exceptions.RequestException as e:
        broken_images.append(src)
        print("Error with image ",src,":",e)

# Report broken images
if broken_images:
    print("Found broken images:",len(broken_images))
    for img in broken_images:
        print(img)
else:
    print("No broken images found.")

# Close the browser
driver.quit()