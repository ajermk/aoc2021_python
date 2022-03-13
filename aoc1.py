import os
import sys
lis = [199,200,208,210,200,207, 240, 269, 260, 263]
newlist = []

ite = 0
current = 0
#for i, item in enumerate(lis):
#with open(sys.argv[1]) as f:
#    current = next(f)
#    for line in f:
#        if int(line) > int(current):
#            ite = ite+1
#        current = int(line)

with open(sys.argv[1]) as f:
    for line in f:
        newlist.append(int(line))
currentsum = sum(newlist[0:0+3])
for i, item in enumerate(newlist):
    sliced = newlist[i:i+3]
    sumofsliced = sum(sliced)
    print(sliced)
    if len(sliced) == 3:
        if sumofsliced > currentsum:
            ite = ite + 1
        currentsum = sumofsliced
        #print("{}, {}".format(currentsum,ite))
print(ite)
