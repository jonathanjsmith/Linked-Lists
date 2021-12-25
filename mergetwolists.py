"""
https://leetcode.com/problems/merge-two-sorted-lists/
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    
    # create dummy node to hold head of merged list
    dummy = cur = Node(0)
    
    # iterate through both lists connecting the least value of each node
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        # move merged list pointer forward
        cur = cur.next
    
    # connect the rest of the non-empty list
    if l1:
        cur.next = l1
    elif l2:
        cur.next = l2
    
    return dummy.next

"""
Time: O(n + m)
Space: O(1)
"""

list_1 = Node(1)
list_2 = Node(1)

list_1.next = Node(2)
list_1.next.next = Node(4)

list_2.next = Node(3)
list_2.next.next = Node(4)

mergedList = mergeTwoLists(list_1, list_2)

def printList(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print('null')
    
printList(mergedList)
