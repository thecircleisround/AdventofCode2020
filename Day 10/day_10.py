from numpy import diff
from collections import defaultdict

f = list(set(map(int, open("day10_input.txt"))))
maxrating = max(f) + 3
f.append(maxrating)
f.insert(0, 0)


def moe(func):
    tried = defaultdict(int)

    def helper(x):
        if x not in tried:
            tried[x] = func(x)
        return tried[x]

    return helper


@moe
def possibilities(item):
    values = []
    x = list(z for z in list(item - y for y in range(1, 4)) if z in f)
    
    if item == 0:
        return 1
    #Line comprehension below causes "max recursion depth" error
    #values = [int(possibilities(value)) for value in x]  
    for i in x:
        value = possibilities(i)
        values.append(value)
    return sum(values)


#part 1                
difference = list(diff(f))
solution = difference.count(1) * difference.count(3)
print(f'Part one answer {solution}')

#part 2              

print(f'{possibilities(maxrating)} total combinations')
