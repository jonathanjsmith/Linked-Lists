"""
https://leetcode.com/problems/reorder-list/
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# find middle node
def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# reverse list
def reverse(head):
    prev, cur = None, head
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev

# reorder list
def reorder(head):
        
    # find middle node
    middle = middleNode(head)
    
    # reverse middle node
    rev = reverse(middle)
    
    # merge lists
    while rev.next:
        head.next, head = rev, head.next
        rev.next, rev = head, rev.next
        
"""
Time: O(n)
Space: O(1)
"""

list_1 = p = Node(1)
for i in range(2, 6):
    p.next = Node(i)
    p = p.next

def printList(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print('null')
    
reorder(list_1)
printList(list_1)