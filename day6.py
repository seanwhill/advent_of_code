
from collections import deque

def part1():
    with open('day6data') as file:
        datastream = file.readline()
        for i in range(len(datastream)):
            char_set = set(datastream[i:i+14])
            print(char_set)
            if len(char_set) == 14:
                print(i+14)
                break

part1()