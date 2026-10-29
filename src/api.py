from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import pandas as pd

# This creates the actual web server application

app = FastAPI(title="Public Health OutBreak API", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
            #We're going  use Pandas to execute a SQL query against our SQLite database
            #we select the 'week' column and whichever province the user requested

            query = f"SELECT week, {province} FROM mortality_data"
            df = pd.read_sql(query, conn)
            df = df.replace({float('nan'):None})

            return df.to_dict(orient="records")


    except Exception as e:
        #If the user types the province that doesnt exist we return a professional 404 error
        raise HTTPException(status_code=404, detail =f"could not find the province{province}.Make sure it is snake_case")
