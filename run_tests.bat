@echo off
:: Navigate to project directory
cd  /d D:\Git-Git-Hub\July-2024\Python_Selenium_2024_July

:: Set up virtual environment
python -m venv venv
call venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt

:: Run Python script
python Date_Picker.py
python Drop_Down.py

