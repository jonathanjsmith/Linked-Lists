"""
https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def countNodes(head):
    # count number of nodes in list
    count = 0
    while head:
        count += 1
        head = head.next
    return count
        
def intersectionNode(list_1, list_2):
    
    # count number of nodes in list1 and list 2
    len1 = countNodes(list_1)
    len2 = countNodes(list_2)
    
    # sync pointers if uneven
    if len1 > len2:
        for i in range(len1 - len2):
            list_1 = list_1.next
    elif len2 > len1:
        for i in range(len2 - len1):
            list_2 = list_2.next
            
    # look through the lists for equal node
    while list_1:
        if list_1 == list_2:
            return list_1
        list_1 = list_1.next
        list_2 = list_2.next
        
    return None
        
"""
Time: O(n + m)
Space: O(1)
"""

l1 = Node(4)
l1.next = Node(1)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(1)

comb = Node(8)
comb.next = Node(4)
comb.next.next = Node(5)

l1.next.next = comb
l2.next.next.next = comb

node = intersectionNode(l1, l2)
print(node.val)
