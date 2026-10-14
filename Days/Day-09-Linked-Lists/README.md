# Day 09 - Linked Lists

Welcome to **Day 09** of my **90 Days of Data Structures and Algorithms** journey.

So far I have learned:

```text
Day 01 - Big-O and Complexity
Day 02 - Arrays and Python Lists
Day 03 - Array Problems and Two Pointers
Day 04 - Strings
Day 05 - String Problems and Patterns
Day 06 - Hash Tables, Dictionaries, and Sets
Day 07 - Stacks
Day 08 - Queues and Deques
```

Today I am learning:

# Linked Lists

A Linked List is a data structure made of separate objects called:

```text
Nodes
```

Each node stores:

```text
data
```

and a reference to:

```text
the next node
```

Today I learned:

- What is a Linked List?
- What is a Node?
- Head
- Next pointer/reference
- Singly Linked List
- Traversal
- Insert at beginning
- Insert at end
- Search
- Delete first node
- Delete by value
- Find length
- Reverse Linked List
- Linked List vs Array
- Time Complexity
- Space Complexity
- Common pointer mistakes

---

# 1. What is a Linked List?

A linked list is a collection of nodes connected together.

Example:

```text
10 -> 20 -> 30 -> None
```

This means:

```text
Node 1 stores 10
Node 1 points to Node 2

Node 2 stores 20
Node 2 points to Node 3

Node 3 stores 30
Node 3 points to None
```

`None` means:

```text
there is no next node
```

---

# 2. What is a Node?

A node is one individual part of a linked list.

A node usually contains:

```text
value
next
```

Example:

```python
class Node:

    def __init__(self, value):

        self.value = value

        self.next = None
```

If we create:

```python
node = Node(10)
```

then:

```text
node.value = 10
node.next = None
```

---

# 3. Visualizing a Node

A node can be imagined like this:

```text
+-------+----------+
| value |   next   |
+-------+----------+
|  10   | pointer  |
+-------+----------+
```

The pointer/reference tells us:

```text
where the next node is
```

---

# 4. Connecting Nodes

Create three nodes:

```python
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
```

Connect them:

```python
node1.next = node2

node2.next = node3
```

Now we have:

```text
10 -> 20 -> 30 -> None
```

---

# 5. What is the Head?

The first node of the linked list is called:

```text
head
```

Example:

```text
HEAD
 ↓
10 -> 20 -> 30 -> None
```

In Python:

```python
head = node1
```

The `head` gives us access to the entire list.

---

# 6. Why is Head Important?

If we lose the head:

```text
we may lose access to the linked list
```

For example:

```text
HEAD
 ↓
10 -> 20 -> 30 -> None
```

Starting from `head`, we can reach:

```text
10
20
30
```

by following:

```text
next
```

---

# 7. Singly Linked List

A singly linked list has nodes that point only in one direction.

```text
10 -> 20 -> 30 -> None
```

Each node knows:

```text
only the next node
```

It does not know the previous node.

This is called:

```text
Singly Linked List
```

---

# 8. Basic Linked List Class

```python
class Node:

    def __init__(self, value):

        self.value = value

        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None
```

Initially:

```text
head = None
```

because the linked list is empty.

---

# 9. Traversing a Linked List

Traversal means:

```text
visit every node
```

Start from:

```text
head
```

Then repeatedly move:

```python
current = current.next
```

---

## Example

```python
def print_list(head):

    current = head

    while current:

        print(current.value)

        current = current.next
```

For:

```text
10 -> 20 -> 30 -> None
```

output:

```text
10
20
30
```

---

# 10. Traversal Step-by-Step

Start:

```text
current = head
```

So:

```text
current = 10
```

Print:

```text
10
```

Move:

```python
current = current.next
```

Now:

```text
current = 20
```

Print:

```text
20
```

Move again:

```text
current = 30
```

Then:

```text
current = None
```

Loop stops.

---

# 11. Traversal Complexity

If there are:

```text
n nodes
```

we visit every node once.

Therefore:

```text
Time = O(n)
```

Extra space:

```text
O(1)
```

for simple iterative traversal.

---

# 12. Insert at Beginning

