f = open("input_short.txt","r")
fishes = [int(x) for x in (f.readline()).split(',')]

def contribution(number,days_left):
    print("number: " + str(number))
    print("days left: " + str(days_left))
    if days_left == 0 and number == 8:
        return 1
    if days_left <= 0:
        return 0
    if number == 8:
        return 1 + contribution(6,days_left-number-1)+contribution(8,days_left-number-1)
    return contribution(6,days_left-number-1)+contribution(8,days_left-number-1)


result = len(fishes)
for i in range(len(fishes)):
    print('\n',end = '')
    print(i)
    result += contribution(fishes[i],18)
print(result)


"""
0: (3)(4)(3)(1)(2)
1: (2)(3)(2)(0)(1)
2: (1)(2)(1)(68)(0)
3: (0)(1)(0)(57)(68)
4: (68)(1)(68)(46)(57)
5: (57)(0)(57)(35)(46)
6: (46)(68)(46)(24)(35)
"""

#8->6,8 (9)
#7->6,8 (8)
#6->6,8 (7)
#5->6,8 (6)
#4->6,8 (5)
#3->6,6 (4)
#2->6,8 (3)
#1->6,8 (2)
#0->6,8 (1)
"""
0- 3
1- 2
2- 1
3- 0
4- 68
5- 57
6- 46
7- 35
8- 24
9- 13
10-02
11-618
12-507
13-4668
14-3557
15-2446
16-1335
17-0224
18-61138
"""