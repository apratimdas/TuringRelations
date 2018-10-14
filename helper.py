
import re

with open("rel4.dot", "r") as ins:
    arr = []
    flag = 0
    for line in ins:
        if " Relationship" in line:
            flag = 1
        if flag:
            arr.append(line)

def hasNumbers(inputString):
    return any(char.isdigit() or char == "\"" for char in inputString)

finallist = []

for i in arr:
    if hasNumbers(i):
        temp = re.findall('"([^"]*)"', i)
        for j in temp:
            if hasNumbers(j):
                finallist.append("\t\"" + j + "\" " + "[style = filled,color=salmon2];")
            else:
                finallist.append("\t\"" + j + "\" " + "[style = filled];")

finallist = set(finallist)

for i in finallist:
    print(i)