Suppose:

```text
10 -> 20 -> 30
```

We want to insert:

```text
5
```

at the beginning.

Result:

```text
5 -> 10 -> 20 -> 30
```

---

# Steps

Create a new node:

```python
new_node = Node(5)
```

Point the new node to the old head:

```python
new_node.next = self.head
```

Move head:

```python
self.head = new_node
```

---

# Code

```python
def insert_at_beginning(self, value):

    new_node = Node(value)

    new_node.next = self.head

    self.head = new_node
```

---

# Complexity

No traversal needed.

Therefore:

```text
Time = O(1)
```

This is one major advantage of linked lists.

---

# 13. Insert at End

Suppose:

```text
10 -> 20 -> 30 -> None
```

Insert:

```text
40
```

Result:

```text
10 -> 20 -> 30 -> 40 -> None
```

---

# Simple Approach

First create:

```python
new_node = Node(value)
```

If the list is empty:

```python
self.head = new_node
```

Otherwise, travel to the last node.

Then:

```python
current.next = new_node
```

---

# Code

```python
def insert_at_end(self, value):

    new_node = Node(value)

    if self.head is None:

        self.head = new_node

        return

    current = self.head

    while current.next:

        current = current.next

    current.next = new_node
```

---

# Complexity

We may need to traverse the entire list.

```text
Time = O(n)
```

If we also stored a tail pointer, insertion at end could be:

```text
O(1)
```

But today we are using the simple version.

---

# 14. Search for a Value

Problem:

```text
10 -> 20 -> 30
```

Search for:

```text
20
```

---

# Solution

```python
def search(self, target):

    current = self.head

    while current:

        if current.value == target:

            return True

        current = current.next

    return False
```

---

# Complexity

Worst case:

```text
O(n)
```

because we may check every node.

---

# 15. Find the Length

We can count nodes while traversing.

```python
def length(self):

    count = 0

    current = self.head

    while current:

        count += 1

        current = current.next

    return count
```

For:

```text
10 -> 20 -> 30
```

length:

```text
3
```

Complexity:

```text
O(n)
```

---

# 16. Delete the First Node

Suppose:

```text
10 -> 20 -> 30
```

Delete first node.

We want:

```text
20 -> 30
```

Very simple:

```python
self.head = self.head.next
```

---

# Code

```python
def delete_first(self):

    if self.head is None:

        return

    self.head = self.head.next
```

---

# Complexity

```text
O(1)
```

---

# 17. Delete by Value

Suppose:

```text
10 -> 20 -> 30 -> 40
```

Delete:

```text
30
```

Result:

```text
10 -> 20 -> 40
```

We need to change:

```text
20.next
```

so that it points to:

```text
40
```

instead of:

```text
30
```

---

# Important Idea

We often need:

```text
current
```

and:

```text
current.next
```

If:

```python
current.next.value == target
```

then skip that node:

```python
current.next = current.next.next
```

---

# Code

```python
def delete_value(self, target):

    if self.head is None:

        return False

    if self.head.value == target:

        self.head = self.head.next

        return True

    current = self.head

    while current.next:

        if current.next.value == target:

            current.next = current.next.next

            return True

        current = current.next

    return False
```

---

# Complexity

Worst case:

```text
O(n)
```

because we may traverse the list.

---

# 18. Why Pointer Changes Matter

Suppose:

```text
10 -> 20 -> 30 -> 40
```

To remove `30`, we do not need to physically shift values.

We change:

```text
20.next
```

from:

```text
30
```

to:

```text
40
```

Now:

```text
10 -> 20 -> 40
```

The `30` node is no longer part of the list.

---

# 19. Reverse a Linked List

This is one of the most important linked list problems.

Input:

```text
10 -> 20 -> 30 -> None
```

Output:

```text
30 -> 20 -> 10 -> None
```

---

# The Problem

Originally:

```text
10 points to 20
20 points to 30
30 points to None
```

We need:

```text
30 points to 20
20 points to 10
10 points to None
```

So we must reverse every pointer.

---

# 20. Three Important Variables

We use:

```text
previous
current
next_node
```

Start:

```text
previous = None
current = head
```

