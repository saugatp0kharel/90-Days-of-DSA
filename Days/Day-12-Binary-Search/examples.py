"""
============================================================
DAY 12 - BINARY SEARCH
============================================================

Topics:

1. Linear Search
2. Iterative Binary Search
3. Recursive Binary Search
4. First Occurrence
5. Last Occurrence
6. Search Insert Position
7. Lower Bound
"""


# ============================================================
# EXAMPLE 1
# LINEAR SEARCH
# ============================================================

def linear_search(numbers, target):

    for index in range(len(numbers)):

        if numbers[index] == target:

            return index

    return -1


numbers = [
    2,
    5,
    8,
    10,
    15,
    20,
    30
]

print("EXAMPLE 1 - LINEAR SEARCH")

print(
    linear_search(
        numbers,
        20
    )
)


# ============================================================
# EXAMPLE 2
# ITERATIVE BINARY SEARCH
# ============================================================

def binary_search(numbers, target):

    left = 0

    right = len(numbers) - 1

    while left <= right:

        mid = (
            left + right
        ) // 2

        if numbers[mid] == target:

            return mid

        elif numbers[mid] < target:

            left = mid + 1

        else:

            right = mid - 1

    return -1


print("\nEXAMPLE 2 - BINARY SEARCH")

print(
    binary_search(
        numbers,
        20
    )
)


# ============================================================
# EXAMPLE 3
# TARGET NOT FOUND
# ============================================================

print("\nEXAMPLE 3 - NOT FOUND")

print(
    binary_search(
        numbers,
        17
    )
)


# ============================================================
# EXAMPLE 4
# BINARY SEARCH TRACE
# ============================================================

def binary_search_trace(
    numbers,
    target
):

    left = 0
    right = len(numbers) - 1

    while left <= right:

        mid = (
            left + right
        ) // 2

        print(
            "Left:",
            left,
            "Right:",
            right,
            "Mid:",
            mid,
            "Value:",
            numbers[mid]
        )

        if numbers[mid] == target:

            return mid

        elif numbers[mid] < target:

            left = mid + 1

        else:

            right = mid - 1

    return -1


print("\nEXAMPLE 4 - TRACE")

print(
    "Result:",
    binary_search_trace(
        numbers,
        15
    )
)


# ============================================================
# EXAMPLE 5
# RECURSIVE BINARY SEARCH
# ============================================================

def binary_search_recursive(
    numbers,
    target,
    left,
    right
):

    if left > right:

        return -1

    mid = (
        left + right
    ) // 2

    if numbers[mid] == target:

        return mid

    if numbers[mid] < target:

        return binary_search_recursive(
            numbers,
            target,
            mid + 1,
            right
        )

    return binary_search_recursive(
        numbers,
        target,
        left,
        mid - 1
    )


print(
    "\nEXAMPLE 5 - RECURSIVE BINARY SEARCH"
)

print(
    binary_search_recursive(
        numbers,
        10,
        0,
        len(numbers) - 1
    )
)


# ============================================================
# EXAMPLE 6
# FIRST OCCURRENCE
# ============================================================

def first_occurrence(
    numbers,
    target
):

    left = 0
    right = len(numbers) - 1

    result = -1

    while left <= right:

        mid = (
            left + right
        ) // 2

        if numbers[mid] == target:

            result = mid

            right = mid - 1

        elif numbers[mid] < target:

            left = mid + 1

        else:

            right = mid - 1

    return result


duplicates = [
    1,
    2,
    2,
    2,
    3,
    4
]

print("\nEXAMPLE 6 - FIRST OCCURRENCE")

print(
    first_occurrence(
        duplicates,
        2
    )
)


# ============================================================
# EXAMPLE 7
# LAST OCCURRENCE
# ============================================================

def last_occurrence(
    numbers,
    target
):

    left = 0
    right = len(numbers) - 1

    result = -1

    while left <= right:

        mid = (
            left + right
        ) // 2

        if numbers[mid] == target:

            result = mid

            left = mid + 1

        elif numbers[mid] < target:

            left = mid + 1

        else:

            right = mid - 1

    return result


print("\nEXAMPLE 7 - LAST OCCURRENCE")

print(
    last_occurrence(
        duplicates,
        2
    )
)


# ============================================================
# EXAMPLE 8
# FIRST AND LAST TOGETHER
# ============================================================

print(
    "\nEXAMPLE 8 - FIRST AND LAST"
)

first = first_occurrence(
    duplicates,
    2
)

last = last_occurrence(
    duplicates,
    2
)

print(
    "First:",
    first
)

print(
    "Last:",
    last
)


# ============================================================
# EXAMPLE 9
# SEARCH INSERT POSITION
# ============================================================

def search_insert(
    numbers,
    target
):

    left = 0
    right = len(numbers) - 1

    while left <= right:

        mid = (
            left + right
        ) // 2

        if numbers[mid] == target:

            return mid

        elif numbers[mid] < target:

            left = mid + 1

        else:

            right = mid - 1

    return left


insert_numbers = [
    1,
    3,
    5,
    6
]

print(
    "\nEXAMPLE 9 - SEARCH INSERT"
)

print(
    search_insert(
        insert_numbers,
        5
    )
)

print(
    search_insert(
        insert_numbers,
        2
    )
)

print(
    search_insert(
        insert_numbers,
        7
    )
)

print(
    search_insert(
        insert_numbers,
        0
    )
)


# ============================================================
# EXAMPLE 10
# LOWER BOUND
# ============================================================

def lower_bound(
    numbers,
    target
):

    left = 0

    right = len(numbers)

    while left < right:

        mid = (
            left + right
        ) // 2

        if numbers[mid] < target:

            left = mid + 1

        else:

            right = mid

    return left


numbers2 = [
    1,
    3,
    3,
    5,
    8
]

print("\nEXAMPLE 10 - LOWER BOUND")

print(
    lower_bound(
        numbers2,
        3
    )
)


# ============================================================
# EXAMPLE 11
# COMPARE NUMBER OF CHECKS
# ============================================================

def linear_search_count(
    numbers,
    target
):

    checks = 0

    for index in range(
        len(numbers)
    ):

        checks += 1

        if numbers[index] == target:

            return index, checks

    return -1, checks


def binary_search_count(
    numbers,
    target
):

    left = 0

    right = len(numbers) - 1

    checks = 0

    while left <= right:

        checks += 1

        mid = (
            left + right
        ) // 2

        if numbers[mid] == target:

            return mid, checks

        elif numbers[mid] < target:

            left = mid + 1

        else:

            right = mid - 1

    return -1, checks


big_numbers = list(
    range(
        1,
        101
    )
)

print(
    "\nEXAMPLE 11 - LINEAR VS BINARY"
)

print(
    "Linear:",
    linear_search_count(
        big_numbers,
        99
    )
)

print(
    "Binary:",
    binary_search_count(
        big_numbers,
        99
    )
)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n======================================")
print("DAY 12 EXAMPLES COMPLETE")
print("======================================")

"""
BINARY SEARCH


REQUIREMENT

Usually sorted data


-----------------------------------------


POINTERS

left
right
mid


-----------------------------------------


MIDDLE

mid = (left + right) // 2


-----------------------------------------


TOO SMALL

left = mid + 1


-----------------------------------------


TOO LARGE

right = mid - 1


-----------------------------------------


TIME

O(log n)


-----------------------------------------


ITERATIVE SPACE

O(1)


-----------------------------------------


RECURSIVE STACK SPACE

O(log n)


-----------------------------------------


FIRST OCCURRENCE

Find target
then continue left


-----------------------------------------


LAST OCCURRENCE

Find target
then continue right
"""