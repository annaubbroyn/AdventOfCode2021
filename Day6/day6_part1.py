f = open("input.txt","r")
fishes = [int(x) for x in (f.readline()).split(',')]
days = 80

for i in range(days):
    fishes_ = fishes
    for j in range(len(fishes_)):
        if fishes_[j] == 0:
            fishes[j] = 6
            fishes.append(8)
        else:
            fishes[j] -= 1

print(len(fishes))