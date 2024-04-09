import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

#
# Create Tables
#
cur.execute("drop table if exists tournamentPlayed")
cur.execute("create table if not exists tournamentPlayed(tournamentName not null, playerName not null, place not null, primary key (tournamentName, playerName), foreign key (tournamentName) references tournaments(udiscname), foreign key (playerName) references players(udiscname))")

#
# Populate Tables
#
# waco
cur.execute("insert into tournamentPlayed values ('waco2023', 'kristintattar', 1)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'ellahansen', 2)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'ohnscoggins', 3)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'sarahhokom', 4)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'haileyking', 5)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'annikensteen', 5)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'deanncarey', 5)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'kathrynmertsch', 8)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'paigeshu', 8)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'catrinaallen', 10)")

#
# Commit
#
con.commit()