"""
============================================================
DAY 10 - LINKED LIST PROBLEMS
FAST & SLOW POINTERS
============================================================
"""


# ============================================================
# NODE
# ============================================================

class Node:

    def __init__(self, value):

        self.value = value
        self.next = None


# ============================================================
# HELPER
# BUILD LINKED LIST
# ============================================================

def build_linked_list(values):

    if not values:
        return None

    head = Node(values[0])

    current = head

    for value in values[1:]:

        current.next = Node(value)

        current = current.next

    return head


# ============================================================
# HELPER
# PRINT LINKED LIST
# ============================================================

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
# EXAMPLE 1
# FIND MIDDLE
# ============================================================

def find_middle(head):

    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next

        fast = fast.next.next

    return slow


head = build_linked_list(
    [1, 2, 3, 4, 5]
)

print("EXAMPLE 1 - MIDDLE NODE")

middle = find_middle(head)

print(
    middle.value
)


# ============================================================
# EXAMPLE 2
# EVEN-LENGTH MIDDLE
# ============================================================

head = build_linked_list(
    [1, 2, 3, 4]
)

print("\nEXAMPLE 2 - EVEN LENGTH MIDDLE")

middle = find_middle(head)

print(
    middle.value
)


# ============================================================
# EXAMPLE 3
# CYCLE USING SET
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


head = build_linked_list(
    [1, 2, 3, 4]
)

print("\nEXAMPLE 3 - CYCLE USING SET")

print(
    has_cycle_set(head)
)


# ============================================================
# EXAMPLE 4
# FLOYD CYCLE DETECTION
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


print("\nEXAMPLE 4 - FLOYD NO CYCLE")

print(
    has_cycle(head)
)


# ============================================================
# EXAMPLE 5
# CREATE A CYCLE
# ============================================================

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

# Create cycle:
# 4 -> 2

node4.next = node2

print("\nEXAMPLE 5 - FLOYD WITH CYCLE")

print(
    has_cycle(node1)
)


# ============================================================
# EXAMPLE 6
# FIND NTH FROM BEGINNING
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


head = build_linked_list(
    [10, 20, 30, 40, 50]
)

print("\nEXAMPLE 6 - NTH FROM BEGINNING")

node = find_nth(
    head,
    3
)

print(
    node.value
)


# ============================================================
# EXAMPLE 7
# NTH FROM END
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


print("\nEXAMPLE 7 - NTH FROM END")

node = nth_from_end(
    head,
    2
)

print(
    node.value
)


# ============================================================
# EXAMPLE 8
# REMOVE NTH FROM END
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


head = build_linked_list(
    [1, 2, 3, 4, 5]
)

print("\nEXAMPLE 8 - BEFORE REMOVE")

print_list(head)

head = remove_nth_from_end(
    head,
    2
)

print(
    "AFTER REMOVING 2ND FROM END"
)

print_list(head)


# ============================================================
# EXAMPLE 9
# MERGE SORTED LINKED LISTS
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


list1 = build_linked_list(
    [1, 3, 5]
)

list2 = build_linked_list(
    [2, 4, 6]
)

print("\nEXAMPLE 9 - MERGE SORTED LISTS")

merged = merge_sorted_lists(
    list1,
    list2
)

print_list(
    merged
)


# ============================================================
# EXAMPLE 10
# REVERSE LINKED LIST
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


head = build_linked_list(
    [10, 20, 30, 40]
)

print("\nEXAMPLE 10 - BEFORE REVERSE")

print_list(head)

head = reverse_list(head)

print(
    "AFTER REVERSE"
)

print_list(head)


# ============================================================
# EXAMPLE 11
# FIND MIDDLE THEN PRINT FROM MIDDLE
# ============================================================

head = build_linked_list(
    [5, 10, 15, 20, 25]
)

middle = find_middle(head)

print(
    "\nEXAMPLE 11 - PRINT FROM MIDDLE"
)

print_list(
    middle
)


# ============================================================
# EXAMPLE 12
# NTH FROM END EDGE CASE
# ============================================================

head = build_linked_list(
    [1, 2, 3]
)

node = nth_from_end(
    head,
    5
)

print(
    "\nEXAMPLE 12 - INVALID N"
)

print(node)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n======================================")
print("DAY 10 EXAMPLES COMPLETE")
print("======================================")

"""
FAST AND SLOW POINTERS

slow = slow.next

fast = fast.next.next


USE FOR:

Middle Node
Cycle Detection


-----------------------------------------


POINTER GAP

Move first pointer ahead by n

Use for:

Nth Node From End


-----------------------------------------


DUMMY NODE

dummy.next = head

Use for:

Deletion
Merge


-----------------------------------------


REVERSE

previous
current
next_node


-----------------------------------------


COMMON COMPLEXITY

Time:

O(n)

Extra Space:

O(1)

for many pointer-based solutions.
"""