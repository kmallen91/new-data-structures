# LRU Cache(Least Recently Used)
# Cache has a limited size
# LRU Cache discards the least recently used item in the cache, when the cache is full(limit is reached)

# Data structures required:

# Hash table: need to be able to look something up with a key. Hash table allows us to quickly look up cache entries by key
# Doubly linked list: need to organize data to least and most recently used data
#   - DLL allows for movement of data to head(O(1))
#   - DLL allows for removal of data from the tail(O(1))

# Most recently used: most recently read or most recently added to the cache
# least recently used: will be discarded when new entry added, as tail holds the least recently used item

# Adding entries to the cache:
#   - if data exists
#       - check the hash with the provided key to see if key exists in cache
#       - move the entry to the head of the list

#   - if not in cache
#       - if hash is full (limit is reached), remove the tail item
#       - delete tail pointer from hash table
#       - create new node in list
#       - create key:value pair in cache that points to new node
#
#   - create a new node in DLL
#   - add hash table entry that holds pointer to new DLL node
#
#   - return the found / new item
#
# Get item from cache:
#   - if data exists in cache
#       - move entry to head of list
#       - return found item
#   - else
#       - return error 'item not found'
#
# Delete item from cache:
#   - if cache is at limit, remove item from tail
#   - delte tail pointer from hash table where key:value pair == removed node value
#
#


from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.cache = {}
        self.size = 0
        self.storage = DoublyLinkedList()
        self.limit = limit

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.cache.keys():
            self.storage.move_to_front(self.cache[key])
            return self.cache[key].value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        if key in self.cache.keys():
            self.cache[key].value = (key, value)
            self.storage.move_to_front(self.cache[key])
            return self.cache[key]

        elif key not in self.cache.keys():
            # increment size
            self.size += 1
            # move node to head of list
            self.cache[key] = self.storage.add_to_head((key, value))

            # remove the LRU obj if we are at capactiy
            if self.size > self.limit:
                self.size -= 1
                # remove from DLL
                old_node = self.storage.remove_from_tail()
                # delete from cache
                del self.cache[old_node.value[0]]

            return self.cache[key]
