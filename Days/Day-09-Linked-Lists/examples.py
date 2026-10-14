"""
============================================================
DAY 09 - LINKED LISTS
============================================================

Topics:

1. Node
2. Connecting Nodes
3. Head
4. Traversal
5. Insert Beginning
6. Insert End
7. Search
8. Length
9. Delete First
10. Delete by Value
11. Reverse Linked List
"""


# ============================================================
# NODE CLASS
# ============================================================

class Node:

    def __init__(self, value):

        self.value = value

        self.next = None


# ============================================================
# EXAMPLE 1
# CREATE ONE NODE
# ============================================================

node = Node(10)

print("EXAMPLE 1 - CREATE NODE")

print(
    "Value:",
    node.value
)

print(
    "Next:",
    node.next
)


# ============================================================
# EXAMPLE 2
# CONNECT NODES
# ============================================================

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

head = node1

print("\nEXAMPLE 2 - CONNECT NODES")

print(
    head.value
)

print(
    head.next.value
)

print(
    head.next.next.value
)


# ============================================================
# EXAMPLE 3
# MANUAL TRAVERSAL
# ============================================================

print("\nEXAMPLE 3 - TRAVERSAL")

current = head

while current:

    print(
        current.value
    )

    current = current.next


# ============================================================
# LINKED LIST CLASS
# ============================================================

class LinkedList:

    def __init__(self):

        self.head = None


    # ========================================================
    # INSERT AT BEGINNING
    # ========================================================

    def insert_at_beginning(self, value):

        new_node = Node(value)

        new_node.next = self.head

        self.head = new_node


    # ========================================================
    # INSERT AT END
    # ========================================================

    def insert_at_end(self, value):

        new_node = Node(value)

        if self.head is None:

            self.head = new_node

            return

        current = self.head

        while current.next:

            current = current.next

        current.next = new_node


    # ========================================================
    # PRINT LIST
    # ========================================================

    def print_list(self):

        current = self.head

        while current:

            print(
                current.value,
                end=" -> "
            )

            current = current.next

        print("None")


    # ========================================================
    # SEARCH
    # ========================================================

    def search(self, target):

        current = self.head

        while current:

            if current.value == target:

                return True

            current = current.next

        return False


    # ========================================================
    # LENGTH
    # ========================================================

    def length(self):

        count = 0

        current = self.head

        while current:

            count += 1

            current = current.next

        return count


    # ========================================================
    # DELETE FIRST
    # ========================================================

    def delete_first(self):

        if self.head is None:

            return

        self.head = self.head.next


    # ========================================================
    # DELETE BY VALUE
    # ========================================================

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


    # ========================================================
    # REVERSE
    # ========================================================

    def reverse(self):

        previous = None

        current = self.head

        while current:

            next_node = current.next

            current.next = previous

            previous = current

            current = next_node

        self.head = previous


# ============================================================
# EXAMPLE 4
# INSERT AT END
# ============================================================

linked_list = LinkedList()

linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)

print("\nEXAMPLE 4 - INSERT AT END")

linked_list.print_list()


# ============================================================
# EXAMPLE 5
# INSERT AT BEGINNING
# ============================================================

linked_list.insert_at_beginning(5)

print("\nEXAMPLE 5 - INSERT AT BEGINNING")

linked_list.print_list()


# ============================================================
# EXAMPLE 6
# SEARCH
# ============================================================

print("\nEXAMPLE 6 - SEARCH")

print(
    "20 found:",
    linked_list.search(20)
)

print(
    "100 found:",
    linked_list.search(100)
)


# ============================================================
# EXAMPLE 7
# LENGTH
# ============================================================

print("\nEXAMPLE 7 - LENGTH")

print(
    linked_list.length()
)


# ============================================================
# EXAMPLE 8
# DELETE FIRST
# ============================================================

linked_list.delete_first()

print("\nEXAMPLE 8 - DELETE FIRST")

linked_list.print_list()


# ============================================================
# EXAMPLE 9
# DELETE VALUE
# ============================================================

linked_list.delete_value(20)

print("\nEXAMPLE 9 - DELETE VALUE 20")

linked_list.print_list()


# ============================================================
# EXAMPLE 10
# ADD MORE VALUES
# ============================================================

linked_list.insert_at_end(40)
linked_list.insert_at_end(50)

print("\nEXAMPLE 10 - BEFORE REVERSE")

linked_list.print_list()


# ============================================================
# EXAMPLE 11
# REVERSE LINKED LIST
# ============================================================

linked_list.reverse()

print("\nEXAMPLE 11 - AFTER REVERSE")

linked_list.print_list()


# ============================================================
# EXAMPLE 12
# TRAVERSE AND SUM
# ============================================================

def sum_linked_list(head):

    total = 0

    current = head

    while current:

        total += current.value

        current = current.next

    return total


print("\nEXAMPLE 12 - SUM")

print(
    sum_linked_list(
        linked_list.head
    )
)


# ============================================================
# EXAMPLE 13
# FIND MAX
# ============================================================

def find_max(head):

    if head is None:

        return None

    largest = head.value

    current = head.next

    while current:

        if current.value > largest:

            largest = current.value

        current = current.next

    return largest


print("\nEXAMPLE 13 - MAX")

print(
    find_max(
        linked_list.head
    )
)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n======================================")
print("DAY 09 EXAMPLES COMPLETE")
print("======================================")

"""
LINKED LIST


NODE

value
next


-----------------------------------------


HEAD

First node


-----------------------------------------


TRAVERSAL

current = head

while current:

    current = current.next


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

O(n) Time

O(1) Extra Space
"""