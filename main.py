from src.extract import extract_samrc_data
from src.transform import clean_samrc_data
from src.load import load_samrc_to_sqlite

def run_pipeline():
    print("Starting ETL Pipeline ....")

    raw_df = extract_samrc_data("data/raw/samrc_mortality_data.xlsx")

    # Tranform

    clean_df = clean_samrc_data(raw_df)

    # Load

    load_samrc_to_sqlite(clean_df)

    print("Pipeline complete")

if __name__ == "__main__":
    run_pipeline()
