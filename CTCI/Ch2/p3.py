"""
CTCI 5th Edition
Chapter 2 - Linked Lists
Problem 3: 
	Implement an algorithm to delete a node in the middle of a singly linked list,
	given only access to that node.
	EXAMPLE
	Input: the node c from the linked list a->b->c->d->e
"""
import LinkedList as ll
import random as r

#copy the dat from the next node into the current node, then delete that node.
#the node is, after all only a container. O(1)
def solution1(node):
	if node.next == None:
		#can't delete end node, mark it
		node.data = None
	else:
		node.data = node.next.data
		node.next = node.next.next

if __name__ == '__main__':
	l = ll.generate_random_list()
	head = ll.LLfromList(l)
	mid = r.randint(3, len(l) - 1)
	node = head
	for _ in range(mid):
		node = node.next

	solution1(node)
	l.pop(mid)
	assert ll.LLtoList(head) == l