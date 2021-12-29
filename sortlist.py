"""
https://leetcode.com/problems/sort-list/
Given the head of a linked list, return the list after sorting it in ascending order.
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
# divide nodes and return second list
def divide(head):
    slow = fast = Node(0, head)
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    middle, slow.next = slow.next, None
    return middle

# merge lists in ascending order
def merge(l1, l2):
    dummy = cur = Node(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next, l1 = l1, l1.next
        else:
            cur.next, l2 = l2, l2.next
        cur = cur.next
    if l1:
        cur.next = l1
    elif l2:
        cur.next = l2
    return dummy.next

# sort list in ascending order
def sortList(head):
    
    # ensure two nodes for recursion
    if not head or not head.next:
        return head
    
    # divide list
    mid = divide(head)
    
    # sort left and right
    left = sortList(head)
    right = sortList(mid)
    
    return merge(left, right)

"""
Time: O(nlgn)
Space: O(1)
"""

input_1 = Node(4)
input_1.next = Node(2)
input_1.next.next = Node(1)
input_1.next.next.next = Node(5)
input_1.next.next.next.next = Node(3)

def printList(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print('null')

ans = sortList(input_1)
printList(ans)