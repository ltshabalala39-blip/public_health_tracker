"""
Data Transformation Module For the Public Health tracker

THis module processes raw COVID-19 data, handling type conversions
and aggregating daily metrics into ISO Epidemiological weeks

"""

import logging
import pandas as pd

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

def transform_official_cases(input_path : str, output_path: str) -> None:
    """
    Reads raw CSV data, converts dates into ISO Epi-weeks, and sets up the dataframe.

    Args:
        input_path (str): The path to the raw daily CSV data.
        output_path (str): The path to save the cleaned, weekly aggregated data.
    """

    logging.info(f"Loading raw data from : {input_path}")
    try:
        # Load the CSV into a Pandas DataFrame
        df = pd.read_csv(input_path)

        #  Convert the raw string column into a Datetime object
        df['date'] = pd.to_datetime(df['YYYYMMDD'], format='%Y%m%d')

        #  Extract the ISO Year and Week number
        df['epi_year'] = df['date'].dt.isocalendar().year
        df['epi_week'] = df['date'].dt.isocalendar().week

        #  Format it to exactly match the SAMRC format (e.g., "2020-W10")
        df['samrc_week_format'] = df['epi_year'].astype(str) + "-W" + df['epi_week'].astype(str)

        # Print the first 5 rows to prove the conversion worked
        logging.info(f"Date conversion complete. Sample data:\n{df[['date', 'samrc_week_format']].head()}")

    except FileNotFoundError:
        logging.error(f"Input file not found at {input_path}")
        raise

    except KeyError as error:
        logging.error(f"Missing expected column in CSV: {error}")
        raise

if __name__ == "__main__" :
    RAW_DATA_PATH = "data/raw/confirmed_cases.csv"
    CLEAN_DATA_PATH = "data/processed/weelkly_cases.csv"


    print("DEBUG : tHE EXECUTION BLOCK HAS STARTED")
    transform_official_cases(input_path = RAW_DATA_PATH, output_path= CLEAN_DATA_PATH)
