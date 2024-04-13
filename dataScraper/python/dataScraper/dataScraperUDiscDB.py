import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3
import time
import re


con = sqlite3.connect("data.db")
#con.row_factory = lambda cursor, row: row[0]
cur = con.cursor()

pd.set_option('display.max_columns', None)

playerNames = cur.execute("select udiscname from players").fetchall()
tournaments = cur.execute("select udiscname, rounds from tournaments").fetchall()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}

driver = webdriver.Chrome()

print(len(playerNames))
print(len(tournaments))
namesToReview = set()

for playerName in playerNames:
    print(playerName[0])
    for tournament in tournaments:
        print(tournament)

        uDiscLiveURL = f"https://udisclive.com/players/{playerName[0]}?t={tournament[0]}"
        print(uDiscLiveURL)

        driver.get(uDiscLiveURL)

        elem = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "react-root"))
        )
        time.sleep(2)

        try:
            # 1 is rounds in tournaments table
            if tournament[1] == 3:
                # 3 rounds
                sgTotal = re.search("STROKES GAINED - TOTAL\n(.*)\n(.*)\n(.*)\n", elem.text).group().split("\n")
                sgTeeToGreen = re.search("STROKES GAINED - TEE TO GREEN\n(.*)\n(.*)\n(.*)\n", elem.text).group().split("\n")
                sgPutting = re.search("STROKES GAINED - PUTTING\n(.*)\n(.*)\n(.*)\n", elem.text).group().split("\n")
                sgC1X = re.search("STROKES GAINED - CIRCLE 1X\n(.*)\n(.*)\n(.*)\n", elem.text).group().split("\n")
                sgC2 = re.search("STROKES GAINED - CIRCLE 2\n(.*)\n(.*)\n(.*)\n", elem.text).group().split("\n")
                sgPenalties = re.search("STROKES LOST - PENALTIES\n(.*)\n(.*)\n(.*)\n", elem.text).group().split("\n")

                print(sgTotal)
                print(sgTeeToGreen)
                print(sgPutting)
                print(sgC1X)
                print(sgC2)
                print(sgPenalties)

                sgTotal1 = 0 if sgTotal[1] == '-' else float(sgTotal[1])
                sgTotal2 = 0 if sgTotal[2] == '-' else float(sgTotal[2])
                sgTotal3 = 0 if sgTotal[3] == '-' else float(sgTotal[3])
                sgTeeToGreen1 = 0 if sgTeeToGreen[1] == '-' else float(sgTeeToGreen[1])
                sgTeeToGreen2 = 0 if sgTeeToGreen[2] == '-' else float(sgTeeToGreen[2])
                sgTeeToGreen3 = 0 if sgTeeToGreen[3] == '-' else float(sgTeeToGreen[3])
                sgPutting1 = 0 if sgPutting[1] == '-' else float(sgPutting[1])
                sgPutting2 = 0 if sgPutting[2] == '-' else float(sgPutting[2])
                sgPutting3 = 0 if sgPutting[3] == '-' else float(sgPutting[3])
                sgC1X1 = 0 if sgC1X[1] == '-' else float(sgC1X[1])
                sgC1X2 = 0 if sgC1X[2] == '-' else float(sgC1X[2])
                sgC1X3 = 0 if sgC1X[3] == '-' else float(sgC1X[3])
                sgC21 = 0 if sgC2[1] == '-' else float(sgC2[1])
                sgC22 = 0 if sgC2[2] == '-' else float(sgC2[2])
                sgC23 = 0 if sgC2[3] == '-' else float(sgC2[3])
                sgPenalties1 = 0 if sgPenalties[1] == '-' else float(sgPenalties[1])
                sgPenalties2 = 0 if sgPenalties[2] == '-' else float(sgPenalties[2])
                sgPenalties3 = 0 if sgPenalties[3] == '-' else float(sgPenalties[3])

                #tournamentName, playerName, roundNumber, sgTotal, sgTeeToGreen, sgPutting, sgCircle1X, sgCircle2, sgPenalties
                cur.execute("delete from roundPlayed")
                cur.execute(f"insert into roundPlayed values ('{tournament[0]}', '{playerName[0]}', 1, {sgTotal1}, {sgTeeToGreen1}, {sgPutting1}, {sgC1X1}, {sgC21}, {sgPenalties1})")
                cur.execute(f"insert into roundPlayed values ('{tournament[0]}', '{playerName[0]}', 2, {sgTotal2}, {sgTeeToGreen2}, {sgPutting2}, {sgC1X2}, {sgC22}, {sgPenalties2})")
                cur.execute(f"insert into roundPlayed values ('{tournament[0]}', '{playerName[0]}', 3, {sgTotal3}, {sgTeeToGreen3}, {sgPutting3}, {sgC1X3}, {sgC23}, {sgPenalties3})")

                con.commit()

                print(f"Player ({playerName[0]}) status saved for tournament ({tournament[0]})")
            elif int(tournaments[1]) == 4:
                # 4 rounds
                sgTotal = re.search("STROKES GAINED - TOTAL\n(.*)\n(.*)\n(.*)\n(.*)\n", elem.text).group().split("\n")
                sgTeeToGreen = re.search("STROKES GAINED - TEE TO GREEN\n(.*)\n(.*)\n(.*)\n(.*)\n", elem.text).group().split("\n")
                sgPutting = re.search("STROKES GAINED - PUTTING\n(.*)\n(.*)\n(.*)\n(.*)\n", elem.text).group().split("\n")
                sgC1X = re.search("STROKES GAINED - CIRCLE 1X\n(.*)\n(.*)\n(.*)\n(.*)\n", elem.text).group().split("\n")
                sgC2 = re.search("STROKES GAINED - CIRCLE 2\n(.*)\n(.*)\n(.*)\n(.*)\n", elem.text).group().split("\n")
                sgPenalties = re.search("STROKES LOST - PENALTIES\n(.*)\n(.*)\n(.*)\n(.*)\n", elem.text).group().split("\n")

                #tournamentName, playerName, roundNumber, sgTotal, sgTeeToGreen, sgPutting, sgCircle1X, sgCircle2, sgPenalties
                cur.execute(f"insert into roundPlayed values ('{tournament[0]}', '{playerName[0]}', 1, {sgTotal[1]}, {sgTeeToGreen[1]}, {sgPutting[1]}, {sgC1X[1]}, {sgC2[1]}, {sgPenalties[1]})")
                cur.execute(f"insert into roundPlayed values ('{tournament[0]}', '{playerName[0]}', 2, {sgTotal[2]}, {sgTeeToGreen[2]}, {sgPutting[2]}, {sgC1X[2]}, {sgC2[2]}, {sgPenalties[2]})")
                cur.execute(f"insert into roundPlayed values ('{tournament[0]}', '{playerName[0]}', 3, {sgTotal[3]}, {sgTeeToGreen[3]}, {sgPutting[3]}, {sgC1X[3]}, {sgC2[3]}, {sgPenalties[3]})")
                cur.execute(f"insert into roundPlayed values ('{tournament[0]}', '{playerName[0]}', 4, {sgTotal[4]}, {sgTeeToGreen[4]}, {sgPutting[4]}, {sgC1X[4]}, {sgC2[4]}, {sgPenalties[4]})")
                con.commit()
                print(f"Player ({playerName[0]}) status saved for tournament ({tournament[0]})")
            else:
                print(f"Tournament ({tournament[0]}) has an unprocessed number of rounds")
        except AttributeError:
            print(f"Player ({playerName[0]}) did not participate at this tournament ({tournament[0]})")
            namesToReview.add((playerName[0], tournament[0]))
        finally:
            print("finally...")
        #except:
        #    print(f"Player ({playerName}) not found in tournament ({tournament})")

driver.quit()

for x in namesToReview:
    print(x)
