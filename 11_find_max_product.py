# How to find maximum product of two integers in the array where all elements are positive 

my_array = [1, 20, 30 , 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]

def find_max_product(array):
    max_product = 0
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] * array[j] > max_product:
                max_product = array[i] * array[j]
                pairs = str(array[i]) + ","+str(array[j])
    print(pairs)
    print(max_product)


find_max_product(my_array)