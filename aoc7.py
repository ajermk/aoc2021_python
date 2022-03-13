import sys
import math
def parseFile(arg):
    with open(arg) as f:
        lines = [int(item) for item in f.read().strip().split(',')]
    return lines

def aocOne(lines):
    prev_sum = math.inf
    nmax = max(lines)
    nmin = min(lines)
    for i in range(nmin, nmax+1):
        
        nsum = 0
        for item in lines:
            absol = abs(item-i)
            # sum of natural numbers
            nsum += int((absol*(absol+1))/2)

        if prev_sum > nsum:
            prev_sum = nsum
    
    return prev_sum

print(aocOne(parseFile(sys.argv[1])))