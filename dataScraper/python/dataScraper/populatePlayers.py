import sqlite3
from selenium import webdriver
from selenium.common import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

debug = False

con = sqlite3.connect("data.db")
cur = con.cursor()

#
# Create Tables
#
cur.execute("drop table if exists players")
cur.execute("create table if NOT EXISTS players(id text not null primary key, name text not null, division text not null, pdgaNumber integer not null)")

#
# get known players from tournamentPlayed
#
players = cur.execute("select distinct playerID, division from tournamentPlayed").fetchall()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
driver = webdriver.Chrome()
time.sleep(2)

if debug:
    print(f"playerIDs: {players}")
    print(f"len(playerIDs): {len(players)}")

for player in players:
    if debug:
        print(f"playerID: {player}")

    driver.get(f"https://udisclive.com/players/{player[0]}")
    time.sleep(2)

    playerName = driver.find_element(By.XPATH, "//h1").text
    playerPDGANumber = driver.find_element(By.XPATH, "//div[contains(string(), 'PDGA#: ')]/span/a").text
    playerDivision = player[1]

    if debug:
        print(f"Player ID: {player[0]}. Player Name: {playerName}, PDGA Number: {playerPDGANumber}, Division: {playerDivision}")

    cur.execute("insert into players values (?, ?, ?, ?)", (str(player[0]), str(playerName), str(playerDivision), str(playerPDGANumber)))

#
# Commit Changes
#
con.commit()