Inside the loop:

```python
next_node = current.next
```

Save the next node first.

Then reverse:

```python
current.next = previous
```

Move `previous`:

```python
previous = current
```

Move `current`:

```python
current = next_node
```

---

# Reverse Code

```python
def reverse(self):

    previous = None

    current = self.head

    while current:

        next_node = current.next

        current.next = previous

        previous = current

        current = next_node

    self.head = previous
```

---

# 21. Reverse Step-by-Step

Start:

```text
previous = None

current = 10
```

Original:

```text
10 -> 20 -> 30 -> None
```

Save:

```text
next_node = 20
```

Reverse:

```text
10 -> None
```

Move:

```text
previous = 10
current = 20
```

Next:

```text
20 -> 10 -> None
```

Then:

```text
30 -> 20 -> 10 -> None
```

Finally:

```text
head = 30
```

---

# 22. Reverse Complexity

Each node is visited once.

```text
Time = O(n)
```

We only use a few pointer variables.

```text
Space = O(1)
```

This is a very important interview solution.

---

# 23. Linked List vs Array

## Array / Python List

Example:

```text
[10, 20, 30, 40]
```

Good at:

```text
direct index access
```

Example:

```python
numbers[2]
```

Typical:

```text
O(1)
```

---

## Linked List

Example:

```text
10 -> 20 -> 30 -> 40
```

There is no direct index access.

To reach `30`, we must start at the head:

```text
10
↓
20
↓
30
```

So access by position is:

```text
O(n)
```

---

# 24. Array vs Linked List Complexity

| Operation | Array / List | Singly Linked List |
|---|---:|---:|
| Access by index | O(1) | O(n) |
| Search | O(n) | O(n) |
| Insert beginning | O(n) | O(1) |
| Delete beginning | O(n) | O(1) |
| Insert end | O(1) amortized | O(n) without tail |
| Traverse | O(n) | O(n) |

---

# 25. Why Linked Lists Exist

Linked lists are useful because nodes do not have to be shifted like array elements.

Example:

Insert at beginning of array:

```text
[10, 20, 30]
```

Add `5`:

```text
[5, 10, 20, 30]
```

Existing items move.

With linked list:

```text
10 -> 20 -> 30
```

Add `5`:

```text
5 -> 10 -> 20 -> 30
```

We mainly change references.

---

# 26. Common Linked List Pattern

Most linked-list code looks like:

```python
current = self.head

while current:

    # do something

    current = current.next
```

This pattern is extremely important.

---

# 27. Common Mistake - Losing the Next Node

When reversing:

```python
current.next = previous
```

changes the pointer.

If we did not save:

```python
next_node = current.next
```

first, we could lose access to the remaining list.

That is why order matters.

Correct:

```python
next_node = current.next

current.next = previous
```

---

# 28. Common Mistake - Forgetting Empty List

Always consider:

```text
head = None
```

Example:

```python
if self.head is None:
```

This protects code from errors.

---

# 29. Common Mistake - Forgetting Head Case

Deleting a target from:

```text
10 -> 20 -> 30
```

is different when target is:

```text
10
```

because `10` is the head.

So we often handle:

```python
if self.head.value == target:
```

separately.

---

# 30. Common Mistake - Infinite Loop

If we forget:

```python
current = current.next
```

the loop may never move.

Bad:

```python
while current:

    print(current.value)
```

`current` never changes.

Correct:

```python
while current:

    print(current.value)

    current = current.next
```

---

# 31. Full Linked List Class

```python
class Node:

    def __init__(self, value):

        self.value = value

        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None


    def insert_at_beginning(self, value):

        new_node = Node(value)

        new_node.next = self.head

        self.head = new_node


    def insert_at_end(self, value):

        new_node = Node(value)

        if self.head is None:

            self.head = new_node

            return

        current = self.head

        while current.next:

            current = current.next

        current.next = new_node


    def print_list(self):

        current = self.head

        while current:

            print(
                current.value,
                end=" -> "
            )

            current = current.next

        print("None")


    def search(self, target):

        current = self.head

        while current:

            if current.value == target:

                return True

            current = current.next

        return False


    def length(self):

        count = 0

        current = self.head

        while current:

            count += 1

            current = current.next

        return count


    def delete_first(self):

        if self.head is None:

            return

        self.head = self.head.next


    def delete_value(self, target):

        if self.head is None:

            return False

        if self.head.value == target:

            self.head = self.head.next

            return True

        current = self.head

        while current.next:

            if current.next.value == target:

                current.next = current.next.next

                return True

            current = current.next

        return False


    def reverse(self):

        previous = None

        current = self.head

        while current:

            next_node = current.next

            current.next = previous

            previous = current

            current = next_node

        self.head = previous
```

