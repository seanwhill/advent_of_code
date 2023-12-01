data = [
    ['F','C','P','G','Q',"R"],
    ['W','T','C','P'],
    ['B','H','P','M','C',],
    ['L','T','Q','S','M',"P", "R"],
    ['P','H','J','Z','V',"G", "N"],
    ['D','P','J'],
    ['L','G','P','Z','F',"J", "T", "R"],
    ['N','L','H','C','F',"P","T", 'J'],
    ['G','V','Z','Q','H',"T", 'C', 'W']
]

# data = [
#     ['Z','N'],
#     ['M','C','D'],
#     ['P'],
# ]
import re

def part1():
    with open('day5data') as file:
        for line in file:
            move_ins, from_ins, to_ins = list(filter(None,re.split("move ([0-9]+) from (\w) to (\w)", line.strip())))
            amount_to_move = int(move_ins)
            from_ins = int(from_ins) - 1
            to_ins = int(to_ins) - 1

            # append amount_to_move elements from the from_ins to the desired to_ins
            data[to_ins] = data[to_ins] + data[from_ins][-amount_to_move:][::-1]

            # remove amount_to_move elements from the from_ins
            data[from_ins] = data[from_ins][:-amount_to_move]
            # print(data)
        
        res = ''
        for row in data:
            res += row[-1]

    print(res)

def part2():
    with open('day5data') as file:
        for line in file:
            move_ins, from_ins, to_ins = list(filter(None,re.split("move ([0-9]+) from (\w) to (\w)", line.strip())))
            amount_to_move = int(move_ins)
            from_ins = int(from_ins) - 1
            to_ins = int(to_ins) - 1

            # append amount_to_move elements from the from_ins to the desired to_ins
            data[to_ins] = data[to_ins] + data[from_ins][-amount_to_move:]

            # remove amount_to_move elements from the from_ins
            data[from_ins] = data[from_ins][:-amount_to_move]
            # print(data)
        
        res = ''
        for row in data:
            res += row[-1]

    print(res)
part2()