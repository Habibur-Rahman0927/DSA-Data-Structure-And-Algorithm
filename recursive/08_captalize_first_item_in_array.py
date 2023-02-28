# captalize first item in array

def captalize_first_item_in_array(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + captalize_first_item_in_array(arr[1:])


print(captalize_first_item_in_array(['car', 'taco', 'banana'])) # ['Car','Taco','Banana']