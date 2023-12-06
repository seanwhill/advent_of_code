def calc_distance(button_held_down, time):
    return (time - button_held_down) * button_held_down

def sol1():
    res = 0
    with open('day6Data') as file:
        data = file.read()
        time, distance = data.split("\n")
    
    times = time.split(":")[1].split()
    distances = distance.split(":")[1].split()

    print(times)
    print(distances)

    
    res = 1
    for i in range(len(times)):
        time = int(times[i])
        distance = int(distances[i])
        count = 0

        for i in range(0, time):
            distanceTraveled = calc_distance(i, time)
            if(distanceTraveled > distance):
                count += 1
        
        print( count)
        res *= count
    


            
    return res

def sol2():
    res = 0
    with open('day6Data') as file:
        data = file.read()
        time, distance = data.split("\n")
    
    time = int(''.join(time.split(":")[1].split()))
    distance = int(''.join(distance.split(":")[1].split()))

    print(time)
    print(distance)

    
    count = 0

    for i in range(0, time):
        distanceTraveled = calc_distance(i, time)
        if(distanceTraveled > distance):
            count += 1
    
    print( count)
    

            
    return count

print(sol2())