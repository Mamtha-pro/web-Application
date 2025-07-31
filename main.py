import pandas as pd
import sqlite3

# Load CSV files
products = pd.read_csv("products.csv")
users = pd.read_csv("users.csv")
orders = pd.read_csv("orders.csv")

# Connect to SQLite
conn = sqlite3.connect("store.db")
cursor = conn.cursor()

# Save data to SQLite tables
products.to_sql("products", conn, if_exists="replace", index=False)
users.to_sql("users", conn, if_exists="replace", index=False)
orders.to_sql("orders", conn, if_exists="replace", index=False)

# Basic SELECT query
print("Sample Products:")
for row in cursor.execute("SELECT * FROM products LIMIT 5"):
    print(row)

conn.close()
