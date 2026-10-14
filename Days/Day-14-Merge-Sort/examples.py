"""
============================================================
DAY 14 - MERGE SORT
DIVIDE AND CONQUER
============================================================
"""


# ============================================================
# EXAMPLE 1
# MERGE TWO SORTED ARRAYS
# ============================================================

def merge(left, right):

    result = []

    i = 0
    j = 0

    while (
        i < len(left)
        and
        j < len(right)
    ):

        if left[i] <= right[j]:

            result.append(
                left[i]
            )

            i += 1

        else:

            result.append(
                right[j]
            )

            j += 1

    while i < len(left):

        result.append(
            left[i]
        )

        i += 1

    while j < len(right):

        result.append(
            right[j]
        )

        j += 1

    return result


print(
    "EXAMPLE 1 - MERGE TWO SORTED ARRAYS"
)

print(
    merge(
        [2, 5, 8],
        [1, 3, 7]
    )
)


# ============================================================
# EXAMPLE 2
# SIMPLE MERGE SORT
# ============================================================

def merge_sort(numbers):

    if len(numbers) <= 1:

        return numbers

    mid = len(numbers) // 2

    left_half = numbers[:mid]

    right_half = numbers[mid:]

    sorted_left = merge_sort(
        left_half
    )

    sorted_right = merge_sort(
        right_half
    )

    return merge(
        sorted_left,
        sorted_right
    )


print(
    "\nEXAMPLE 2 - MERGE SORT"
)

numbers = [
    8,
    3,
    5,
    1,
    9,
    2
]

print(
    merge_sort(numbers)
)


# ============================================================
# EXAMPLE 3
# ORIGINAL LIST DOES NOT CHANGE
# ============================================================

numbers = [
    5,
    2,
    8,
    1
]

sorted_numbers = merge_sort(
    numbers
)

print(
    "\nEXAMPLE 3 - ORIGINAL VS SORTED"
)

print(
    "Original:",
    numbers
)

print(
    "Sorted:",
    sorted_numbers
)


# ============================================================
# EXAMPLE 4
# MERGE TRACE
# ============================================================

def merge_trace(left, right):

    result = []

    i = 0
    j = 0

    print(
        "\nMerging:",
        left,
        "and",
        right
    )

    while (
        i < len(left)
        and
        j < len(right)
    ):

        print(
            "Compare:",
            left[i],
            "and",
            right[j]
        )

        if left[i] <= right[j]:

            result.append(
                left[i]
            )

            print(
                "Take left:",
                left[i]
            )

            i += 1

        else:

            result.append(
                right[j]
            )

            print(
                "Take right:",
                right[j]
            )

            j += 1

        print(
            "Result:",
            result
        )

    result.extend(
        left[i:]
    )

    result.extend(
        right[j:]
    )

    print(
        "Final merge:",
        result
    )

    return result


print(
    "\nEXAMPLE 4 - MERGE TRACE"
)

merge_trace(
    [2, 5, 8],
    [1, 3, 7]
)


# ============================================================
# EXAMPLE 5
# MERGE SORT TRACE
# ============================================================

def merge_sort_trace(
    numbers,
    depth=0
):

    indent = "  " * depth

    print(
        indent,
        "merge_sort:",
        numbers
    )

    if len(numbers) <= 1:

        print(
            indent,
            "Base case:",
            numbers
        )

        return numbers

    mid = len(numbers) // 2

    left = merge_sort_trace(
        numbers[:mid],
        depth + 1
    )

    right = merge_sort_trace(
        numbers[mid:],
        depth + 1
    )

    merged = merge(
        left,
        right
    )

    print(
        indent,
        "Merged:",
        merged
    )

    return merged


print(
    "\nEXAMPLE 5 - RECURSION TRACE"
)

merge_sort_trace(
    [6, 2, 4, 1]
)


# ============================================================
# EXAMPLE 6
# EMPTY LIST
# ============================================================

print(
    "\nEXAMPLE 6 - EMPTY LIST"
)

print(
    merge_sort([])
)


# ============================================================
# EXAMPLE 7
# ONE VALUE
# ============================================================

print(
    "\nEXAMPLE 7 - ONE VALUE"
)

print(
    merge_sort(
        [10]
    )
)


# ============================================================
# EXAMPLE 8
# ALREADY SORTED
# ============================================================

print(
    "\nEXAMPLE 8 - ALREADY SORTED"
)

print(
    merge_sort(
        [1, 2, 3, 4, 5]
    )
)


# ============================================================
# EXAMPLE 9
# REVERSE SORTED
# ============================================================

print(
    "\nEXAMPLE 9 - REVERSE SORTED"
)

print(
    merge_sort(
        [5, 4, 3, 2, 1]
    )
)


# ============================================================
# EXAMPLE 10
# DUPLICATES
# ============================================================

print(
    "\nEXAMPLE 10 - DUPLICATES"
)

print(
    merge_sort(
        [4, 2, 4, 1, 2, 3]
    )
)


# ============================================================
# EXAMPLE 11
# NEGATIVE VALUES
# ============================================================

print(
    "\nEXAMPLE 11 - NEGATIVES"
)

print(
    merge_sort(
        [-3, 5, -1, 0, 2]
    )
)


# ============================================================
# EXAMPLE 12
# MERGE WITH ONE SIDE EMPTY
# ============================================================

print(
    "\nEXAMPLE 12 - EMPTY SIDE"
)

print(
    merge(
        [],
        [1, 2, 3]
    )
)


# ============================================================
# EXAMPLE 13
# STRINGS
# ============================================================

print(
    "\nEXAMPLE 13 - STRINGS"
)

print(
    merge_sort(
        [
            "dog",
            "apple",
            "cat",
            "banana"
        ]
    )
)


# ============================================================
# EXAMPLE 14
# COMPARE WITH PYTHON SORT
# ============================================================

numbers = [
    9,
    2,
    7,
    4,
    1,
    8
]

print(
    "\nEXAMPLE 14 - COMPARE RESULTS"
)

print(
    "Merge Sort:",
    merge_sort(numbers)
)

print(
    "Python sorted:",
    sorted(numbers)
)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n======================================")
print("DAY 14 EXAMPLES COMPLETE")
print("======================================")

"""
MERGE SORT


DIVIDE

Split array into halves


-----------------------------------------


CONQUER

Recursively sort halves


-----------------------------------------


COMBINE

Merge sorted halves


-----------------------------------------


BASE CASE

len(numbers) <= 1


-----------------------------------------


MERGE

Two pointers:

i
j


-----------------------------------------


TIME COMPLEXITY

Best:

O(n log n)

Average:

O(n log n)

Worst:

O(n log n)


-----------------------------------------


EXTRA SPACE

O(n)


-----------------------------------------


KEY PATTERN

Base
Split
Recurse
Merge
"""