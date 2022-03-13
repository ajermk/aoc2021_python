import sys
from collections import deque

def parseFile(arg):
    return_list = []
    with open(arg) as f:
        lines = [item for item in f.read().strip().split()]
        for item in lines:
            sublist = [int(i) for i in item]
            return_list.append(sublist)
            
    return return_list


def aocOne(grid,width,height):
    nums = []
    coords = []
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            if y == 9:
                continue
            to_append = True
            positions = []
            if i != 0:
                positions.append(grid[i-1][j])
            if j != 0:
                positions.append(grid[i][j-1])
            if i != height-1:
                positions.append(grid[i+1][j])
            if j != width-1:
                positions.append(grid[i][j+1])
            for item in positions:
                if item < y:
                    to_append=False
                    break
            if to_append:
                coords.append((i,j))
                nums.append(y)

    return sum([item+1 for item in nums]), coords

def floodFill(grid, coords, width, height):
    basins = []
    for coord in coords:
        q = deque()
        q.append(coord)
        basin_size = 0
        seen_coords = []
        while q:
            current_coord = q.pop()
            if current_coord in seen_coords:
                continue
            x, y = current_coord
            n = grid[x][y]
            seen_coords.append((x,y))
            if n < 9:
                basin_size += 1
                if y < width-1:
                    q.append((x,y+1))
                if y > 0:
                    q.append((x,y-1))
                if x < height-1:
                    q.append((x+1, y))
                if x > 0:
                    q.append((x-1, y))
        basins.append(basin_size)
    basins.sort()
    return basins[-3:]

grid = parseFile(sys.argv[1])
width = len(grid[0])
height = len(grid)
а, coords = aocOne(grid,width,height)
print(floodFill(grid, coords, width, height))