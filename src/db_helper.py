import sqlite3
import pandas as pd

DB = "bookstore.db"

def get_books():
    conn = sqlite3.connect(DB)
    df = pd.read_sql(
        "SELECT * FROM books",
        conn
    )
    conn.close()
    return df

def get_customers():
    conn = sqlite3.connect(DB)
    df = pd.read_sql(
        "SELECT * FROM customers",
        conn
    )
    conn.close()
    return df

def get_sales():
    conn = sqlite3.connect(DB)
    df = pd.read_sql(
        "SELECT * FROM sales",
        conn
    )
    conn.close()
    return df