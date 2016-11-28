"""
1.6 Given an image represented by an NxN matrix, where each pixel in the image is
4 bytes, write a method to rotate the image by 90 degrees. Can you do this in 
place?
"""

N3 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

N4 = [
    ['a', 'b', 'c', 'd'],
    ['e', 'f', 'g', 'h'],
    ['i', 'j', 'k', 'l'],
    ['m', 'n', 'o', 'p']
]

N5 = [
    ['a', 'b', 'c', 'd', 'e'],
    ['f', 'g', 'h', 'i', 'j'],
    ['k', 'l', 'm', 'n', 'o'],
    ['p', 'q', 'r', 's', 't'],
    ['u', 'v', 'w', 'x', 'y']
]


def rotate_left(matrix):
    N = len(matrix)
    max_index = N - 1
    j = 0
    while j < N/2:
        i = j
        while i < max_index - j:
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][max_index - i]
            matrix[j][max_index - i] = matrix[max_index - i][max_index - j]
            matrix[max_index - i][max_index - j] = matrix[max_index - j][i]
            matrix[max_index - j][i] = temp
            i += 1
        j += 1
    return


def rotate_right(matrix):
    N = len(matrix)
    max_index = N - 1
    i = 0
    while i < N/2:
        j = i
        while j < max_index - i:
            temp = matrix[i][j]
            matrix[i][j] = matrix[max_index - j][i]
            matrix[max_index - j][i] = matrix[max_index - i][max_index - j]
            matrix[max_index - i][max_index - j] = matrix[j][max_index - i]
            matrix[j][max_index - i] = temp
            j += 1
        i += 1
    return


def print_matrix(matrix):
    for row in matrix:
        print " ".join([str(n) for n in row])
    return

