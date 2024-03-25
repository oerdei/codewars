def shortcut( s ):
    st = ""
    for char in s:
        if char != "a" and char != "e" and char != "i" and char != "o" and char != "u":
            st = st + char
    return st
    
    
    
s = "codewars"
print(shortcut(s))
