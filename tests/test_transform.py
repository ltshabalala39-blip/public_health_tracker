import pandas as pd
from src.extract import extract_samrc_data
from src.transform import clean_samrc_data

def test_clean_samrc_data_formats_columns_correctly():
    raw_df = extract_samrc_data("data/raw/samrc_mortality_data.xlsx")

    clean_df = clean_samrc_data(raw_df)

    assert "week" in clean_df.columns, "Expected column 'week' was not found!"
    assert "eastern_cape" in clean_df.columns, "Expected 'Eastern_cape'"
    assert "Unnamed" not in clean_df.columns, "The old column name should have been removed"




