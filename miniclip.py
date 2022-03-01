import requests
import os
from bs4 import BeautifulSoup

url = 'https://www.miniclip.com/games/page/en/downloadable-games/#privacy-settings'
print('Sending Request to URL')
html = requests.get(url)
print("Request Complete, Starting Download...")

soup = BeautifulSoup(html.text, 'html.parser')

links = soup.ul

i = 0
games = {}

for link in links.find_all('a', class_="button positive small greedy"):
	gameLink = link.get('href')
	name = gameLink.split('=')[1]
	games[name] = f'https://miniclip.com{gameLink}'

folderName = "MiniClip Games"
curDir = os.getcwd()

try:
	os.mkdir(folderName)
	print("Created games folder in current directory")

except:
    print("Found Games Folder")

os.chdir(f'{curDir}\\{folderName}')

for count, game in enumerate(games, start=1):
	print('Requesting Game (' + str(count) + '/' + '77): ' + game, end='')
	r = requests.get(games[game])

	open(f'{game}.exe', 'wb').write(r.content)
	print(' - Done')

print("Downloaded Games can be found at " + os.getcwd())
