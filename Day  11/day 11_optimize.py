from itertools import product
from time import time

starttime = time()
f = list(
    filter(lambda x: x != '', list(open('day11_input.txt').read().split(
        "\n"))))

mods = list(product([0, 1, -1], repeat=2))
mods.pop(0)
coords = {}


def applyrules(limit=4):
    coordscop = coords.copy()
    coordscompare = coords.copy()
    nearestseats = {}
    while True:
        for i in coordscompare:
            if i not in nearestseats: 
                adjseats = findseats(coordscop,i)
                nearestseats[i] = adjseats
            else: 
                adjseats = nearestseats[i]
            occupiedseats = len([
                coordscop[value] for value in adjseats
                if value in coordscop if coordscop[value] == "#"])
            if coordscompare[i] == ".":
                pass
            elif coordscompare[i] == "L" and occupiedseats == 0:
                coordscompare[i] = "#"
            elif coordscompare[i] == "#" and occupiedseats >= limit:
                coordscompare[i] = "L"
        if coordscompare == coordscop:
            totaloccupiedseats = sum(x == "#" for x in coordscop.values())
            print(f'There are {totaloccupiedseats} total occupied seats')
            break
        else:
            coordscop = coordscompare.copy()


def findseats(coordscop, i):
    adjseats = list(tuple(map(sum, zip(i, mod))) for mod in mods)
    occupiedseats = []
    for i in adjseats:
        index = adjseats.index(i)
        factor = 1
        found = False
        while found == False:
            x, y = i
            if i not in coordscop:
                found = True
            elif coordscop[i] == ".":
                x += mods[index][0]
                y += mods[index][1]
                i = x, y
            elif coordscop[i] == "L":
                found = True
            elif coordscop[i] == "#":
                found = True
    return adjseats


#Build grid
y = 0
for i in f[-1::-1]:
    x = 0
    for e in i:
        coord = x, y
        coords[coord] = e
        x += 1
    y += 1

#Solve puzzle
applyrules()
applyrules(5)

timer = "{:.2f}".format(time() - starttime)
print(f'{timer}s')
