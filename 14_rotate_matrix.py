# rotate matrix

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def rotate_matrix(matrix):
    n = len(matrix)
    # print(n//2)
    for layer in range(n//2):
        first = layer
        last = n - layer -1
        # print(last)
        for i in range(first, last):
            # save top element
            top = matrix[layer][i]
            # move left element to top
            matrix[layer][i] = matrix[-i-1][layer]
            # move bottom element to left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            # move right to bottom
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            # move to right
            matrix[i][-layer-1] = top
            # print(matrix[-layer-1][-i-1])
    return matrix


print(rotate_matrix(my_list))
