#Run to update active NBA players

from bs4 import BeautifulSoup
from selenium import webdriver
import csv

driver = webdriver.Chrome(executable_path='C:/Users/jkobler/Downloads/WebDriver/chromedriver.exe')

playerURLs = {}
teamURLs = {
    'BOS': 'https://www.espn.com/nba/team/roster/_/name/bos/boston-celtics',
    'BKN': 'https://www.espn.com/nba/team/roster/_/name/bkn/brooklyn-nets',
    'NYK': 'https://www.espn.com/nba/team/roster/_/name/ny/new-york-knicks',
    'PHI': 'https://www.espn.com/nba/team/roster/_/name/phi/philadelphia-76ers',
    'TOR': 'https://www.espn.com/nba/team/roster/_/name/tor/toronto-raptors',
    'GSW': 'https://www.espn.com/nba/team/roster/_/name/gs/golden-state-warriors',
    'LAC': 'https://www.espn.com/nba/team/roster/_/name/lac/la-clippers',
    'LAL': 'https://www.espn.com/nba/team/roster/_/name/lal/los-angeles-lakers',
    'PHX': 'https://www.espn.com/nba/team/roster/_/name/phx/phoenix-suns',
    'SAC': 'https://www.espn.com/nba/team/roster/_/name/sac/sacramento-kings',
    'CHI': 'https://www.espn.com/nba/team/roster/_/name/chi/chicago-bulls',
    'CLE': 'https://www.espn.com/nba/team/roster/_/name/cle/cleveland-cavaliers',
    'DET': 'https://www.espn.com/nba/team/roster/_/name/det/detroit-pistons',
    'IND': 'https://www.espn.com/nba/team/roster/_/name/ind/indiana-pacers',
    'MIL': 'https://www.espn.com/nba/team/roster/_/name/mil/milwaukee-bucks',
    'DAL': 'https://www.espn.com/nba/team/roster/_/name/dal/dallas-mavericks',
    'HOU': 'https://www.espn.com/nba/team/roster/_/name/hou/houston-rockets',
    'MEM': 'https://www.espn.com/nba/team/roster/_/name/mem/memphis-grizzlies',
    'NOP': 'https://www.espn.com/nba/team/roster/_/name/no/new-orleans-pelicans',
    'SAS': 'https://www.espn.com/nba/team/roster/_/name/sa/san-antonio-spurs',
    'ATL': 'https://www.espn.com/nba/team/roster/_/name/atl/atlanta-hawks',
    'CHA': 'https://www.espn.com/nba/team/roster/_/name/cha/charlotte-hornets',
    'MIA': 'https://www.espn.com/nba/team/roster/_/name/mia/miami-heat',
    'ORL': 'https://www.espn.com/nba/team/roster/_/name/orl/orlando-magic',
    'WSH': 'https://www.espn.com/nba/team/roster/_/name/wsh/washington-wizards',
    'DEN': 'https://www.espn.com/nba/team/roster/_/name/den/denver-nuggets',
    'MIN': 'https://www.espn.com/nba/team/roster/_/name/min/minnesota-timberwolves',
    'OKC': 'https://www.espn.com/nba/team/roster/_/name/okc/oklahoma-city-thunder',
    'POR': 'https://www.espn.com/nba/team/roster/_/name/por/portland-trail-blazers',
    'UTAH': 'https://www.espn.com/nba/team/roster/_/name/utah/utah-jazz'
}

for team in teamURLs.values():
    driver.get(team)
    content = driver.page_source
    soup = BeautifulSoup(content)
    for element in soup.body.find("tbody", "Table__TBODY").find_all('a'):
        name = element.text
        link = element['href']
        playerURLs[name] = link

with open('playerURLs.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in playerURLs.items():
        writer.writerow([key.lower(), value])


