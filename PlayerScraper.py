from os import stat
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import FormCalculations


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
        
        score = FormCalculations.playerScore(statDict,position)

        playerSum = {"Name": name, "Number": number,
                     "Position": position, "Score": score}

        playerList.append(playerSum)
        driver.quit
    
    return playerList
