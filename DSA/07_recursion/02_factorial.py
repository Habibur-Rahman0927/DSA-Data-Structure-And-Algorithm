import time
start_time = time.time()
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(4))

print("Total Running time = {:.5f} seconds".format(time.time() - start_time))

