"""
============================================================
DAY 09 PRACTICE
LINKED LISTS
============================================================

Try every question before reading the solutions.

For every problem ask:

1. Where is the head?
2. What does current point to?
3. What does current.next point to?
4. Will I lose the rest of the list?
5. Do I need to change a pointer?
6. What is the Time Complexity?
7. What is the Space Complexity?
"""


# ============================================================
# NODE CLASS FOR PRACTICE
# ============================================================

class Node:

    def __init__(self, value):

        self.value = value

        self.next = None


# ============================================================
# QUESTION 1
# CREATE NODE
# ============================================================

"""
Create a node containing:

10

Print:

value
next

MY SOLUTION:
"""


# ============================================================
# QUESTION 2
# CONNECT TWO NODES
# ============================================================

"""
Create:

10 -> 20 -> None

MY SOLUTION:
"""


# ============================================================
# QUESTION 3
# CONNECT THREE NODES
# ============================================================

"""
Create:

10 -> 20 -> 30 -> None

Set:

head = first node

MY SOLUTION:
"""


# ============================================================
# QUESTION 4
# TRAVERSAL
# ============================================================

"""
Traverse:

10 -> 20 -> 30

Print every value.

Expected:

10
20
30

MY SOLUTION:
"""


# ============================================================
# QUESTION 5
# COUNT NODES
# ============================================================

"""
For:

10 -> 20 -> 30 -> 40

Return:

4

MY SOLUTION:
"""


# ============================================================
# QUESTION 6
# SEARCH
# ============================================================

"""
For:

10 -> 20 -> 30

Search:

20

Expected:

True

MY SOLUTION:
"""


# ============================================================
# QUESTION 7
# SEARCH NOT FOUND
# ============================================================

"""
For:

10 -> 20 -> 30

Search:

100

Expected:

False

MY SOLUTION:
"""


# ============================================================
# QUESTION 8
# INSERT AT BEGINNING
# ============================================================

"""
Start:

10 -> 20 -> 30

Insert:

5

Expected:

5 -> 10 -> 20 -> 30

MY SOLUTION:
"""


# ============================================================
# QUESTION 9
# INSERT AT END
# ============================================================

"""
Start:

10 -> 20 -> 30

Insert:

40

Expected:

10 -> 20 -> 30 -> 40

MY SOLUTION:
"""


# ============================================================
# QUESTION 10
# DELETE FIRST
# ============================================================

"""
Start:

10 -> 20 -> 30

Delete first node.

Expected:

20 -> 30

MY SOLUTION:
"""


# ============================================================
# QUESTION 11
# DELETE BY VALUE
# ============================================================

"""
Start:

10 -> 20 -> 30 -> 40

Delete:

30

Expected:

10 -> 20 -> 40

MY SOLUTION:
"""


# ============================================================
# QUESTION 12
# SUM
# ============================================================

"""
Find the sum:

10 -> 20 -> 30

Expected:

60

MY SOLUTION:
"""


# ============================================================
# QUESTION 13
# MAXIMUM
# ============================================================

"""
Find maximum:

4 -> 10 -> 2 -> 8

Expected:

10

MY SOLUTION:
"""


# ============================================================
# QUESTION 14
# REVERSE
# ============================================================

"""
Reverse:

10 -> 20 -> 30

Expected:

30 -> 20 -> 10

Use:

previous
current
next_node

MY SOLUTION:
"""


# ============================================================
# QUESTION 15
# COMPLEXITY
# ============================================================

"""
Linked List traversal:

Time = ?

Extra Space = ?

MY ANSWER:
"""


# ============================================================
# QUESTION 16
# COMPLEXITY
# ============================================================

"""
Insert at beginning:

Time = ?

MY ANSWER:
"""


# ============================================================
# QUESTION 17
# COMPLEXITY
# ============================================================

"""
Search for a value:

Worst-case Time = ?

MY ANSWER:
"""


# ============================================================
# QUESTION 18
# COMPLEXITY
# ============================================================

"""
Insert at end WITHOUT tail pointer:

Worst-case Time = ?

MY ANSWER:
"""


# ============================================================
# QUESTION 19
# COMPLEXITY
# ============================================================

"""
Reverse Linked List iteratively:

Time = ?

Extra Space = ?

MY ANSWER:
"""


# ============================================================
# QUESTION 20
# ARRAY VS LINKED LIST
# ============================================================

"""
Which is faster for direct index access?

Array or Linked List?

Why?
"""


# ============================================================
# QUESTION 21
# POINTER SAFETY
# ============================================================

"""
When reversing a linked list,
why must we do:

next_node = current.next

before:

current.next = previous

?
"""


# ============================================================
# QUESTION 22
# EMPTY LIST
# ============================================================

"""
What is the value of:

head

in an empty linked list?
"""


