import sqlite3
from selenium import webdriver
from selenium.common import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
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
cur.execute("drop table if exists roundPlayed")
cur.execute("create table if not exists roundPlayed(tournamentID text not null, playerID text not null, roundNumber int not null, sgTotal real not null, sgTeeToGreen real not null, sgPutting real not null, sgCircle1X real not null, sgCircle2 real not null, sgPenalties real not null, primary key (tournamentID, playerID, roundNumber))")

#
# Populate Tables
#
#
# get known players from tournamentPlayed
#
tournamentPlayed = cur.execute("select tournamentID, playerID, division, t.rounds as rounds from tournamentPlayed as td, tournaments t where td.tournamentID = t.id").fetchall()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options)

time.sleep(2)

if debug:
    print(f"tournamentPlayed: {tournamentPlayed}")
    print(f"len(tournamentPlayed): {len(tournamentPlayed)}")

for player in tournamentPlayed:
    if debug:
        print(f"player: {player}")

    driver.get(f"https://udisclive.com/players/{player[1]}?t={player[0]}")
    time.sleep(2)

    for i in range(player[3]):
        sgTotal = driver.find_element(By.XPATH, f"//div[contains(string(), 'SG:Total')]/following-sibling::div[{i+1}]/div/div").text
        sgTeeToGreen = driver.find_element(By.XPATH, f"//div[contains(string(), 'SG:Tee→Green')]/following-sibling::div[{i+1}]/div/div").text
        sgPutting = driver.find_element(By.XPATH, f"//div[contains(string(), 'SG:Putting')]/following-sibling::div[{i+1}]/div/div").text
        sgC1X = driver.find_element(By.XPATH, f"//div[contains(string(), 'SG:C1X')]/following-sibling::div[{i+1}]/div/div").text
        sgC2 = driver.find_element(By.XPATH, f"//div[contains(string(), 'SG:C2')]/following-sibling::div[{i+1}]/div/div").text
        sgOB = driver.find_element(By.XPATH, f"//div[contains(string(), 'SL:OB')]/following-sibling::div[{i+1}]/div/div").text

        if debug:
            print(f"sgTotal: {sgTotal}")
            print(f"sgTeeToGreen: {sgTeeToGreen}")
            print(f"sgPutting: {sgPutting}")
            print(f"sgC1X: {sgC1X}")
            print(f"sgC2: {sgC2}")
            print(f"sgOB: {sgOB}")

        con.commit()