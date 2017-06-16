

import csv
import requests
from bs4 import BeautifulSoup
year = 2009

while (year != 2018):
	url = 'http://www.baseball-reference.com/players/gl.fcgi?id=troutmi01&t=b&year=' + str(year)
	resultsPage = requests.get(url)
	soup = BeautifulSoup(resultsPage.text, "html5lib")
	table = soup.select_one("#batting_gamelogs")
	year += 1
	if (table != None):
		headers = [th.text.encode("utf-8") for th in table.select("tr th")]
		
		with open("out3.csv", "a") as f:
		    wr = csv.writer(f)
		    wr.writerow(headers)
		    wr.writerows([[td.text.encode("utf-8") for td in row.find_all("td")] for row in table.select("tr + tr")])



