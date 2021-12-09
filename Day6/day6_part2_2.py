f = open("input.txt","r")
fishes = [int(x) for x in (f.readline()).split(',')]

count_fishes = [0 for x in range(9)]

days = 256

for fish in fishes:
    count_fishes[fish]+=1

print(count_fishes)

for day in range(days):
    count_fishes_temp = count_fishes.copy()
    count_zero = count_fishes[0]
    for i in range(len(count_fishes)):
        count_fishes[i-1]=count_fishes_temp[i]
    count_fishes[6] += count_zero
    count_fishes[8] = count_zero

print(sum(count_fishes))