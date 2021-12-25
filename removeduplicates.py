"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def deleteDuplicates(head):
    
    # hold head node to return list
    cur = head
    
    # iterate through list and compare each value with the next
    while cur and cur.next:
        # delete all nodes that are equal to next
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
            
    return head

"""
Time: O(n)
Space: O(1)
"""

list_1 = Node(1)
list_1.next = Node(1)
list_1.next.next = Node(2)
list_1.next.next.next = Node(3)
list_1.next.next.next.next = Node(3)

def printList(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print('null')
    
answer = deleteDuplicates(list_1)
printList(answer)