"""
============================================================
DAY 08 - QUEUES AND DEQUES
============================================================
"""

from collections import deque


# ============================================================
# EXAMPLE 1
# CREATE QUEUE
# ============================================================

queue = deque()

print("EXAMPLE 1 - CREATE QUEUE")

print(queue)


# ============================================================
# EXAMPLE 2
# ENQUEUE
# ============================================================

queue.append(10)
queue.append(20)
queue.append(30)

print("\nEXAMPLE 2 - ENQUEUE")

print(queue)


# ============================================================
# EXAMPLE 3
# PEEK
# ============================================================

print("\nEXAMPLE 3 - PEEK")

print(
    "Front:",
    queue[0]
)

print(
    "Back:",
    queue[-1]
)


# ============================================================
# EXAMPLE 4
# DEQUEUE
# ============================================================

removed = queue.popleft()

print("\nEXAMPLE 4 - DEQUEUE")

print(
    "Removed:",
    removed
)

print(
    "Queue:",
    queue
)


# ============================================================
# EXAMPLE 5
# EMPTY CHECK
# ============================================================

print("\nEXAMPLE 5 - EMPTY CHECK")

print(
    not queue
)


# ============================================================
# EXAMPLE 6
# APPENDLEFT
# ============================================================

dq = deque([10, 20])

dq.appendleft(5)

print("\nEXAMPLE 6 - APPENDLEFT")

print(dq)


# ============================================================
# EXAMPLE 7
# POP FROM RIGHT
# ============================================================

removed = dq.pop()

print("\nEXAMPLE 7 - POP RIGHT")

print("Removed:", removed)

print("Deque:", dq)


# ============================================================
# EXAMPLE 8
# TASK PROCESSING
# ============================================================

tasks = deque()

tasks.append("Task A")
tasks.append("Task B")
tasks.append("Task C")

print("\nEXAMPLE 8 - TASK PROCESSING")

while tasks:

    current = tasks.popleft()

    print(
        "Processing:",
        current
    )


# ============================================================
# EXAMPLE 9
# SIMPLE QUEUE CLASS
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

        return len(self.items) == 0


q = Queue()

q.enqueue(100)
q.enqueue(200)
q.enqueue(300)

print("\nEXAMPLE 9 - QUEUE CLASS")

print(
    "Front:",
    q.peek()
)

print(
    "Removed:",
    q.dequeue()
)

print(
    "New Front:",
    q.peek()
)


# ============================================================
# EXAMPLE 10
# MOVING AVERAGE
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


moving_average = MovingAverage(3)

print("\nEXAMPLE 10 - MOVING AVERAGE")

print(
    moving_average.next(1)
)

print(
    moving_average.next(10)
)

print(
    moving_average.next(3)
)

print(
    moving_average.next(5)
)


# ============================================================
# EXAMPLE 11
# KEEP ONLY LAST 3 ITEMS
# ============================================================

recent = deque()

print("\nEXAMPLE 11 - LAST 3 ITEMS")

for number in [1, 2, 3, 4, 5]:

    recent.append(number)

    if len(recent) > 3:

        recent.popleft()

    print(
        "After adding",
        number,
        ":",
        list(recent)
    )


# ============================================================
# EXAMPLE 12
# SIMPLE BFS
# ============================================================

graph = {

    "A": ["B", "C"],

    "B": ["D", "E"],

    "C": [],

    "D": [],

    "E": []
}


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


print("\nEXAMPLE 12 - BFS")

print(
    bfs(
        graph,
        "A"
    )
)


# ============================================================
# EXAMPLE 13
# STACK VS QUEUE
# ============================================================

stack = []

stack.append(1)
stack.append(2)
stack.append(3)

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print("\nEXAMPLE 13 - STACK VS QUEUE")

print(
    "Stack removes:",
    stack.pop()
)

print(
    "Queue removes:",
    queue.popleft()
)

"""
Stack removes:

3

Queue removes:

1

Stack = LIFO
Queue = FIFO
"""


# ============================================================
# EXAMPLE 14
# REMOVE EVERYTHING IN FIFO ORDER
# ============================================================

queue = deque(
    ["A", "B", "C", "D"]
)

print("\nEXAMPLE 14 - FIFO ORDER")

while queue:

    print(
        queue.popleft()
    )


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n======================================")
print("DAY 08 EXAMPLES COMPLETE")
print("======================================")

"""
QUEUE

FIFO

First In
First Out


-----------------------------------------


ENQUEUE

queue.append(x)


-----------------------------------------


DEQUEUE

queue.popleft()


-----------------------------------------


PEEK

queue[0]


-----------------------------------------


DEQUE

Efficient at both ends


-----------------------------------------


QUEUE USE CASES

Task Processing
Moving Average
Recent Items
BFS


-----------------------------------------


STACK

LIFO


QUEUE

FIFO
"""