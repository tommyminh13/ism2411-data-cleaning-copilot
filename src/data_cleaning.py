"""
data_cleaning.py

This script loads a messy sales dataset, cleans it, and saves a processed version.
It demonstrates data cleaning and responsible use of GitHub Copilot.
"""

import pandas as pd

# This function loads the CSV file and returns a DataFrame.
def load_data(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        print("Loaded file successfully.")
        return df
    except FileNotFoundError:
        print("File not found:", file_path)
        raise

# This function cleans and standardizes column names.
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df

# This function handles missing values in the DataFrame.
def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["price", "quantity"])
    return df

# This function add invalid row removal function.
def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df["price"] >= 0]
    df = df[df["quantity"] >= 0]
    return df



