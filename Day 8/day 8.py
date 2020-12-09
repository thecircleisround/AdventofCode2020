    import re
    
    steps = list(filter(lambda x: x != " ", 
            re.split('[\n " "]',open('day8_input.txt', 'r').read())))
    
    accel = 0
    
    def part1(steps): 
        global accel
        currentitem = 0 
        moveslist = []
        while True:
            currentmove = steps[currentitem+1]
            if steps[currentitem] == 'acc': 
                accel += int(currentmove)
                currentitem += 2
            elif steps[currentitem] == 'jmp':
                currentitem = int(currentitem) + (int(currentmove) * 2)
            elif steps[currentitem] == 'nop':
                currentitem += 2
            if currentitem in moveslist: 
                print(f'LOOP DETECTED - Accel is set to {accel}')
                return False
            else:
                moveslist.append(currentitem)
    
    
    def part2(steps): 
        global accel
        accel = 0
        currentitem = 0 
        tryalt = False
        moveslist = []
        alttries = []
        copymoves = []
        storeitem = "" 
        
        while currentitem <= 1270:
            currentmove = steps[currentitem+1]
            if steps[currentitem] == 'acc': 
                accel += int(currentmove)
                currentitem += 2
            elif steps[currentitem] == 'jmp':
                if tryalt != True and currentitem not in alttries: 
                    copymoves = moveslist.copy()
                    alttries.append(currentitem)
                    tempaccel = accel
                    currentitem = alternatives(steps, currentitem)
                    tryalt = True
                else:
                    currentitem = int(currentitem) + (int(currentmove) * 2)
            elif steps[currentitem] == 'nop':
                if tryalt != True and currentitem not in alttries: 
                    copymoves = moveslist.copy()
                    alttries.append(currentitem)
                    tempaccel = accel
                    currentitem = alternatives(steps, currentitem)
                    tryalt = True
                else: 
                    currentitem += 2
            if currentitem in moveslist:
                currentitem = alttries[-1]
                moveslist = copymoves
                accel = tempaccel
                tryalt = False     
            else:
                moveslist.append(currentitem)
            
        print(f'Program Halted - Accel is set to {accel}')
                
    def alternatives(steps, currentitem):
        currentmove = steps[currentitem+1]
        if steps[currentitem] == 'nop':
                currentitem = int(currentitem) + (int(currentmove) * 2)  
                return currentitem     
        elif steps[currentitem] == 'jmp':
                currentitem += 2
                return currentitem
                
    part1(steps)
    part2(steps)
