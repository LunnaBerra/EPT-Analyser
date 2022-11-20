import Scraper
import PlayerURLs
import tabulate


def main():

    URL1 = PlayerURLs.getList("Tottenham")
    #URL1 = ["https://www.premierleague.com/players/4408/Ben-Davies/stats"]
    playerList = Scraper.scoreTeam(URL1, False)

    header = playerList[0].keys()
    rows = [x.values() for x in playerList]
    print(tabulate.tabulate(rows, header))


if __name__ == "__main__":
    main()
