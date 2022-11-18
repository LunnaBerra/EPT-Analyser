import Scraper
import PlayerURLs
import tabulate


def main():

    URL1 = PlayerURLs.getList("Tottenham")
    playerList = Scraper.scoreTeam(URL1)

    header = playerList[0].keys()
    rows = [x.values() for x in playerList]
    print(tabulate.tabulate(rows, header))

if __name__ == "__main__":
    main()