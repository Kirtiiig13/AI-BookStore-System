import sqlite3
import pandas as pd

conn = sqlite3.connect("bookstore.db")

pd.read_csv("data/books.csv").to_sql(
    "books",
    conn,
    if_exists="replace",
    index=False
)

pd.read_csv("data/customers.csv").to_sql(
    "customers",
    conn,
    if_exists="replace",
    index=False
)

pd.read_csv("data/sales.csv").to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Data Imported")