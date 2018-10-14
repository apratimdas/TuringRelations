from bs4 import BeautifulSoup
import requests

page = requests.get("https://en.wikipedia.org/wiki/Turing_Award")

soup = BeautifulSoup(page.content, 'html.parser')

data = []
table = soup.find('table', attrs={'class':'wikitable'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

# print(data)

namelist=[]

for i in data:
    if(len(i)>0):
        if i[0].find('and') != -1:
            temp = i[0].find('and')
            namelist.append(i[0][0:temp-1])
            namelist.append(i[0][temp+5:])
        else:
            namelist.append(i[0])

for i in namelist:
    print(i)