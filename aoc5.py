import os
import sys
from collections import defaultdict
from aocd import lines
import math
import numpy
import cProfile

def parseFile(arg):
    with open(arg) as f:
        lines = f.read().splitlines()
    return lines

def aocOne(lines, part2=False):
    diagram = defaultdict(int)
    #highestY = 0
    #highestX = 0
    for line in lines:
        x, y = line.split('->')
        x1, y1 = map(int, x.split(','))
        x2, y2 = map(int, y.split(','))
        
        #x1, y1, x2, y2  = [int(item) for items in line.split('->') for item in items.split(',')]
        
        ## used in printing the array
        #if highestY < max([y1,y2]):
            #highestY = max([y1,y2])
        #if highestX < max([x1,x2]):
            #highestX = max([x1,x2])
        
        if x1 == x2:
            ## if 1,1 -> 1,3, or 9,9 -> 9,7.
            # range will be directly getting specific indexes, so in latters case 9,8,7
            ran = range(y1, y2+1) if y1 < y2 else range(y2, y1+1)
            for y in ran:
                diagram[(x1, y)] += 1
        elif y1 == y2:
            ran = range(x1, x2+1) if x1 < x2 else range(x2, x1+1)
            for x in ran:
                diagram[(x, y1)] += 1
        elif part2:
            ## unlike part one were getting difference between two coords
            xMultiplier = 1 if x2 > x1 else -1
            yMultiplier = 1 if y2 > y1 else -1
            ran = range(abs(x2-x1)+1)
            for i in ran:
                diagram[(x1 + (i*xMultiplier), y1 + (i*yMultiplier))] += 1
                
            ### shortened from all slope checks:
            
            # backwards slope
            #if (x2 > x1 and y2 > y1):
                #ran = range(abs(x2-x1)+1)
                ##print(f'{x1}:{y1}, {x2}:{y2}')
                #for i in ran:
                    #diagram[(x1 + i, y1+i)] += 1
                    #print(f'{diagram[(x1 + x, y1+x)]}')
            #elif (x2 < x1 and y2 < y1):
                #ran = range(abs(x2-x1)+1)
                ##print(f'{x1}:{y1}, {x2}:{y2}')
                #for i in ran:
                    #diagram[(x1 - i, y1-i)] += 1
                    #print(f'{diagram[(x1 + i, y1-i)]}')
            ## forward slope
            ## 9,7->7,9
            #elif (x1 > x2 and y2 > y1):
                #ran = range(abs(x2-x1)+1)
                ##print(f'{x1}:{y1}, {x2}:{y2}')
                #for i in ran:
                    #diagram[(x1 - i, y1+i)] += 1
                    #print(f'{x1-i}, {y1+i}')
            ## 7,9->9,7
            #elif (x2 > x1 and y2 < y1):
                #ran = range(abs(x2-x1)+1)
                ##print(f'{x1}:{y1}, {x2}:{y2}')
                #for i in ran:
                    #diagram[(x1 + i, y1-i)] += 1
                    #print(f'{x1-i}, {y1+i}')
    return diagram #, highestX, highestY

def printDiagram(diagram, highestX, highestY):
    lis = numpy.zeros((int(highestX),int(highestY)),dtype=int, order='C')
    for key in diagram:
        x, y = key
        lis[y-1][x-1] = int(diagram[key])
    for items in lis:
        print(" ".join(map(str, [item if item!=0 else '_' for item in items])))

## run on local file
#diagram = aocOne(parseFile(sys.argv[1]), True)
#printDiagram(diagram,highestX, highestY)

## run from aocd
diagram = cProfile.run('aocOne(lines, True)')

print(sum(value >= 2 for value in diagram.values()))
