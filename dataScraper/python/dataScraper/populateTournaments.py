import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

#
# Create Tables
#
cur.execute("drop table if exists tournaments")
cur.execute("create table if NOT EXISTS tournaments(id not null, udiscName primary key not null, name not null, location not null, date not null, year not null, rounds not null)")

#
# Populate Tables
#
###
cur.execute("insert into tournaments values (1, 'waco2023', 'Prodigy Presents WACO', 'Waco, TX', 'Mar 10-12', 2023, 3)")
cur.execute("insert into tournaments values (2, 'austin2023', 'The Open at Austin', 'Austin, TX', 'Mar 17-19', 2023, 3)")
cur.execute("insert into tournaments values (3, 'txstates2023', 'Innova Open at the 28th Annual Texas Sates', 'Houstan, TX', 'Mar 24-26', 2023, 3)")
cur.execute("insert into tournaments values (4, 'musiccity2023', 'Music City Open', 'Nashville, TN', 'Apr 7-9', 2023, 3)")
cur.execute("insert into tournaments values (5, 'blueridge2023', 'Innova Blue Ridge Championship at North Cove', 'Marion, NC', 'Apr 14-16', 2023, 3)")

#
# Commit Changes
#
con.commit()