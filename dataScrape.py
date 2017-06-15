

import csv
import requests
from bs4 import BeautifulSoup
url = 'http://www.baseball-reference.com/players/gl.fcgi?id=troutmi01&t=b&year=2013'
resultsPage = requests.get(url)
soup = BeautifulSoup(resultsPage.text, "html5lib")
table = soup.select_one("#batting_gamelogs")

headers = [th.text.encode("utf-8") for th in table.select("tr th")]

with open("out.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(headers)
    wr.writerows([[td.text.encode("utf-8") for td in row.find_all("td")] for row in table.select("tr + tr")])



