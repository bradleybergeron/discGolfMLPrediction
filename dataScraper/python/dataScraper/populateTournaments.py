import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

#
# Create Tables
#
cur.execute("drop table if exists tournaments")
cur.execute("create table if NOT EXISTS tournaments(id integer not null, udiscName primary key not null, name text not null, location text not null, date text not null, year integer not null, rounds integer not null)")

#
# Populate Tables
#
###
#cur.execute("insert into tournaments values (1, 'lmo2022', 'Lake Marshall Open', 'Lake Marshall, VA', 'Oct 28-30', 2022, 3)")
#cur.execute("insert into tournaments values (1, 'nwc2022', 'New World Championship', 'Jacksonville, FL', 'Nov 11-13', 2022, 3)")
#cur.execute("insert into tournaments values (1, 'allstars2023', 'DGPT All-Stars', 'Tucson, Az', 'Feb 17-19', 2023, 3)")
#cur.execute("insert into tournaments values (1, 'lvc2023', 'Las Vegas Challenge Presented by Innova', 'Henderson, NV', 'Feb 23-26', 2023, 4)")
cur.execute("insert into tournaments values (2, 'waco2023', 'Prodigy Presents WACO', 'Waco, TX', 'Mar 10-12', 2023, 3)")
cur.execute("insert into tournaments values (3, 'austin2023', 'The Open at Austin', 'Austin, TX', 'Mar 17-19', 2023, 3)")
#cur.execute("insert into tournaments values (4, 'txstates2023', 'Innova Open at the 28th Annual Texas Sates', 'Houstan, TX', 'Mar 24-26', 2023, 3)")
#cur.execute("insert into tournaments values (5, 'musiccity2023', 'Music City Open', 'Nashville, TN', 'Apr 7-9', 2023, 3)")
#cur.execute("insert into tournaments values (6, 'blueridge2023', 'Innova Blue Ridge Championship at North Cove', 'Marion, NC', 'Apr 14-16', 2023, 3)")
#cur.execute("insert into tournaments values (7, 'championscup2023', 'PDGA Champions Cup', 'Appling, GA', 'Apr 20-23', 2023, 4)")
#cur.execute("insert into tournaments values (8, 'jonesboro2023', 'Play It Again Sports Jonesboro Open', 'Jonesboro, AR', 'Apr 20-30', 2023, 3)")
#cur.execute("insert into tournaments values (9, 'copenhagen2023', 'Copenhagen Open', 'Copenhagen, Denmark', 'May 5-7', 2023, 3)")
#cur.execute("insert into tournaments values (10, 'otbopen2023', 'OTB Open', 'Stockton, CA', 'May 12-14', 2023, 3)")
#cur.execute("insert into tournaments values (11, 'beaverstate2023', 'Beaver State Fling', 'Estacada, OR', 'May 19-21', 2023, 3)")
#cur.execute("insert into tournaments values (12, 'belgian2023', 'Belgian Open', 'Braine-I'Alleud, Belgium', 'May 19-21', 2023, 3)")
#cur.execute("insert into tournaments values (13, 'cascade2023', 'Discrafts Cascade Challenge', 'Washington State', 'May 26-28', 2023, 3)")
#cur.execute("insert into tournaments values (14, 'helsinki2023', 'Helsinki', 'Helsinki, Finland', 'May 26-28', 2023, 3)")
#cur.execute("insert into tournaments values (15, 'portlandopen2023', 'Portland Open', 'Portland, OR', 'Jun 1-4', 2023, 4)")
#cur.execute("insert into tournaments values (16, 'estonia2023', 'Estonian Open', 'Korvemaa, Estonia', 'June 2-4', 2023, 3)")
#cur.execute("insert into tournaments values (17, 'proforester2023', 'Pro Forester', 'Varazdin, Croatia', 'Jun 9-11', 2023, 3)")
#cur.execute("insert into tournaments values (18, 'zootown2023', 'Zoo Town Open', 'Missoula, MT', 'June 9-11', 2023, 3)")
#cur.execute("insert into tournaments values (19, 'nokia2023', 'Nokia Open', 'Nokia, Finland', 'Jun 9-11', 2023, 3)")
#cur.execute("insert into tournaments values (20, 'norwegianchamps2023', 'Norwegian Disc Golf Championships', 'Selbu, Norway', 'Jun 16-19', 2023, 4)")
#cur.execute("insert into tournaments values (21, 'konopiste2023', 'Konopiste Open', 'Benesov, Czech Republic', 'Jun 16-18', 2023, 3)")
#cur.execute("insert into tournaments values (22, 'ddo2023', 'Dynamic Discs Open', 'Emporia, KS', 'June 16-18', 2023, 3)")
#cur.execute("insert into tournaments values (23, 'oulu2023', 'Oulu', 'Oulu, Finland', 'JUn 16-18', 2023, 3)")
#cur.execute("insert into tournaments values (24, 'krokhol2023', 'Krokhol Open', 'Krokhol, Norway', 'Jun 23-25', 2023, 3)")
#cur.execute("insert into tournaments values (25, 'dmc2023', 'TruBank Des Moines Challenge', 'Des Moines, IA', 'Jun 23-25', 2023, 3)")
#cur.execute("insert into tournaments values (26, 'sweden2023', 'Swedish Open', 'Boras, Sweden', 'Jun 30-Jul 2', 2023, 3)")
#cur.execute("insert into tournaments values (27, 'preserve2023', 'The Preserve Championship', 'Clearwater, MN', 'Jun30-Jul 2', 2023, 3)")
#cur.execute("insert into tournaments values (28, 'tyyni2023', 'Tyyni Open', 'Sipoo, Finland', 'Jun 30-Jul 2', 2023, 3)")
#cur.execute("insert into tournaments values (29, 'skelleftea2023', 'Skelleftea Open', 'Skelleftea, Sweden', 'Jul 7-9', 2023, 3)")
#cur.execute("insert into tournaments values (30, 'kcwo2023', 'GRIPeq KC Wide Open', 'Kansas City, MO', 'Jul 7-9', 2023, 3)")
#cur.execute("insert into tournaments values (31, 'pcsopen2023', 'PCS Open 2023', 'Overas, Norway', 'Jul 13-15', 2023, 3)")
#cur.execute("insert into tournaments values (32, 'turku2023', 'Turku Open', 'Turku, Finland', 'Jul 13-15', 2023, 3)")
#cur.execute("insert into tournaments values (33, 'presidentscup2023', 'Presidents Cup', 'Nokia, Finland', 'Jul 19', 2023, 1)")
#cur.execute("insert into tournaments values (34, 'europeanopen2023', 'European Open', 'Nokia, Finland', 'Jul 20-23', 2023, 4)")
#cur.execute("insert into tournaments values (35, 'aland2023', 'Aland Open', 'Jomala, Finland', 'Jul 27-29', 2023, 3)")
#cur.execute("insert into tournaments values (36, 'midamerica2023', 'Mid America Open', 'Columbia, MO', 'Jul 28-30', 2023, 3)")
#cur.execute("insert into tournaments values (37, 'jarva2023', 'Jarva Open', 'Stockholm, Sweden', 'Jul 28-30', 2023, 3)")
#cur.execute("insert into tournaments values (38, 'finnishchamps2023', 'Finnish Nationals', 'Lahti, Finland', 'Aug 3-6', 2023, 4)")
#cur.execute("insert into tournaments values (39, 'ledgestone2023', 'Discraft Ledgestone Open', 'Peoria, IL', 'Aug 3-6', 2023, 4)")
#cur.execute("insert into tournaments values (40, 'canadianchamps2023', 'Canadian Championships', 'Thunder Bay, Ontario, Canada', 'Aug 5-7', 2023, 3)")
#cur.execute("insert into tournaments values (41, 'alutaguse2023', 'Alutaguse Open', 'Johvi, Estonia', 'Aug 10-12', 2023, 3)")
#cur.execute("insert into tournaments values (42, 'idlewild2023', 'LWS Open at Idlewild', 'Burlington, KY', 'Aug 11-13', 2023, 3)")
#cur.execute("insert into tournaments values (43, 'junioredgc2023', 'Jr European DGC', 'Tallinn, Estonia', 'Aug 16-19', 2023, 4)")
#cur.execute("insert into tournaments values (44, 'edgc2023', 'European DGC 2023', 'Tallinn, Estonia', 'Aug 16-19', 2023, 4)")
#cur.execute("insert into tournaments values (45, 'greatlakes2023', 'Discraft Great Lakes Open', 'Milford, MI', 'Aug 17-20', 2023, 4)")
#cur.execute("insert into tournaments values (46, 'sieravuori2023', 'Sieravuori Challenge', 'Eura, Finland', 'Aug 25-27', 2023, 3)")
#cur.execute("insert into tournaments values (47, 'rochester2023', 'Jim Palmeris 50th AFDO', 'Rochester, NY', 'Aug 25-27', 2023, 3)")
#cur.execute("insert into tournaments values (48, 'kuopio2023', 'Kuopio', 'Kuopio, Finland', 'Aug 25-27', 2023, 3)")
#cur.execute("insert into tournaments values (49, 'proworlds2023', 'PDGA Pro World Championships', 'Jeffersonville, VT', 'Aug 30-Sept 3', 2023, 4)")
#cur.execute("insert into tournaments values (50, 'southestonia2023', 'South Estonia Open', 'Annikoru, Estonia', 'Sep 8-10', 2023, 3)")  # Cancelled
#cur.execute("insert into tournaments values (51, 'discmania2023', 'Discmania Open', 'PEI, Canada', 'Sept 8-10', 2023, 3)")
#cur.execute("insert into tournaments values (52, 'heinola2023', 'Heinola', 'Neinola, Finland', 'Sep 8-10', 2023, 3)")
#cur.execute("insert into tournaments values (53, 'mvpopen2023', 'MVP Open', 'Leicester, MA', 'Sep 14-17', 2023, 4)")
#cur.execute("insert into tournaments values (54, '9hill2023', '9Hill Open', 'Talsi, Latvia', 'Sep 15-17', 2023, 3)")
#cur.execute("insert into tournaments values (55, 'tampere2023', 'Tampere', 'Tampere, Finland', 'Sep 15-17', 2023, 3)")
#cur.execute("insert into tournaments values (56, 'uswdgc2023', 'USWDGC', 'Burlington, NC', 'Sep 21-24', 2023, 4)")
#cur.execute("insert into tournaments values (57, 'usdgc2023', 'USDGC', 'Rock Hill, SC', 'Oct 5-8', 2023, 4)")
#cur.execute("insert into tournaments values (58, 'tpwdgc2023', 'TPWDGC', 'Rock Hill, SC', 'Oct 5-8', 2023, 4)")
#cur.execute("insert into tournaments values (59, 'dgptchampionship2023-sf', 'DGPT Champoinship Semifinals', 'Charlotte, NC', 'Oct 12-13', 2023, 2)")
#cur.execute("insert into tournaments values (60, 'dgptchampionship2023', 'DGPT Championship', 'Charlotte, NC', 'Oct 14-15', 2023, 2)")
#cur.execute("insert into tournaments values (61, 'andalucia2023', 'Andalucia Open', 'Chipiona, Spain', 'Oct 20-22', 2023, 3)")
#cur.execute("insert into tournaments values (61, 'eptallstars2023', 'EPT All-Stars', 'Mijas, Spain', 'Oct 27-29', 2023, 3)")



#
# Commit Changes
#
con.commit()