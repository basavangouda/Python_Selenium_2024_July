@echo off
:: Navigate to project directory


:: Set up virtual environment
python -m venv venv
call venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt

:: Run Python script
python Date_Picker.py
python Drop_Down.py

