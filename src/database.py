import sqlite3
import pandas as pd


def create_database():
    df = pd.read_csv("data/marketing_AB.csv")

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    conn = sqlite3.connect("ab_test.db")
    df.to_sql("marketing", conn, if_exists="replace", index=False)
    conn.close()

    print("Database created successfully!")


def run_query(query_file):
    conn = sqlite3.connect("ab_test.db")

    with open(query_file, "r") as file:
        query = file.read()

    result = pd.read_sql_query(query, conn)

    conn.close()

    return result