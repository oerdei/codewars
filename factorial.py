def factorial(n):
    if n > 0 and n < 12:
        if n == 0:
            return 1
        else:
            i = 1
            s = 1
            while i <= n:
                s = s * (s + 1)
                i = i + 1
            return s
    else:
        return ValueError
                
n = 5
print(factorial(n))
