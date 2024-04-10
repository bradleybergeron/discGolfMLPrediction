import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

#
# Create Tables
#
cur.execute("drop table if exists roundPlayed")
cur.execute("create table if not exists roundPlayed(tournamentName text, playerName text, roundNumber int, sgTotal real, sgTeeToGreen real, sgPutting real, sgCircle1X real, sgCircle2 real, sgPenalties real, primary key (tournamentName, playerName, roundNumber))")

#
# Populate Tables
#
#
# Run dataScraperUDiscWIP.py
#

con.commit()