"""
https://leetcode.com/problems/rotate-list/
Given the head of a linked list, rotate the list to the right by k places.
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
# return number of nodes in list
def countNodes(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

# rotate list right k places
def rotate(head, k):
    # base case
    if not head:
        return head
    
    # solution requires two pointers
    p = q = head
    
    # count nodes in list
    count = countNodes(head)
    
    # find kth node in circular list
    k %= count
    for i in range(k):
        q = q.next
        
    # case: list unchanged
    if q == head:
        return head
    
    # find the end of both sublists
    while q.next:
        p = p.next
        q = q.next
    
    # move second list in front of first list
    first = p.next
    p.next = None
    q.next = head
    
    return first

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
        print(head.val, end = ' -> ')
        head = head.next
    print('null')
    
ans = rotate(list_1, 2)
printList(ans)
    
    