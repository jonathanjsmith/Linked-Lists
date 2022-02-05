"""
https://leetcode.com/problems/merge-k-sorted-lists/submissions/
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    
    # merge two lists to "divide and conquer"
    k = len(lists)
    interval = 1
    while interval < k:
        for i in range(0, k - interval, interval * 2):
            lists[i] = merge2Lists(lists[i], lists[interval+i])
        interval *= 2
    return lists[0]
    
def merge2Lists(l1, l2):
    sentinel = p = Node(0)
    while l1 and l2:
        if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
        p = p.next
    p.next = l1 or l2
    return sentinel.next
        
"""
Time: O(n * lgk)
Space: O(1)
"""

list_1 = Node(1, Node(4, Node(5)))
list_2 = Node(1, Node(3, Node(4)))
list_3 = Node(2, Node(6))
lists = [list_1, list_2, list_3]

def printList(head):
    while head:
        print(head.val, end='->')
        head = head.next
    print("null")

ans = mergeKLists(lists)
printList(ans)
    