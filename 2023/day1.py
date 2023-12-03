import heapq


substrings = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
} 

substrings_rev = {'eno': '1', 'owt': '2', 'eerht': '3', 'ruof': '4', 'evif': '5', 'xis': '6', 'neves': '7', 'thgie': '8', 'enin': '9'}


def find_first_occurrence(main_string, substrings):
    for substring in substrings:
        index = main_string.find(substring)
        if index != -1:
            return substring, index
    return None, -1

# abcone    12

# one -> abc == one?
#three -> abcon == three?
# ...
# nine ..

# one -> bco == one 

def sol():
    
    sum = 0
    with open('day1Data') as file:
        for line in file:
            val = ''
            curr = ""
            for c in line:
                curr += c
                if c.isnumeric():
                    val = c
                    break
                else:
                    result, index = find_first_occurrence(curr, substrings.keys())
                    if result:
                        val = substrings[result]
                        break
            curr = ""                   
            for c in line[::-1]:
                curr += c
                if c.isnumeric():
                    val += c
                    break
                else:
                    result, index = find_first_occurrence(curr, substrings_rev.keys())
                    if result:
                        val += substrings_rev[result]
                        break

            sum += int(val)
    return sum

print(sol())