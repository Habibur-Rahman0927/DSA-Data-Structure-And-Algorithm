def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))


def fibonacci1(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a 

print(fibonacci1(10))

# https://technobeans.com/2012/04/16/5-ways-of-fibonacci-in-python/