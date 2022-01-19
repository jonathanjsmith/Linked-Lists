"""
https://leetcode.com/problems/linked-list-cycle-ii/solution/
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def identifyCycle(head):
    
    slow = fast = entry = head
    
    # if cycle exists, pointers will intersect at a given node
    # the cycle entrance will be met by both pointers (entry and slow) at the same time at same speed
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            while slow != entry:
                slow = slow.next
                entry = entry.next
            return entry
        
    return None

"""
Time: O(n)
Space: O(1)
"""

input_1 = Node(3)
input_1.next = Node(2)
input_1.next.next = Node(0)
input_1.next.next.next = Node(-4)
input_1.next.next.next.next = input_1.next

ans = identifyCycle(input_1)
print(ans.val)

