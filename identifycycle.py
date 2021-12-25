"""
https://leetcode.com/problems/linked-list-cycle/solution/
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def hasCycle(head):
    
    # solution requires a fast and slow pointer
    slow = fast = head
    
    # check if fast pointer catches up with slow pointer
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
        
    # if fast pointer reaches end of list, there is no cycle
    return False

"""
Time: O(n + k) where k is length of cycle
Space: O(1)
"""

list_1 = Node(3)
list_1.next = pos = Node(2)
list_1.next.next = Node(0)
list_1.next.next.next = Node(-4)
list_1.next.next.next.next = pos

list_2 = Node(1)
list_2.next = Node(2)

print(hasCycle(list_1))
print(hasCycle(list_2))