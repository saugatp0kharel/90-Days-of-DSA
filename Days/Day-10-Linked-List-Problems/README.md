# Day 10 - Linked List Problems and Fast & Slow Pointers

Welcome to **Day 10** of my **90 Days of Data Structures and Algorithms** journey.

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
Day 09 - Linked Lists
```

Today I am learning:

# Linked List Problems and Pointer Patterns

Day 9 taught me how linked lists work.

Today I am learning how to solve common linked-list interview problems efficiently.

Today I learned:

- Fast and Slow Pointers
- Middle of Linked List
- Detect Cycle
- Why Cycle Detection works
- Find Nth Node
- Nth Node from End
- Remove Nth Node from End
- Merge Two Sorted Linked Lists
- Reverse Linked List Review
- Dummy Nodes
- Linked List Time Complexity
- Common Linked List Interview Patterns

---

# 1. Review - Linked List

A singly linked list looks like:

```text
10 -> 20 -> 30 -> 40 -> None
```

Each node contains:

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

---

# 2. Why Linked List Problems Feel Different

With an array, we can often use:

```python
arr[i]
```

But in a linked list, we usually cannot jump directly to an index.

We must follow:

```text
head
↓
next
↓
next
↓
next
```

Because of this, linked-list problems often depend on:

```text
pointer movement
```

The most important pointer patterns are:

```text
one pointer
two pointers
fast and slow pointers
dummy node
```

---

# 3. What are Fast and Slow Pointers?

Fast and Slow Pointers use two references.

One moves:

```text
1 step at a time
```

The other moves:

```text
2 steps at a time
```

Example:

```python
slow = head
fast = head
```

Then:

```python
slow = slow.next
fast = fast.next.next
```

---

# 4. Why Use Two Different Speeds?

Suppose the list is:

```text
1 -> 2 -> 3 -> 4 -> 5
```

Start:

```text
slow = 1
fast = 1
```

After one round:

```text
slow = 2
fast = 3
```

After another:

```text
slow = 3
fast = 5
```

Fast reached the end while slow reached the middle.

This lets us find the middle without counting the list first.

---

# 5. Middle of Linked List

Problem:

```text
1 -> 2 -> 3 -> 4 -> 5
```

Expected middle:

```text
3
```

Use:

```text
slow = one step
fast = two steps
```

---

# Solution

```python
def find_middle(head):

    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next

        fast = fast.next.next

    return slow
```

---

# Step-by-Step

List:

```text
1 -> 2 -> 3 -> 4 -> 5
```

Start:

```text
slow = 1
fast = 1
```

Move:

```text
slow = 2
fast = 3
```

Move again:

```text
slow = 3
fast = 5
```

Fast cannot move two more steps.

So:

```text
slow = 3
```

That is the middle.

---

# Complexity

We traverse roughly half or all of the list.

```text
Time = O(n)
```

Extra space:

```text
O(1)
```

---

# 6. Even Number of Nodes

Example:

```text
1 -> 2 -> 3 -> 4
```

Using the common fast/slow implementation:

```python
while fast and fast.next:
```

slow finishes at:

```text
3
```

So for an even number of nodes, this version returns the second middle.

---

# 7. Cycle in a Linked List

Normally a linked list ends with:

```text
None
```

Example:

```text
1 -> 2 -> 3 -> 4 -> None
```

But sometimes a node points back to an earlier node.

Example:

```text
1 -> 2 -> 3 -> 4
         ^         |
         |_________|
```

This creates a:

```text
cycle
```

The list never reaches:

```text
None
```

---

# 8. Why Cycles are Dangerous

Consider:

```python
while current:

    current = current.next
```

If the linked list contains a cycle:

```text
current never becomes None
```

This can cause an infinite loop.

---

# 9. Detect Cycle Using a Set

One simple solution is to remember visited nodes.

```python
def has_cycle_set(head):

    visited = set()

    current = head

    while current:

        if current in visited:

            return True

        visited.add(current)

        current = current.next

    return False
