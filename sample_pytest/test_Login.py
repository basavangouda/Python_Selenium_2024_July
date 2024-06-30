import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
@allure.severity(allure.severity_level.CRITICAL)
class TestLogin:
    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.ID,"input-email").send_keys("basavana003@gmail.com")
        self.driver.find_element(By.ID,"input-password").send_keys("@fYAguUXRq8J@y")
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        assert self.driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="login_with_valid_credentials",attachment_type=AttachmentType.PNG)

    def test_login_without_entering_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys("")
        self.driver.find_element(By.ID, "input-password").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_warning_message="Warning: No match for E-Mail Address and/or Password."
        #Now error message having not only text include, I tags so i will check contains
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)
        allure.attach(self.driver.get_screenshot_as_png(), name="login_without_entering_credentials",attachment_type=AttachmentType.PNG)