import heapq
from collections import defaultdict
import re



def sol():
    
    sum = 0
    with open('day4Data') as file:
        for line in file:
            game, card = line.split(":")
            win, yours = card.split("|")
            winnerSet = set(win.split(" "))

            # print(winnerSet)
            # print(yours)
            yours = yours.split(" ")
            found = False
            inc = 0
            for num in yours:
                num = num.strip()
                if(num.isnumeric() and num in winnerSet):
                    if(inc == 0):
                        inc += 1
                    if (found):
                        inc *= 2
                    found = True

            sum += inc                    

    return sum



def sol2():
    sum = 0
    cardsCanWin = defaultdict(int)
    cardsWon = []
    scoreCards = []

    def calculateCards(card, orig):
        id, winnerSet, yours = card
        print("Caluclating for id: ", id)
        print("Caluclating from original: ", orig)

        if(id in cardsCanWin):
            return cardsCanWin[id]
        
        numCardsWon = 0
        for num in yours:
            num = num.strip()
            if(num.isnumeric() and num in winnerSet):
                numCardsWon += 1
                
        res = numCardsWon
        
        for i in range(1, numCardsWon + 1):
            res += calculateCards(scoreCards[id + i - 1], id)
            print(res)
        
        cardsCanWin[id] = res

        return res
    
    with open('day4Data') as file:
        for line in file:

            game, card = line.split(":")
            win, yours = card.split("|")
            winnerSet = set(win.split(" "))

            regex = re.compile(r'Card *([0-9]*)')
            match = regex.match(game)
            id = int(match.groups()[0])
            yours = yours.split(" ")

            scoreCards.append((id, winnerSet, yours))

        sum = 0
        for idx, card in enumerate(scoreCards):
            sum += 1 + calculateCards(card, idx + 1) # + 1 to include the card itself 


    return sum

print(sol2())