# flatten solution

def flatten(arr):
    resultArr = []
    # print(type(resultArr))
    for custItem in arr:
        if type(custItem) is list:
            # print(type(custItem))
            # print(list)
            resultArr.extend(flatten(custItem))
        else:
            resultArr.append(custItem)
    return resultArr

print(flatten([1, 2, 3, [4, 5]])) # [1, 2, 3, 4, 5]
# print(flatten([1, [2, [3, 4], [[5]]]])) # [1, 2, 3, 4, 5]
# print(flatten([[1], [2], [3]])) # [1, 2, 3]
# print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])) # [1, 2, 3]



# print(flatten([1, 2, 3,]))
