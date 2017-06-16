

import csv
import requests
from bs4 import BeautifulSoup
year = 2009
not_entered = True
while (year != 2018):
	url = 'http://www.baseball-reference.com/players/gl.fcgi?id=troutmi01&t=b&year=' + str(year)
	resultsPage = requests.get(url)
	soup = BeautifulSoup(resultsPage.text, "html5lib")
	table = soup.select_one("#batting_gamelogs")
	year += 1
	items = ["Gcar", "Gtm", "Date", "Tm", "Away" ,"Opp", "Rslt", "Inngs", "PA", "AB", "R", "H", "2B", "3B", "HR", "RBI", "BB", "IBB", "SO", "HBP", "SH", "SF", "ROE", "GDP", "SB", "CS", "BA", "OBP", "SLG", "OPS", "BOP", "aLI", "WPA", "RE24", "Pos"]
	headers = items
	if (table != None):
		with open("out6.csv", "a") as f:
		    wr = csv.writer(f)
		    if (not_entered):
		    	wr.writerow(headers)

		    	not_entered = False
		    headers = [th.text.encode("utf-8") for th in table.select("tr th")]
		    wr.writerows([[td.text.encode("utf-8") for td in row.find_all("td")] for row in table.select("tr + tr")])



