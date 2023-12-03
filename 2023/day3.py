import heapq
from collections import defaultdict 


directions = [[0, -1], [-1, -1], [-1, 0], [0, 1], [1, 1], [1, 0], [-1, 1], [1, -1]]

nums = []

def sol():
    sum = 0
    with open('day3Data') as file:
        lines = []
        for line in file:
            lines.append(line)

        for i in range(len(lines)):
            num = ""
            validNum = False
            for j in range(len(lines[i])):
                if not lines[i][j].isnumeric():
                    if(validNum):
                        nums.append(int(num))
                        sum += int(num)
                    validNum = False
                    num = ""
                if lines[i][j].isnumeric():
                    num += lines[i][j]
                    for row, col in directions:
                        if(i + row >= 0 and i + row < len(lines) - 1 and j + col >= 0 and j + col < len(lines[i]) - 1):
                           if not lines[i + row][j + col].isnumeric() and lines[i + row][j + col] != ".":
                               print(num)
                               print(row, col)
                               validNum = True
        
    return sum

def sol2():
    gears = defaultdict(list) 
    with open('day3Data') as file:
        lines = []
        for line in file:
            lines.append(line)

        for i in range(len(lines)):
            num = ""
            currGears = set()
            validNum = False
            for j in range(len(lines[i])):
                if not lines[i][j].isnumeric():
                    if(validNum):
                        for gear in currGears:
                            gears[gear].append(num)
                    validNum = False
                    num = ""
                    currGears = set()
                if lines[i][j].isnumeric():
                    num += lines[i][j]
                    for row, col in directions:
                        if(i + row >= 0 and i + row < len(lines) - 1 and j + col >= 0 and j + col < len(lines[i]) - 1):
                           if lines[i + row][j + col] == "*" and lines[i + row][j + col] != ".":
                               currGears.add((i + row, j + col))
                               validNum = True
    
    print(gears)
    sum = 0
    for k, v in gears.items():
        print(k)
        print(v)
        mul = 0
        if len(v) >= 2:
            mul = 1
            for val in v:
                print(val)
                mul *= int(val)
        sum += mul
    return sum


print(sol2())
