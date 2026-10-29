import sqlite3
import pandas as pd

# Dimension Data: 2022 SA Census Estimates
POPULATION = {
    "gauteng": 15000000,
    "kwazulu_natal": 11500000,
    "western_cape": 7200000,
    "eastern_cape": 6600000,
    "limpopo": 5900000,
    "mpumalanga": 4700000,
    "north_west": 4100000,
    "free_state": 2900000,
    "northern_cape": 1300000
}

def enrich_data():
    # 1. Connect and load
    engine = sqlite3.connect("data/health_data.db")
    df = pd.read_sql("SELECT * FROM mortality_cases", engine)

    # 2. Join the dimension data (Population)
    df["population"] = df["province"].map(POPULATION)

    # 3. Calculate the per-capita rate
    df["mortality_rate_per_100k"] = (df["deaths"] / df["population"]) * 100000

    # 4. Clean up the floats for JSON compliance
    df["mortality_rate_per_100k"] = df["mortality_rate_per_100k"].round(2)

    # 5. Load into a new analytical table
    df.to_sql("enriched_mortality", engine, if_exists="replace", index=False)

    print(f"Successfully enriched {len(df)} rows and saved to 'enriched_mortality' table.")

if __name__ == "__main__":
    enrich_data()