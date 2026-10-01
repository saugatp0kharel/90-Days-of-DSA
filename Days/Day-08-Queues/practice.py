"""
============================================================
DAY 08 PRACTICE
QUEUES AND DEQUES
============================================================

Try every problem before checking the solutions.

Ask:

1. Does the problem need FIFO?
2. What should enter the queue?
3. What should leave from the front?
4. Do I need recent values?
5. Could BFS use this queue?
6. What is the Time Complexity?
7. What is the Space Complexity?
"""

from collections import deque


# ============================================================
# QUESTION 1
# CREATE QUEUE
# ============================================================

"""
Create an empty queue using deque.

MY SOLUTION:
"""


# ============================================================
# QUESTION 2
# ENQUEUE
# ============================================================

"""
Add:

10
20
30

Expected:

deque([10, 20, 30])

MY SOLUTION:
"""


# ============================================================
# QUESTION 3
# FRONT ITEM
# ============================================================

"""
For:

[10, 20, 30]

print the front item.

Expected:

10

Do not remove it.

MY SOLUTION:
"""


# ============================================================
# QUESTION 4
# DEQUEUE
# ============================================================

"""
Remove the front value.

Expected removed:

10

Remaining:

[20, 30]

MY SOLUTION:
"""


# ============================================================
# QUESTION 5
# EMPTY CHECK
# ============================================================

"""
Check whether an empty deque is empty.

Expected:

True

MY SOLUTION:
"""


# ============================================================
# QUESTION 6
# APPENDLEFT
# ============================================================

"""
Start:

deque([10, 20])

Add:

5

to the LEFT.

Expected:

deque([5, 10, 20])

MY SOLUTION:
"""


# ============================================================
# QUESTION 7
# POP RIGHT
# ============================================================

"""
Start:

deque([5, 10, 20])

Remove from the RIGHT.

Expected removed:

20

MY SOLUTION:
"""


# ============================================================
# QUESTION 8
# FIFO PROCESSING
# ============================================================

tasks = [
    "Task 1",
    "Task 2",
    "Task 3"
]

"""
Process all tasks in FIFO order.

Expected:

Task 1
Task 2
Task 3

MY SOLUTION:
"""


# ============================================================
# QUESTION 9
# LAST 3 VALUES
# ============================================================

numbers = [
    1,
    2,
    3,
    4,
    5
]

"""
Keep only the latest 3 values.

Final expected queue:

[3, 4, 5]

MY SOLUTION:
"""


# ============================================================
# QUESTION 10
# MOVING AVERAGE
# ============================================================

"""
Window size:

3

Values:

1
10
3
5

Calculate the moving average
after every new number.

MY SOLUTION:
"""


# ============================================================
# QUESTION 11
# STACK VS QUEUE
# ============================================================

"""
If we add:

1
2
3

What will a STACK remove first?

What will a QUEUE remove first?

MY ANSWER:
"""


# ============================================================
# QUESTION 12
# FIFO
# ============================================================

"""
What does FIFO mean?

Explain with a real-life example.
"""


# ============================================================
# QUESTION 13
# COMPLEXITY
# ============================================================

"""
deque.append(x)

Time = ?

MY ANSWER:
"""


# ============================================================
# QUESTION 14
# COMPLEXITY
# ============================================================

"""
deque.popleft()

Time = ?

MY ANSWER:
"""


# ============================================================
# QUESTION 15
# LIST QUEUE COMPLEXITY
# ============================================================

"""
list.pop(0)

Time = ?

Why?

MY ANSWER:
"""


# ============================================================
# QUESTION 16
# DEQUE VS LIST
# ============================================================

"""
Which is better for a normal queue?

A. Python list with pop(0)
B. collections.deque

Explain why.
"""


# ============================================================
# QUESTION 17
# SIMPLE BFS
# ============================================================

graph = {

    "A": ["B", "C"],

    "B": ["D"],

    "C": ["E"],

    "D": [],

    "E": []
}

"""
Perform BFS starting from A.

Expected:

A
B
C
D
E

MY SOLUTION:
"""


# ============================================================
# QUESTION 18
# BFS CONCEPT
# ============================================================

"""
Why does BFS use a queue?

Explain using FIFO.
"""


# ============================================================
# QUESTION 19
# BFS VISITED
# ============================================================

"""
Why do we normally use a visited set
when doing BFS on a graph?
"""


# ============================================================
# QUESTION 20
# QUEUE OR STACK
# ============================================================

"""
Choose Queue or Stack:

A. Undo operation
B. Customer waiting line
C. BFS
D. Browser back history
E. Print jobs in arrival order

MY ANSWER:
"""


# ============================================================
# QUESTION 21
# DEQUE OPERATIONS
# ============================================================

"""
Explain:

append()
appendleft()
pop()
popleft()
"""


# ============================================================
# QUESTION 22
# PROCESS REQUESTS
# ============================================================

requests = [
    "Request A",
    "Request B",
    "Request C"
]

"""
Process the requests
in the order they arrived.

MY SOLUTION:
"""


# ============================================================
# QUESTION 23
# EMPTY QUEUE ERROR
# ============================================================

"""
What happens if:

queue = deque()

queue.popleft()

How can we avoid the error?
"""


# ============================================================
# QUESTION 24
# QUEUE CLASS
# ============================================================

"""
Create a Queue class with:

enqueue()
dequeue()
peek()
is_empty()

MY SOLUTION:
"""


# ============================================================
# QUESTION 25
# PATTERN RECOGNITION
# ============================================================

"""
Which pattern fits each?

A. Process jobs in arrival order
B. Level-order traversal
C. Latest 5 measurements
D. Undo last action
E. Check parentheses

Choose:

Queue
Stack
"""


