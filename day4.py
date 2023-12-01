

def part1():
    with open('day4data') as file:
        count = 0
        for line in file:
            p1, p2 = line.split(',')
            p1_num1, p1_num2 = p1.split('-')
            p2_num1, p2_num2 = p2.split('-')


            if(int(p1_num1) <= int(p2_num1) and int(p1_num2) >= int(p2_num2)):        
                count += 1
            elif(int(p2_num1) <= int(p1_num1) and int(p2_num2) >= int(p1_num2)):
                count += 1
            else:
                print("no fit")
        print(count)


def part2():
    with open('day4data') as file:
        count = 0
        for line in file:
            p1, p2 = line.split(',')
            p1_num1, p1_num2 = p1.split('-')
            p2_num1, p2_num2 = p2.split('-')


            if(int(p1_num1) >= int(p2_num1) and int(p1_num1) <= int(p2_num2)):        
                count += 1
            elif(int(p2_num1) >= int(p1_num1) and int(p2_num1) <= int(p1_num2)):
                count += 1
            else:
                print("no fit")
        print(count)

part2()