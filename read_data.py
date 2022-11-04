import sqlite3
import pandas as pd

conn = sqlite3.connect("amazontracker.db")

df = pd.read_sql_query("""SELECT * FROM prices""", conn)

print(df)
