
from graphics import *
from random import randint
import csv

grid = []
for i in range(11):
    grid.append([])
    for j in range(11):
        grid[i].append(j)

# print(grid)

gcm=[]

with open('gcm') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        gcm.append(row)

print(gcm)

def main():
    win = GraphWin("My Window", 660, 660)
    squares = []
    i=0
    j=0
    while i < 11:
        j=0
        while j < 11:
            square = Rectangle(Point(j*66,i*66), Point((j+1)*66,(i+1)*66))
            x = gcm[i][j]
            y = float(x) + 1
            rval = int(y / 2 * 255)
            bval = int( (1 - y / 2) * 255)
            square.setFill(color_rgb(rval,0,bval))
            squares.append(square)
            square.draw(win)
            j+=1
        i+=1

    win.getMouse()


main()