def part1():

    win = {
        "A" : "Y",
        "B" : "Z",
        "C" : "X",
    }


    W = ord("W")



    with open('day2data') as file:
        score = 0
        for line in file:
            theirs, mine = line.strip("\n").split(" ")
            curr = 0

            print(theirs)

            if((ord("Z") - ord(mine)) - (ord("C") - ord(theirs)) == 0):
                print("tie")
                curr += 3
            elif(win[theirs] == mine):
                print("win")
                curr += 6
            else:
                print("lose")
            curr += ord(mine) - W
            score += curr
        print(score)

def part2():

    win = {
        "A" : "Y",
        "B" : "Z",
        "C" : "X",
    }

    lose = {
        "A": "Z",
        "B": "X",
        "C": "Y"
    }

    tie = {
        "A": "X",
        "B": "Y",
        "C": "Z"
    }


    W = ord("W")



    with open('day2data') as file:
        score = 0
        for line in file:
            theirs, winOrLose = line.strip("\n").split(" ")
            curr = 0

            mine = ""
            if(winOrLose == "Z"): #WIN
                mine = win[theirs]
                curr += 6
            elif(winOrLose == "X"): #LOSE
                mine = lose[theirs]
            else: #TIE
                mine = tie[theirs]
                curr += 3

            curr += ord(mine) - W
            score += curr
        print(score)

part2()