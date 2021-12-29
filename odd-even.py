"""
https://leetcode.com/problems/odd-even-linked-list/
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def oddEvenList(head):
    
    # ensure there are at least two nodes to rearrange
    if not head or not head.next:
        return head
    
    # odd and even pointers
    # hold even head to reattach
    odd, even = head, head.next
    evenHead = even
    
    # create two sublists odd and even
    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
        
    # reattach sublists
    odd.next = evenHead
    
    return head

"""
Time: O(n)
Space: O(1)
"""

input_1 = p = Node(1)
for i in range(2, 6):
    p.next = Node(i)
    p = p.next
    
def printList(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print('null')
    
ans = oddEvenList(input_1)
printList(ans)
        
        