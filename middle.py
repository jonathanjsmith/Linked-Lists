"""
https://leetcode.com/problems/middle-of-the-linked-list/
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle(head):
    
    # fast pointer moves twice as fast as slow pointer
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow

"""
Time: O(n)
Space: O(1)
"""

list_1 = Node(1)
list_1.next = Node(2)
list_1.next.next = Node(3)
list_1.next.next.next = Node(4)
list_1.next.next.next.next = Node(5)

middle = middle(list_1)
print(middle.val)