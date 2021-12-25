"""
https://leetcode.com/problems/swap-nodes-in-pairs/
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def swapPairs(head):
    
    # return head if sub-list is less than nodes
    if not head or not head.next:
        return head
    
    # each recursive call handles two nodes to swap
    t = head.next
    head.next = swapPairs(t.next)
    t.next = head
    
    return t

"""
Time: O(n)
Space: O(1)
"""

list_1 = p = Node(1)

for i in range(2, 8):
    p.next = Node(i)
    p = p.next

mergedList = swapPairs(list_1)

def printList(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print('null')
    
printList(mergedList)