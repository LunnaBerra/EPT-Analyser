import PlayerScraper
import PlayerURLs
import tabulate
import TeamScraper
import ResultsScraping
import FormCalculations


def main():
    '''
    formDict = ResultsScraping.checkLatestResults("Tottenham")
    TFS = FormCalculations.teamFormScore(formDict)
    print(TFS)
    '''

    URL1Players = PlayerURLs.getList("Tottenham")
    #URL1Team = PlayerURLs.getList("TottenhamTeam")
    #URL1Players = ["https://www.premierleague.com/players/4112/Eric-Dier/stats"]
    playerList = PlayerScraper.scoreTeam(URL1Players, True)
    #teamList = TeamScraper.scoreTeam(URL1Team,False)

    header = playerList[0].keys()
    rows = [x.values() for x in playerList]
    print(tabulate.tabulate(rows, header))



if __name__ == "__main__":
    main()
