import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

#
# Create Tables
#
cur.execute("drop table if exists roundPlayed")
cur.execute("create table if not exists roundPlayed(tournamentName, playerName, roundNumber, sgTotal, sgTeeToGreen, sgPutting, sgCircle1X, sgCircle2, sgPenalties, primary key (tournamentName, playerName, roundNumber))")

#
# Populate Tables
#
#
# Run dataScraperUDiscWIP.py
#

con.commit()