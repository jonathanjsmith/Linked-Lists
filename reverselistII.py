"""
https://leetcode.com/problems/reverse-linked-list-ii/solution/
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverseBetween(head, left, right):
    
    # create sentinel node
    dummy = prev = Node(0, head)
    
    # find prev node from beginning of reversal
    for i in range(left-1):
        prev = prev.next
        
    # establish pointers to connect after reversal
    node1 = prev
    cur = node2 = prev.next
    
    # reverse list
    for i in range(right - left + 1):
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
        
    # connect nodes after reversal
    node1.next = prev
    node2.next = cur
    
    return dummy.next

"""
Time: O(n)
Space: O(1)
"""

list_1 = p = Node(0)
for i in range(1, 6):
    p.next = Node(i)
    p = p.next
    
def printList(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print('null')

ans = reverseBetween(list_1, 2, 5)
printList(ans)