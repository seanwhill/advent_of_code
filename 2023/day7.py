from collections import defaultdict
# def sol1():
#     res = 0
#     with open('day7Data') as file:
#         data = file.read()
#         time, distance = data.split("\n")

            
#     return res

def checkCardValue(cards):
    dct = defaultdict(int)

    val = 0
    for card in cards:
        dct[card] += 1

    print(dct)
    for card, card_val in dct.items():

        if(card_val) == 5:
            val = max(val, 7)
        elif(card_val) == 4:
            val = max(val, 6)
        elif(card_val) == 3: #CHECK FULL HOUSE
            for k, v in dct.items():
                if k != card and v == 2:
                    val = max(val, 5)
                else: #If it's not a full house than it's 3 of a kind
                    val = max(val, 4)
        elif(card_val) == 2:
            #Check 2 pair
            found2 = False
            found1= False
            valid1Pair = True
            for k, v in dct.items():
                if k != card and v == 2:
                    valid1Pair = False
                    found2 = True
                if k != card and v == 1:
                    found1 = True
            if(found1 and found2): #2 pair
                val = max(val, 3)
            else: #CHECK 1 Pair
                if(valid1Pair):
                    val = max(val, 2)
        else:
            val = max(val ,1)
    return val


def calculate_strength_part_1(char):
    character_strengths = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}
    return character_strengths.get(char, 0)

def sort_strings_by_strength(arr):
    return sorted(arr, key=lambda s: [calculate_strength_part_1(char) for char in s[0]], reverse=False)


# Example usage:
# strings_array = ["KQJ", "T987", "A54", "23"]
# sorted_array = sort_strings_by_strength(strings_array)
# print(sorted_array)

def sol1():
    res = 0
    with open('day7Data') as file:
        rankings = [ [] for i in range(7)]
        # print(rankings)
        for line in file:
            cards, bid = line.strip().split(" ")
            val = checkCardValue(cards)

            rankings[val - 1].append((cards, bid))
        
        for i in range(len(rankings)):
            rankings[i] = sort_strings_by_strength(rankings[i])

        res = 0
        rank = 1
        for r in rankings:
            for cards, bid in r:
                print(f"bid {bid} times rank {rank}")
                res += int(bid) * rank
                rank += 1
        
    return res

# print(sol1())


# QJJJJ 7
# QJJJT 6
# QJQTT 5
# QJQ3T 4
# 23432 3
# J1234 2
# JJ234 3

def checkCardValue_2(cards):
    dct = defaultdict(int)

    val = 0
    for card in cards:
        dct[card] += 1

    for card, card_val in dct.items():

        if(card_val) == 5 or (card != 'J' and card_val + dct.get('J', 0) == 5):
            val = max(val, 7)
        elif(card_val) == 4 or (card != 'J' and card_val + dct.get('J', 0) == 4):
            val = max(val, 6)
        elif(card_val) == 3 or (card != 'J' and card_val + dct.get('J', 0) == 3): #CHECK FULL HOUSE
            isJ = False
            if(card_val != 3 and card_val + dct.get('J', 0) == 3):
                isJ = True
            for k, v in dct.items():
                if k != card and (v == 2 and not (k == 'J' and isJ)) :
                    val = max(val, 5)
                else: #If it's not a full house than it's 3 of a kind
                    val = max(val, 4)
        elif(card_val) == 2 or (card != 'J' and card_val + dct.get('J', 0) == 2):
            #Check 2 pair
            found2 = False
            found1= False
            valid1Pair = True
            for k, v in dct.items():
                if k != card and v == 2:
                    valid1Pair = False
                    found2 = True
                if k != card and v == 1:
                    found1 = True
            if(found1 and found2): #2 pair
                val = max(val, 3)
            else: #CHECK 1 Pair
                if(valid1Pair):
                    val = max(val, 2)
        else:
            val = max(val ,1)
    return val


def calculate_strength_2(char):
    character_strengths = {'A': 13, 'K': 12, 'Q': 11, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1, 'J': 0}
    return character_strengths.get(char, 0)

def custom_key(item):
    string_value, numeric_value = item
    return [calculate_strength_2(char) for char in string_value]

def sort_tuples_by_strength(tuples_list):
    return sorted(tuples_list, key=custom_key)

# Example usage:
input_tuples = [('QQQJA', '483'), ('T55J5', '684'), ('KTJJT', '220')]
sorted_tuples = sort_tuples_by_strength(input_tuples)
print(sorted_tuples)

# Example usage:
# strings_array = ["KQJ", "T987", "A54", "23"]
# sorted_array = sort_strings_by_strength(strings_array)
# print(sorted_array)

def sol2():
    res = 0
    with open('day7Data') as file:
        rankings = [ [] for i in range(7)]
        # print(rankings)
        for line in file:
            cards, bid = line.strip().split(" ")
            val = checkCardValue_2(cards)
            print(val)

            rankings[val - 1].append((cards, bid))
        
        for i in range(len(rankings)):
            rankings[i] = sort_tuples_by_strength(rankings[i])


        print(rankings)
        res = 0
        rank = 1
        for r in rankings:
            for cards, bid in r:
                print(f"bid {bid} times rank {rank}")
                res += int(bid) * rank
                rank += 1
        
    return res

print(sol2())


# 249114007
248909434