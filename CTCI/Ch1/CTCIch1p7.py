"""
Cracking the Coding Interview 5th Edition
Chapter 1 - Arrays and Strings
Problem 7: 
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
"""
def print_matrix(matrix):
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			print str(matrix[row][col]) + ' ',
		print ""
		
def solution(matrix):
	M = len(matrix)
	N = len(matrix[0])
	rowset = set()
	colset = set()

	for row in range(M):
		for col in range(N):
			if matrix[row][col] == 0:
				if row not in rowset:
					rowset.add(row)
				if col not in colset:
					colset.add(col)

	for row in range(M):
		for col in range(N):
			if row in rowset or col in colset:
				matrix[row][col] = 0

	print_matrix(matrix)
