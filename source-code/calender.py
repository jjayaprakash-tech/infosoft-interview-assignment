"""
Script: calender.py
Description: The objective is to ensure that new events can be booked without causing overlaps with existing events.
Developer: Jayaprakash J
Date: June 21, 2024
"""



class Node:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.left_child = None
        self.right_child = None
      

    def insert(self, node: 'Node') -> bool:
        
        # Check for overlap                      
        if node.start < self.end and node.end > self.start:
            return False  # Overlapping interval
        
        # Insert new intervals into a binary search tree structure
        if node.end <= self.start:
            if not self.left_child:
                self.left_child = node
                return True
            return self.left_child.insert(node) # Inserting node as left child
        elif node.start >= self.end:
            if not self.right_child:
                self.right_child = node
                return True
            return self.right_child.insert(node) # Inserting node as Right child

class Calendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:

        # Check Invalid interval
        if start >= end:
            return False  # Invalid interval
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))



# Example usage:
calendar = Calendar()
print(calendar.book(5, 10))  # Expect True: [5, 10] is added
print(calendar.book(8, 13))  # Expect False: [8, 13] overlaps with [5, 10]
print(calendar.book(10, 15)) # Expect True: [10, 15] does not overlap with any event
print(calendar.book(3, 5))   # Expect True: [3, 5] is back-to-back with [5, 10]
print(calendar.book(20, 20))   # Expect False: Invalid interval, start equals end
print(calendar.book(1, 4))   # Expect False: [1, 4] overlaps with [3, 5]
print(calendar.book(14, 16)) # Expect False: [14, 16] overlaps with [10, 15]
print(calendar.book(9, 12))  # Expect False: [9, 12] overlaps with [10, 15]
print(calendar.book(22, 23)) # Expect True: [22, 23] does not overlap with any event
