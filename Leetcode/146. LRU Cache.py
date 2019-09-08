"""
146. LRU Cache
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = 0
        self.next = 0

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)
    
    def _remove_node(self, node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev
    
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
    
    def _pop_tail(self):
        last = self.tail.prev
        self._remove_node(last)
        return last
    
    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            new_node = DLinkedNode()
            new_node.key = key
            new_node.value = value
            
            self.cache[key] = new_node
            self._add_node(new_node)
            self.size += 1
            
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)