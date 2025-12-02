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
    df = df.dropna(subset=["price", "qty"])
    return df

# This function add invalid row removal function.
def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df["price"] >= 0]
    df = df[df["qty"] >= 0]
    return df

# Add the Required Main Block
if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)

    # Convert numeric columns (price, qty)
    df_clean["price"] = pd.to_numeric(df_clean["price"], errors="coerce")
    df_clean["qty"] = pd.to_numeric(df_clean["qty"], errors="coerce")

    # Strip whitespace from strings
    for col in df_clean.columns:
        if df_clean[col].dtype == "object":
            df_clean[col] = df_clean[col].str.strip()

    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)

    df_clean.to_csv(cleaned_path, index=False)

    print("Cleaning complete. First few rows:")
    print(df_clean.head())
