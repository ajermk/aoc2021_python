from aocd import lines
#import unittest
import os
import sys
# https://topaz.github.io/paste/#XQAAAQAoBAAAAAAAAAAyGUj/T32X5leZ5R0tKWDjkddL9H++ZF7s8GIpRG65NYAdX4XUFMBnBPMCWPasKGD1MNiagYgm6Zse4IoIbZ+cZd7bwpU9JlOjF+aCgvsFcKI2dI9TNIJwMaMINMyICS6zJYAaSVIDddYTzx2bZei8jG0DhO0Q5Gmf/5H6y70K0UWF68yxJq5B9CvaTKENKx1OLlajcoMco0izJFT1DpfW0RSzU5InRNfuiiFJLxNHEAQSQPOd2qe20ARaSnCP7mHBx/Jt213aNJy9SaMXX/v1jhz2cpBsohYZ8qnNUMb16OpPqfALv0Ezfs5QlEpHKNbMhxvVdxzsmk5wc0IYarOUM87Vx7dajRM6Xhw6oaw0vRl1peOiD8RTjXu7OKy6hOiMzNJaTUoMlTcC/ZuOVYtqs85r//Ioaso=

def aocOne(lines):
    lengthOfByte = len(lines[0])
    finalBinary = ""
    for i in range(lengthOfByte): # check each binarys 0th pos first, then all 1st ...
        counter = ""
        for byte in lines:
            #print("bit:{}, bit at {} pos: {}".format(x,i&1,int(x,2) >> i & 1))
            counter += byte[i]#str(int(x,2) >> i & 1) 
        if counter.count("0") > counter.count("1"): finalBinary += "0"
        else: finalBinary += "1"
    invertBinary = ''.join(['1' if i=='0' else '0' for i in finalBinary])
    
    return finalBinary, invertBinary

def aocTwo(lines, opposite):
    #2d array get 
    
    values = lines.copy()
    for i in range(len(values[0])):
        col = [row[i] for row in values]
        if col.count('0') > col.count('1'):
            values = [items for items in values if items[i] == '0']
        else:
            values = [items for items in values if items[i] == '1']
    return values

def aocTwo(lines, opposite=False):
    #2d array get 
    one = '0' if opposite else '1'
    zero = '1' if opposite else '0' 
    values = lines.copy()
    for i in range(len(values[0])):
        col = [row[i] for row in values]
        if len(values) == 1:
            break
        if col.count('0') > col.count('1'):
            values = [items for items in values if items[i] == zero]
        else:
            values = [items for items in values if items[i] == one]
    return int(values[0],2)


print(aocTwo(lines) * aocTwo(lines, True))
#co2 = aocTwo(invertBinary, lines)
#print(oxy*co2)
#lines = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
binary, invertBinary = aocOne(lines)