```

---

# Complexity

Time:

```text
O(n)
```

Space:

```text
O(n)
```

because we store nodes.

But we can do better in space.

---

# 10. Floyd's Cycle Detection Algorithm

The famous solution uses:

```text
slow pointer
fast pointer
```

This is also called:

# Tortoise and Hare Algorithm

Why?

```text
slow = tortoise
fast = hare
```

---

# Cycle Detection Solution

```python
def has_cycle(head):

    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next

        fast = fast.next.next

        if slow is fast:

            return True

    return False
```

---

# 11. Why Fast and Slow Detect a Cycle

Imagine two people running around a circular track.

One person moves:

```text
1 step
```

The other moves:

```text
2 steps
```

If the track is circular, the faster person will eventually catch the slower person.

Similarly, if a linked list contains a cycle:

```text
fast
```

will eventually meet:

```text
slow
```

If there is no cycle:

```text
fast reaches None
```

---

# Complexity

Time:

```text
O(n)
```

Extra space:

```text
O(1)
```

This is better than the set solution in space.

---

# 12. Find Nth Node from Beginning

Suppose:

```text
10 -> 20 -> 30 -> 40 -> 50
```

Find:

```text
3rd node
```

Expected:

```text
30
```

Simple traversal:

```python
def find_nth(head, n):

    current = head

    position = 1

    while current:

        if position == n:

            return current

        position += 1

        current = current.next

    return None
```

---

# Complexity

Time:

```text
O(n)
```

Space:

```text
O(1)
```

---

# 13. Nth Node from End

This is more interesting.

Example:

```text
10 -> 20 -> 30 -> 40 -> 50
```

Find:

```text
2nd node from end
```

Expected:

```text
40
```

One approach:

1. Count nodes
2. Calculate target position
3. Traverse again

But that requires two passes.

We can solve it with two pointers in one pass.

---

# 14. Two Pointer Gap Technique

Use:

```text
first
second
```

Move `first` ahead by `n` steps.

Then move both pointers together.

When `first` reaches the end:

```text
second
```

will be at the nth node from the end.

---

# Example

List:

```text
10 -> 20 -> 30 -> 40 -> 50
```

Find:

```text
2nd from end
```

Move first pointer two steps:

```text
first = 30
second = 10
```

Move both:

```text
first = 40
second = 20
```

Move:

```text
first = 50
second = 30
```

Move:

```text
first = None
second = 40
```

Answer:

```text
40
```

---

# Solution

```python
def nth_from_end(head, n):

    first = head
    second = head

    for _ in range(n):

        if first is None:

            return None

        first = first.next

    while first:

        first = first.next

        second = second.next

    return second
```

---

# Complexity

Time:

```text
O(n)
```

Extra space:

```text
O(1)
```

---

# 15. Remove Nth Node from End

Problem:

```text
1 -> 2 -> 3 -> 4 -> 5
```

Remove:

```text
2nd node from end
```

That node is:

```text
4
```

Result:

```text
1 -> 2 -> 3 -> 5
```

---

# 16. Why a Dummy Node Helps

Removing nodes can become annoying when we must remove:

```text
the head
```

Example:

```text
1 -> 2 -> 3
```

Remove third node from end.

That means remove:

```text
1
```

Instead of writing many special cases, we can create:

```text
dummy
```

before the head.

Example:

```text
dummy -> 1 -> 2 -> 3
```

Now every real node has a node before it.

---

# 17. What is a Dummy Node?

A dummy node is a temporary helper node.

Example:

```python
dummy = Node(0)

dummy.next = head
```

The value:

```text
0
```

usually does not matter.

The purpose is to make pointer logic easier.

---

# 18. Remove Nth from End Solution

```python
def remove_nth_from_end(head, n):

    dummy = Node(0)

    dummy.next = head

    first = dummy
    second = dummy

    for _ in range(n + 1):

        if first is None:

            return head

        first = first.next

    while first:

        first = first.next

        second = second.next

    second.next = second.next.next

    return dummy.next
```

---

# Why n + 1?

We want:

```text
second
```

to stop one node before the node that should be deleted.

Then:

```python
second.next = second.next.next
```

can skip the target node.

---

# Complexity

Time:

```text
O(n)
```

Extra space:

```text
O(1)
```

---

# 19. Merge Two Sorted Linked Lists

Suppose:

```text
List 1:

1 -> 3 -> 5
```

and:

```text
List 2:

