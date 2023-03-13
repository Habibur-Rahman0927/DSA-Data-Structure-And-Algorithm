def sum_func(n):
    
    # Base Case
    if n == 0:
        return n
    else:
        return n % 10 + sum_func(n/10)
    

print(sum_func(12341))
