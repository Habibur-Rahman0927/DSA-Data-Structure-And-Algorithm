# product of array

def product_of_array(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * product_of_array(arr[1:])


# print(product_of_array([1, 2, 3]))  # 6
print(product_of_array([1, 2, 3, 10]))  # 60

# arra = [1,2,3,10]

# print(arra[2:])
