from aocd import lines
import unittest
import os

xy = [0,0,0]
current = ''
units = ''
#lines = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

for item in lines:
    current, units = item.split()
    units = int(units)
    if current == 'forward':
        xy[0] = xy[0] + units
        xy[1] = xy[1] + (xy[2] * units)
    elif current == 'up':
        xy[2] = xy[2] - units
    elif current == 'down':
        xy[2] = xy[2] + units
        
print(xy[0]*xy[1])
