from functools import reduce

def sol():
    max_dice = {
        'red':12,
        'green':13,
        'blue':14
    }
    
    with open('day2Data') as file:
        sum = 0
        for line in file:
            line = line.strip()
            gameID, games_iteration = line.split(":")
            id = int(gameID.split(" ")[1])
            each_game = games_iteration.split(";")
            valid = True;
            for  idx, game in enumerate(each_game):
                count = {}
                cubes = game.split(",")
                for cube in cubes:
                    _, amt, color = cube.split(" ")
                    # count[color] = count.get(color, 0) + int(amt)
                
                    if int(amt) > max_dice[color]:
                        valid = False 

            if(valid):
                sum += id
                
        
            


    return sum

def sol2():
    
    
    with open('day2Data') as file:
        sum = 0

        for line in file:
            max_dice = {
                'red':0,
                'green':0,
                'blue':0
            }
            line = line.strip()
            gameID, games_iteration = line.split(":")
            id = int(gameID.split(" ")[1])
            each_game = games_iteration.split(";")
            valid = True;
            for  idx, game in enumerate(each_game):
                count = {}
                cubes = game.split(",")
                for cube in cubes:
                    _, amt, color = cube.split(" ")
                    # count[color] = count.get(color, 0) + int(amt)
                
                    
                    if int(amt) > max_dice[color]:
                        max_dice[color] = int(amt)
                        

            
            sum += reduce(lambda x, y: x*y, max_dice.values())
                
    


    return sum
    


print(sol())
print(sol2())


