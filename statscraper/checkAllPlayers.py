from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://api.prizepicks.com/projections'

driver = webdriver.Chrome(executable_path='C:/Users/jkobler/Downloads/WebDriver/chromedriver.exe')
driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

picksJson = soup.body.find('pre').text
print(picksJson)

#TODO: decode picksJson to create a method that calls bestSelectionForPlayer on all NBA players
#TODO: refactor bestSelectionForPlayer into a reusable function that can be called with parameters: playerName, overUnders[(stat, overUnder)]