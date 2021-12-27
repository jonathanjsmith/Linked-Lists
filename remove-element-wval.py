"""
https://leetcode.com/problems/remove-linked-list-elements/
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# iterative solution
def removeElements(head, val):
    
    # create sentinel node
    dummy = cur = Node(0, head)
    
    # delete all nodes that are equal to val
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
            
    return dummy.next

# recursive solution
def recursiveRemoveElements(head, val):
    
    if not head:
        return None
    
    head.next = recursiveRemoveElements(head.next, val)
    
    if head.val == val:
        return head.next
    return head


"""
Time: O(n)
Space: O(1)
"""

input_1 = Node(1)
input_1.next = Node(2)
input_1.next.next = Node(6)
input_1.next.next.next = Node(3)
input_1.next.next.next.next = Node(4)
input_1.next.next.next.next.next = Node(5)
input_1.next.next.next.next.next.next = Node(6)

def printList(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print('null')
    
ans1 = removeElements(input_1, 6)
ans2 = recursiveRemoveElements(input_1, 6)

printList(ans1)
printList(ans2)