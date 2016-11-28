"""
CTCI 5th Edition
Chapter 2 - Linked Lists
Problem 7:
	Implement a function to check if a linked list is a palindrome
"""
import LinkedList as ll
#this solution uses a stack - O(N) space, O(N) time
def solution(head):
	if not head.next:
		return True

	length = ll.LengthofLL(head)
	walker = head
	runner = head.next
	stack = [head.data]
	while runner.next != None:
		runner = runner.next.next
		if not runner:
			break
		walker = walker.next
		stack.append(walker.data)
		else:
			runner = runner.next

	if length%2 != 0:
		stack.pop()
		walker = walker.next

	while walker != None:
		if walker.data != stack.pop():
			return False
		walker = walker.next

	return True

if __name__ == '__main__':
	l = ['a', 'b', 'c', 'c', 'b', 'a']
	# l = ["a", "b", "c", "b", "a"]
	head = ll.LLfromList(l)
	assert solution(head)


