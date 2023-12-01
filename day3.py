
def sol1():

    result = 0
    with open('day3data') as file:
        for line in file:
            line = line.strip()
            size = len(line)
            ruck1 = line[:(size // 2)]
            ruck2 = line[(size // 2):]

            set1 = set()
            for char in ruck1:
                set1.add(char)
            for char in ruck2:
                if(char in set1):
                    if(char.isupper()):
                        result += ord(char) - ord('A') + 27
                    else:
                        result += ord(char) - ord('a') + 1
                    break
                    
    
    print(result)

def sol2():

    result = 0
    with open('day3data') as file:
        groupCount = 0
        sets = []
        for line in file:
            groupCount += 1
            line = line.strip()

            set1 = set()
            for char in line:
                set1.add(char)

            sets.append(set1)
            if(groupCount == 3):
                for char in set1:
                    if char in sets[0] and char in sets[1]:
                        if(char.isupper()):
                            result += ord(char) - ord('A') + 27
                        else:
                            result += ord(char) - ord('a') + 1
                        break
                groupCount = 0
                sets = []
    
    print(result)

# sol1()
sol2()