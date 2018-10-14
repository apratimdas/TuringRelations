from bs4 import BeautifulSoup
import requests
import re


with open("dump3", "r") as ins:
    namelist = []
    for line in ins:
        temp = line[:-1]
        temp1 = temp[:temp.find('--')-1]
        temp2 = temp[temp.find('--') + 3:]
        print("\"" + temp1 + '\" -- \"' + temp2 + "\"")
        # print(line[:-1])