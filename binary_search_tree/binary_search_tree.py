from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')

# INSERT:
# insert value
# base case: if no node at root, insert as root
# compare value to root
# if smaller:
#       look left if node, repeat
#           if no node, make new node
# if value is greater or equal
#       look right, repeat
#           if no node, make new node
#
# CONTAINS/FIND:
# base case: if no node at root, return false
# else, compare value to root
#   if smaller:
#       go left, compare
#   if greater/equal:
#       go right, compare
#
# GET MAX:
# if no self.right child/node:
#       return value
# else, go right
#
#
#
#


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if no node, insert node
        if self.value is None:
            self.value = BinarySearchTree(value)
        else:
            # if value is greater than node, look right, insert node if none, otherwise recurse
            if value >= self.value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    return self.right.insert(value)
            # if value is less than node, look left, insert node if none, otherwise recurse
            else:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    return self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value is None:
            return False
        else:
            if target == self.value:
                return True
            elif target >= self.value and self.right is None:
                return False
            elif target >= self.value and self.right is not None:
                return self.right.contains(target)
            elif target < self.value and self.left is None:
                return False
            elif target < self.value and self.left is not None:
                return self.left.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        bft = Queue()
        bft.enqueue(node)
        current_node = bft.dequeue()

        while current_node:
            print(current_node.value)
            # if right node, put in queue
            if current_node.right:
                bft.enqueue(current_node.right)
            # if left node, put in queue
            if current_node.left:
                bft.enqueue(current_node.left)
            # if items in queue, dequeue (ie print) those values before moving down layers
            if bft.size > 0:
                current_node = bft.dequeue()
            else:
                break

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        dft = Stack()
        # push initial node to stack
        dft.push(node)

        while dft.size > 0:
            # store initial value in variable
            current = dft.pop()
            print(current.value)
            if current.right:
                dft.push(current.right)
            if current.left:
                dft.push(current.left)

        # STRETCH Goals -------------------------
        # Note: Research may be required

        # Print Pre-order recursive DFT

    def pre_order_dft(self, node=None):
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self, node=None):
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)


bst = BinarySearchTree(1)
print(bst.insert(8))
print(bst.insert(7))
print(bst.insert(6))
print(bst.insert(3))
print(bst.insert(4))
print(bst.insert(2))
