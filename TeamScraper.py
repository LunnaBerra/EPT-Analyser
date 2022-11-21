from os import stat
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


def scoreTeam(teamURLList, allTime: bool):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    URL_list = teamURLList
    teamList = []
    cookies = False
    for url in URL_list:
        driver.get(url)
        if not cookies:
            time.sleep(5)
            cookies = True
        statDict = {}
        try:
            if allTime == False:
                time.sleep(1)
                WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                    (By.XPATH, "//div[@class='dropDown mobile'][1]"))).click()
                time.sleep(0.5)
                driver.find_element(
                    By.XPATH, "//div[@class='dropDown mobile open']/ul[@class='dropdownList']/li[2]").click()
                time.sleep(1)

            main = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "playerStats"))
            )
            stats = main.text
            x = stats.split("\n")
            statList = list(x)
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
        # TODO add calculations giving the teams Attack and Defense a score
        teamList.append(statDict)
        driver.quit

    return teamList
