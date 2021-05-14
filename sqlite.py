import sqlite3

conn = sqlite3.connect('rap.db')

c = conn.cursor()

# STEP 1
# c.execute("""CREATE TABLE raps (
#     artist text,
#     album text,
#     lyrics text
#     )""")

conn.commit()

conn.close()