# Public Health Tracker

## Overview
[Write 2-3 sentences here explaining that this is an ETL pipeline built in Python to process South African COVID-19 and mortality data, and eventually load it into a PostgreSQL Star Schema.]

## Architecture & Tech Stack
* **Language:** Python 3
* **Data Processing:** Pandas
* **Database:** PostgreSQL (Star Schema)
* **Environment:** Ubuntu Linux

## Data Sources
* **Confirmed Cases:** 
* **Excess Mortality:** 

## Local Setup & Installation
To run this pipeline locally, run the following commands in your terminal:

1. Clone the repository:
   `git clone https://github.com/ltshabalala39-blip/public_health_tracker.git`
2. Navigate into the directory:
   `cd public_health_tracker`
3. Create and activate the virtual environment:
   `python3 -m venv venv`
   `source venv/bin/activate`
4. Install the required dependencies:
   `pip install -r requirements.txt`

## Project Status
Currently in active development. Completed the ingestion and daily transformation scripts. Working on parsing the SAMRC Excel datasets.
