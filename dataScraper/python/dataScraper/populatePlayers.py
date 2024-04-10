import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

#
# Create Tables
#
cur.execute("drop table if exists players")
cur.execute("create table if NOT EXISTS players(id integer not null, udiscName text primary key not null, name text not null, division text not null, pdgaNumber integer not null)")


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
cur.execute("insert into players values (11, 'annikenkristiansensteen', 'Anniken K. Steen', 'FPO', 109996)")
cur.execute("insert into players values (12, 'deanndonaldson', '', 'FPO', 66842)")
cur.execute("insert into players values (13, 'paigebjerkaas', 'Paige Shue', 'FPO', 33833)")
cur.execute("insert into players values (14, 'lisafajkus', 'Lisa Fajkus', 'FPO', 32654)")
cur.execute("insert into players values (15, 'alexismandujano', 'Alexis Mandujano', 'FPO', 62880)")
cur.execute("insert into players values (16, 'julianakorver', 'Juliana Korver', 'FPO', 7438)")
cur.execute("insert into players values (17, 'hennablomroos', 'Henna Blomroos', 'FPO', 59227)")
cur.execute("insert into players values (18, 'hollyfinley', 'Holly Finley', 'FPO', 51277)")
cur.execute("insert into players values (19, 'ariacastruita', 'Aria Castruita', 'FPO', 105126)")
cur.execute("insert into players values (20, 'jessicaweese', 'Jessica Weese', 'FPO', 50656)")
cur.execute("insert into players values (21, 'paigepierce', 'Paige Pierce', 'FPO', 29190)")
cur.execute("insert into players values (22, 'rebeccacox', 'Rebecca Cox', 'FPO', 32917)")
cur.execute("insert into players values (23, 'mariaoliva', 'Maria Oliva', 'FPO', 63257)")
cur.execute("insert into players values (24, 'erikastinchcomb', 'Erika Stinchcomb', 'FPO', 71262)")
cur.execute("insert into players values (25, 'alismith', 'Ali Smith', 'FPO', 147050)")
cur.execute("insert into players values (26, 'saiananda', 'Sai Ananda', 'FPO', 58303)")
cur.execute("insert into players values (27, 'madisonwalker', 'Madison Walker', 'FPO', 59431)")
cur.execute("insert into players values (28, 'cynthiaricciotti', 'Cynthia Ricciotti', 'FPO', 75029)")
cur.execute("insert into players values (29, 'carolinehenderson', 'Caroline Henderson', 'FPO', 171555)")
cur.execute("insert into players values (30, 'caseypennington', 'Casey Pennington', 'FPO', 74708)")
cur.execute("insert into players values (31, 'lykkesandvik', 'Lykke Lorentzen', 'FPO', 99441)")
cur.execute("insert into players values (32, 'hannahuynh', 'Hanna Huynh', 'FPO', 112647)")
cur.execute("insert into players values (33, 'lydialyons', 'Lydia Cochran', 'FPO', 58968)")
cur.execute("insert into players values (34, 'stephanievincent', 'Stephanie Vincent', 'FPO', 29947)")
cur.execute("insert into players values (35, 'stacierawnsley', 'Stacie Rawnsley', 'FPO', 122208)")
cur.execute("insert into players values (36, 'staciekiefer', 'Stacie Kiefer', 'FPO', 124963)")
cur.execute("insert into players values (37, 'ravenklein', 'Raven Klein', 'FPO', 138272)")
cur.execute("insert into players values (38, 'vanessavandyken', 'Vanessa Van Dyken', 'FPO', 62325)")
cur.execute("insert into players values (39, 'leahtsinajinnie', 'Leah Tsinajinnie', 'FPO', 139109)")
cur.execute("insert into players values (40, 'eveliinasalonen', 'Eveliina Salonen', 'FPO', 64927)")
cur.execute("insert into players values (41, 'keititätte', 'Keiti Tatte', 'FPO', 94085)")
cur.execute("insert into players values (42, 'jillnorwick', 'Jill Norwick', 'FPO', 142944)")
cur.execute("insert into players values (43, 'emilybeach', 'Emily Beach', 'FPO', 61144)")
cur.execute("insert into players values (44, 'shiruliu', 'Shiru Liu', 'FPO', 158461)")
cur.execute("insert into players values (45, 'danikleidon', 'Dani Kleidon', 'FPO', 146137)")
cur.execute("insert into players values (46, 'kelleyfoster', 'Kelley Foster', 'FPO', 152191)")
cur.execute("insert into players values (47, 'krissiefountain', 'Krissie Fountain', 'FPO', 73693)")
cur.execute("insert into players values (48, 'alexiskerman', 'Alexis Kerman', 'FPO', 142354)")
cur.execute("insert into players values (49, 'ratanameekham', 'Ratana Meekham', 'FPO', 101949)")
cur.execute("insert into players values (50, 'melodycastruita', 'Melody Castruita', 'FPO',50171 )")
cur.execute("insert into players values (51, 'madisontomaino', 'Madison Tomaino', 'FPO', 60798)")
cur.execute("insert into players values (52, 'nathaliestrom', 'Nathalie Ortiz', 'FPO', 133701)")

#austin2023
cur.execute("insert into players values (53, 'cadenceburge', 'Cadence Burge', 'FPO', 76233)")
cur.execute("insert into players values (54, 'emilyyale', 'Emily Yale', 'FPO', 144791)")
cur.execute("insert into players values (55, 'carleakubicek', 'Carlea Kubicek', 'FPO', 186636)")
#cur.execute("insert into players values (56, 'carolina""reaper""halstead', 'Carolina 'Reaper' Halstead', 'FPO', 113817)")
cur.execute("insert into players values (54, 'rebeccaminnick', 'Rebecca Minnick', 'FPO', 170182)")
cur.execute("insert into players values (54, 'jessicahopper', 'Jessica Hopper', 'FPO', 197708)")
cur.execute("insert into players values (54, 'kimberlyhlava', 'Kimberly Hlava', 'FPO', 180525)")

#
# Commit Changes
#
con.commit()