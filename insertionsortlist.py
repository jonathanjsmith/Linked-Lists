"""
https://leetcode.com/problems/insertion-sort-list/
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.
The steps of the insertion sort algorithm:
    Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
    At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
    It repeats until no input elements remain.
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def insertionSort(head):
    
    # only need to sort if two or more nodes
    if not head or not head.next:
        return head
    
    # pointers to head to keep track of sorted and unsorted list
    sortedHead = p = head
    cur = head.next
    sortedHead.next = None
    
    while cur:
        # hold next unsorted node
        temp = cur.next
        
        # reset sorted pointer to front
        p = sortedHead
        prev = None
        
        # find place to insert node in sorted list
        while p and p.val < cur.val:
            prev = p
            p = p.next
        
        # insert node into sorted list
        if prev:
            prev.next = cur
        else:
            sortedHead = cur
        cur.next = p
        
        # move to next unsorted node
        cur = temp
    
    return sortedHead

"""
Time: O(n^2)
Space: O(1)
"""

input_1 = Node(5)
input_1.next = Node(1)
input_1.next.next = Node(3)
input_1.next.next.next = Node(2)
input_1.next.next.next.next = Node(4)

def printList(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print('null')
    
ans = insertionSort(input_1)
printList(ans)
    