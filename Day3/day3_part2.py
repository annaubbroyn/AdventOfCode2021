def addFileToArray(filename):
    f = open(filename,"r")
    array = []
    for line in f:
        linearray = []
        for i in range(len(line)-1):
            linearray.append(int(line[i]))
        array.append(linearray)
    return array

def getValidBit(array, pos):
    count0 = 0
    count1 = 0
    for i in range(len(array)):
        if array[i][pos] == 0:
            count0 += 1
        else:
            count1 += 1
    if count0 > count1:
        return 0
    elif count1 > count0:
        return 1
    else:
        return -1
    
def OxygenGenerator(array,pos):
    length = len(array)
    if length == 1:
        return array
    valid_bit = getValidBit(array,pos)
    if valid_bit == -1:
        valid_bit = 1
    new_array = []
    for i in range(length):
        if array[i][pos]==valid_bit:
            new_array.append(array[i])
    return OxygenGenerator(new_array,pos+1)

def CO2Generator(array,pos):
    length = len(array)
    if length == 1:
        return array
    valid_bit = getValidBit(array,pos)
    if valid_bit == -1:
        valid_bit = 1
    new_array = []
    for i in range(length):
        if array[i][pos]!=valid_bit:
            new_array.append(array[i])
    return CO2Generator(new_array,pos+1)

array = addFileToArray("input.txt")
oxygen_generator = OxygenGenerator(array,0)
oxygen_generator_decimal = int("".join(str(x) for x in oxygen_generator[0]), 2)
co2_generator = CO2Generator(array,0)
co2_generator_decimal = int("".join(str(x) for x in co2_generator[0]), 2)

print(oxygen_generator_decimal*co2_generator_decimal)