# ============================================================
# QUESTION 23
# LAST NODE
# ============================================================

"""
What does:

next

contain in the last node?
"""


# ============================================================
# QUESTION 24
# FIND LAST VALUE
# ============================================================

"""
For:

10 -> 20 -> 30 -> 40

Return the last value.

Expected:

40

MY SOLUTION:
"""


# ============================================================
# QUESTION 25
# PATTERN RECOGNITION
# ============================================================

"""
Match the operation:

A. Traverse
B. Insert beginning
C. Delete a middle node
D. Reverse
E. Search

Choose the important idea:

- Follow current.next
- new_node.next = head
- Skip a node
- previous/current/next_node
- Compare each node value
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
# SOLUTION 1
# ============================================================

node = Node(10)

print(node.value)

print(node.next)


# ============================================================
# SOLUTION 2
# ============================================================

node1 = Node(10)

node2 = Node(20)

node1.next = node2

head = node1


# ============================================================
# SOLUTION 3
# ============================================================

node1 = Node(10)

node2 = Node(20)

node3 = Node(30)

node1.next = node2

node2.next = node3

head = node1


# ============================================================
# SOLUTION 4
# ============================================================

current = head

while current:

    print(
        current.value
    )

    current = current.next


# ============================================================
# SOLUTION 5
# ============================================================

def count_nodes(head):

    count = 0

    current = head

    while current:

        count += 1

        current = current.next

    return count


# ============================================================
# SOLUTION 6 AND 7
# ============================================================

def search(head, target):

    current = head

    while current:

        if current.value == target:

            return True

        current = current.next

    return False


# ============================================================
# SOLUTION 8
# ============================================================

def insert_beginning(head, value):

    new_node = Node(value)

    new_node.next = head

    return new_node


# ============================================================
# SOLUTION 9
# ============================================================

def insert_end(head, value):

    new_node = Node(value)

    if head is None:

        return new_node

    current = head

    while current.next:

        current = current.next

    current.next = new_node

    return head


# ============================================================
# SOLUTION 10
# ============================================================

def delete_first(head):

    if head is None:

        return None

    return head.next


# ============================================================
# SOLUTION 11
# ============================================================

def delete_value(head, target):

    if head is None:

        return None

    if head.value == target:

        return head.next

    current = head

    while current.next:

        if current.next.value == target:

            current.next = current.next.next

            return head

        current = current.next

    return head


# ============================================================
# SOLUTION 12
# ============================================================

def linked_list_sum(head):

    total = 0

    current = head

    while current:

        total += current.value

        current = current.next

    return total


# ============================================================
# SOLUTION 13
# ============================================================

def linked_list_max(head):

    if head is None:

        return None

    largest = head.value

    current = head.next

    while current:

        if current.value > largest:

            largest = current.value

        current = current.next

    return largest


# ============================================================
# SOLUTION 14
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
# SOLUTION 15
# ============================================================

"""
Traversal:

Time:

O(n)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 16
# ============================================================

"""
Insert at beginning:

O(1)
"""


# ============================================================
# SOLUTION 17
# ============================================================

"""
Search:

Worst case:

O(n)
"""


# ============================================================
# SOLUTION 18
# ============================================================

"""
Insert at end without tail:

O(n)
"""


# ============================================================
# SOLUTION 19
# ============================================================

"""
Reverse:

Time:

O(n)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 20
# ============================================================

"""
ARRAY

is faster for direct index access.

Array:

O(1)

Linked List:

O(n)

because linked lists must follow
nodes from the head.
"""


# ============================================================
# SOLUTION 21
# ============================================================

"""
We save:

next_node = current.next

because after:

current.next = previous

the original next reference
has been changed.

Without saving it first,
we could lose access to
the rest of the linked list.
"""


# ============================================================
# SOLUTION 22
# ============================================================

"""
Empty linked list:

head = None
"""


# ============================================================
# SOLUTION 23
# ============================================================

"""
The final node has:

next = None
"""


# ============================================================
# SOLUTION 24
# ============================================================

def last_value(head):

    if head is None:

        return None

    current = head

    while current.next:

        current = current.next

    return current.value


# ============================================================
# SOLUTION 25
# ============================================================

"""
A. Traverse

Follow current.next


B. Insert Beginning

new_node.next = head


C. Delete Middle Node

Skip a node


D. Reverse

previous
current
next_node


E. Search

Compare each node value
"""


# ============================================================
# FINAL DAY 9 SUMMARY
# ============================================================

"""
LINKED LIST


NODE

value + next


-----------------------------------------


HEAD

first node


-----------------------------------------


TRAVERSAL

follow current.next


-----------------------------------------


INSERT BEGINNING

O(1)


-----------------------------------------


SEARCH

O(n)


-----------------------------------------


REVERSE

previous
current
next_node

Time:

O(n)

Space:

O(1)
"""