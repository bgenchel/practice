"""
CTCI 5th Edition
Chapter 2 - Linked Lists
Problem 1: 
	Write code to remove duplicates from an unsorted linked list.
	FOLLOW UP
	How would you solve this problem if a temporary buffer is not allowed?
"""
import LinkedList as ll

#using a buffer, this solution is O(N)
def solution1(head):
	buff = set()
	curr = head
	prev = None
	while curr != None:
		if curr.data in buff:
			prev.next = curr.next
		else:
			buff.add(curr.data)
			prev = curr
		curr = curr.next

	return head

# without a buffer, this solution is O(N^2)
def solution2(head):
	curr = head
	while curr != None:
		prev = curr
		next = curr.next
		while next != None:
			if next.data == curr.data:
				prev.next = next.next
			else:
				prev = next
			next = next.next
		curr = curr.next

	return head

if __name__ == '__main__':
	duplicates_list = [1, 2, 2, 5, 4, 1, 3, 3]
	head = ll.LLfromList(duplicates_list)
	solution1(head)
	assert ll.LLtoList(head) == [e for i, e in enumerate(duplicates_list) if e not in duplicates_list[:i]]

	head = ll.LLfromList(duplicates_list)
	solution2(head)
	assert ll.LLtoList(head) == [e for i, e in enumerate(duplicates_list) if e not in duplicates_list[:i]]




	