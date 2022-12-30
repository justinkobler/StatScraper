from bs4 import BeautifulSoup
from selenium import webdriver
from statscraper import compareStatsToProp
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

playerURLs = {}
with open('playerURLs.csv') as csv_file:
    reader = csv.reader(csv_file)
    playerURLs = dict(reader)

inputName = input('Enter player:\n').lower()
#gameLimit = input('Enter game limit, leave blank to ignore:\n')
#if gameLimit == '':
#    gameLimit = None
#else:
#    gameLimit = int(gameLimit)
#while inputName != 'done' and inputName != 'end' and inputName != 'quit' and inputName != 'q':
#    inputProp = input('Enter prop:\n').lower()
#    playerProps[inputName] = inputProp
#    print('\n')
#    inputName = input('Enter player:\n').lower()

overUnderPts = input("Points Over/Under:\n")
overUnderRebs = input("Rebounds Over/Under:\n")
overUnderAsts = input("Assists Over/Under:\n")
overUnderBlk = input("Blocks Over/Under:\n")
overUnderStl = input("Steals Over/Under:\n")
overUnder3Pt = input("3-Pt Made Over/Under:\n")
overUnderFT = input("FT Made Over/Under:\n")
overUnderTO = input("Turnovers Over/Under:\n")        
overUnderFant = input("Fantasy Score Over/Under:\n")
overUnderPRA = input("Points + Rebounds + Assists Over/Under:\n")
overUnderPR = input("Points + Rebounds Over/Under:\n")
overUnderPA = input("Points + Assists Over/Under:\n")
overUnderRA = input("Rebounds + Assists Over/Under:\n")
overUnderBS = input("Blocks + Steals Over/Under:\n")

