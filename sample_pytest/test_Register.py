import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class TestRegister:
    def test_creating_an_account_with_all_mandatory_field(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Register").click()
        self.driver.find_element(By.ID,"input-firstname").send_keys("Basavana")
        self.driver.find_element(By.ID,"input-lastname").send_keys("Gouda")
        self.driver.find_element(By.ID,"input-email").send_keys(self.generate_email_time_stamp())
        self.driver.find_element(By.ID, "input-telephone").send_keys("123456789")
        self.driver.find_element(By.ID,"input-password").send_keys("12345")
        self.driver.find_element(By.ID,"input-confirm").send_keys("12345")
        self.driver.find_element(By.NAME,"agree").click()
        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        expected_text="Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH,"//div[@id='content']/h1").text.__eq__(expected_text)
        allure.attach(self.driver.get_screenshot_as_png(),name="creating_an_account_with_all_mandatory_field",attachment_type=AttachmentType.PNG)
        self.driver.quit()

    def test_creating_an_account_by_providing_all_field(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Register").click()
        self.driver.find_element(By.ID,"input-firstname").send_keys("Basavana")
        self.driver.find_element(By.ID,"input-lastname").send_keys("Gouda")
        self.driver.find_element(By.ID,"input-email").send_keys(self.generate_email_time_stamp())
        self.driver.find_element(By.ID, "input-telephone").send_keys("123456789")
        self.driver.find_element(By.ID,"input-password").send_keys("12345")
        self.driver.find_element(By.ID,"input-confirm").send_keys("12345")
        self.driver.find_element(By.XPATH,"//input[@value='1' and @name='newsletter']").click()
        self.driver.find_element(By.NAME,"agree").click()
        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        expected_text="Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH,"//div[@id='content']/h1").text.__eq__(expected_text)
        allure.attach(self.driver.get_screenshot_as_png(), name="creating_an_account_by_providing_all_field",attachment_type=AttachmentType.PNG)
        self.driver.quit()

    def generate_email_time_stamp(self):
        import datetime
        # Get the current date and time
        now = datetime.datetime.now()
        # Format the timestamp as a string and replace '-', ':', and ' ' with '_'
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S").replace("-", "_").replace(":", "_").replace(" ", "_")
        print("Formatted Timestamp:", timestamp)
        return "basava"+timestamp+"@gmail.com"
