import csv
from os import stat
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

URL_list = ["https://www.premierleague.com/players/3960/Harry-Kane/stats"]
for url in URL_list:
    driver.get(url)
    print(driver.title)

    try:
        main = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "statsListBlock"))
        )
        stats = main.text
        x = stats.split("\n")
        statList = list(x)
        header = statList.pop(0)
        statDict = {}
        while len(statList) > 1:
            s = statList.pop(0)
            statDict[s] = statList.pop(0)
        print(statDict)

    except:
        driver.quit()

    driver.quit
