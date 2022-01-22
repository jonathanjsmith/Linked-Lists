"""
https:#leetcode.com/problems/lru-cache/
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
    1. LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    2. int get(int key) Return the value of the key if the key exists, otherwise return -1.
    3. void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""

class Node:
    
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        node = self.cache.get(key)
        
        if not node:
            print('-1')
            return -1
        
        self._remove(node)
        self._add(node)
        
        print(node.val)
        return node.val
    
    def put(self, key, value):
        node = self.cache.get(key)
        
        if not node:
            new_node = Node(key, value)
            self._add(new_node)
            self.cache[key] = new_node
            self.size += 1
            if self.size > self.capacity:
                del self.cache[self.tail.prev.key]
                self._remove(self.tail.prev)
                self.size -= 1
        else:
            node.val = value
            self._remove(node)
            self._add(node)
        print('null')
    
    def _add(self, node):
        node.next = self.head.next
        node.prev = self.head
        
        self.head.next.prev = node
        self.head.next = node
    
    def _remove(self, node):
        p = node.prev
        n = node.next
        
        p.next = n
        n.prev = p
        
"""

"""

lRUCache = LRUCache(2)
lRUCache.put(1, 1)  # cache is {1=1}
lRUCache.put(2, 2)  # cache is {1=1, 2=2}
lRUCache.get(1)     # return 1
lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2)     # returns -1 (not found)
lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1)     # return -1 (not found)
lRUCache.get(3)     # return 3
lRUCache.get(4)     # return 4