# ism2411-data-cleaning-copilot

This project cleans a messy sales dataset using Python. It was created for my ISM2411 class to practice basic data cleaning and using GitHub Copilot.

## What the project does
- Loads the raw CSV file
- Cleans column names
- Removes extra spaces in text columns
- Handles missing price and quantity values
- Removes negative values
- Saves a cleaned CSV file

## Folder structure
- data/raw/ → contains the original CSV  
- data/processed/ → cleaned CSV output  
- src/data_cleaning.py → the main script  
- README.md → project info  
- reflection.md → my explanation of Copilot use  

## How to run the script
From the project’s main folder, run:
python src/data_cleaning.py

The cleaned file will appear in:
data/processed/sales_data_clean.csv


## Copilot usage
I used GitHub Copilot to help generate some functions in my script, especially `load_data()` and `clean_column_names()`. I reviewed and edited the generated code.

