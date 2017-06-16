

import csv
import requests
import re
from bs4 import BeautifulSoup

teamCode = 'SFG'

url = 'http://www.baseball-reference.com/teams/' + teamCode + '/2017-roster.shtml'
resultsPage = requests.get(url)
soup = BeautifulSoup(resultsPage.text, "html5lib")
table = soup.select_one("#appearances")

rows = table.select("tbody tr")

nameCode = []
for row in rows:
	for th in row.find_all("th"):	
		for a in th.find_all("a"):
			nameCode.append(re.search(r"(\w)+(?=\.shtml)", str(a)).group(0))

print(nameCode)