# ============================================================
#
# STOP HERE
#
# TRY QUESTIONS BEFORE READING SOLUTIONS
#
# ============================================================































# ============================================================
# SOLUTIONS
# ============================================================


# ============================================================
# SOLUTION 1
# ============================================================

queue = deque()

print(queue)


# ============================================================
# SOLUTION 2
# ============================================================

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)


# ============================================================
# SOLUTION 3
# ============================================================

print(
    queue[0]
)


# ============================================================
# SOLUTION 4
# ============================================================

removed = queue.popleft()

print(
    "Removed:",
    removed
)

print(
    "Remaining:",
    queue
)


# ============================================================
# SOLUTION 5
# ============================================================

empty_queue = deque()

print(
    not empty_queue
)


# ============================================================
# SOLUTION 6
# ============================================================

queue = deque(
    [10, 20]
)

queue.appendleft(5)

print(queue)


# ============================================================
# SOLUTION 7
# ============================================================

removed = queue.pop()

print(
    "Removed:",
    removed
)


# ============================================================
# SOLUTION 8
# ============================================================

tasks = deque(
    [
        "Task 1",
        "Task 2",
        "Task 3"
    ]
)

while tasks:

    print(
        tasks.popleft()
    )


# ============================================================
# SOLUTION 9
# ============================================================

recent = deque()

for number in [
    1,
    2,
    3,
    4,
    5
]:

    recent.append(number)

    if len(recent) > 3:

        recent.popleft()

print(
    list(recent)
)

"""
Output:

[3, 4, 5]
"""


# ============================================================
# SOLUTION 10
# ============================================================

class MovingAverage:

    def __init__(self, size):

        self.size = size

        self.queue = deque()

        self.total = 0

    def next(self, value):

        self.queue.append(value)

        self.total += value

        if len(self.queue) > self.size:

            removed = self.queue.popleft()

            self.total -= removed

        return (
            self.total
            /
            len(self.queue)
        )


moving = MovingAverage(3)

print(
    moving.next(1)
)

print(
    moving.next(10)
)

print(
    moving.next(3)
)

print(
    moving.next(5)
)


# ============================================================
# SOLUTION 11
# ============================================================

"""
Add:

1
2
3


STACK removes:

3

because Stack = LIFO


QUEUE removes:

1

because Queue = FIFO
"""


# ============================================================
# SOLUTION 12
# ============================================================

"""
FIFO means:

First In
First Out

Example:

People waiting in a line.

The person who entered first
is served first.
"""


# ============================================================
# SOLUTION 13
# ============================================================

"""
deque.append(x)

O(1)
"""


# ============================================================
# SOLUTION 14
# ============================================================

"""
deque.popleft()

O(1)
"""


# ============================================================
# SOLUTION 15
# ============================================================

"""
list.pop(0)

O(n)

because remaining items
must shift left.
"""


# ============================================================
# SOLUTION 16
# ============================================================

"""
collections.deque

is better for a normal queue.

Why?

append():

O(1)

popleft():

O(1)


With list:

pop(0)

is:

O(n)
"""


# ============================================================
# SOLUTION 17
# ============================================================

def bfs(graph, start):

    queue = deque([start])

    visited = {start}

    result = []

    while queue:

        node = queue.popleft()

        result.append(node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append(neighbor)

    return result


print(
    bfs(
        graph,
        "A"
    )
)

"""
Output:

['A', 'B', 'C', 'D', 'E']
"""


# ============================================================
# SOLUTION 18
# ============================================================

"""
BFS uses a queue because it
processes nodes in discovery order.

The first discovered node
should be processed first.

That is:

FIFO
"""


# ============================================================
# SOLUTION 19
# ============================================================

"""
A graph can contain cycles.

Example:

A -> B
B -> A

Without a visited set,
we could repeatedly process
the same nodes.

visited prevents that.
"""


# ============================================================
# SOLUTION 20
# ============================================================

"""
A. Undo

Stack


B. Customer waiting line

Queue


C. BFS

Queue


D. Browser Back

Stack


E. Print jobs in arrival order

Queue
"""


# ============================================================
# SOLUTION 21
# ============================================================

"""
append()

Add to right


appendleft()

Add to left


pop()

Remove from right


popleft()

Remove from left
"""


# ============================================================
# SOLUTION 22
# ============================================================

requests = deque(
    [
        "Request A",
        "Request B",
        "Request C"
    ]
)

while requests:

    print(
        requests.popleft()
    )


# ============================================================
# SOLUTION 23
# ============================================================

"""
Calling:

popleft()

on an empty deque raises:

IndexError


Safer:

if queue:

    queue.popleft()
"""


# ============================================================
# SOLUTION 24
# ============================================================

class Queue:

    def __init__(self):

        self.items = deque()

    def enqueue(self, value):

        self.items.append(value)

    def dequeue(self):

        if self.items:

            return self.items.popleft()

        return None

    def peek(self):

        if self.items:

            return self.items[0]

        return None

    def is_empty(self):

        return not self.items


# ============================================================
# SOLUTION 25
# ============================================================

"""
A. Process jobs in arrival order

Queue


B. Level-order traversal

Queue


C. Latest 5 measurements

Queue / Deque


D. Undo last action

Stack


E. Check parentheses

Stack
"""


# ============================================================
# FINAL DAY 8 SUMMARY
# ============================================================

"""
QUEUE

FIFO

First In
First Out


-----------------------------------------


ENQUEUE

append()


-----------------------------------------


DEQUEUE

popleft()


-----------------------------------------


DEQUE

O(1) operations
at both ends


-----------------------------------------


QUEUE USE CASES

Waiting Lines
Task Processing
Recent Values
BFS


-----------------------------------------


STACK

LIFO


QUEUE

FIFO
"""