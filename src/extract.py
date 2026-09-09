"""
Data Extraction Module for Public health tracker

This module handles the ingestion of raw Covid-19 data from external sources it includes
network error handling and logs execution states for monitoring
"""


import requests
import os
import logging
import pandas as pd


#Configuring professional logging
logging.basicConfig(
    level = logging.INFO,
    format ='%(asctime)s - %(levelname)s - %(message)s'
)

def download_official_cases(url:str, output_path: str) -> None:
    """
    Downloads a data file from a specified URL and saves it to a local directory.

    Args:
        url (str): The direct web URL to the target data file.
        output_path (str): The local relative file path where the data should be saved.

    Raises:
        requests.exceptions.RequestException: If the network connection fails or the URL is invalid.
    """
    # This Ensures that our target directory exists before attempting to save
    os.makedirs(os.path.dirname(output_path),exist_ok= True)
    logging.info(f"Starting the data extraction from : {url}")

    try:
        #This prevents the script from hanging infinitely incase the network is bad
        response = requests.get(url, timeout = 15)

        #This triggers and exception for 404(not found) or 500(SErver is down)
        response.raise_for_status()

        #Write the file in binary mode
        with open(output_path, "wb") as file:
            file.write(response.content)

        logging.info(f"Data securely saved to{output_path}")

    except requests.exceptions.RequestException as error :
        logging.error(f"Extraction failed. Network error occured : {error}")
        raise #Raise the error so that  the pipeline knows the extraction failed

def extract_samrc_data(file_path : str) -> pd.DataFrame:
    """
    Parses the SAMRC Excel file ,handling the formatted header rows and
    slicing out non-date summary rows.
    :param file_path:
    :return:
    """
    logging.info(f"Extracting SAMRC data from :{file_path}")

    # 1. Skip the first 2 rows so the province codes (EC, FS, GT) become headers
    print("Available sheets:", pd.ExcelFile(file_path, engine="openpyxl").sheet_names)
    df = pd.read_excel(
        file_path,
        engine="openpyxl",
        sheet_name="Province natural 1+yr",
        skiprows = 1
    )

    # 2. Its going to slice the dataframe to skip the first data row("Cumulative prior to first week")
    #iloc[1:] just means keep everything from index 1 only

    # df = df.iloc[1:].reset_index(drop=True)

    return df




if __name__ == "__main__" :
    # TARGET_URL = "https://raw.githubusercontent.com/dsfsi/covid19za/master/data/covid19za_provincial_cumulative_timeline_confirmed.csv"
    # LOCAL_FILE_PATH = "data/raw/confirmed_cases.csv"
    # download_official_cases(url=TARGET_URL, output_path=LOCAL_FILE_PATH)

    # tHis the to test the SAMRC extraction :
    samrc_file_path = "data/raw/samrc_mortality_data.xlsx"
    df_samrc = extract_samrc_data(samrc_file_path)
    print(df_samrc.head())
