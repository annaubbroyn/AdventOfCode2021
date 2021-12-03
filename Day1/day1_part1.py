f = open("input.txt","r")
count = 0
previous_depth = 9999999
for line in f:
    current_depth = int(line)
    if current_depth > previous_depth:
        count += 1
    previous_depth = current_depth
print(count)