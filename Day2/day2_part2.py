f = open("input.txt","r")

horizontal = 0
depth = 0
aim = 0

for line in f:
    array = line.split()
    command = array[0]
    x = int(array[1])
    if command == "forward":
        horizontal += x
        depth += aim * x
    elif command == "down":
        aim += x
    elif command == "up":
        aim -= x

print(horizontal*depth)
