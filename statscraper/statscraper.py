# input player name/id, stat, over/under
# returns number of games over, num games under, total games played

from bs4 import BeautifulSoup
from selenium import webdriver
import csv

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

statcodes = {
    'pts': 16,
    'reb': 10,
    'ast': 11,
    'blk': 12,
    'stl': 13,
    'to': 15,
    '3pt': 6,
    'ft': 8
}
playerURLs = {}
with open('playerURLs.csv') as csv_file:
    reader = csv.reader(csv_file)
    playerURLs = dict(reader)

def compareStatsToProp(soupContent, stat, overUnder, gameLimit, opponent):
    over = 0
    under = 0
    totGames = 0
    overOpp = 0
    underOpp = 0
    totOppGames = 0
    searchBody = soupContent.body.find("div", "PageLayout__Main").find("div", "mb5 flex justify-between flex-row items-center").find_next_sibling("div")
    months = searchBody.find_all(class_ = "mb5")
    for month in months:
        games = month.find("tbody", "Table__TBODY").find_all("tr")
        games.pop()
        for game in games:
            if gameLimit != None and totGames >= gameLimit:
                break
            gameinfo = game.find_all(class_ = "Table__TD")
            opp = gameinfo[1].find("span", "pr2 TeamLink__Logo").next_sibling.a.string.lower()
            val = 0.
            if stat == "pra":
                points = float(gameinfo[statcodes.get('pts')].text)
                rebounds = float(gameinfo[statcodes.get('reb')].text)
                assists = float(gameinfo[statcodes.get('ast')].text)
                val = points + rebounds + assists
            elif stat == 'pr':
                points = float(gameinfo[statcodes.get('pts')].text)
                rebounds = float(gameinfo[statcodes.get('reb')].text)
                val = points + rebounds
            elif stat == 'pa':
                points = float(gameinfo[statcodes.get('pts')].text)
                assists = float(gameinfo[statcodes.get('ast')].text)
                val = points + assists
            elif stat == 'ra':
                rebounds = float(gameinfo[statcodes.get('reb')].text)
                assists = float(gameinfo[statcodes.get('ast')].text)
                val = rebounds + assists
            elif stat == 'bs':
                blocks = float(gameinfo[statcodes.get('blk')].text)
                steals = float(gameinfo[statcodes.get('stl')].text)
                val = blocks + steals
            elif stat == 'fant':
                points = float(gameinfo[statcodes.get('pts')].text)
                rebounds = float(gameinfo[statcodes.get('reb')].text)
                assists = float(gameinfo[statcodes.get('ast')].text)
                blocks = float(gameinfo[statcodes.get('blk')].text)
                steals = float(gameinfo[statcodes.get('stl')].text)
                turnovers = float(gameinfo[statcodes.get('to')].text)
                val = points + 1.2*rebounds + 1.5*assists + 3*blocks + 3*steals - turnovers
            else:
                temp = gameinfo[statcodes.get(stat)].text
                if stat == "3pt" or stat == "ft":
                    idx=0
                    while (temp[idx] != '-'):
                        idx+=1
                    val = float(temp[:idx])
                else: 
                    val = float(temp)

            if val > overUnder:
                over+=1
                if opponent == opp:
                    overOpp+=1
            elif val < overUnder:
                under+=1
                if opponent == opp:
                    underOpp+=1
            totGames+=1
            if opponent == opp:
                    totOppGames+=1
        else:
            continue
        break

    return {
        'over': over,
        'under': under,
        'totGames': totGames,
        'overOpp': overOpp,
        'underOpp': underOpp,
        'totOppGames': totOppGames
    }

def main():
    player = input('Enter name of player?\n').lower()
    while playerURLs.get(player) == None:
        player = input(color.RED + 'Invalid player name' + color.END + '\nEnter name of an ' + color.BOLD + 'active' + color.END + ' NBA player?\n').lower()

    stat = input('Stat?\nOptions are: PTS (Points), REB (Rebounds), AST (Assists), BLK (Blocks), STL (Steals), TO (Turnovers), PRA (Points+Rebounds+Assists), PR (Points+Rebounds), PA (Points+Assists), RA (Rebounds+Assists), BS(Blocks+Steals), 3PT (3-Pt Made), FT (FTs Made), FANT (Fantasy Score)\n').lower()
    while statcodes.get(stat) == None and stat != 'fant' and stat != 'pra' and stat != 'pr' and stat != 'pa' and stat != 'ra' and stat != 'bs':
        stat = input(color.RED + 'Invalid stat code' + color.END + '\nOptions are: ' + color.BOLD + 'PTS, REB, AST, BLK, STL, TO, 3PT, FT, FANT, PRA, PR, PA, RA, BS' + color.END + '\n').lower()

    overUnder = float(input('Over/Under?\n'))
    gameLimit = input('Enter game limit, leave blank to ignore:\n')
    opponent = input('Enter opponent\'s team code, leave blank to ignore:\n').lower()
    if gameLimit == '':
        gameLimit = None
    else:
        gameLimit = int(gameLimit)

    driver = webdriver.Chrome(executable_path='C:/Users/jkobler/Downloads/WebDriver/chromedriver.exe')
    gamelogURL = playerURLs.get(player)
    gamelogURL = gamelogURL[:32] + "gamelog/" + gamelogURL[32:]
    driver.get(gamelogURL)
    content = driver.page_source
    soup = BeautifulSoup(content)
    driver.quit()
    results = compareStatsToProp(soup, stat, overUnder, gameLimit, opponent)

    print("\n")
    print("\n")
    if results['totOppGames'] > 0:
        print("Number of games over " + color.BOLD + "against " + opponent.upper() + color.END + ": " + color.GREEN + str(results['overOpp']) + "/" + str(results['totOppGames']) + color.END + " games played\n")
        print("Number of games under " + color.BOLD + "against " + opponent.upper() + color.END + ": " + color.RED + str(results['underOpp']) + "/" + str(results['totOppGames']) + color.END + " games played\n")
        print("\n")
    print("Number of games over: " + color.GREEN + str(results['over']) + "/" + str(results['totGames']) + color.END + " games played\n")
    print("Number of games under: " + color.RED + str(results['under']) + "/" + str(results['totGames']) + color.END + " games played\n")
    percentage = 100.0 * (float(results['over'])/float(results['totGames']))
    print("There is a " + color.BOLD + str(percentage) + "%" + color.END + " chance that " + color.BOLD + player.title() + color.END + " hits the over.")
    print("\n")

if __name__ == "__main__":
        main()