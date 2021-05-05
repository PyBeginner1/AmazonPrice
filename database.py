import sqlite3
import pandas as pd

#connecting to database
conn =sqlite3.connect('amazontracker1.db')

df =pd.read_sql_query('''SELECT * FROM prices''', conn)

print(df)