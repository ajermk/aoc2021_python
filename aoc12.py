import sys
from collections import defaultdict, deque

def parseFile(arg):
    with open(arg) as f:
        lines = [list(map(str,item.split('-'))) for item in f.read().strip().split()]
    return lines

# first try for part 2
# def bfs(graph, root):
#     q = deque()
#     explored = []
#     explored.append('start')
#     q.append('start')
#     path = []
#     print(q, explored)
#     while q:
#         v = q.popleft()
#         path.append(v)
#         if v == 'end':
#             return path
#         for value in graph.get(v):
#             if value.isupper():
#                 if explored.count(value) < 2:
#                     explored.append(value)
#                     q.append(value)
#             elif value not in explored:
#                 explored.append(value)
#                 q.append(value)
#     return explored

# part 1
# def is_not_visited(value, path):
#     if not value.isupper():
#         if value in path:
#             return False
#     return True

# def bfs(graph, start, end):
#     q = deque()
#     path = []
#     path.append(start)
#     q.append(path.copy())
#     results = []

#     while q:
#         path = q.popleft()
#         curr = path[-1]

#         if curr == end:
#             results.append(path)
        
#         for value in graph.get(curr):
#             if is_not_visited(value, path):
#                 new_path = path.copy()
#                 new_path.append(value)
#                 q.append(new_path)

#     return len(results)

# part 2
def visited(path, visited_twice):
    for item in path:
        if item.islower():
            if path.count(item) > 1:
                visited_twice = True
                break
    return visited_twice
    
def bfs(graph, start, end):
    q = deque()
    path = []
    visited_twice = False
    path.append(start)
    q.append([path.copy(), visited_twice])
    results = []

    while q:
        path, visited_twice = q.popleft()
        curr = path[-1]

        if curr == end:
            results.append(path)
            continue
        
        for value in graph.get(curr):
            visited_twice = visited(path,visited_twice)
            if value != 'start':
                #big caves can be visited any number of times
                if (value.isupper() or 
                    # a single small cave can be visited at most twice
                    (visited_twice == False or 
                    # the remaining small caves can be visited at most once
                    (value not in path))):
                        new_path = path.copy()
                        new_path.append(value)
                        q.append([new_path, visited_twice])
                        #print(new_path, visited_twice)
           
    # results.sort()
    # for item in results:
    #     print(item)
    return len(results)

def aocOne(lines):
    graph = defaultdict(list)
    for elements in lines:
        graph[elements[0]].append(elements[1])
        graph[elements[1]].append(elements[0])
    print(graph)
    print(bfs(graph, 'start', 'end'))
lines = parseFile(sys.argv[1])
aocOne(lines)