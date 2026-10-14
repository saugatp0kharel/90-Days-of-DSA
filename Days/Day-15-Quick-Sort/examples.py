"""
============================================================
DAY 15 - QUICK SORT
============================================================

Topics:

1. Functional Quick Sort
2. Pivot
3. Partitioning
4. Lomuto Partition
5. In-place Quick Sort
6. Duplicates
7. Complexity intuition
"""


# ============================================================
# EXAMPLE 1
# SIMPLE FUNCTIONAL QUICK SORT
# ============================================================

def quick_sort(numbers):

    if len(numbers) <= 1:

        return numbers

    pivot = numbers[
        len(numbers) // 2
    ]

    less = []

    equal = []

    greater = []

    for number in numbers:

        if number < pivot:

            less.append(number)

        elif number == pivot:

            equal.append(number)

        else:

            greater.append(number)

    return (
        quick_sort(less)
        +
        equal
        +
        quick_sort(greater)
    )


print("EXAMPLE 1 - FUNCTIONAL QUICK SORT")

print(
    quick_sort(
        [8, 3, 5, 1, 7, 2]
    )
)


# ============================================================
# EXAMPLE 2
# SHOW PARTITIONS
# ============================================================

def show_partition(numbers):

    if len(numbers) <= 1:

        return

    pivot = numbers[
        len(numbers) // 2
    ]

    less = []
    equal = []
    greater = []

    for number in numbers:

        if number < pivot:

            less.append(number)

        elif number == pivot:

            equal.append(number)

        else:

            greater.append(number)

    print(
        "Original:",
        numbers
    )

    print(
        "Pivot:",
        pivot
    )

    print(
        "Less:",
        less
    )

    print(
        "Equal:",
        equal
    )

    print(
        "Greater:",
        greater
    )


print("\nEXAMPLE 2 - PARTITION")

show_partition(
    [7, 2, 5, 1, 9, 3]
)


# ============================================================
# EXAMPLE 3
# QUICK SORT TRACE
# ============================================================

def quick_sort_trace(
    numbers,
    depth=0
):

    indent = "  " * depth

    print(
        indent,
        "Quick Sort:",
        numbers
    )

    if len(numbers) <= 1:

        print(
            indent,
            "Base:",
            numbers
        )

        return numbers

    pivot = numbers[
        len(numbers) // 2
    ]

    less = []
    equal = []
    greater = []

    for number in numbers:

        if number < pivot:

            less.append(number)

        elif number == pivot:

            equal.append(number)

        else:

            greater.append(number)

    print(
        indent,
        "Pivot:",
        pivot
    )

    print(
        indent,
        "Less:",
        less
    )

    print(
        indent,
        "Equal:",
        equal
    )

    print(
        indent,
        "Greater:",
        greater
    )

    sorted_less = quick_sort_trace(
        less,
        depth + 1
    )

    sorted_greater = quick_sort_trace(
        greater,
        depth + 1
    )

    result = (
        sorted_less
        +
        equal
        +
        sorted_greater
    )

    print(
        indent,
        "Combined:",
        result
    )

    return result


print("\nEXAMPLE 3 - TRACE")

quick_sort_trace(
    [6, 2, 8, 3, 5]
)


# ============================================================
# LOMUTO PARTITION
# ============================================================

def partition(
    numbers,
    low,
    high
):

    pivot = numbers[high]

    i = low - 1

    for j in range(
        low,
        high
    ):

        if numbers[j] <= pivot:

            i += 1

            numbers[i], numbers[j] = (
                numbers[j],
                numbers[i]
            )

    numbers[i + 1], numbers[high] = (
        numbers[high],
        numbers[i + 1]
    )

    return i + 1


# ============================================================
# EXAMPLE 4
# PARTITION ONLY
# ============================================================

numbers = [
    4,
    2,
    7,
    3,
    6
]

print("\nEXAMPLE 4 - LOMUTO PARTITION")

pivot_index = partition(
    numbers,
    0,
    len(numbers) - 1
)

print(
    "Array:",
    numbers
)

print(
    "Pivot index:",
    pivot_index
)

print(
    "Pivot value:",
    numbers[pivot_index]
)


# ============================================================
# IN-PLACE QUICK SORT
# ============================================================

def quick_sort_in_place(
    numbers,
    low,
    high
):

    if low < high:

        pivot_index = partition(
            numbers,
            low,
            high
        )

        quick_sort_in_place(
            numbers,
            low,
            pivot_index - 1
        )

        quick_sort_in_place(
            numbers,
            pivot_index + 1,
            high
        )


# ============================================================
# EXAMPLE 5
# IN-PLACE QUICK SORT
# ============================================================

numbers = [
    8,
    3,
    1,
    7,
    0,
    10,
    2
]

print("\nEXAMPLE 5 - IN-PLACE QUICK SORT")

print(
    "Before:",
    numbers
)

quick_sort_in_place(
    numbers,
    0,
    len(numbers) - 1
)

print(
    "After:",
    numbers
)


# ============================================================
# EXAMPLE 6
# DUPLICATES
# ============================================================

print("\nEXAMPLE 6 - DUPLICATES")

print(
    quick_sort(
        [4, 2, 4, 1, 4, 2]
    )
)


# ============================================================
# EXAMPLE 7
# NEGATIVE NUMBERS
# ============================================================

print("\nEXAMPLE 7 - NEGATIVES")

print(
    quick_sort(
        [-3, 5, 0, -1, 2]
    )
)


# ============================================================
# EXAMPLE 8
# ALREADY SORTED
# ============================================================

print("\nEXAMPLE 8 - ALREADY SORTED")

print(
    quick_sort(
        [1, 2, 3, 4, 5]
    )
)


# ============================================================
# EXAMPLE 9
# REVERSE SORTED
# ============================================================

print("\nEXAMPLE 9 - REVERSE SORTED")

print(
    quick_sort(
        [5, 4, 3, 2, 1]
    )
)


# ============================================================
# EXAMPLE 10
# EMPTY
# ============================================================

print("\nEXAMPLE 10 - EMPTY")

print(
    quick_sort([])
)


# ============================================================
# EXAMPLE 11
# ONE VALUE
# ============================================================

print("\nEXAMPLE 11 - ONE VALUE")

print(
    quick_sort(
        [100]
    )
)


# ============================================================
# EXAMPLE 12
# STRINGS
# ============================================================

print("\nEXAMPLE 12 - STRINGS")

print(
    quick_sort(
        [
            "dog",
            "apple",
            "cat",
            "banana"
        ]
    )
)


# ============================================================
# EXAMPLE 13
# COMPARE WITH MERGE SORT IDEA
# ============================================================

print("\nEXAMPLE 13 - CORE DIFFERENCE")

print(
    """
Merge Sort:

Split first
Then merge sorted pieces


Quick Sort:

Choose pivot
Partition first
Then recursively sort partitions
"""
)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n======================================")
print("DAY 15 EXAMPLES COMPLETE")
print("======================================")

"""
QUICK SORT


PIVOT

Value used to divide array


-----------------------------------------


PARTITION

Smaller
Pivot
Larger


-----------------------------------------


AVERAGE TIME

O(n log n)


-----------------------------------------


WORST TIME

O(n^2)


-----------------------------------------


GOOD PIVOT

Balanced partitions


-----------------------------------------


IN-PLACE VERSION

Partition with swaps


-----------------------------------------


MAIN PATTERN

Choose Pivot
Partition
Recurse Left
Recurse Right
"""