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



f = open("input_short.txt","r")
mapping = initial_mapping(original,input)
print(mapping)
#print(final_mapping(mapping,original,input))

