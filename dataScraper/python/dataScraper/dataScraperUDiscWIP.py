import pandas as pd
import requests
from pandas._typing import TimeUnit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

pd.set_option('display.max_columns', None)
import time
import numpy as np
import re

playerNames = [
    "kristintattar",
    "ohnscoggins",
    "missygannon",
    "holynhandley",
    "ellahansen",
    "kathrynmertsch",
    "haileyking",
    "catrinaallen",
    "sarahhokom",
    "macievelediaz",
    "jessicaweese",
    "alismith",
    "mariaoliva",
#    "jenniferallen",
    "stacierawnsley",
    "hollyfinley",
    "lisafajkus",
    "lykkelorentzen",
    "julianakorver",
    "hennablomroos",
    "deanncarey",
    "saiananda",
    "emilybeach",
    "hannahuynh",
    "eveliinasalonen",
    "vanessavankyken",
#    "heidilaine",
    "alexismandujano",
    "rebeccacox",
#    "valeriemandujano",
    "madisonwalker",
    "annikensteen",
    "paigepierce",
    "cynthiaricciotti",
    "erikastinchcomb",
    "keititatte",
    "staciekiefer",
    "paigeshu",
#    "silvasaarinen",
    "ravenklein",
#    "natalieryan",
    "danikleidon",
    "ariacastruita",
    "rachelturton",
#    "sarahgilpin",
#    "stephanievincent",
##    "leahtsinajinnie",
##    "carolinehenderson",
##    "chantelbudinsky",
##    "ellenwidboom"
]
tournament = "waco2023"
#pdgaPlayerURL = "https://api.pdga.com/services/json/players?pdga_number=93029"
pdgaPlayerURL = "https://www.dgpt.com/player/?player_id=73986&season=2024&division=FPO"
statMandoURL = "https://statmando.com/stats/stats-elite-series-majors-2023-fpo"
uDiscLiveURL = f"https://udisclive.com/players/{playerNames[0]}?t={tournament}"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}

#
# Preload page because it's slow
#
driver = webdriver.Chrome()
#driver.get(uDiscLiveURL)
#time.sleep(2)

for playerName in playerNames:
    print(playerName)

    uDiscLiveURL = f"https://udisclive.com/players/{playerName}?t={tournament}"
    driver.get(uDiscLiveURL)

    elem = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "react-root"))
    )
    time.sleep(2)

    if driver.current_url == uDiscLiveURL:
        #print(elem.text)

        sgTotalText = "STROKES GAINED - TOTAL"
        sgTeeToGreenText = "STROKES GAINED - TEE TO GREEN"
        sgPuttingText = "STROKES GAINED - PUTTING"
        sgC1XText = "STROKES GAINED - CIRCLE 1X"
        sgC2Text = "STROKES GAINED - CIRCLE 2"
        sGLostPenalties = "STROKES LOST - PENALTIES"

        # 3 rounds
        #sgTotal = re.search("STROKES GAINED - TOTAL\n(.*)\n(.*)\n(.*)\n", elem.text)
        # 4 rounds
        sgTotal = re.search("STROKES GAINED - TOTAL\n(.*)\n(.*)\n(.*)\n(.*)\n", elem.text).group().split("\n")
        sgTeeToGreen = re.search("STROKES GAINED - TEE TO GREEN\n(.*)\n(.*)\n(.*)\n(.*)\n", elem.text).group().split("\n")
        sgPutting = re.search("STROKES GAINED - PUTTING\n(.*)\n(.*)\n(.*)\n(.*)\n", elem.text).group().split("\n")
        sgC1X = re.search("STROKES GAINED - CIRCLE 1X\n(.*)\n(.*)\n(.*)\n(.*)\n", elem.text).group().split("\n")
        sgC2 = re.search("STROKES GAINED - CIRCLE 2\n(.*)\n(.*)\n(.*)\n(.*)\n", elem.text).group().split("\n")
        sgPenalties = re.search("STROKES LOST - PENALTIES\n(.*)\n(.*)\n(.*)\n(.*)\n", elem.text).group().split("\n")

        print(sgTotal)
        print(sgTeeToGreen)
        print(sgPutting)
        print(sgC1X)
        print(sgC2)
        print(sgPenalties)
    else:
        print(f"Player ({playerName}) not found in tournament ({tournament})")

#finally:
driver.quit()