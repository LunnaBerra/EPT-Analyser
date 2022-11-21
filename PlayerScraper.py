from os import stat
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


def scoreTeam(playerURLList, allTime: bool):
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
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "playerDetails"))
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
            if allTime == False:
                time.sleep(1)
                WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='dropDown mobile'][1]"))).click()
                time.sleep(0.5)
                driver.find_element(By.XPATH, "//div[@class='dropDown mobile open']/ul[@class='dropdownList']/li[2]").click()
                time.sleep(1)

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
        #TODO add calculations giving each player a score
        for k, v in statDict.items():
            statDict[k] = float(v)
        if position == "Forward":        
            scoreAttack = ((statDict["Shooting accuracy %"]/100+statDict["Goals per match"])/2)*(1+statDict["Goals with right foot"]+statDict["Goals with left foot"]+1.2*statDict["Headed goals"]+0.2*statDict["Penalties scored"]+0.7*statDict["Freekicks scored"])/(1+statDict["Goals"])-(1+statDict["Big chances missed"])/(1+statDict["Shots"])
            scoreTeamPlay = (1+statDict["Assists"])/(1+statDict["Big Chances Created"])+((statDict["Big Chances Created"]+statDict["Crosses"]+1)/statDict["Passes"]+1)
            scoreDiscipline = (statDict["Yellow cards"]+3*statDict["Red cards"]+1)/(statDict["Fouls"]+1)
            scoreDefense = statDict["Tackles"]/(statDict["Fouls"]+1) + (1+statDict["Interceptions"]+statDict["Clearances"])/(1+statDict["Blocked shots"])
            score = ((2*scoreAttack + 0.75*scoreTeamPlay - 0.25*scoreDiscipline + 0.5*scoreDefense)*((1+statDict["Wins"])/(1+statDict["Appearances"])+(statDict["Wins"]+statDict["Losses"]+1)/(1+statDict["Appearances"])))*statDict["Appearances"]/100
        elif position == "Defender":
            #TODO perfect scoring
            scoreAttack = (1+statDict["Goals with right foot"]+statDict["Goals with left foot"]+1.2*statDict["Headed goals"])/(1+statDict["Goals"])
            scoreTeamPlay = (1+statDict["Assists"])/(1+statDict["Big Chances Created"])+((statDict["Big Chances Created"]+statDict["Crosses"]+statDict["Accurate long balls"]+1)/statDict["Passes"]+1)
            scoreDiscipline = (statDict["Yellow cards"]+3*statDict["Red cards"]+1)/(statDict["Fouls"]+1)
            scoreDefense = statDict["Tackle success %"]+statDict["Tackles"]/(statDict["Fouls"]+1) + (1+statDict["Interceptions"]+statDict["Clearances"]+1+statDict["Blocked shots"])/(1+statDict["Goals Conceded"]) + (statDict["Duels won"]+1)/(1+statDict["Duels won"] + statDict["Duels lost"]) + (statDict["Aerial battles won"]+1)/(statDict["Aerial battles won"]+(statDict["Clean sheets"]-statDict["Own goals"]-statDict["Errors leading to goal"])/statDict["Appearances"]+1)
            score = ((0.5*scoreAttack + 1*scoreTeamPlay - 0.5*scoreDiscipline + 2*scoreDefense)*((1+statDict["Wins"])/(1+statDict["Appearances"])+(statDict["Wins"]+statDict["Losses"]+1)/(1+statDict["Appearances"])))*statDict["Appearances"]/100
        elif position == "Midfielder":
            score = statDict["Appearances"]
        elif position == "Goalkeeper":
            score = statDict["Appearances"]
        else:
            score = 0

        playerSum = {"Name": name, "Number": number,
                     "Position": position, "Score": score}

        playerList.append(playerSum)
        driver.quit
    
    return playerList
