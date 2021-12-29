"""
https://leetcode.com/problems/plus-one-linked-list/
Given a non-negative integer represented as a linked list of digits, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list.
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def plusOne(head):
    
    # p represents first non-9 digit
    sentinel = p = Node(0, head)
    cur = head
    
    # find the last non-9 digit in original list, if any
    while cur:
        if cur.val < 9:
            p = cur
        cur = cur.next
    
    # increment first non-9 digit
    # flip all nines to zeros after last non-9 digit
    p.val += 1
    p = p.next
    while p:
        p.val = 0
        p = p.next
    
    if sentinel.val == 0:
        return sentinel.next
    return sentinel

"""
Time: O(n)
Space: O(1)
"""

input_1 = Node(9)
input_1.next = Node(9)
input_1.next.next = Node(9)

input_2 = Node(3)
input_2.next = Node(9)
input_2.next.next = Node(2)
input_2.next.next.next = Node(9)
input_2.next.next.next.next = Node(9)

input_3 = Node(3)

def printList(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print('null')
    
ans1 = plusOne(input_1)
ans2 = plusOne(input_2)
ans3 = plusOne(input_3)

printList(ans1)
printList(ans2)
printList(ans3)

    