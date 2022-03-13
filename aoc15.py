import sys
from collections import defaultdict
import heapq
import cProfile

def parse_file(arg):
    with open(arg) as f:
        data = f.read()
    grid = [list(map(int,item)) for item in data.strip().split()]
    return grid

def neighbors(grid, curr):
    x,y = curr
    #print(grid[x][y])
    nbs = [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]
    #remove_coords = []
    nbs = [coord for coord in nbs if (0 <= coord[0] < len(grid[0]) and 0 <= coord[1] < len(grid))]
    # for nb in nbs:
    #     x, y = nb
        #print(grid[x][y])
    return nbs

def dijkstra(grid, source, destination):
    q = [((0,0),0)]
    #https://stackoverflow.com/questions/29901564/defaultdict-with-values-defaulted-to-negative-infinity
    dist = defaultdict(lambda: float('inf'))
    prev = defaultdict(tuple)
    visited = defaultdict(lambda: False)

    while q:
        xy, curr_dist = heapq.heappop(q)

        if visited[xy]:
            continue

        visited[xy] = True
        for nx, ny in neighbors(grid, xy):
            alt = curr_dist + grid[nx][ny]
            if alt < dist[(nx, ny)]:
                dist[(nx,ny)] = alt
                heapq.heappush(q, (((nx,ny),alt)))
                prev[(nx,ny)] = xy

    print(dist[destination])
    return dist

def build_grid(grid):
    n, m = len(grid), len(grid[0])
    row, col = n*5, m*5
    new_grid = [[0 for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            # depending on quadrant +0-4 for row/col
            diff = i // n + j // m - 1
            # get original grid coord and add diff in new quadrant
            changed_weight = grid[i % n][j % m] + diff
            # -1 +1 is so that if changed weight is 9 it changes to 1
            changed_weight = changed_weight % 9 +1
            new_grid[i][j] = changed_weight
    return new_grid


grid = parse_file(sys.argv[1])
print(grid)
new_grid = build_grid(grid)
cProfile.run('dijkstra(new_grid, (0,0), (len(new_grid)-1,len(new_grid)-1))')