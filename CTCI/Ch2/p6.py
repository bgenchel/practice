"""
CTCI 5th Edition
Chapter 2 - Linked Lists
Problem 6: 
	Given a circular linked list, implement an algorithm which returns the node at the beginning of the loop.
	DEFINITION
	Circular linked list: A (corrupt) linked list in which a node's next pointer points
	to an earlier node, so as to make a loop in the linked list.
	EXAMPLE
	Input: A -> B -> C -> D -> E -> C [the same C as earlier]
	Output: C
"""

""" 
High level reasoning: Start a "runner" and a "walker" at the beginnning of the list.
For every one step the "walker" takes, the "runner" takes 2. 

Let's say the beginning of the loop happens k nodes after the start of the list, and the loop is m nodes long.
When the "walker" has reached the beginning of the loop, the "runner" will have traveled k nodes in the loop.
It's position will therefore be at k % m, and it will be a distance of (m - k%m) from the "walker". 

Since "runner" moves at a speed of 2x the speed of the "walker", "runner" will move 2*(m - k%m) steps in the time
it takes "walker" to move (m - k%m). Since the "runner" starts at (m - k%m), this means they will meet at (m - k%m)
after the start of the loop. This means they are k%m steps away from the beginning of the loop. This means that it 
is also k steps from the start of the loop, since some part of the k will just make a full circle.

This means, that if you start a third pointer at the beginning of the list, after the first two meet, the third
will meet the "walker" at the beginning of the loop!
"""
import LinkedList as ll

def solution(head):
	prt1 = head
	prt2 = head
	ptr3 = head
	while ptr1 is not ptr2:
		ptr1 = ptr1.next
		ptr2 = ptr2.next.next

	while ptr3 is not ptr1:
		ptr1 = ptr1.next
		ptr3 = ptr3.next

	return ptr3


if __name__ == __main__'