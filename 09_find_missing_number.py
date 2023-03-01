# find the missing number

my_list = [1, 2, 3, 4, 5, 6, 7, 9, 10]


def find_missing_number(list, n):
    # formula 1+2+3+4+.......+n = n(n+1)/2
    sum1 = n*(n+1)/2
    # print(sum1)
    sum2 = sum(list)
    # print(sum2)
    print(sum1 - sum2)



find_missing_number(my_list, 10)
