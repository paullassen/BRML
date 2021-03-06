

import csv
import requests
from bs4 import BeautifulSoup



def scrapeData(playerCode):
	year = 2009
	not_entered = True
	while (year != 2018):
		url = 'http://www.baseball-reference.com/players/gl.fcgi?id=' + playerCode + '&t=b&year=' + str(year)
		resultsPage = requests.get(url)
		soup = BeautifulSoup(resultsPage.text, "html5lib")
		table = soup.select_one("#batting_gamelogs")
		year += 1
		headers = ["Gcar", "Gtm", "Date", "Tm", "Away" ,"Opp", "Rslt", "Inngs", "PA", "AB", "R", "H", "2B", "3B", "HR", "RBI", "BB", "IBB", "SO", "HBP", "SH", "SF", "ROE", "GDP", "SB", "CS", "BA", "OBP", "SLG", "OPS", "BOP", "aLI", "WPA", "RE24", "Pos"]
		filename = playerCode + '.csv'
		if (table != None):
			with open("out6.csv", "a") as f:
			    wr = csv.writer(f)

		    	wr.writerow(headers)
			    wr.writerows([[td.text.encode("utf-8") for td in row.find_all("td")] for row in table.select("tbody tr[id]")])
	return

def scrapePlayer(teamCode):
	url = 'http://www.baseball-reference.com/teams/' + teamCode + '/2017-roster.shtml'
	resultsPage = requests.get(url)
	soup = BeautifulSoup(resultsPage.text, "html5lib")
	table = soup.select_one("#appearances")

	rows = table.select("tbody tr")

	nameCodes = []
	for row in rows:
		for th in row.find_all("th"):	
			for a in th.find_all("a"):
				nameCode = (re.search(r"(\w)+(?=\.shtml)", str(a)).group(0))
				scrapeData(nameCode)

def scrapeTeam():
	url = 'http://www.baseball-reference.com/leagues/MLB/2017.shtml'
	resultsPage = requests.get(url)
	teamSoup = BeautifulSoup(resultsPage.text, "html5lib")
	table = teamSoup.select_one("#teams_standard_batting")

	rows = table.select("tbody tr")

	teamCodes = []

	for row in rows:
		for th in row.find_all("th"):
			for a in th.find_all("a"):
				teamCode = a.text.encode("utf-8")
				scrapePlayer(teamCode)
