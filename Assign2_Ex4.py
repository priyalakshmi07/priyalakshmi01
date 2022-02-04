import sqlite3
conn = sqlite3.connect('TestDB.db')
c = conn.cursor()
c.execute('''CREATE TABLE MOVIES
  ([id] INTEGER PRIMARY KEY,[Movie_name] text, [Year_of_release] date, [Genre] text, [Awards_won] text, [Lead_actor] text, [Lead_actress] text)''')
conn.commit()
