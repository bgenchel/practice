import random as r

class LinkedListNode:
	next = None
	def __init__(self, value):
		self.data = value

def LengthofLL(head):
	count = 0
	while head != None:
		head = head.next
		count += 1
	return count

def printLL(head):
	curr = head
	while curr != None:
		print curr.data
		curr = curr.next

def LLfromList(l):
	head = LinkedListNode(l[0])
	prev = head
	for i in range(1, len(l)):
		node = LinkedListNode(l[i])
		prev.next = node
		prev = node
	return head

def LLtoList(head):
	ret = []
	curr = head
	while curr != None:
		ret.append(curr.data)
		curr = curr.next

	return ret

def generate_random_list():
	ret = []
	for i in range(r.choice(range(100))):
		ret.append(r.randint(1, 10))
	return ret
