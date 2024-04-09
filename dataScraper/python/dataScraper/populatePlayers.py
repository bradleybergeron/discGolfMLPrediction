import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

#
# Create Tables
#
cur.execute("drop table if exists players")
cur.execute("create table if NOT EXISTS players(id not null, udiscName primary key not null, name not null, division not null, pdgaNumber not null)")


#
# Populate Tables
#
###
cur.execute("insert into players values (1, 'kristintattar', 'Kristin Tattar', 'FPO', 73986)")
cur.execute("insert into players values (2, 'ohnscoggins', 'Ohn Scoggins', 'FPO', 48976)")
cur.execute("insert into players values (3, 'missygannon', 'Missy Gannon', 'FPO', 85942)")
cur.execute("insert into players values (4, 'holynhandley', 'Holyn Handley', 'FPO', 133547)")
cur.execute("insert into players values (5, 'ellahansen', 'Ella Hansen', 'FPO', 144112)")
cur.execute("insert into players values (6, 'kathrynmertsch', 'Kat Mertsch', 'FPO', 99455)")
cur.execute("insert into players values (7, 'haileyking', 'Hailey King', 'FPO', 81351)")
cur.execute("insert into players values (8, 'catrinaallen', 'Catrina Allen', 'FPO', 44184)")
cur.execute("insert into players values (9, 'sarahhokom', 'Sarah Hokom', 'FPO', 34563)")
cur.execute("insert into players values (10, 'macievelediaz', 'Macie Velediaz', 'FPO', 104187)")

#
# Commit Changes
#
con.commit()