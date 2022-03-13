import os
import sys
import math
import cProfile

# get initial input and split by double lines twice. aka empty lines will not be there
with open(sys.argv[1]) as f:
    lines = f.read().split('\n\n')
nums = [int(item) for item in lines[0].split(',')]
bingos = [[int(n) for n in items.split()] for items in lines[1:]]

def aocOne(nums, bingos):
    for counter, num in enumerate(nums):
        for i, bingo in enumerate(bingos):
            if counter >= 5:
                j = 0
                for n in range(0,25,5):
                    if all(x == 'marked' for x in bingo[n:n+5]) or all(x == 'marked' for x in bingo[j::5]):
                        return sum([x for x in bingo if x != 'marked']) * nums[counter-1]
                    j += 1
            changedBingo = ['marked' if item==num else item for item in bingo]
            bingos[i] = changedBingo
        
        
    return None

print(cProfile.run('aocOne(nums, bingos)'))


def aocTwo(nums, bingos):
    # for each win number. count how many iterations there were to not check for the first four numbers - 
    #               - this is mainly for optimization since then the winstate is impossible at first 4 nums
    # check each bingo board, a list of lists. enumerate is to change bingo board via bingos[i], since if a number found it will be 'marked'
    winningBoards = []
    winSize = int(math.sqrt(len(bingos[0]))) # should be 5 but basically supports bigger boards that have n*n nums
    for counter, num in enumerate(nums):
        for i, bingo in enumerate(bingos):
            if counter >= winSize:
                j = 0
                for n in range(0,winSize*winSize,winSize):
                    # navigate each row and column for win state. for row requires +5. for column rquires +1, which j provides
                    # do not check for boards that have won already
                    if i not in winningBoards and (all(x == 'marked' for x in bingo[n:n+winSize]) or all(x == 'marked' for x in bingo[j::winSize])):
                        # if we get final winning board, get the last winning board's sum and the last number that was called  
                        if len(winningBoards) == len(bingos)-1:
                            return sum([x for x in bingo if x != 'marked']) * nums[counter-1]
                        # otherwise use a list to append the winning's board index
                        winningBoards.append(i)
                        #
                    j += 1
            
            bingoChanged = ['marked' if item==num else item for item in bingo]
            bingos[i] = bingoChanged
    return None

        
        

#

print(cProfile.run('aocTwo(nums, bingos)'))
    
