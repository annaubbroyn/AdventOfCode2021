f = open("input.txt","r")
length = 12
count1 = [0]*length
count0 = [0]*length
gamma_rate = [0]*length
epsilon_rate = [0]*length

for line in f:
    for i in range (length):
        x = int(line[i])
        if x == 1:
            count1[i] += 1
        else:
            count0[i] += 1


for i in range (length):
    if count1[i]>count0[i]:
        gamma_rate[i] = 1
        epsilon_rate[i] = 0
    else:
        gamma_rate[i] = 0
        epsilon_rate[i] = 1

gamma_rate_decimal = int("".join(str(x) for x in gamma_rate), 2)
epsilon_rate_decimal = int("".join(str(x) for x in epsilon_rate), 2)

print(gamma_rate_decimal*epsilon_rate_decimal)