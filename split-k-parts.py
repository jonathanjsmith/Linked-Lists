"""
https://leetcode.com/problems/split-linked-list-in-parts/
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
Return an array of the k parts.
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# count nodes in list
def countNodes(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count
     
# split list in k parts
def splitToParts(head, k):
    
    split = []
    cur = head
    
    # find number of nodes in each split
    count = countNodes(head)
    width, rem = divmod(count, k)
    
    # create each list with width or width+1 nodes
    for _ in range(k):
        prev, head = None, cur
        for _ in range(width):
            prev, cur = cur, cur.next
        if rem:
            prev, cur = cur, cur.next
            rem -= 1
        # end sublist and append to split list
        if prev:
            prev.next = None
        split.append(head)
        
    return split

"""
Time: O(n + k)
Space: O(k)
"""

input_1 = p = Node(1)
for i in range(2, 11):
    p.next = Node(i)
    p = p.next
    
def printList(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print('null')

ans = splitToParts(input_1, 3)

for a in ans:
    printList(a)
            
    