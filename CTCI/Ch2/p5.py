"""
CTCI 5th Edition
Chapter 2 - Linked Lists
Problem 5: 
	You have two numbers represented by a linked list, where each node contains a single digit. The digits are
	stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the 
	two numbers and returns the sum as a linked list.
	EXAMPLE
	Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295
	Output: 2 -> 1 -> 9. That is, 912
	FOLLOW UP
	Suppose the digits are stored in forward order. Repeat the above problem.
	EXAMPLE
	Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295
	Output: 9 -> 1 -> 2. That is, 912.
"""
import LinkedList as ll

#add the individual nodes together and pass up the carry
def solution(head1, head2):
	carry = 0
	curr1 = head1
	curr2 = head2
	solhead = None
	while curr1 or curr2:
		if curr1 and not curr2:
			currsum = curr1.data + carry
		elif not curr1 and curr2:
			currsum = curr2.data + carry
		elif curr1 and curr2:
			currsum = curr1.data + curr2.data + carry

		carry = currsum/10
		new_node = ll.LinkedListNode(currsum%10)

		if not solhead:
			solhead = new_node
			solcurr = new_node
		else:
			solcurr.next = new_node
			solcurr = solcurr.next

		curr1 = curr1.next
		curr2 = curr2.next

	if carry:
		fn = ll.LinkedListNode(carry)
		solcurr.next = fn

	return solhead

def testsolution():
	arg1 = [7, 1, 6] #617
	arg2 = [5, 9, 2] #295
	head1 = ll.LLfromList(arg1)
	head2 = ll.LLfromList(arg2)
	
	solhead = solution(head1, head2)
	assert ll.LLtoList(solhead) == [2, 1, 9] #912	

def followupsolution(head1, head2):
	len1 = ll.LengthofLL(head1)
	len2 = ll.LengthofLL(head2)
	while len1 != len2:
		sub = ll.LinkedListNode(0)
		if len1 > len2:
			sub.next = head2
			head2 = sub
			len2 += 1
		else:
			sub.next = head1
			head1 = sub
			len1 += 1
	
	def recurseadd(head1, head2):
		carry = 0
		prevnode = None
		if head1.next and head2.next:
			(carry, prevnode) = recurseadd(head1.next, head2.next)

		dsum = head1.data + head2.data + carry
		carry = dsum/10
		value = dsum%10
		new_node = ll.LinkedListNode(value)
		new_node.next = prevnode
		return (carry, new_node)

	(carry, front) = recurseadd(head1, head2)
	if carry:
		solhead = ll.LinkedListNode(carry)
		solhead.next = front
	else:
		solhead = front

	return solhead

def testfollowupsolution():
	arg1 = [6, 1, 7] #617
	arg2 = [3, 9, 5] #295
	head1 = ll.LLfromList(arg1)
	head2 = ll.LLfromList(arg2)
	
	solhead = followupsolution(head1, head2)
	assert ll.LLtoList(solhead) == [1, 0, 1, 2] #912	

if __name__ == '__main__':
	testsolution()
	testfollowupsolution()