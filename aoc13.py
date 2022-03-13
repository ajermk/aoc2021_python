import sys
import cProfile

def parse_file_1(arg):
    with open(arg) as f:
        data = f.read()
    lines, instructions = data.strip().split("\n\n")
    lines = [list(map(int,item.split(','))) for item in lines.split()]
    instructions = parse_file_2(instructions)
    return lines, instructions

def parse_file_2(instruct):
    # instructions = []
    # for line in instruct.split():
    #     for item in line.split():
    #         if item == 'fold' or item == 'along':
    #             continue
    #         axis, coord = item.split('=')
    #         instructions.append([axis,coord])

    instructions = [list(map(str,item.split('='))) 
        for line in instruct.split() 
            for item in line.split() 
                if item != 'fold' and item != 'along']
    return instructions

def find_grid_size(lines):
    max_x = max(coord[0] for coord in lines) + 1
    max_y = max(coord[1] for coord in lines) + 1
    return max_x, max_y

def print_paper(lines):
    max_x, max_y = find_grid_size(lines)
    for y in range(max_y):
        to_print = ''
        for x in range(max_x):
            if [x,y] in lines:
                to_print += '#'
            else:
                to_print += '.'
        print(to_print)
    result = ''.join

def aocOne(lines, instructions):
    for instruct in instructions:
        axis, middle = instruct
        middle = int(middle)
        to_remove = []
        for i, item in enumerate(lines):
            x, y = item
            if axis == 'x':
                if x <= middle:
                    continue
                x = x - ((x - middle)*2)
            if axis == 'y':
                if y <= middle:
                    continue
                y = y - ((y - middle)*2)
            if [x,y] not in lines:
                lines[i] = [x,y]
            else:
                to_remove.append(item)
        for item in to_remove:
            lines.remove(item)
            
    print(len(lines))

    print_paper(lines)

lines, instructions = parse_file_1(sys.argv[1])
max_x, max_y = find_grid_size(lines)
#instructions = parse_file_2(sys.argv[2])
aocOne(lines,instructions)