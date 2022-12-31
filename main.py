from re import X
import PlayerScraper
import PlayerURLs
import tabulate
import TeamScraper
import ResultsScraping
import FormCalculations
import time
import GUI


def main():
    gui = GUI.Ui_MainWindow()
    ''''''
    '''formDict = ResultsScraping.checkLatestResults("Tottenham")
    TFS = FormCalculations.teamFormScore(formDict)
    print(TFS)'''
    '''
    teamP1 = "Tottenham"
    teamT1 = teamP1 + "Team"
    teamP2 = "Liverpool"
    teamT2 = teamP2 + "Team"

    URL1Players = PlayerURLs.getList(teamP1)
    URL1Team = PlayerURLs.getList(teamT1)
    URL2Players = PlayerURLs.getList(teamP2)
    URL2Team = PlayerURLs.getList(teamT2)

    x = ResultsScraping.checkLatestResults(teamP1)
    ResultsP1 = FormCalculations.teamFormScore(x)
    playerList = PlayerScraper.scoreTeam(URL1Players, False)
    PositionScoreP1 = FormCalculations.positionEval(playerList)
    teamList = TeamScraper.scoreTeam(URL1Team, False)
    TeamScoreP1 = FormCalculations.teamScore(teamList[0])


    x = ResultsScraping.checkLatestResults(teamP2)
    ResultsP2 = FormCalculations.teamFormScore(x)
    playerList = PlayerScraper.scoreTeam(URL2Players, False)
    PositionScoreP2 = FormCalculations.positionEval(playerList)
    teamList = TeamScraper.scoreTeam(URL2Team, False)
    TeamScoreP2 = FormCalculations.teamScore(teamList[0])

    ResultsScoreDiff = ResultsP1 - ResultsP2
    print("RSD: ", " ", ResultsScoreDiff)
    print(PositionScoreP1)
    print(PositionScoreP2)
    print(TeamScoreP1)
    print(TeamScoreP2)
    k = 0
    PositionScoreDiff = []

    while k < 3:
        PositionScoreDiff.append(PositionScoreP1[k] - PositionScoreP2[k])
        k = k + 1

    k = 0
    TeamScoreDiff = []
    while k < 3:
        TeamScoreDiff.append(TeamScoreP1[k] - TeamScoreP2[k])
        k = k + 1

    print("RSD: ", " ", ResultsScoreDiff)
    print("PSD: ", " ", PositionScoreDiff)
    print("TSD: ", " ", TeamScoreDiff)

    '''
    '''header = playerList[0].keys()
    rows = [x.values() for x in playerList]
    print(tabulate.tabulate(rows, header))'''
    '''
'''


if __name__ == "__main__":
    main()
