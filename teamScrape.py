

import csv
import requests
from bs4 import BeautifulSoup

url = 'http://www.baseball-reference.com/leagues/MLB/2017.shtml'
resultsPage = requests.get(url)
soup = BeautifulSoup(resultsPage.text, "html5lib")
table = soup.select_one("#teams_standard_batting")

rows = table.select("tbody tr")

teamCodes = []

for row in rows:
	for th in row.find_all("th"):
		for a in th.find_all("a"):
			teamCodes.append(a.text.encode("utf-8"))

print(teamCodes)
