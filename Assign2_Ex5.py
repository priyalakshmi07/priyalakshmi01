import sqlite3

conn = sqlite3.connect('TestDB.db')
print('Connected to database successfully.')

cur = conn.cursor()
Movie1 = [
   ("Inception", "2010", "science fiction", "7",
   "Learnado Dicaprio", "Marion Cortillard")
]
Movie2 = [
   ("Spiderman", "2002", "science fiction", "0",
   "Toby Maguire", "Kriston Dunst")
]
Movie3 = [
   ("The Matrix", "1999", "science fiction", "4",
   "Keanu Reeves", "Carrie-Anne Moss")
]

cur.executemany("insert into MOVIES(Movie_name, Year_of_release, Genre, Awards_won, Lead_actor, Lead_actress) values(?, ?, ?, ?, ?, ?)", Movie1)
cur.executemany("insert into MOVIES(Movie_name, Year_of_release, Genre, Awards_won, Lead_actor, Lead_actress) values(?, ?, ?, ?, ?, ?)", Movie2)
cur.executemany("insert into MOVIES(Movie_name, Year_of_release, Genre, Awards_won, Lead_actor, Lead_actress) values(?, ?, ?, ?, ?, ?)", Movie3)
print('Records inserted successfully.')

conn.commit()
conn.close()
