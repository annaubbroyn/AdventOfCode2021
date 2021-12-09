f = open("input.txt","r")
count = 0
for line in f:
    output = (line.split('|')[1]).split()
    for digit in output:
        length = len(digit)
        if length == 2 or length == 4 or length == 3 or length == 7:
            count += 1

print(count)