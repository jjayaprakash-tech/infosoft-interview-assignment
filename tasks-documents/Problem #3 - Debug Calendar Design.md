## Problem #3 - Debug Calendar Design

## Calendar Event Booker - Debug and Documentation

#### Overview

This project involves debugging and documenting a calendar scheduling system implemented in Python. The objective is to ensure that new events can be booked without causing overlaps with existing events. The system uses a binary-like structure (`Node` and `Calendar` classes) to manage intervals.

#### Code Structure

#### `Node` Class

The `Node` class represents a node in a binary-like tree structure, where each node holds an interval (start and end times).

#### Constructor (`__init__` method)

```python
class Node:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.left_child = None
        self.right_child = None
```

- **Attributes**:
  - `start`: Start time of the interval.
  - `end`: End time of the interval.
  - `left_child`: Reference to the left child node.
  - `right_child`: Reference to the right child node.

#### `insert` Method

The `insert` method in the `Node` class is responsible for inserting a new node (interval) into the tree structure while ensuring no overlaps occur.

```python
def insert(self, node: 'Node') -> bool:
    # Check for overlap
    if node.start < self.end and node.end > self.start:
        return False  # Overlapping interval

    if node.end <= self.start:
        if not self.left_child:
            self.left_child = node
            return True
        return self.left_child.insert(node)
    else:  # node.start >= self.end
        if not self.right_child:
            self.right_child = node
            return True
        return self.right_child.insert(node)
```

- **Functionality**:
  - Checks if the new interval overlaps with the current node's interval.
  - If no overlap, inserts the new node to the left or right child based on the interval comparison.

#### `Calendar` Class

The `Calendar` class manages the scheduling of events using the `Node` class to maintain a structured interval tree.

#### Constructor (`__init__` method)

```python
class Calendar:
    def __init__(self):
        self.root = None
```

- **Attributes**:
  - `root`: The root node of the interval tree.

#### `book` Method

The `book` method in the `Calendar` class allows scheduling of new events by inserting new intervals into the interval tree.

```python
def book(self, start: int, end: int) -> bool:
    if start >= end:
        return False  # Invalid interval

    if self.root is None:
        self.root = Node(start, end)
        return True

    return self.root.insert(Node(start, end))
```

- **Parameters**:
  - `start`: Start time of the new event.
  - `end`: End time of the new event.
    
- **Functionality**:
  - Checks if the interval is valid (start < end).
  - Inserts a new `Node` into the interval tree using the `insert` method of `Node`.
  - Returns `True` if the event was successfully booked (no overlaps), otherwise `False`.

#### Debug Issues Identified

1. **Incorrect Overlap Check**: The original `insert` method did not correctly detect overlapping intervals, leading to potential double bookings.
2. **Invalid Interval Handling**: The `book` method did not handle cases where `start` is equal to or greater than `end`, which are invalid intervals.

#### Fixes Implemented

1. **Corrected Overlap Check in `insert` Method**: Updated the `insert` method in `Node` class to correctly detect overlaps between intervals.
2. **Added Interval Validation in `book` Method**: Implemented a check in the `book` method to ensure `start` is less than `end` for a valid interval.

#### Implementation Details

- **Overlap Check**: The `insert` method now checks if a new interval overlaps with any existing intervals before insertion, ensuring no double bookings occur.
- **Tree Structure**: The interval tree structure is maintained using binary-like insertion logic, where intervals are inserted recursively based on their start and end times.
- **Error Handling**: Invalid intervals (where `start` >= `end`) are explicitly rejected by the `book` method to maintain data integrity.

#### How to Use

To use the `Calendar` scheduling system:

1. Create a new `Calendar` object:
   ```python
   calendar = Calendar()
   ```

2. Book events using the `book` method, providing start and end times:
   ```python
   calendar.book(5, 10)  # Example: Book an event from 5 to 10
   ```

3. The `book` method returns `True` if the event was successfully booked (no overlaps), otherwise `False`.

#### Testing

Testing ensures that the fixed `Calendar` class behaves as expected:

```python
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

```

#### Summary

The updated `Calendar` class provides a robust solution for scheduling events without double bookings, ensuring efficient management of time intervals.

#### Source Code

The source code for the `Calendar` and `Node` classes can be found in [calendar.py](https://github.com/jjayaprakash-tech/infosoft-interview-assignment/blob/main/source-code/calender.py).

#### Assignment Document

For the assignment details and requirements, refer to the [Assignment Document](https://github.com/jjayaprakash-tech/infosoft-interview-assignment/blob/main/assignment-documents).
