import sqlite3
import pandas as pd

def load_samrc_to_sqlite(df, db_path = "data/processed/health_data.db"):
    """Loads the cleaned Dataframe into SQLite database"""

    #I used a context manager (with) so the database connection closses automatically

    with sqlite3.connect(db_path) as conn:
        df.to_sql("mortality_data", con=conn, if_exists ="replace", index=False)

    print(f"Succesfully loaded data into {db_path}")