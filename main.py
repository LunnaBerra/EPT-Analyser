import Scraper
import PlayerURLs
import tabulate
import TeamScraper
import ResultsScraping
import FormCalculations


def main():
    formDict = ResultsScraping.checkLatestResults("Tottenham")
    TFS = FormCalculations.teamFormScore(formDict)
    print(TFS)


'''
    URL1Players = PlayerURLs.getList("Tottenham")
    URL1Team = PlayerURLs.getList("TottenhamTeam")
    #URL1 = ["https://www.premierleague.com/players/4408/Ben-Davies/stats"]
    #playerList = Scraper.scoreTeam(URL1Players, False)
    teamList = TeamScraper.scoreTeam(URL1Team,False)

    header = teamList[0].keys()
    rows = [x.values() for x in teamList]
    print(tabulate.tabulate(rows, header))
'''


if __name__ == "__main__":
    main()