2 -> 4 -> 6
```

We want:

```text
1 -> 2 -> 3 -> 4 -> 5 -> 6
```

---

# 20. Main Idea

Look at the front node of both lists.

Choose the smaller one.

Example:

```text
1 vs 2
```

Choose:

```text
1
```

Then:

```text
3 vs 2
```

Choose:

```text
2
```

Continue until one list ends.

---

# 21. Dummy Node for Merge

Dummy nodes are very useful here.

Start:

```text
dummy
```

Use:

```text
tail
```

to point to the end of the new list.

---

# Solution

```python
def merge_sorted_lists(list1, list2):

    dummy = Node(0)

    tail = dummy

    while list1 and list2:

        if list1.value <= list2.value:

            tail.next = list1

            list1 = list1.next

        else:

            tail.next = list2

            list2 = list2.next

        tail = tail.next

    if list1:

        tail.next = list1

    else:

        tail.next = list2

    return dummy.next
```

---

# 22. Merge Step-by-Step

List 1:

```text
1 -> 3 -> 5
```

List 2:

```text
2 -> 4 -> 6
```

Compare:

```text
1 and 2
```

Take:

```text
1
```

Result:

```text
1
```

Compare:

```text
3 and 2
```

Take:

```text
2
```

Result:

```text
1 -> 2
```

Continue:

```text
1 -> 2 -> 3 -> 4 -> 5 -> 6
```

---

# Merge Complexity

If:

```text
n = number of nodes in list1
m = number of nodes in list2
```

then:

```text
Time = O(n + m)
```

Extra space:

```text
O(1)
```

because we reuse existing nodes.

---

# 23. Reverse Linked List Review

This problem is so important that it is worth reviewing.

Input:

```text
1 -> 2 -> 3 -> None
```

Output:

```text
3 -> 2 -> 1 -> None
```

Code:

```python
def reverse_list(head):

    previous = None

    current = head

    while current:

        next_node = current.next

        current.next = previous

        previous = current

        current = next_node

    return previous
```

---

# Reverse Pattern

Remember:

```text
Save
Reverse
Move
Move
```

Code:

```python
next_node = current.next

current.next = previous

previous = current

current = next_node
```

---

# 24. Important Pointer Patterns

## Pattern 1 - Simple Traversal

```python
current = head

while current:

    current = current.next
```

Use for:

```text
search
count
sum
maximum
```

---

## Pattern 2 - Fast and Slow

```python
slow = head
fast = head
```

Use for:

```text
middle node
cycle detection
```

---

## Pattern 3 - Pointer Gap

```text
first pointer starts n nodes ahead
```

Use for:

```text
nth node from end
remove nth node from end
```

---

## Pattern 4 - Dummy Node

```python
dummy = Node(0)

dummy.next = head
```

Use when:

```text
head may change
```

or:

```text
merging lists
```

---

## Pattern 5 - Reverse Pointers

```text
previous
current
next_node
```

Use for:

```text
reverse linked list
```

---

# 25. Why Dummy Nodes are Powerful

Without dummy node:

```text
deleting head
```

may require a special condition.

With dummy:

```text
dummy -> head -> ...
```

the head behaves more like every other node.

Dummy nodes simplify:

- Deletion
- Merging
- Building new lists

---

# 26. Identity vs Value

Consider two different nodes:

```text
Node A value = 10

