"""
CTCI 5th Edition
Chapter 2 - Linked Lists
Problem 4: 
	Write code to partition a linked list around a value x, such that all nodes less than x 
	come before all nodes greater than or equal to x.
"""
import LinkedList as ll

def solution1(head, x):
	ltlist = []
	gtlist = []
	curr = head
	while curr != None:
		if curr.data < x:
			ltlist.append(curr)
		else:
			gtlist.append(curr)
		curr = curr.next

	ltfront = ltlist[0]
	prev = ltfront
	for node in ltlist[1:]:
		prev.next = node
		prev = node
	ltend = prev

	gtfront = gtlist[0]
	prev = gtfront
	for node in gtlist[1:]:
		prev.next = node
		prev = node
	gtend = prev
	gtend.next = None

	ltend.next = gtfront
	return ltfront

if __name__ == '__main__':
	l = [1, 3, 2, 7,4, 8, 2, 3]
	x = 6

	head = ll.LLfromList(l)
	new_head = solution1(head, x)
	assert ll.LLtoList(new_head) == [1, 3, 2, 4, 2, 3, 7, 8]
