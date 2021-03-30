
import pandas as pd
import urllib.request
import urllib2
import lxml.html as lh
import requests
from bs4 import BeautifulSoup

url = 'https://www.atptour.com/en/players/atp-head-2-head/novak-djokovic-vs-daniil-medvedev/D643/MM58'
print('result code:' + str(url.getcode()))

data = url.read()
print(data)
# url = "https://www.atptour.com/en/players/atp-head-2-head/novak-djokovic-vs-daniil-medvedev/D643/MM58"
# request = urllib2.Request(url)
# page = urllib2.urlopen(request)
# soup = BeautifulSoup(page, 'html.parser')

# rows = soup.find('div', _class="page-scores-h2h-table").find_all('div', recursive = False)
# print(rows)



# page = 'https://www.atptour.com/en/rankings/singles'
# r = requests.get(page)
# soup = BeautifulSoup(r.text, 'html.parser')

# # player_stats = soup.find(id = "rankingsTable")

# ranking_table = soup.find('table', class_ = "scores-table")

# print(ranking_table)
# request_page = urlopen(url_to_scrape)
# page_html = request_page.read()
# request_page.close()

# html_soup = BeatifulSoup(page_html, "html.parser")

# player_age = html_soup.find_all('div', class_= "table-big-value")

# filename = 'products.csv'
# f = open(filename, 'w')

# headers = "Title, Weight \n"

# f.write(headers)

# for player in player_age:
#     title = player.find('div', class_= "table-big-value").text
#     weight = player.find('div', class_= "table-weight-lbs").text
#     f.write(title + "," + weight)
# f.close()