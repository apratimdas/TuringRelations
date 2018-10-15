import re

dict = {}
ctr = 1
with open("dump5", "r") as ins:
    namelist = []
    for line in ins:
        temp = re.findall('"([^"]*)"', line)
        for i in temp:
            if i not in dict:
                dict[i] = ctr
                ctr += 1

# print(dict)

with open("dump5", "r") as ins:
    namelist = []
    for line in ins:
        temp = re.findall('"([^"]*)"', line)
        print(str(dict[temp[0]]) + ',' + str(dict[temp[1]]))

