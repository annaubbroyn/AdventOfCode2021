#mapping = ['abcdeg','ab','acdfg','abcdf','abef','bcdef','bcdefg','abd','abcdefg','abcdef']

original = ['abcefg','cf','acdeg','acdfg','bcdf','abdfg','abdefg','acf','abcdefg','abcdfg']
input = ['acedgfb','cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']

mapping = { 
    "a": {'a','b','c','d','e','f','g'},
    "b": {'a','b','c','d','e','f','g'},
    "c": {'a','b','c','d','e','f','g'},
    "d": {'a','b','c','d','e','f','g'},
    "e": {'a','b','c','d','e','f','g'},
    "f": {'a','b','c','d','e','f','g'},
    "g": {'a','b','c','d','e','f','g'}
}

def initial_mapping(original,input):
    mapping = {"a": set(), "b": set(), "c": set(), "d": set(), "e": set(), "f": set(), "g": set()}
    invalid_segments = set()
    for digit in input:
        if len(digit) == 2:
            for x in digit:
                mapping['c'].add(x)
                mapping['f'].add(x)
                invalid_segments.add(x)
            break
    for digit in input:
        if len(digit) == 3:
            for x in digit:
                if x not in invalid_segments:
                    mapping['a'].add(x)
                    invalid_segments.add(x)
            break
    for digit in input:
        if len(digit) == 4:
            for x in digit:
                if x not in invalid_segments:
                    mapping['b'].add(x)
                    mapping['d'].add(x)
                    invalid_segments.add(x)
            break
    for digit in input:
        if len(digit) == 7:
            for x in digit:
                if x not in invalid_segments:
                    mapping['e'].add(x)
                    mapping['g'].add(x)
                    invalid_segments.add(x)
            break
    return mapping

def find0(original,mapping,input):
    candidates = []
    for digit in input:
        if len(digit) == 6:
            candidates.append(digit)
    for digit in candidates:
        if list(mapping['c'])[0] in digit and list(mapping['c'])[1] in digit and list(mapping['e'])[0] in digit and list(mapping['e'])[1] in digit:
            return ''.join(sorted(digit))
    return None

def find1(original,mapping,input):
    for digit in input:
        if len(digit) == 2:
            return ''.join(sorted(digit))
    return None        

def find2(original,mapping,input):
    candidates = []
    for digit in input:
        if len(digit) == 5:
            candidates.append(digit)
    for digit in candidates:
        if list(mapping['e'])[0] in digit and list(mapping['e'])[1] in digit:
            return ''.join(sorted(digit))
    return None

def find3(original,mapping,input):
    candidates = []
    for digit in input:
        if len(digit) == 5:
            candidates.append(digit)
    for digit in candidates:
        if list(mapping['c'])[0] in digit and list(mapping['c'])[1] in digit:
            return ''.join(sorted(digit))
    return None

def find4(original,mapping,input):
    for digit in input:
        if len(digit) == 4:
            return ''.join(sorted(digit))
    return None

def find5(original,mapping,input):
    candidates = []
    for digit in input:
        if len(digit) == 5:
            candidates.append(digit)
    for digit in candidates:
        if list(mapping['b'])[0] in digit and list(mapping['b'])[1] in digit:
            return ''.join(sorted(digit))
    return None

def find6(original,mapping,input):
    candidates = []
    for digit in input:
        if len(digit) == 6:
            candidates.append(digit)
    for digit in candidates:
        if list(mapping['b'])[0] in digit and list(mapping['b'])[1] in digit and list(mapping['e'])[0] in digit and list(mapping['e'])[1] in digit:
            return ''.join(sorted(digit))
    return None

def find7(original,mapping,input):
    for digit in input:
        if len(digit) == 3:
            return ''.join(sorted(digit))
    return None

def find8(original,mapping,input):
    for digit in input:
        if len(digit) == 7:
            return ''.join(sorted(digit))
    return None

def find9(original,mapping,input):
    candidates = []
    for digit in input:
        if len(digit) == 6:
            candidates.append(digit)
    for digit in candidates:
        if list(mapping['b'])[0] in digit and list(mapping['b'])[1] in digit and list(mapping['c'])[0] in digit and list(mapping['c'])[1] in digit:
            return ''.join(sorted(digit))
    return None

f = open("input.txt","r")
mapping = initial_mapping(original,input)
#print(mapping)
#print(find9(original,mapping,input))

sum = 0
for line in f:
    input = (line.split('|')[0]).split()
    output = (line.split('|')[1]).split()
    mapping = initial_mapping(original,input)
    digit_mapping = []
    digit_mapping.append(find0(original,mapping,input))
    digit_mapping.append(find1(original,mapping,input))
    digit_mapping.append(find2(original,mapping,input))
    digit_mapping.append(find3(original,mapping,input))
    digit_mapping.append(find4(original,mapping,input))
    digit_mapping.append(find5(original,mapping,input))
    digit_mapping.append(find6(original,mapping,input))
    digit_mapping.append(find7(original,mapping,input))
    digit_mapping.append(find8(original,mapping,input))
    digit_mapping.append(find9(original,mapping,input))
    #print(digit_mapping)
    #for o in output:
    #    print(o)
    #    print(digit_mapping.index(''.join(sorted(o))))
    #    part_sum
    #print('\n')
    part_sum = digit_mapping.index(''.join(sorted(output[0])))*1000 + digit_mapping.index(''.join(sorted(output[1])))*100 + digit_mapping.index(''.join(sorted(output[2])))*10 + digit_mapping.index(''.join(sorted(output[3])))
    #print(part_sum)
    sum += part_sum

print(sum)





