from fastapi import FastAPI, HTTPException
import sqlite3
import pandas as pd

# This creates the actual web server application

app = FastAPI(title="Public Health OutBreak API", version="1.0.0")

@app.get("health")
def health_check():
    """DevOps endpoint to verify the server is running"""
    return {"status": "online", "system": "operational"}

@app.get("/api/v1/cases/{province}")
def get_province_cases(province: str):
    """Fetches mortality/case data for a specific province"""
    db_path = "data/processed/health_data.db"

    try:
        with sqlite3.connect(db_path) as conn:
            #We goinhg  use Pands to execute a SQL query against our SQLite databse
            #we select the 'week' column and whicever province the user requested

            query = f"SELECT week, {province} FROM mortality_data"
            df = pd.read_sql(query, conn)

            return df.to_dict(orient="records")


    except Exception as e:
        #If the user types the province that doesnt exist we return a proffesional 404 error
        raise HTTPException(status_code=404, detail =f"could not find the province{province}.Make sure it is snake_case")
