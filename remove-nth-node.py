"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def removeNthFromEnd(head, n):
    
    # solution requires two pointers
    p = head
    q = head
    
    # move second pointer n nodes ahead
    for i in range(n):
        q = q.next
    
    # case: n is equal to number of nodes in list -- remove head
    if not q:
        return head.next
    
    # move both pointers (total nodes - n - 1) iterations
    # p should be n-1th node
    # q should be last node in list
    while q.next:
        p = p.next 
        q = q.next
        
    # delete nth node
    p.next = p.next.next
    
    return head

# input: [1, 2, 3, 4, 5], n = 2
# output: [1, 2, 3, 5]

list_1 = p = Node(0)
for i in range(1, 6):
    p.next = Node(i)
    p = p.next
    
def printList(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print('null')

answer = removeNthFromEnd(list_1.next, 2)
printList(answer)