Node B value = 10
```

Their values are equal.

But they are not necessarily the same node.

For cycle detection, we care whether:

```text
slow and fast point to the exact same node
```

So:

```python
if slow is fast:
```

is a clear way to express identity.

---

# 27. Common Mistake - Fast Pointer Safety

Bad:

```python
fast = fast.next.next
```

without checking if `fast` or `fast.next` exists.

Correct:

```python
while fast and fast.next:
```

Then:

```python
fast = fast.next.next
```

is safe.

---

# 28. Common Mistake - Losing Nodes

Whenever you change:

```python
current.next
```

be careful.

Save anything needed first.

Example in reverse:

```python
next_node = current.next
```

before:

```python
current.next = previous
```

---

# 29. Common Mistake - Off-by-One Error

Problems involving:

```text
nth node
```

often create off-by-one mistakes.

Always ask:

```text
Are positions starting at 1 or 0?
```

For this lesson:

```text
1st node = head
```

---

# 30. Common Mistake - Forgetting Edge Cases

Always consider:

```text
empty list
one node
two nodes
target is head
n equals list length
cycle exists
cycle does not exist
```

---

# 31. Complexity Summary

| Problem | Time | Extra Space |
|---|---:|---:|
| Middle Node | O(n) | O(1) |
| Cycle with Set | O(n) | O(n) |
| Floyd Cycle Detection | O(n) | O(1) |
| Find Nth from Beginning | O(n) | O(1) |
| Nth from End | O(n) | O(1) |
| Remove Nth from End | O(n) | O(1) |
| Merge Sorted Lists | O(n + m) | O(1) |
| Reverse Linked List | O(n) | O(1) |

---

# 32. Brute Force vs Pointer Pattern

Sometimes there is an easy solution that uses:

```text
extra array
extra set
multiple passes
```

But linked-list pointer patterns can often reduce:

```text
extra memory
```

Example:

Cycle detection with set:

```text
O(n) Space
```

Floyd's algorithm:

```text
O(1) Space
```

---

# 33. Day 10 Self-Test

Before completing Day 10, I should be able to explain:

1. What are Fast and Slow Pointers?
2. Why does slow move one step?
3. Why does fast move two steps?
4. How do we find the middle node?
5. What does the algorithm return for an even-length list?
6. What is a linked-list cycle?
7. Why can a cycle cause an infinite loop?
8. How can a set detect a cycle?
9. What is Floyd's Cycle Detection Algorithm?
10. Why do fast and slow meet inside a cycle?
11. Why is Floyd's extra space O(1)?
12. How do we find the nth node from the beginning?
13. How do we find the nth node from the end?
14. What is the pointer-gap technique?
15. What is a dummy node?
16. Why are dummy nodes useful?
17. How do we remove the nth node from the end?
18. Why do we sometimes move the first pointer n+1 steps?
19. How do we merge two sorted linked lists?
20. What does `tail` represent?
21. Why is merge O(n + m)?
22. How do we reverse a linked list?
23. Why must we save `next_node`?
24. What is an off-by-one error?
25. What edge cases should linked-list code handle?

---

# My Day 10 Progress

- [x] Reviewed Linked Lists
- [x] Learned Fast and Slow Pointers
- [x] Found Middle Node
- [x] Learned Cycles
- [x] Detected Cycle with Set
- [x] Learned Floyd's Cycle Detection
- [x] Found Nth Node
- [x] Found Nth Node from End
- [x] Learned Pointer Gap Technique
- [x] Learned Dummy Nodes
- [x] Removed Nth Node from End
- [x] Merged Two Sorted Lists
- [x] Reviewed Linked List Reversal
- [x] Learned Pointer Safety
- [x] Analyzed Time Complexity
- [x] Analyzed Space Complexity

---

# Day 10 Quick Cheat Sheet

```text
Middle
→ slow = 1 step
→ fast = 2 steps
```

```text
Cycle
→ Floyd's Algorithm
→ slow + fast
```

```text
Nth from End
→ create n-node gap
```

```text
Remove Nth from End
→ Dummy Node + Two Pointers
```

```text
Merge Sorted Lists
→ Dummy + Tail
```

```text
Reverse
→ previous
→ current
→ next_node
```

```text
Fast/Slow Time
→ O(n)
```

```text
Fast/Slow Space
→ O(1)
```

---

# Files in Day 10

```text
Day-10-Linked-List-Problems/
├── README.md
├── examples.py
└── practice.py
```

---

# Next - Day 11

Next topic:

# Recursion

Possible topics:

- What is Recursion?
- Base Case
- Recursive Case
- Call Stack
- Factorial
- Sum of Numbers
- Fibonacci
- Reverse String Recursively
- Recursion Time and Space Complexity

---

# 90 Days of DSA

Day 10 is important because linked-list interviews are often not about writing a Node class.

They are about recognizing pointer patterns:

```text
Fast and Slow
Pointer Gap
Dummy Node
Reverse Pointers
```

The goal is to look at a new linked-list problem and ask:

```text
Which pointer pattern fits this problem?
```