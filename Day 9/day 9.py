from itertools import accumulate
import time 
import re

start_time = time.time()
f =  [int(value) for value in list(filter(lambda x : x !="",re.split('[\n]',(open('day9_input.txt', 'r').read()))))]

wrongnumber = "" 
wrongnumberindex = 0


def mylambda(n): 
    return lambda x: n - x

x,y = 0, 25

for i in f[25:]: 
    calc = mylambda(int(i))
    founditem = False
    for j in f[x:y]:
        result = calc(int(j))
        if result != j and result in f[x:y]: 
            #print("found")
            founditem = True
            break
    if founditem == True: 
        x += 1
        y += 1
    else: 
        wrongnumber = i 
        wrongnumberindex = f.index(wrongnumber)
        print(f'Invalid number is: {wrongnumber}')
        break

def finderror(fcounter, x, y):
    result = False
    results = []
    currentrange = f[x:x+fcounter]
    for i in accumulate(currentrange): 
        results.append(i)
    if max(results) == wrongnumber:
        weakness = min(currentrange) + max(currentrange)
        print(f'Found {wrongnumber}, encryption weakness is {weakness}')
        return True
    return result

fcounter = 1
fresult = False
x = 0 
y = 25

while fresult != True:
    fresult = finderror(fcounter, x, y)
    fcounter += 1
    if fcounter > 25: 
        fcounter = 2 
        x += 1
        y += 1
    
totaltime = (time.time() - start_time)
rounded = "{:.4f}".format(totaltime)

print(f'Program took {rounded}s to run')
        
        
