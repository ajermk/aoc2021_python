import sys

def parseFile(arg):
    with open(arg) as f:
        lines = [list(map(int, item)) for item in f.read().strip().split()]
    return lines
#clockwise
adjacent = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]

def explode(grid, i, j, will_explode_coords, flashed):
    # logic of comments 3) and 3.5)
    for n in adjacent:
        x, y = n
        k = i+x
        l = j+y
        if k>=0 and k<(len(grid)) and l>=0 and l<(len(grid[0])):
            if grid[k][l] != 0:
                grid[k][l] += 1
            if grid[k][l] > 9:
                grid[k][l] = 0
                will_explode_coords.append((k,l))
                flashed.append((k,l))

    return


def single_step(grid):
    # 1) go through grid and +1 all items
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            grid[i][j] += 1
    
    flashed = []
    # 2) go through all items and check for any 10+s, 
    # if any, set it to 0
    # make sure it hasnt been checked before, as we can only flash once per step
    # otherwise and save the coord
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            if grid[i][j] > 9 and (i, j) not in flashed:
                grid[i][j] = 0
                flashed.append((i,j))
                # 3) flash (+1) all adjacent coords
                # 3.5) in an event an adjacent coord is now 10+
                #      save that coord in will_explode_coords,
                #      and check all adjs again.
                #      continue this until we don't have any 10+ coords left to flash
                will_explode_coords = []
                will_explode_coords.append((i,j))
                while will_explode_coords:
                    xx, yy = will_explode_coords.pop()
                    explode(grid, xx, yy, will_explode_coords, flashed)
    return len(flashed)


grid = parseFile(sys.argv[1])

times_flashed = 0
# part 1
# for i in range(100):
    
#     times_flashed += single_step(grid)
#     #print(grid)

# part 2
while True:
    single_step(grid)
    times_flashed += 1
    # The following expression returns 
    # True if all elements are 0 (or False), 
    # else return False
    if not any(any(x) for x in grid):
        break


print(times_flashed)







