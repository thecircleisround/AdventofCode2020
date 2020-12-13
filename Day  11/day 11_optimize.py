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
        for coord in coordscompare:
            if coord not in nearestseats: 
                adjseats = findseats(coordscop,coord,limit)
                nearestseats[coord] = adjseats
            else: 
                adjseats = nearestseats[coord]
            occupiedseats = len([
                coordscop[value] for value in adjseats
                if value in coordscop if coordscop[value] == "#"])
            if coordscompare[coord] == ".":
                pass
            elif coordscompare[coord] == "L" and occupiedseats == 0:
                coordscompare[coord] = "#"
            elif coordscompare[coord] == "#" and occupiedseats >= limit:
                coordscompare[coord] = "L"
        if coordscompare == coordscop:
            totaloccupiedseats = sum(x == "#" for x in coordscop.values())
            print(f'There are {totaloccupiedseats} total occupied seats')
            break
        else:
            coordscop = coordscompare.copy()


def findseats(coords, coord, limit):
    adjseats = list(tuple(map(sum, zip(coord, mod))) for mod in mods)
    occupiedseats = []
    for i in adjseats:
        index = adjseats.index(i)
        x, y = i
        found = False
        if limit == 4: 
            return adjseats
        while found == False:
            if i not in coords:
                found = True
            elif coords[i] == ".":
                x += mods[index][0]
                y += mods[index][1]
                i = x, y
            elif coords[i] == "L" or coords[i] == "#":
                adjseats[index] = i
                found = True
   # print(adjseats)
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

