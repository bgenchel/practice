# Remove all elements from a linked list of integers that have value val.

# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5

# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.

# Subscribe to see which companies asked this question

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return

        while head and head.val == val:
            head = head.next

        prev = None
        curr = head
        while curr:
            if curr.val == val and prev:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return head

def create_linked_list(lst):
    head = ListNode(lst.pop())
    while lst:
        prev = ListNode(lst.pop())
        prev.next = head
        head = prev

    return head

def print_linked_list(head):
    if not head:
        print "EMPTY LIST"
        return

    sol = str(head.val)
    while head.next:
        head = head.next
        sol += "->%s"%head.val

    print sol

if __name__ == '__main__':
    lst = [1, 2, 1, 1, 3, 1, 1, 1]
    head = create_linked_list(lst)
    s = Solution()
    head = s.removeElements(head, 1)
    print_linked_list(head)


