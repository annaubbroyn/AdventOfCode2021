f = open("input.txt","r")

array = []
length = 0
sum1 = 0; sum2 = 0
count = 0

for line in f:
    array.append(int(line))
    length += 1

for i in range(length - 3):
    sum1 = int(array[i]) + int(array[i+1]) + int(array[i+2])
    sum2 = int(array[i+1]) + int(array[i+2]) + int(array[i+3])
    if sum2 > sum1:
        count += 1

print(count)
    