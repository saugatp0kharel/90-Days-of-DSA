"""
============================================================
DAY 13 - SORTING ALGORITHMS
============================================================

Topics:

1. Bubble Sort
2. Optimized Bubble Sort
3. Selection Sort
4. Insertion Sort
5. Python sorted()
6. Python .sort()
7. Ascending / Descending
"""


# ============================================================
# HELPER
# ============================================================

def print_section(title):

    print(
        "\n" + "=" * 50
    )

    print(title)

    print(
        "=" * 50
    )


# ============================================================
# EXAMPLE 1
# BUBBLE SORT
# ============================================================

def bubble_sort(numbers):

    n = len(numbers)

    for i in range(n):

        for j in range(
            0,
            n - i - 1
        ):

            if numbers[j] > numbers[j + 1]:

                numbers[j], numbers[j + 1] = (
                    numbers[j + 1],
                    numbers[j]
                )

    return numbers


print_section(
    "EXAMPLE 1 - BUBBLE SORT"
)

numbers = [
    5,
    3,
    8,
    2
]

print(
    bubble_sort(numbers)
)


# ============================================================
# EXAMPLE 2
# BUBBLE SORT TRACE
# ============================================================

def bubble_sort_trace(numbers):

    n = len(numbers)

    for i in range(n):

        print(
            "\nPass:",
            i + 1
        )

        for j in range(
            0,
            n - i - 1
        ):

            print(
                "Compare:",
                numbers[j],
                "and",
                numbers[j + 1]
            )

            if numbers[j] > numbers[j + 1]:

                numbers[j], numbers[j + 1] = (
                    numbers[j + 1],
                    numbers[j]
                )

                print(
                    "Swap:",
                    numbers
                )

    return numbers


print_section(
    "EXAMPLE 2 - BUBBLE TRACE"
)

bubble_sort_trace(
    [4, 3, 2, 1]
)


# ============================================================
# EXAMPLE 3
# OPTIMIZED BUBBLE SORT
# ============================================================

def bubble_sort_optimized(numbers):

    n = len(numbers)

    for i in range(n):

        swapped = False

        for j in range(
            0,
            n - i - 1
        ):

            if numbers[j] > numbers[j + 1]:

                numbers[j], numbers[j + 1] = (
                    numbers[j + 1],
                    numbers[j]
                )

                swapped = True

        if not swapped:

            break

    return numbers


print_section(
    "EXAMPLE 3 - OPTIMIZED BUBBLE"
)

print(
    bubble_sort_optimized(
        [1, 2, 3, 4, 5]
    )
)


# ============================================================
# EXAMPLE 4
# SELECTION SORT
# ============================================================

def selection_sort(numbers):

    n = len(numbers)

    for i in range(n):

        min_index = i

        for j in range(
            i + 1,
            n
        ):

            if numbers[j] < numbers[min_index]:

                min_index = j

        numbers[i], numbers[min_index] = (
            numbers[min_index],
            numbers[i]
        )

    return numbers


print_section(
    "EXAMPLE 4 - SELECTION SORT"
)

print(
    selection_sort(
        [5, 3, 8, 2]
    )
)


# ============================================================
# EXAMPLE 5
# SELECTION TRACE
# ============================================================

def selection_sort_trace(numbers):

    n = len(numbers)

    for i in range(n):

        min_index = i

        for j in range(
            i + 1,
            n
        ):

            if numbers[j] < numbers[min_index]:

                min_index = j

        print(
            "Minimum for position",
            i,
            "=",
            numbers[min_index]
        )

        numbers[i], numbers[min_index] = (
            numbers[min_index],
            numbers[i]
        )

        print(
            "Array:",
            numbers
        )

    return numbers


print_section(
    "EXAMPLE 5 - SELECTION TRACE"
)

selection_sort_trace(
    [4, 2, 5, 1]
)


# ============================================================
# EXAMPLE 6
# INSERTION SORT
# ============================================================

