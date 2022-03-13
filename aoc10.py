import sys
from collections import defaultdict, deque

def parseFile(arg):
    with open(arg) as f:
        lines = [list(map(str, item)) for item in f.read().strip().split()]
    return lines

item_table = {
    ')':'(', ']':'[', '}':'{', '>':'<'
}

item_points = {
    ')': 3, ']': 57, '}':1197, '>':25137
}
def aocOne(lines):
    illegal_character = defaultdict(int)
    for line in lines:
        stack = deque()
        for item in line:
            if item in item_table:
                comparator = stack.pop()
                if comparator != item_table.get(item):
                    illegal_character[item] += 1
            else:
                stack.append(item)

    return sum([item_points[key]*value for key, value in illegal_character.items()])

item_points_2 = {
    '(':1, '[':2, '{':3, '<':4
}
def aocTwo(lines):
    sums = []
    for line in lines:
        stack = deque()
        for item in line:
            if item in item_table:
                comparator = stack.pop()
                # discard incorrect lines
                if comparator != item_table.get(item):
                    stack.clear()
                    break
            else:
                stack.append(item)
        if stack:
            score = 0
            for item in list(stack)[::-1]:
                score *= 5
                score += item_points_2.get(item)
            sums.append(score)
    sums.sort()
    middle_index = int((len(sums) - 1)/2)
    return sums[middle_index]
lines = parseFile(sys.argv[1])
print(aocTwo(lines))
