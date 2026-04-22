import sqlite3
import pandas as pd

DB_PATH = "ola_rides.db"
CSV_PATH = "cleaned_ola_data.csv"


def get_connection():
    return sqlite3.connect(DB_PATH)


def run_query(query):
    conn = get_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def create_database():
    df = pd.read_csv(CSV_PATH)

    conn = get_connection()
    df.to_sql("rides", conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()

    print("DB created with rows:", len(df))