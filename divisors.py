def divisors(n):
    x = 1
    for i in range(1,n):
        if n % i == 0:
            x=x+1
    return x

print(divisors(30))