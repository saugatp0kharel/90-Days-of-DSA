"""
============================================================
DAY 10 PRACTICE
LINKED LIST PROBLEMS
============================================================

Try each problem before checking the solutions.

Ask:

1. Can Fast and Slow Pointers help?
2. Can I create a pointer gap?
3. Would a dummy node simplify this?
4. Am I changing the head?
5. Am I about to lose a reference?
6. What is the Time Complexity?
7. What is the Extra Space?
"""


class Node:

    def __init__(self, value):

        self.value = value
        self.next = None


def build_linked_list(values):

    if not values:
        return None

    head = Node(values[0])

    current = head

    for value in values[1:]:

        current.next = Node(value)

        current = current.next

    return head


def print_list(head):

    current = head

    while current:

        print(
            current.value,
            end=" -> "
        )

        current = current.next

    print("None")


# ============================================================
# QUESTION 1
# MIDDLE NODE
# ============================================================

"""
List:

1 -> 2 -> 3 -> 4 -> 5

Find the middle using:

slow
fast

Expected:

3

MY SOLUTION:
"""


# ============================================================
# QUESTION 2
# EVEN MIDDLE
# ============================================================

"""
List:

1 -> 2 -> 3 -> 4

Using the common fast/slow method,
which middle is returned?

Expected:

3

MY SOLUTION:
"""


# ============================================================
# QUESTION 3
# FAST POINTER
# ============================================================

"""
Why do we check:

while fast and fast.next:

before doing:

fast = fast.next.next
"""


# ============================================================
# QUESTION 4
# CYCLE WITH SET
# ============================================================

"""
Write a function that detects
a linked-list cycle using a set.

Time = ?

Space = ?

MY SOLUTION:
"""


# ============================================================
# QUESTION 5
# FLOYD CYCLE DETECTION
# ============================================================

"""
Detect a cycle using:

slow
fast

Expected complexity:

Time = O(n)
Space = O(1)

MY SOLUTION:
"""


# ============================================================
# QUESTION 6
# WHY FLOYD WORKS
# ============================================================

"""
Explain in simple words why
a fast pointer eventually meets
a slow pointer if a cycle exists.
"""


# ============================================================
# QUESTION 7
# NTH FROM BEGINNING
# ============================================================

"""
List:

10 -> 20 -> 30 -> 40 -> 50

Find the 4th node.

Expected:

40

MY SOLUTION:
"""


# ============================================================
# QUESTION 8
# NTH FROM END
# ============================================================

"""
List:

10 -> 20 -> 30 -> 40 -> 50

Find 2nd node from end.

Expected:

40

Use two pointers.

MY SOLUTION:
"""


# ============================================================
# QUESTION 9
# NTH FROM END
# ============================================================

"""
List:

1 -> 2 -> 3 -> 4 -> 5

Find 5th node from end.

Expected:

1

MY SOLUTION:
"""


# ============================================================
# QUESTION 10
# INVALID N
# ============================================================

"""
List:

1 -> 2 -> 3

Find 5th node from end.

Expected:

None

MY SOLUTION:
"""


# ============================================================
# QUESTION 11
# DUMMY NODE
# ============================================================

"""
What is a dummy node?

Why is it useful?
"""


# ============================================================
# QUESTION 12
# REMOVE NTH FROM END
# ============================================================

"""
List:

1 -> 2 -> 3 -> 4 -> 5

Remove 2nd node from end.

Expected:

1 -> 2 -> 3 -> 5

MY SOLUTION:
"""


# ============================================================
# QUESTION 13
# REMOVE HEAD FROM END
# ============================================================

"""
List:

1 -> 2 -> 3

Remove 3rd node from end.

Expected:

2 -> 3

Think about why a dummy node helps.

MY SOLUTION:
"""


# ============================================================
# QUESTION 14
# MERGE SORTED LISTS
# ============================================================

"""
List 1:

1 -> 3 -> 5

List 2:

2 -> 4 -> 6

Expected:

1 -> 2 -> 3 -> 4 -> 5 -> 6

MY SOLUTION:
"""


# ============================================================
# QUESTION 15
# MERGE UNEQUAL LENGTHS
# ============================================================

"""
List 1:

1 -> 2 -> 10

List 2:

3 -> 4 -> 5 -> 6

Expected:

1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 10

MY SOLUTION:
"""


# ============================================================
# QUESTION 16
# REVERSE REVIEW
# ============================================================

"""
Reverse:

1 -> 2 -> 3 -> 4

Expected:

4 -> 3 -> 2 -> 1

MY SOLUTION:
"""


# ============================================================
# QUESTION 17
# MIDDLE COMPLEXITY
# ============================================================

"""
Find middle using Fast/Slow:

Time = ?

Extra Space = ?
"""


# ============================================================
# QUESTION 18
# FLOYD COMPLEXITY
# ============================================================

"""
Cycle Detection using Floyd:

Time = ?

Extra Space = ?
"""


# ============================================================
# QUESTION 19
# NTH FROM END COMPLEXITY
# ============================================================

"""
Two-pointer nth-from-end:

Time = ?

Extra Space = ?
"""


# ============================================================
# QUESTION 20
# MERGE COMPLEXITY
# ============================================================

"""
List 1 contains n nodes.

List 2 contains m nodes.

Merge Sorted Lists:

Time = ?

Extra Space = ?
"""


# ============================================================
# QUESTION 21
# PATTERN RECOGNITION
# ============================================================

"""
Match:

A. Middle Node
B. Cycle Detection
C. Nth From End
D. Remove Nth From End
E. Merge Sorted Lists
F. Reverse

Patterns:

Fast/Slow
Fast/Slow
Pointer Gap
Dummy + Pointer Gap
Dummy + Tail
previous/current/next_node
"""


