import sys

def parseFile(arg):
    lis = []
    start_reading = False
    with open(arg, 'r') as f:
        for line in f:
            for word in line.split():
                if start_reading:
                    lis.append(word)
                if word == '|':
                    start_reading = True
            start_reading = False
    return lis

num_dict = {
    'abcefg' : 0,
    'cf' : 1,
    'acdeg' : 2,
    'acdfg' : 3,
    'bcdf' : 4,
    'abdfg' : 5,
    'abdefg' : 6,
    'acf' : 7,
    'abcdefg' : 8,
    'abcdfg' : 9
}

def aocOne(lines):
    #lines = list(filter(lambda x: x!='|', lines))
    global num_dict
    print(lines)
    count = 0
    print(len(lines))
    for item in lines:
        sorted_item = "".join(sorted(item))
        if len(item) == 7: # 8
            count += 1
        elif len(item) == 4: # 4
            count +=1
        elif len(item) == 2: # 1
            count += 1
        elif len(item) == 3: # 7
            count+= 1
        # for word, value in num_dict.items():
        #     print(sorted_item, word, value)
        #     if word == sorted_item and int(value)==1:
        #         count+=1
        #     if word == sorted_item and int(value)==4:
        #         count+=1
        #     if word == sorted_item and int(value)==7:
        #         count+=1
        #     if word == sorted_item and int(value)==8:
                # count+=1

    return count

print(aocOne(parseFile(sys.argv[1])))

# create dict
# get 4 items
# for each item
# check lengths first, if so then either 1 4 7 8
# otherwise sort item, check it against every dict
# if we get a dict match, get value
# put values in a list and make a number
# then add that number to a total sum


##
# For 6-length numbers:
# 0 is the number whose only missing segment exists in all three of the 5-length numbers
# 6 is the number whose only missing segment exists in exactly two of the 5-length numbers
# 9 is the number whose only missing segment exists in exactly one of the 5-length numbers

# For 5-length numbers:
# 2 is the number that contains the missing segment of 9
# 3 is the number that is not 2 and contains the missing segment of 6
# 5 is the only number left