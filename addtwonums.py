"""
https://leetcode.com/problems/add-two-numbers/
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    
    # keep track if sum of nodes exceeds 9
    carry = 0
    
    # create new list
    dummy = node = Node(0)
    
    while l1 or l2 or carry:
        # add nodes
        v = carry
        if l1:
            v += l1.val
            l1 = l1.next
        if l2:
            v += l2.val
            l2 = l2.next
        
        # check if sum exceeds 9
        if v > 9:
            carry = 1
            v -= 10
        else:
            carry = 0
        
        # add node to list
        node.next = Node(v)
        node = node.next
        
    return dummy.next

"""
Time: O(max(n, m))
Space: O(max(n, m))
"""

list_1 = p = Node(0)
list_2 = q = Node(0)

for i in range(7):
    p.next = Node(9)
    p = p.next

for i in range(4):
    q.next = Node(9)
    q = q.next
    
def printList(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print('null')

answer = addTwoNumbers(list_1.next, list_2.next)
printList(answer)
        
        
