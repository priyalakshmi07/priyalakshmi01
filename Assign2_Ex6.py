import sqlite3
import json

db_demo='TestDB.DB'
conn=sqlite3.connect(db_demo)
c=conn.cursor()

sql_query='SELECT Movie_name,Year_of_release,Awards_won FROM MOVIES'
c.execute(sql_query)
rows=(c.fetchall())

rowarray_list = []
for row in rows:
    t = (row[0], row[1], row[2])
    rowarray_list.append(t)

    j = json.dumps(rowarray_list)

with open("Moviesdata.json", "w") as f:
    f.write(j)

conn.close()
