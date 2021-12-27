"""
https://leetcode.com/problems/reverse-linked-list/submissions/
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# recursive solution
def recursiveReverse(head):
    
    # sublist must have at least two nodes to change direction
    if not head or not head.next:
        return head
    
    # recursive solution to change direciton of pointers
    last = recursiveReverse(head.next)
    
    # change direction next node
    head.next.next = head
    head.next = None
    
    # return last node in original list
    return last

# iterative solution
def iterReverse(head):
    
    # solution requires 3 pointers
    prev = None
    cur = head
    
    while cur:
        # hold original next node
        t = cur.next
        # change direction of pointer
        cur.next = prev
        # move both pointers forward
        prev = cur
        cur = t
        
    return prev
        
"""
Time: O(n)
Space: O(1)
"""

input_1 = p = Node(1)
for i in range (2, 6):
    p.next = Node(i)
    p = p.next
    
def printList(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print('null')
    
reverse = iterReverse(input_1)
printList(reverse)
orig = recursiveReverse(reverse)
printList(orig)