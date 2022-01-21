"""
https://leetcode.com/problems/palindrome-linked-list/
Given the head of a singly linked list, return true if it is a palindrome.
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    
    # reverse the first half the list
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, slow.next, slow = slow, rev, slow.next
    
    # case: middle node
    if fast:
        slow = slow.next
    
    # compare each node in first half of list (reversed) and second half
    while rev:
        if rev.val != slow.val:
            return False
        rev, slow = rev.next, slow.next
        
    return True

"""
Time: O(n)
Space: O(1)
"""

input_1 = Node(1)
input_1.next = Node(2)
input_1.next.next = Node(2)
input_1.next.next.next = Node(1)
ans = isPalindrome(input_1)
print(ans)

input_2 = Node(1)
input_2.next = Node(2)
ans = isPalindrome(input_2)
print(ans)