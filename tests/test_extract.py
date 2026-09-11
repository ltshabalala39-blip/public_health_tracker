import pandas as pd
from src.extract import extract_samrc_data

def test_extract_samrc_returns_dataframe():
    file_path = "data/raw/samrc_mortality_data.xlsx"

    df = extract_samrc_data(file_path)

    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_extract_samrc_has_expected_colums():
    file_path = "data/raw/samrc_mortality_data.xlsx"
    df = extract_samrc_data(file_path)

    expected_provinces = ["EASTERN CAPE", "WESTERN CAPE" , "GAUTENG" , "KWAZULU NATAL"]

    for province in expected_provinces :
        assert province in df.columns, f"Missing expected column :{province}"