driver = webdriver.Chrome(executable_path='C:/Users/jkobler/Downloads/WebDriver/chromedriver.exe')
gamelogURL = playerURLs.get(inputName)
gamelogURL = gamelogURL[:32] + "gamelog/" + gamelogURL[32:]
driver.get(gamelogURL)
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()
gameLimits = [None, 10, 5]
for gameLimit in gameLimits:
    maxPercent = 0.0
    bestLine = ''

    if overUnderPts != '':
        overUnderPts = float(overUnderPts)
        res = compareStatsToProp(soup, 'pts', overUnderPts, gameLimit, '')
        percentOver = float(res['over'])/float(res['totGames'])
        percentUnder = float(res['under'])/float(res['totGames'])
        percent = max(percentOver, percentUnder)
        if percent > maxPercent:
            if percentOver >= percentUnder:
                bestLine = 'Points Over'
            else:
                bestLine = 'Points Under'
            maxPercent = percent

    if overUnderRebs != '':
        overUnderRebs = float(overUnderRebs)
        res = compareStatsToProp(soup, 'reb', overUnderRebs, gameLimit, '')
        percentOver = float(res['over'])/float(res['totGames'])
        percentUnder = float(res['under'])/float(res['totGames'])
        percent = max(percentOver, percentUnder)
        if percent > maxPercent:
            if percentOver >= percentUnder:
                bestLine = 'Rebounds Over'
            else:
                bestLine = 'Rebounds Under'
            maxPercent = percent
        elif percent == maxPercent:
            if percentOver >= percentUnder:
                bestLine = bestLine + ' | Rebounds Over'
            else:
                bestLine = bestLine + ' | Rebounds Under'

    if overUnderAsts != '':
        overUnderAsts = float(overUnderAsts)
        res = compareStatsToProp(soup, 'ast', overUnderAsts, gameLimit, '')
        percentOver = float(res['over'])/float(res['totGames'])
        percentUnder = float(res['under'])/float(res['totGames'])
        percent = max(percentOver, percentUnder)
        if percent > maxPercent:
            if percentOver >= percentUnder:
                bestLine = 'Assists Over'
            else:
                bestLine = 'Assists Under'
            maxPercent = percent
        elif percent == maxPercent:
            if percentOver >= percentUnder:
                bestLine = bestLine + ' | Assists Over'
            else:
                bestLine = bestLine + ' | Assists Under'

    if overUnderBlk != '':
        overUnderBlk = float(overUnderBlk)
        res = compareStatsToProp(soup, 'blk', overUnderBlk, gameLimit, '')
        percentOver = float(res['over'])/float(res['totGames'])
        percentUnder = float(res['under'])/float(res['totGames'])
        percent = max(percentOver, percentUnder)
        if percent > maxPercent:
            if percentOver >= percentUnder:
                bestLine = 'Blocks Over'
            else:
                bestLine = 'Blocks Under'
            maxPercent = percent
        elif percent == maxPercent:
            if percentOver >= percentUnder:
                bestLine = bestLine + ' | Blocks Over'
            else:
                bestLine = bestLine + ' | Blocks Under'

    if overUnderStl != '':
        overUnderStl = float(overUnderStl)
        res = compareStatsToProp(soup, 'stl', overUnderStl, gameLimit, '')
        percentOver = float(res['over'])/float(res['totGames'])
        percentUnder = float(res['under'])/float(res['totGames'])
        percent = max(percentOver, percentUnder)
        if percent > maxPercent:
            if percentOver >= percentUnder:
                bestLine = 'Steals Over'
            else:
                bestLine = 'Steals Under'
            maxPercent = percent
        elif percent == maxPercent:
            if percentOver >= percentUnder:
                bestLine = bestLine + ' | Steals Over'
            else:
                bestLine = bestLine + ' | Steals Under'

    if overUnder3Pt != '':
        overUnder3Pt = float(overUnder3Pt)
        res = compareStatsToProp(soup, '3pt', overUnder3Pt, gameLimit, '')
        percentOver = float(res['over'])/float(res['totGames'])
        percentUnder = float(res['under'])/float(res['totGames'])
        percent = max(percentOver, percentUnder)
        if percent > maxPercent:
            if percentOver >= percentUnder:
                bestLine = '3-Pt Made Over'
            else:
                bestLine = '3-Pt Made Under'
            maxPercent = percent
        elif percent == maxPercent:
            if percentOver >= percentUnder:
                bestLine = bestLine + ' | 3-Pt Made Over'
            else:
                bestLine = bestLine + ' | 3-Pt Made Under'

    if overUnderFT != '':
        overUnderFT = float(overUnderFT)
        res = compareStatsToProp(soup, 'ft', overUnderFT, gameLimit, '')
        percentOver = float(res['over'])/float(res['totGames'])
        percentUnder = float(res['under'])/float(res['totGames'])
        percent = max(percentOver, percentUnder)
        if percent > maxPercent:
            if percentOver >= percentUnder:
                bestLine = 'Free Throws Made Over'
            else:
                bestLine = 'Free Throws Made Under'
            maxPercent = percent
        elif percent == maxPercent:
            if percentOver >= percentUnder:
                bestLine = bestLine + ' | FT Made Over'
            else:
                bestLine = bestLine + ' | FT Made Under'

    if overUnderTO != '':
        overUnderTO = float(overUnderTO)
        res = compareStatsToProp(soup, 'to', overUnderTO, gameLimit, '')
        percentOver = float(res['over'])/float(res['totGames'])
        percentUnder = float(res['under'])/float(res['totGames'])
        percent = max(percentOver, percentUnder)
        if percent > maxPercent:
            if percentOver >= percentUnder:
                bestLine = 'Turnovers Over'
            else:
                bestLine = 'Turnovers Under'
            maxPercent = percent
        elif percent == maxPercent:
            if percentOver >= percentUnder:
                bestLine = bestLine + ' | Turnovers Over'
            else:
                bestLine = bestLine + ' | Turnovers Under'

    if overUnderFant != '':
        overUnderFant = float(overUnderFant)
        res = compareStatsToProp(soup, 'fant', overUnderFant, gameLimit, '')
        percentOver = float(res['over'])/float(res['totGames'])
        percentUnder = float(res['under'])/float(res['totGames'])
        percent = max(percentOver, percentUnder)
        if percent > maxPercent:
            if percentOver >= percentUnder:
                bestLine = 'Fantasy Score Over'
            else:
                bestLine = 'Fantasy Score Under'
            maxPercent = percent
        elif percent == maxPercent:
            if percentOver >= percentUnder:
                bestLine = bestLine + ' | Fantasy Score Over'
            else:
                bestLine = bestLine + ' | Fantasy Score Under'

    if overUnderPRA != '':
        overUnderPRA = float(overUnderPRA)
        res = compareStatsToProp(soup, 'pra', overUnderPRA, gameLimit, '')
        percentOver = float(res['over'])/float(res['totGames'])
        percentUnder = float(res['under'])/float(res['totGames'])
        percent = max(percentOver, percentUnder)
        if percent > maxPercent:
            if percentOver >= percentUnder:
                bestLine = 'PRA Over'
            else:
                bestLine = 'PRA Under'
            maxPercent = percent
        elif percent == maxPercent:
            if percentOver >= percentUnder:
                bestLine = bestLine + ' | PRA Over'
            else:
                bestLine = bestLine + ' | PRA Under'

    if overUnderPR != '':
        overUnderPR = float(overUnderPR)
        res = compareStatsToProp(soup, 'pr', overUnderPR, gameLimit, '')
        percentOver = float(res['over'])/float(res['totGames'])
        percentUnder = float(res['under'])/float(res['totGames'])
        percent = max(percentOver, percentUnder)
        if percent > maxPercent:
            if percentOver >= percentUnder:
                bestLine = 'PR Over'
            else:
                bestLine = 'PR Under'
            maxPercent = percent
        elif percent == maxPercent:
            if percentOver >= percentUnder:
                bestLine = bestLine + ' | PR Over'
            else:
                bestLine = bestLine + ' | PR Under'

    if overUnderPA != '':
        overUnderPA = float(overUnderPA)
        res = compareStatsToProp(soup, 'pa', overUnderPA, gameLimit, '')
        percentOver = float(res['over'])/float(res['totGames'])
        percentUnder = float(res['under'])/float(res['totGames'])
        percent = max(percentOver, percentUnder)
        if percent > maxPercent:
            if percentOver >= percentUnder:
                bestLine = 'PA Over'
            else:
                bestLine = 'PA Under'
            maxPercent = percent
        elif percent == maxPercent:
            if percentOver >= percentUnder:
                bestLine = bestLine + ' | PA Over'
            else:
                bestLine = bestLine + ' | PA Under'

    if overUnderRA != '':
        overUnderRA = float(overUnderRA)
        res = compareStatsToProp(soup, 'ra', overUnderRA, gameLimit, '')
        percentOver = float(res['over'])/float(res['totGames'])
        percentUnder = float(res['under'])/float(res['totGames'])
        percent = max(percentOver, percentUnder)
        if percent > maxPercent:
            if percentOver >= percentUnder:
                bestLine = 'RA Over'
            else:
                bestLine = 'RA Under'
            maxPercent = percent
        elif percent == maxPercent:
            if percentOver >= percentUnder:
                bestLine = bestLine + ' | RA Over'
            else:
                bestLine = bestLine + ' | RA Under'

    if overUnderBS != '':
        overUnderBS = float(overUnderBS)
        res = compareStatsToProp(soup, 'bs', overUnderBS, gameLimit, '')
        percentOver = float(res['over'])/float(res['totGames'])
        percentUnder = float(res['under'])/float(res['totGames'])
        percent = max(percentOver, percentUnder)
        if percent > maxPercent:
            if percentOver >= percentUnder:
                bestLine = 'BS Over'
            else:
                bestLine = 'BS Under'
            maxPercent = percent
        elif percent == maxPercent:
            if percentOver >= percentUnder:
                bestLine = bestLine + ' | BS Over'
            else:
                bestLine = bestLine + ' | BS Under'

    print(color.PURPLE + "Game Limit: " + color.BOLD + str(gameLimit) + color.END + "\n")
    print("Best Line is: " + color.BOLD + bestLine + color.END + " with a " + color.BOLD + str(100.0*maxPercent) + "% chance" + color.END + " of winning.\n")