---

# 32. Day 9 Complexity Summary

| Operation | Time | Extra Space |
|---|---:|---:|
| Traverse | O(n) | O(1) |
| Search | O(n) | O(1) |
| Insert Beginning | O(1) | O(1) |
| Insert End | O(n) | O(1) |
| Delete First | O(1) | O(1) |
| Delete by Value | O(n) | O(1) |
| Find Length | O(n) | O(1) |
| Reverse | O(n) | O(1) |

---

# 33. Day 9 Important Patterns

## Pattern 1 - Traversal

```python
current = head

while current:

    current = current.next
```

---

## Pattern 2 - Insert at Head

```python
new_node.next = head

head = new_node
```

---

## Pattern 3 - Skip a Node

```python
current.next = current.next.next
```

Used when deleting.

---

## Pattern 4 - Reverse Pointers

```python
next_node = current.next

current.next = previous

previous = current

current = next_node
```

---

# 34. Day 9 Self-Test

Before completing Day 9, I should be able to explain:

1. What is a linked list?
2. What is a node?
3. What does a node store?
4. What is head?
5. What does `next` mean?
6. What is `None` at the end?
7. What is a singly linked list?
8. How do we traverse a linked list?
9. Why is traversal O(n)?
10. How do we insert at the beginning?
11. Why is insertion at beginning O(1)?
12. How do we insert at the end?
13. Why can insertion at end be O(n)?
14. How do we search?
15. How do we count nodes?
16. How do we delete the first node?
17. How do we delete by value?
18. What does it mean to skip a node?
19. How do we reverse a linked list?
20. Why must `next_node` be saved before reversing?
21. Why is reversing O(n)?
22. Why is reverse extra space O(1)?
23. Difference between arrays and linked lists?
24. Why is linked-list index access O(n)?
25. What pointer mistakes can cause problems?

---

# My Day 9 Progress

- [x] Learned Nodes
- [x] Learned Head
- [x] Learned Next references
- [x] Learned Singly Linked Lists
- [x] Learned Traversal
- [x] Inserted at Beginning
- [x] Inserted at End
- [x] Searched a Linked List
- [x] Counted Nodes
- [x] Deleted First Node
- [x] Deleted by Value
- [x] Reversed a Linked List
- [x] Compared Linked Lists and Arrays
- [x] Learned Pointer Safety
- [x] Analyzed Time Complexity
- [x] Analyzed Space Complexity

---

# Day 9 Quick Cheat Sheet

```text
Node
→ value + next
```

```text
Head
→ first node
```

```text
Last node
→ next = None
```

```text
Traversal
→ current = current.next
```

```text
Insert beginning
→ O(1)
```

```text
Search
→ O(n)
```

```text
Delete beginning
→ O(1)
```

```text
Reverse
→ previous + current + next_node
```

```text
Reverse Time
→ O(n)
```

```text
Reverse Space
→ O(1)
```

---

# Files in Day 09

```text
Day-09-Linked-Lists/
├── README.md
├── examples.py
└── practice.py
```

---

# Next - Day 10

Next topic:

# Linked List Problems and Fast & Slow Pointers

Possible topics:

- Middle of Linked List
- Fast and Slow Pointers
- Detect Cycle
- Find Nth Node
- Remove Nth Node
- Merge Two Sorted Lists
- Reverse Linked List Review
- Linked List Interview Patterns

---

# 90 Days of DSA

The goal is not only to memorize:

```python
current = current.next
```

The goal is to understand how nodes connect and how changing one reference can change the structure of the entire linked list.