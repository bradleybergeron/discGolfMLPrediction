import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

#
# Create Tables
#
cur.execute("drop table if exists tournamentPlayed")
cur.execute("create table if not exists tournamentPlayed(tournamentName text not null, playerName text not null, place integer not null, primary key (tournamentName, playerName), foreign key (tournamentName) references tournaments(udiscname), foreign key (playerName) references players(udiscname))")

#
# Populate Tables
#
# waco2023
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
cur.execute("insert into tournamentPlayed values ('waco2023', 'macievelediaz', 11)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'lisafajkus', 11)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'alexismandujano', 13)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'julianakorver', 14)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'hennablomroos', 14)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'hollyfinley', 16)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'ariacastruita', 16)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'jessicaweese', 16)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'paigepierce', 16)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'missygannon', 16)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'holynhandley', 21)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'rebeccacox', 21)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'mariaoliva', 21)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'erikastinchcomb', 21)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'alismith', 25)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'saiananda', 25)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'madisonwalker', 27)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'cynthiaricciotti', 27)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'carolinehenderson', 29)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'caseypennington', 30)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'lykkelorentzen', 31)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'hannahuynh', 32)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'lydiacochran', 32)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'stephanievincent', 32)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'stacierawnsley', 35)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'staciekiefer', 35)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'ravenklein', 35)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'vanessavandyken', 35)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'leahtsinajinnie', 39)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'eveliinasalonen', 40)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'keititatte', 40)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'jillnorwick', 42)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'emilybeach', 42)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'shiruliu', 44)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'danikleidon', 45)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'kelleyfoster', 46)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'krissiefountain', 46)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'alexiskerman', 48)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'ratanameekham', 49)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'melodycastruita', 50)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'madisontomaino', 51)")
cur.execute("insert into tournamentPlayed values ('waco2023', 'nathalieortiz', 52)")

#
# Commit
#
con.commit()