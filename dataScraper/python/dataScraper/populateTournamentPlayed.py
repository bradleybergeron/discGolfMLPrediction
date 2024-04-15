import sqlite3
from selenium import webdriver
from selenium.common import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

debug = True

con = sqlite3.connect("data.db")
cur = con.cursor()

#
# Create Tables
#
cur.execute("drop table if exists tournamentPlayed")
cur.execute("create table if not exists tournamentPlayed(tournamentID text not null, playerID text not null, division text not null, place integer not null, primary key (tournamentID, playerID), foreign key (tournamentID) references tournaments(id), foreign key (playerID) references players(id))")


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
driver = webdriver.Chrome()

#
# Get Tournament IDs
#
tournamentIDs = cur.execute("select id from tournaments").fetchall()

if debug:
    print(f"tournamentIDs: {tournamentIDs}")

for tournamentID in tournamentIDs:
    if debug:
        print(f"tournamentID: {tournamentID[0]}")

    driver.get(f"https://udisclive.com/live/{tournamentID[0]}")
    time.sleep(2)

    for div in ("MPO", "FPO"):
        #
        # Click {div} Link
        #
        driver.get(f"https://udisclive.com/live/{tournamentID[0]}/?d={div}")
        time.sleep(2)

        if driver.current_url != f"https://udisclive.com/live/{tournamentID[0]}/?d={div}":
            print(f"Could not find {div} division for tournament: {tournamentID[0]}")
            continue

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='main-content']/div/div[2]/div[3]/div"))
            )

            rows = driver.find_elements(By.XPATH, "//div[@id='main-content']/div/div[2]/div[3]/div")
            if debug:
                print(f"num players: {len(rows)}")

            for row in rows:
                try:
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//div/div"))
                    )

                    placement = row.find_element(By.XPATH, ".//div/div").text.split("\n", 1)[0].replace('T', '')
                    nameLink = row.find_element(By.XPATH, ".//div/div[2]/span[2]")
                    nameLink.click()
                    playerIDURL = row.find_element(By.XPATH, ".//div[2]/div/a").get_attribute("href")
                    questionMarkLocation = playerIDURL.index("?")
                    playerID = playerIDURL[30:questionMarkLocation:]

                    if debug:
                        print(f"placement: {placement}")
                        print(f"playerID: {playerID}")

                    # tournamentName text not null, playerName text not null, place integer not null
                    if tournamentID[0] == '' or playerID == '' or placement == '':
                        print("Incomplete data, unable to add to database")
                        print(f"tournamentID: {tournamentID[0]}, playerID: {playerID}, div: {div}, placement: {placement}")
                    else:
                        print("Inserting data into database...")
                        cur.execute(f"insert into tournamentPlayed values (?, ?, ?, ?)", (str(tournamentID[0]), str(playerID), str(div), str(placement)))
                except NoSuchElementException:
                    print(f"Likely processing an ad row")

        except TimeoutException:
            print(f"No data found for tournament: {tournamentID[0]}")

#
# Commit
#
con.commit()
