import sqlite3
conn = sqlite3.connect("users.db")
c = conn.cursor()

# for row in c.execute('SELECT * FROM stocks ORDER BY price'):
#   print(row)

c.execute('SELECT name FROM sqlite_master WHERE type =\'table\' AND name NOT LIKE \'sqlite_%\';')

c.execute("SELECT * FROM stocks")

print(c.fetchall())