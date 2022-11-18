import csv
from os import stat
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tabulate
def scoreTeam(playerURLList):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    URL_list = playerURLList
    playerList = []
    cookies = False
    for url in URL_list:
        driver.get(url)
        if not cookies:
            time.sleep(5)
            cookies = True
        statDict = {}
        position = ""
        name = ""
        number = ""
        score = 0
    # name t-colour
        try:
            main = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "playerDetails"))
            )
            stats = main.text
            x = stats.split("\n")
            number = x[0]
            name = x[1]
        except:
            driver.quit()
        try:
            main = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "fixedSidebar"))
            )

            stats = main.text
            x = stats.split("\n")
            statList = list(x)
            Ok = False
            for i in statList:
                if Ok == True:
                    position = i
                    break

                if i == "Position":
                    Ok = True
        except:
            driver.quit()

        try:
            # statsListBlock
            main = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "playerStats"))
            )
            stats = main.text
            x = stats.split("\n")
            statList = list(x)
            #header = statList.pop(0)

            while len(statList) > 1:
                NoN = False
                head = statList.pop(0)
                if statDict.__contains__(head):
                    statList.pop(0)
                    continue
                value = statList.pop(0)
                x = value.split(".")
                x = "".join(x)
                y = value.split(",")
                y = "".join(y)
                if y.isnumeric():
                    value = y
                k = value.split("%")
                k = "".join(k)
                if k.isnumeric():
                    value = k
                if not x.isnumeric() and not y.isnumeric() and not k.isnumeric():
                    statList.insert(0, value)
                    NoN = True
                if NoN is True:
                    continue
                statDict[head] = value

        except:
            driver.quit()

        if position == "Forward":
            score = float(statDict["Goals"])/float(statDict["Appearances"])
        elif position == "Defender":
            pass
        elif position == "Midfielder":
            pass
        elif position == "Goalkeeper":
            pass
        else:
            pass

        playerSum = {"Name": name, "Number": number,
                    "Position": position, "Score": score}

        playerList.append(playerSum)
        driver.quit

    # print(playerList)
    return playerList

