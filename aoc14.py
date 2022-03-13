import sys
from collections import defaultdict
import cProfile

def parse_file(arg):
    with open(arg) as f:
        data = f.read()
    polymer, pairs = data.strip().split("\n\n")
    polymer = [item for item in polymer.split()]
    pairs = [[i for i in item.split(' -> ')] for item in pairs.split('\n')]
    return polymer, pairs

POLYMER_VALUES = defaultdict(str)

def create_polymer_values(pairs):
    global POLYMER_VALUES
    for item in pairs:
        POLYMER_VALUES[item[0]] = item[1] 

def aocOne(polymer, iters=10):
    global POLYMER_VALUES
    # to count occurence for each separate 2pair elems
    polymer_dict = defaultdict(int)
    # to count occurence for each letter
    letter_dict = defaultdict(int)

    # create dict out of initial string
    polymer = polymer[0]
    for i, item in enumerate(polymer):
        letter_dict[item] += 1
        if i+1 < len(polymer):
            polymer_dict[polymer[i] + polymer[i+1]] += 1

    for _ in range(iters):
        replacement_dict = defaultdict(int)
        # for each 2pair elems
        for key, value in polymer_dict.items():
            insertion = POLYMER_VALUES.get(key)
            # for each occruence(var = value) of a 2pair element, 
            # split into two
            replacement_dict[key[0] + insertion] += value
            replacement_dict[insertion + key[1]] += value
            # for each occurence of a single 2pair element, 
            # occurence will be same for new letter between the 2pair
            letter_dict[insertion] += value

        polymer_dict = replacement_dict
    final_values = letter_dict.values()
    return max(final_values) - min(final_values)


polymer, pairs = parse_file(sys.argv[1])
create_polymer_values(pairs)
#print(POLYMER_VALUES)
cProfile.run('aocOne(polymer, 1000000)')