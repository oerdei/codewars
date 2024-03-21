def factorial(n):
    if n > 0 or n < 12:
        try:
            if n == 0:
                return 1
            else:
                i = 1
                while i < n:
                    i = i * (i + 1)
                return i
        except:
            return ValueError
                
n = 5
print(factorial(n))
