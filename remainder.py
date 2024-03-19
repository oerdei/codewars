def remainder(a,b):
    if a == 0 or b == 0:
        return ""
    else:
        return max(a,b) % min(a,b)
        
print(remainder(5, 17))

