@echo off
:: Navigate to your project directory
cd  d/  D:\Git-Git-Hub\July-2024\Python_Selenium_2024_July\sample_pytest

:: Activate virtual environment
call venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt

:: Run pytest with Allure
pytest --alluredir=allure-results

:: Generate Allure report (optional, if you want to see it locally)
allure generate allure-results --clean -o allure-report

:: Deactivate virtual environment
deactivate