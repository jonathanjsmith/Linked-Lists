"""
https://leetcode.com/problems/palindrome-linked-list/
Given the head of a singly linked list, return true if it is a palindrome.
"""

class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# return the second half of the list after middle node
def getSecondHalf(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# reverse linked list
def reverseList(head):
    prev = None
    cur = head
    while cur:
        t = cur.next
        cur.next = prev
        prev = cur
        cur = t
    return prev

# check whether list is palindrome
def isPalindrome(head):
    # get the second half of the list and reverse it
    m = getSecondHalf(head)
    m = reverseList(m)
    
    # compare both lists
    while head and m:
        if head.val != m.val:
            return False
        head = head.next
        m = m.next
    return True

"""
Time: O(n)
Space: O(1)
"""

list_1 = Node(1)
list_1.next = Node(2)
list_1.next.next = Node(2)
list_1.next.next.next = Node(1)

list_2 = Node(1)
list_2.next = Node(2)
list_2.next.next = Node(1)

list_3 = Node(1)
list_3.next = Node(2)

print(isPalindrome(list_1))
print(isPalindrome(list_2))
print(isPalindrome(list_3))
