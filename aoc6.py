import sys
from collections import defaultdict
#from aocd import lines
import functools
import cProfile

def parseFile(arg):
    with open(arg) as f:
        lines = lines = [int(item) for item in f.read().strip().split(',')]
    return lines

def aocOne(lines):
    
    day = 0
    while day < 256:
        countAppend = 0
        for i, item in enumerate(lines):
            if item == 0:
                lines[i] = 6
                countAppend += 1
            else:
                lines[i] -= 1
        if countAppend > 0:
            for i in range(countAppend):
                lines.append(8)
        day += 1
    return len(lines)

def aocTwo(lines):
    fishState = [0] * 9
    lines = [int(item) for item in lines]
    for item in lines:
         fishState[item] += 1
    days = 256
    for i in range(days):
        births = fishState[0]
        for i in range(len(fishState)-1):
            fishState[i] = fishState[i+1]
            fishState[i+1] = 0
        if births > 0:
            fishState[8] += births
            fishState[6] += births
    
    return sum(fishState)

lines = parseFile(sys.argv[1])
print(aocTwo(lines))
cProfile.run('aocTwo(lines)')