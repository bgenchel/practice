"""
CTCI 5th edition
Chapter 2 - Linked Lists
Problem 2:
	Implement an algorithm to find the kth to last element of a singly linked list.
"""
import LinkedList as ll
import random as r

#this solution is iterative, and the most clever of those 
#listed in the book. O(N)
def solution1(head, k):
	ptr1 = head
	ptr2 = head
	for _ in range(k):
		if ptr1 != None:
			ptr1 = ptr1.next
		else:
			return None

	while ptr1 != None:
		ptr1 = ptr1.next
		ptr2 = ptr2.next

	return ptr2.data

#recursive; kind of weird because you need to pass an object and a counter
#back through the recursion; O(N) space for N stacks, O(N) time
def solution2(head, k):
	def recurse(head, k):
		if head.next != None:
			(count, data) = recurse(head.next, k)
		else:
			return (0, head.data)

		if count == k:
			return (count, data)
		else:
			count += 1
			return (count, head.data)

	(_, kth) = recurse(head, k)
	return kth

if __name__ == '__main__':
	length = r.choice(range(100))
	k = r.choice(range(length))

	l = range(length)
	head = ll.LLfromList(l)
	kth = solution1(head, k)
	assert kth == l[-k]

	kth = solution2(head, k)
	assert kth == l[-(k+1)]


