# capitalize array 


def capitalize_array(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalize_array(arr[1:])

print(capitalize_array(['i', 'am', 'learning', 'recursion']))