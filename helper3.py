from bs4 import BeautifulSoup
import requests
import re

page = requests.get("https://en.wikipedia.org/wiki/Turing_Award")

soup = BeautifulSoup(page.content, 'html.parser')

with open("namelist.txt", "r") as ins:
    namelist = []
    for line in ins:
        namelist.append(line[:-1].replace(' ', '_'))

weblinks = []
# print(namelist)
for link in soup.findAll('a', attrs={'href': re.compile("/wiki/")}):
    temp = link.get('href')[6:] 
    if temp in namelist:
        weblinks.append(temp)

weblinks = set(weblinks)
wikilinks = []
for i in weblinks:
    wikilinks.append("https://en.wikipedia.org/wiki/" + i)

for link in wikilinks:
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = []
    table = soup.find('table', attrs={'class':'infobox biography vcard'})
    if table is None:
        continue
    table_body = table.find('tbody')
    print(link[30:].replace('_',' '), end=" -- ")

    rows = table_body.find_all('tr')
    for row in rows:
        col1 = row.find_all('th')
        col1 = [ele.text.strip() for ele in col1]
        data.append([ele for ele in col1 if ele])
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    try:
        if(data.index(['Doctoral advisor'])):
            print(data[data.index(['Doctoral advisor']) + 1][0])
    except:
        print("not found")