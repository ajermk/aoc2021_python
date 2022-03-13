import os
import sys
#from aocd import lines

def aocOne(lis, lines, drawNumbersAll):
    singleBingo = []
    checkFiveNum = []
    for j in range(0, len(drawNumbersAll), 5):
        checkFiveNum = drawNumbersAll[j:j+5]
        for i in range(0, len(lis), 5):
            singleBingo = lis[i:i+5]
            print(singleBingo)


def processInput(lines):
    lines = [item for item in lines if item != '']
    drawNumbersAll = [int(item) for item in lines[0].split(',') if item != '']
    lines.pop(0)
    counter = 0
    lis = []
    for item in lines:
        sublist = []
        for i in item.split(' '):
            if i != '':
                sublist.append(int(i))
        lis.append(sublist)
    print(lis)
    
    return lis, lines, drawNumbersAll

lines = []
with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f]
    
print(lines)
lis, lines, drawNumbersAll = processInput(lines)
aocOne(lis, lines, drawNumbersAll)
