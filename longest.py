def longest(a1, a2):
    unique_letters_set = set(a1 + a2)
    return ''.join(sorted(unique_letters_set))
    
    
a1 = "xyaabbbccccdefww"
a2 = "xxxxyyyyabklmopq"
print(longest(a1, a2))