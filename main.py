import os
import json
import requests
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()  # loads .env in the project root

# def extract_data(url):


#     headers = {"accept": "application/json",
#            'X-Api-Key':'23563a7b6971484fbb59485aba2ecd79'}

#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#             data = response.json()
#             df = pd.json_normalize(data)
#             print('data extracted')
#             return df
#     else:
#             print(f'error occurred due to :  {response.status_code}')
# url = "https://api.rentcast.io/v1/properties/random?limit=500"
# data = extract_data(url)
# #print(data)

# def transform_data():


# --- Config ---
API_URL = "https://api.rentcast.io/v1/properties/random?limit=500"
API_KEY = os.getenv("RENTCAST_API_KEY")

PGHOST = os.getenv("PGHOST", "localhost")
PGPORT = os.getenv("PGPORT", "5433")
PGUSER = os.getenv("PGUSER", "postgres")
PGPASSWORD = os.getenv("PGPASSWORD")
PGDATABASE = os.getenv("PGDATABASE", "MetroPeak_staging")

STAGING_SCHEMA = "staging"
STAGING_TABLE = "rentcast_properties_stg"   # table name in staging schema

# --- Helpers ---
def extract_data(url: str) -> pd.DataFrame:
    headers = {
        "accept": "application/json",
        "X-Api-Key": API_KEY
    }
    r = requests.get(url, headers=headers, timeout=60)
    if r.status_code != 200:
        raise RuntimeError(f"API error: {r.status_code} - {r.text[:300]}")
    data = r.json()
    # normalize JSON -> flat table
    df = pd.json_normalize(data)
    # optional: ensure postgres-friendly column names
    df.columns = (
        df.columns
        .str.replace("[^0-9a-zA-Z_]", "_", regex=True)
        .str.replace("_+", "_", regex=True)
        .str.strip("_")
        .str.lower()
    )
    # optional: convert lists/dicts to JSON strings so to_sql won’t choke
    for c in df.columns:
        if df[c].apply(lambda x: isinstance(x, (list, dict))).any():
            df[c] = df[c].apply(lambda x: json.dumps(x) if isinstance(x, (list, dict)) else x)
    return df

def get_engine():
    url = f"postgresql+psycopg2://{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}/{PGDATABASE}"
    return create_engine(url, future=True)

def load_to_staging(df: pd.DataFrame):
    engine = get_engine()
    with engine.begin() as conn:
        # ensure schema exists
        conn.execute(text(f'CREATE SCHEMA IF NOT EXISTS "{STAGING_SCHEMA}"'))
        # load (replace = truncate-and-recreate for staging); use batches
        df.to_sql(
            STAGING_TABLE,
            con=conn,
            schema=STAGING_SCHEMA,
            if_exists="replace",   # or "append" if you want to accumulate
            index=False,
            method="multi",
            chunksize=1000,
        )
        # (optional) add ingestion timestamp column
        conn.execute(text(f'''
            ALTER TABLE "{STAGING_SCHEMA}"."{STAGING_TABLE}"
            ADD COLUMN IF NOT EXISTS ingested_at timestamptz DEFAULT now();
        '''))

def main():
    df = extract_data(API_URL)
    print(f"Extracted {len(df)} rows, {len(df.columns)} columns")
    load_to_staging(df)
    print(f'Loaded into {STAGING_SCHEMA}.{STAGING_TABLE}')

if __name__ == "__main__":
    main()
