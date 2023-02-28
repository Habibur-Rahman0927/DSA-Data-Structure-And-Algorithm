
def recursiveMethod(n):
    if n < 1:
        print('N Is less than 1')
    else:
        recursiveMethod(n - 1)
        print(n)

recursiveMethod(4)

def factorial_using_while(n):
    num = 1
    while n >= 1:
        num = n * num
        n = n - 1
    return num

print(factorial_using_while(4))



def fibonacci(n):
    assert n >= 0 and int(n) == n, 'Fibonacci number can\'t be negitive or non integer'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(4))


# Taking user input for the position of the number in the series
n = int(input("Enter the position of the number in the Fibonacci series: "))

# Initializing the first two terms of the series
a, b = 0, 1

# Generating the required term of the series using a loop
for i in range(2, n+1):
    c = a + b
    a = b
    b = c

# Printing the required term of the series
print(f"The {n}th number in the Fibonacci series is {b}")