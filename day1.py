import heapq

def sol(capacity):
    with open('day1Data') as file:
        maxCal = 0
        curr = 0
        h = []
        for line in file:
            
            if("\n" == line):
                heapq.heappush(h, -curr)
                curr = 0
            else:
                curr += int(line)

    return abs(heapq.heappop(h)) + abs(heapq.heappop(h)) + abs(heapq.heappop(h))

print(sol(3))