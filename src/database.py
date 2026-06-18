import sqlite3

conn = sqlite3.connect("bookstore.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    Book_ID TEXT PRIMARY KEY,
    Title TEXT,
    Author TEXT,
    Category TEXT,
    Price REAL,
    Stock INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers(
    Customer_ID TEXT PRIMARY KEY,
    Name TEXT,
    Age INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales(
    Sale_ID TEXT PRIMARY KEY,
    Customer_ID TEXT,
    Book_ID TEXT,
    Quantity INTEGER,
    Date TEXT
)
""")

conn.commit()
conn.close()

print("Database Created")