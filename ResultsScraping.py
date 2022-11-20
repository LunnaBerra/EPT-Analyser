from selenium import webdriver
import pandas as pd
from tabulate import tabulate
import os


def checkLatestResults(team):
    os.chdir(r"C:\Users\simon\OneDrive\Skrivbord\FRITID\EPT Analyser\Results")
    cwd = os.getcwd()
    print(cwd)

    browser = webdriver.Chrome()

    browser.get(
        "https://www.oddsportal.com/soccer/england/premier-league/results/")

    df = pd.read_html(browser.page_source, header=0)[0]

    dateList = []
    gameList = []
    scoreList = []
    home_odds = []
    draw_odds = []
    away_odds = []

    for row in df.itertuples():
        if not isinstance(row[1], str):
            continue
        elif ':' not in row[1]:
            date = row[1].split('-')[0]
            continue
        time = row[1]
        dateList.append(date)
        gameList.append(row[2])
        scoreList.append(row[3])
        home_odds.append(row[4])
        draw_odds.append(row[5])
        away_odds.append(row[6])

    result_comp_1 = pd.DataFrame({'date': dateList,
                                  'game': gameList,
                                  'score': scoreList,
                                  'Home': home_odds,
                                  'Draw': draw_odds,
                                  'Away': away_odds})

    print(tabulate(result_comp_1))

    browser.get(
        "https://www.oddsportal.com/soccer/england/premier-league/results/#/page/2/")

    df = pd.read_html(browser.page_source, header=0)[0]

    dateList = []
    gameList = []
    scoreList = []
    home_odds = []
    draw_odds = []
    away_odds = []

    for row in df.itertuples():
        if not isinstance(row[1], str):
            continue
        elif ':' not in row[1]:
            date = row[1].split('-')[0]
            continue
        time = row[1]
        dateList.append(date)
        gameList.append(row[2])
        scoreList.append(row[3])
        home_odds.append(row[4])
        draw_odds.append(row[5])
        away_odds.append(row[6])

    result_comp = pd.DataFrame({'date': dateList,
                                'game': gameList,
                                'score': scoreList,
                                'Home': home_odds,
                                'Draw': draw_odds,
                                'Away': away_odds})

    new_df = result_comp_1.append(result_comp, ignore_index=True)

    latestGame = []
    latestGameIndex = []
    latestGameResults = []
    c = 0
    for i in gameList:
        k = i.split(" ")
        if k[2] == "-":
            k[0] = k[0] + " " + k[1]
            k.pop(1)
        if k[1] == "-" and len(k) > 3:
            k[len(k)-1] = k[len(k)-2] + " " + k[len(k)-1]
            k.pop(len(k)-2)
        for j in k:
            if j == team:
                latestGame.append(i)
                latestGameIndex.append(c)
                latestGameResults.append(scoreList[c])
        c = c + 1
    f = 0
    W = 0
    L = 0
    D = 0
    GoalsConceded = 0
    GoalsMade = 0
    GamesPlayed = len(latestGame)
    for i in latestGame:
        k = i.split(" ")
        if k[2] == "-":
            k[0] = k[0] + " " + k[1]
            k.pop(1)
        if k[1] == "-" and len(k) > 3:
            k[len(k)-1] = k[len(k)-2] + " " + k[len(k)-1]
            k.pop(len(k)-2)
        n = latestGameResults[f].split(":")

        if n[0] == n[1]:
            D = D + 1
        elif k[0] == team:
            if n[0] > n[1]:
                W = W + 1
            else:
                L = L + 1
            GoalsMade = GoalsMade + int(n[0])
            GoalsConceded = GoalsConceded + int(n[1])
        elif k[len(k)-1] == team:
            if n[0] < n[1]:
                W = W + 1
            else:
                L = L + 1
            GoalsMade = GoalsMade + int(n[1])
            GoalsConceded = GoalsConceded + int(n[0])
        f = f + 1

    results = {"Wins": W, "Draws": D, "Losses": L, "Goals Made": GoalsMade, "Goals Conceded": GoalsConceded, "Games Played": GamesPlayed}
    return results