# ============================================================
# QUESTION 22
# POINTER SAFETY
# ============================================================

"""
Why should linked-list code
care about the order in which
references are changed?
"""


# ============================================================
# QUESTION 23
# NODE IDENTITY
# ============================================================

"""
What is the difference between:

slow.value == fast.value

and:

slow is fast

Which one matters for
cycle detection?
"""


# ============================================================
# QUESTION 24
# EDGE CASES
# ============================================================

"""
Name at least five linked-list
edge cases you should test.
"""


# ============================================================
# QUESTION 25
# EXPLAIN THE BIG IDEA
# ============================================================

"""
Explain when you would use:

Fast/Slow Pointers

Pointer Gap

Dummy Node

Reverse Pointer Pattern
"""


# ============================================================
#
# STOP HERE
#
# TRY EVERYTHING BEFORE SOLUTIONS
#
# ============================================================































# ============================================================
# SOLUTIONS
# ============================================================


# ============================================================
# SOLUTION 1 AND 2
# ============================================================

def find_middle(head):

    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next

        fast = fast.next.next

    return slow


# ============================================================
# SOLUTION 3
# ============================================================

"""
We check:

fast
and
fast.next

because:

fast.next.next

would fail if either:

fast is None

or:

fast.next is None.
"""


# ============================================================
# SOLUTION 4
# ============================================================

def has_cycle_set(head):

    visited = set()

    current = head

    while current:

        if current in visited:

            return True

        visited.add(current)

        current = current.next

    return False


"""
Time:

O(n)

Space:

O(n)
"""


# ============================================================
# SOLUTION 5
# ============================================================

def has_cycle(head):

    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next

        fast = fast.next.next

        if slow is fast:

            return True

    return False


# ============================================================
# SOLUTION 6
# ============================================================

"""
Inside a cycle, both pointers
keep moving around the same loop.

The fast pointer gains one node
on the slow pointer each round.

Eventually they must land on
the same node.
"""


# ============================================================
# SOLUTION 7
# ============================================================

def find_nth(head, n):

    current = head

    position = 1

    while current:

        if position == n:

            return current

        position += 1

        current = current.next

    return None


# ============================================================
# SOLUTION 8, 9, 10
# ============================================================

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


# ============================================================
# SOLUTION 11
# ============================================================

"""
A dummy node is a temporary
helper node placed before
the real head.

Example:

dummy -> head -> ...

It helps because operations
that change the real head can
be handled like normal nodes.
"""


# ============================================================
# SOLUTION 12 AND 13
# ============================================================

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

    if second.next:

        second.next = second.next.next

    return dummy.next


# ============================================================
# SOLUTION 14 AND 15
# ============================================================

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


# ============================================================
# SOLUTION 16
# ============================================================

def reverse_list(head):

    previous = None

    current = head

    while current:

        next_node = current.next

        current.next = previous

        previous = current

        current = next_node

    return previous


# ============================================================
# SOLUTION 17
# ============================================================

"""
Middle Node:

Time:

O(n)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 18
# ============================================================

"""
Floyd Cycle Detection:

Time:

O(n)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 19
# ============================================================

"""
Nth From End:

Time:

O(n)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 20
# ============================================================

"""
Merge Sorted Lists:

Time:

O(n + m)

Extra Space:

O(1)

when reusing existing nodes.
"""


# ============================================================
# SOLUTION 21
# ============================================================

"""
A. Middle Node

Fast / Slow


B. Cycle Detection

Fast / Slow


C. Nth From End

Pointer Gap


D. Remove Nth From End

Dummy + Pointer Gap


E. Merge Sorted Lists

Dummy + Tail


F. Reverse

previous
current
next_node
"""


# ============================================================
# SOLUTION 22
# ============================================================

"""
If we change a next reference
too early, we can lose access
to the rest of the linked list.

That is why pointer-update order
is very important.
"""


# ============================================================
# SOLUTION 23
# ============================================================

"""
slow.value == fast.value

checks whether the two nodes
contain equal values.


slow is fast

checks whether both pointers
refer to the exact same Node object.


For cycle detection:

node identity matters.

So:

slow is fast

is the important check.
"""


# ============================================================
# SOLUTION 24
# ============================================================

"""
Possible edge cases:

1. Empty list

2. One-node list

3. Two-node list

4. Removing the head

5. Removing the last node

6. n equals list length

7. n is larger than list length

8. Cycle exists

9. No cycle

10. Lists have different lengths
"""


# ============================================================
# SOLUTION 25
# ============================================================

"""
FAST / SLOW

Use when two different
pointer speeds reveal information.

Examples:

Middle
Cycle Detection


-----------------------------------------


POINTER GAP

Use when one pointer should
stay a fixed distance behind another.

Example:

Nth From End


-----------------------------------------


DUMMY NODE

Use when:

head might change

or

we need an easy starting node.

Examples:

Remove Nth
Merge Lists


-----------------------------------------


REVERSE POINTER PATTERN

Use when the direction of
next references must change.

Uses:

previous
current
next_node
"""


# ============================================================
# FINAL DAY 10 SUMMARY
# ============================================================

"""
DAY 10 PATTERNS


FAST / SLOW

Middle
Cycle


-----------------------------------------


POINTER GAP

Nth From End


-----------------------------------------


DUMMY NODE

Deletion
Merge


-----------------------------------------


REVERSE

previous
current
next_node


-----------------------------------------


MANY LINKED LIST SOLUTIONS

Time:

O(n)

Extra Space:

O(1)
"""