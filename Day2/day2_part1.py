f = open("input.txt","r")

horizontal = 0
depth = 0

for line in f:
    array = line.split()
    command = array[0]
    x = int(array[1])
    if command == "forward":
        horizontal += x
    elif command == "down":
        depth += x
    elif command == "up":
        depth -= x

print(horizontal*depth)
