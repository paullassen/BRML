import sys
import os
import csv
import requests
import re
from bs4 import BeautifulSoup



def scrapeData(playerCode, teamCode):
	year = 2009
	writtenHeader = False
	while (year != 2018):
		url = 'http://www.baseball-reference.com/players/gl.fcgi?id=' + str(playerCode) + '&t=b&year=' + str(year)
		resultsPage = requests.get(url)
		soup = BeautifulSoup(resultsPage.text, "html5lib")
		table = soup.select_one("#batting_gamelogs")
		year += 1
		headers = ["Gcar", "Gtm", "Date", "Tm", "Away" ,"Opp", "Rslt", "Inngs", "PA", "AB", "R", "H", "2B", "3B", "HR", "RBI", "BB", "IBB", "SO", "HBP", "SH", "SF", "ROE", "GDP", "SB", "CS", "BA", "OBP", "SLG", "OPS", "BOP", "aLI", "WPA", "RE24", "Pos"]
		filename = teamCode + '/' + playerCode + '.csv'
		if (table != None):
			with open(filename, "a") as f:
				wr = csv.writer(f)
				if not writtenHeader:
					wr.writerow(headers)
					writtenHeader = True
				if sys.version[0] == '2':
					wr.writerows([[td.text.encode("utf-8") for td in row.find_all("td")] for row in table.select("tbody tr[id]")])
				else:
					wr.writerows([[td.text for td in row.find_all("td")] for row in table.select("tbody tr[id]")])
	return

def scrapePlayer(teamCode):
	url = 'http://www.baseball-reference.com/teams/' + teamCode + '/2017-roster.shtml'
	print(url)
	resultsPage = requests.get(url)
	soup = BeautifulSoup(resultsPage.text, "html5lib")
	table = soup.select_one("#appearances")

	rows = table.select("tbody tr")

	nameCodes = []
	for row in rows:
		for th in row.find_all("th"):	
			for a in th.find_all("a"):
				nameCode = (re.search(r"(\w)+(?=\.shtml)", str(a)).group(0))
				print('Scraping data for ' + nameCode + ' in team ' + teamCode)
				scrapeData(nameCode, teamCode)
	return

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
				teamCode = a.text
				print(teamCode)
				directory = os.getcwd() + '/' + teamCode
				if not os.path.exists(directory):
					os.makedirs(directory)
				scrapePlayer(teamCode)
	return

scrapeTeam()