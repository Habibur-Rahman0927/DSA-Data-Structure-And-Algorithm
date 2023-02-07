# Python If-Else

# Task
# Given an integer, n, perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# Input Format
# A single line containing a positive integer, n.

# Constraints
# 1 <= n <= 100

# Output Format
# Print Weird if the number is weird; otherwise, print Not Weird.

n = int(input().strip())
if n % 2 != 0:
        print('Weird')
else:
    if n >=2 and n <=5:
        print('Not Weird')
    elif n >= 6 and n <=20:
        print('Weird')
    elif n >= 20:
        print('Not Weird')


m = int(input())
for i in range(m):print(i+1, end="")

for i in range(1,int(input())): print(pow(10, i)//9 * i)