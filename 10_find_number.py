my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_array)


def find_number(array, number):
    for i in range(len(array)):
        if array[i] == number:
            print(i)
    # another way find number.
    if number in my_array:
        print(number)



find_number(my_array, 10)
