import pandas as pd 
import sys, os
import sqlite3

questions = pd.read_csv(os.path.abspath("init_scripts\questions.csv")).drop(columns=['ID'])
conn = sqlite3.connect("myet.db")
cur = conn.cursor()

cur.execute("delete from question")
conn.commit()

questions.to_sql("question", conn, if_exists='append', index=False)

print(f"df len: {len(questions)}")
cur.execute("select count(*) from question")
n = cur.fetchone()
print(f"db len: {n}")

conn.commit()
conn.close()