import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
   outcome = yield
   rep = outcome.get_result()
   setattr(item, "rep_" + rep.when, rep)
   return rep


@pytest.fixture()
def log_on_failure(request):
   msgs = []
   yield
   item = request.node
   if item.rep_call.failed:
      allure.attach(driver.get_screenshot_as_png(), name="Failed Test Cases",
                    attachment_type=AttachmentType.PNG)


@pytest.fixture(params=["chrome","firefox","edge"])
def setup_and_teardown(request):
  #make drive as global, Otherwise we will get problem
  global driver
  if request.param == "chrome":
      driver = webdriver.Chrome()
  elif request.param == "firefox":
      driver = webdriver.Firefox()
  elif request.param == "edge":
      driver = webdriver.Edge()
  else:
      print("Please enter the valid browser")

  driver.get("https://tutorialsninja.com/demo/")
  driver.maximize_window()
  request.cls.driver = driver
  yield
  driver.quit()


