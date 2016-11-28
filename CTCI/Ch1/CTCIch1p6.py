
"""
Cracking the Coding Interview 5th Edition
Chapter 1 - Arrays and Strings
Problem 1.6: 
Given an image represented by an NxN matrix, where each pixel in the image is 
4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""

def print_matrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			print matrix[i][j],
		print ""

def solution(matrix):
	N = len(matrix)
	for layer in range(N/2 + 1):
		print "\nlayer: " + str(layer)
		first = layer
		last = N - 1 - layer
		print "first: " + str(first)
		print "last: " + str(last)

		for i in range(last - first):
			print "i " + str(i+1)
			temp = matrix[first + i][last]

			matrix[first + i][last] = matrix[first][first + i]

			matrix[first][first + i] = matrix[last - i][first]

			matrix[last - i][first] = matrix[last][last - i]

			matrix[last][last - i] = temp

	print_matrix(matrix)

if __name__ == '__main__':
	# mat = [[1,2,3], [4,5,6], [7,8,9]]
	# mat = [
	# 	["a", "b", "c", "d"], 
	# 	["e", "f", "g", "h"], 
	# 	["i", "j", "k", "l"],
	# 	["m", "n", "o", "p"]
	# ] 
	mat = [
		['a', 'b', 'c', 'd', 'e'],
		['f', 'g', 'h', 'i', 'j'],
		['k', 'l', 'm', 'n', 'o'],
		['p', 'q', 'r', 's', 't'],
		['u', 'v', 'w', 'x', 'y']
	]
	solution(mat)