def insertion_sort(numbers):

    for i in range(
        1,
        len(numbers)
    ):

        current = numbers[i]

        j = i - 1

        while (
            j >= 0
            and
            numbers[j] > current
        ):

            numbers[j + 1] = numbers[j]

            j -= 1

        numbers[j + 1] = current

    return numbers


print_section(
    "EXAMPLE 6 - INSERTION SORT"
)

print(
    insertion_sort(
        [5, 3, 8, 2]
    )
)


# ============================================================
# EXAMPLE 7
# INSERTION TRACE
# ============================================================

def insertion_sort_trace(numbers):

    for i in range(
        1,
        len(numbers)
    ):

        current = numbers[i]

        print(
            "\nCurrent:",
            current
        )

        j = i - 1

        while (
            j >= 0
            and
            numbers[j] > current
        ):

            print(
                "Shift:",
                numbers[j]
            )

            numbers[j + 1] = numbers[j]

            j -= 1

        numbers[j + 1] = current

        print(
            "Array:",
            numbers
        )

    return numbers


print_section(
    "EXAMPLE 7 - INSERTION TRACE"
)

insertion_sort_trace(
    [5, 3, 8, 2]
)


# ============================================================
# EXAMPLE 8
# PYTHON SORTED
# ============================================================

print_section(
    "EXAMPLE 8 - sorted()"
)

numbers = [
    3,
    1,
    2
]

result = sorted(numbers)

print(
    "Original:",
    numbers
)

print(
    "Sorted copy:",
    result
)


# ============================================================
# EXAMPLE 9
# PYTHON .sort()
# ============================================================

print_section(
    "EXAMPLE 9 - .sort()"
)

numbers = [
    3,
    1,
    2
]

numbers.sort()

print(
    numbers
)


# ============================================================
# EXAMPLE 10
# DESCENDING
# ============================================================

print_section(
    "EXAMPLE 10 - DESCENDING"
)

numbers = [
    5,
    1,
    8,
    2
]

numbers.sort(
    reverse=True
)

print(
    numbers
)


# ============================================================
# EXAMPLE 11
# STRINGS
# ============================================================

print_section(
    "EXAMPLE 11 - SORT STRINGS"
)

words = [
    "banana",
    "apple",
    "dog",
    "cat"
]

print(
    sorted(words)
)


# ============================================================
# EXAMPLE 12
# SORT BY LENGTH
# ============================================================

print_section(
    "EXAMPLE 12 - SORT BY LENGTH"
)

words = [
    "elephant",
    "cat",
    "dog",
    "python"
]

print(
    sorted(
        words,
        key=len
    )
)


# ============================================================
# EXAMPLE 13
# COMPARE ALGORITHMS
# ============================================================

original = [
    9,
    4,
    6,
    2,
    8,
    1
]

print_section(
    "EXAMPLE 13 - COMPARISON"
)

print(
    "Bubble:",
    bubble_sort(
        original.copy()
    )
)

print(
    "Selection:",
    selection_sort(
        original.copy()
    )
)

print(
    "Insertion:",
    insertion_sort(
        original.copy()
    )
)

print(
    "Python:",
    sorted(original)
)


# ============================================================
# EXAMPLE 14
# ALREADY SORTED INPUT
# ============================================================

print_section(
    "EXAMPLE 14 - ALREADY SORTED"
)

numbers = [
    1,
    2,
    3,
    4,
    5
]

print(
    bubble_sort_optimized(
        numbers
    )
)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n======================================")
print("DAY 13 EXAMPLES COMPLETE")
print("======================================")

"""
BUBBLE SORT

Compare adjacent values
Swap when needed

Typical:

O(n^2)


-----------------------------------------


SELECTION SORT

Find minimum
Place it in position

O(n^2)


-----------------------------------------


INSERTION SORT

Insert current value into
sorted left section

Best:

O(n)

Worst:

O(n^2)


-----------------------------------------


PYTHON sorted()

Returns new list


-----------------------------------------


PYTHON .sort()

Changes original list


-----------------------------------------


PYTHON SORTING

Highly optimized

Worst-case:

O(n log n)
"""