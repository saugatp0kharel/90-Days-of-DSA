"""
============================================================
DAY 03 - ARRAY PROBLEMS AND TWO POINTERS
============================================================

90 Days of Data Structures and Algorithms

This file contains clear working examples of:

1. Find Sum
2. Find Maximum
3. Find Minimum
4. Count Occurrences
5. Contains Duplicate
6. Reverse Array Using Slicing
7. Reverse Array Using Two Pointers
8. Palindrome
9. Move Zeros
10. Second Largest
11. Pair Sum
12. Brute Force vs Optimized Approach

For every example, look at:

- What problem are we solving?
- Why does the solution work?
- What is the Time Complexity?
- What is the Space Complexity?
"""


# ============================================================
# EXAMPLE 1
# FIND SUM
# ============================================================

def find_sum(numbers):
    """
    Problem:
    Find the total sum of all numbers.

    Example:
    [5, 10, 15, 20, 25]

    Output:
    75

    Time Complexity:
    O(n)

    Extra Space:
    O(1)
    """

    total = 0

    for number in numbers:
        total += number

    return total


numbers = [5, 10, 15, 20, 25]

print("EXAMPLE 1 - FIND SUM")
print(find_sum(numbers))


# ============================================================
# EXAMPLE 2
# FIND MAXIMUM
# ============================================================

def find_maximum(numbers):
    """
    Problem:
    Find the largest value without using max().

    Time:
    O(n)

    Space:
    O(1)
    """

    largest = numbers[0]

    for number in numbers:

        if number > largest:
            largest = number

    return largest


numbers = [14, 3, 99, 21, 7]

print("\nEXAMPLE 2 - FIND MAXIMUM")
print(find_maximum(numbers))


# ============================================================
# EXAMPLE 3
# FIND MINIMUM
# ============================================================

def find_minimum(numbers):
    """
    Problem:
    Find the smallest value without using min().

    Time:
    O(n)

    Space:
    O(1)
    """

    smallest = numbers[0]

    for number in numbers:

        if number < smallest:
            smallest = number

    return smallest


numbers = [14, 3, 99, 21, 7]

print("\nEXAMPLE 3 - FIND MINIMUM")
print(find_minimum(numbers))


# ============================================================
# EXAMPLE 4
# COUNT OCCURRENCES
# ============================================================

def count_occurrences(numbers, target):
    """
    Problem:
    Count how many times target appears.

    Example:
    [1, 2, 3, 2, 4, 2, 5]

    target = 2

    Output:
    3

    Time:
    O(n)

    Space:
    O(1)
    """

    count = 0

    for number in numbers:

        if number == target:
            count += 1

    return count


numbers = [1, 2, 3, 2, 4, 2, 5]

print("\nEXAMPLE 4 - COUNT OCCURRENCES")
print(count_occurrences(numbers, 2))


# ============================================================
# EXAMPLE 5
# CONTAINS DUPLICATE
# ============================================================

def contains_duplicate(numbers):
    """
    Problem:
    Check whether any value appears more than once.

    We use a set to remember values we already saw.

    Average Time:
    O(n)

    Space:
    O(n)
    """

    seen = set()

    for number in numbers:

        if number in seen:
            return True

        seen.add(number)

    return False


print("\nEXAMPLE 5 - CONTAINS DUPLICATE")

print(
    contains_duplicate(
        [1, 2, 3, 4, 2]
    )
)

print(
    contains_duplicate(
        [1, 2, 3, 4, 5]
    )
)


# ============================================================
# EXAMPLE 6
# REVERSE ARRAY USING SLICING
# ============================================================

def reverse_with_slicing(numbers):
    """
    Python slicing creates a new reversed list.

    Time:
    O(n)

    Space:
    O(n)
    """

    return numbers[::-1]


numbers = [1, 2, 3, 4, 5]

print("\nEXAMPLE 6 - REVERSE USING SLICING")
print(reverse_with_slicing(numbers))


# ============================================================
# EXAMPLE 7
# REVERSE ARRAY USING TWO POINTERS
# ============================================================

def reverse_array(numbers):
    """
    Use two pointers:

    left
    right

    Swap both ends and move inward.

    This modifies the original list.

    Time:
    O(n)

    Extra Space:
    O(1)
    """

    left = 0

    right = len(numbers) - 1

    while left < right:

        numbers[left], numbers[right] = \
            numbers[right], numbers[left]

        left += 1

        right -= 1

    return numbers


numbers = [1, 2, 3, 4, 5]

print("\nEXAMPLE 7 - REVERSE USING TWO POINTERS")
print(reverse_array(numbers))


# ============================================================
# EXAMPLE 8
# PALINDROME
# ============================================================

def is_palindrome(numbers):
    """
    A palindrome reads the same from both sides.

    Example:

    [1, 2, 3, 2, 1]

    Use two pointers.

    Time:
    O(n)

    Space:
    O(1)
    """

    left = 0

    right = len(numbers) - 1

    while left < right:

        if numbers[left] != numbers[right]:
            return False

        left += 1

        right -= 1

    return True


print("\nEXAMPLE 8 - PALINDROME")

print(
    is_palindrome(
        [1, 2, 3, 2, 1]
    )
)

print(
    is_palindrome(
        [1, 2, 3, 4]
    )
)


# ============================================================
# EXAMPLE 9
# MOVE ZEROS
# ============================================================

def move_zeros(numbers):
    """
    Move all zeros to the end.

    Keep the order of non-zero values.

    Example:

    [0, 1, 0, 3, 12]

    becomes:

    [1, 3, 12, 0, 0]

    Time:
    O(n)

    Extra Space:
    O(1)
    """

    insert_position = 0

    for number in numbers:

        if number != 0:

            numbers[insert_position] = number

            insert_position += 1

    while insert_position < len(numbers):

        numbers[insert_position] = 0

        insert_position += 1

    return numbers


print("\nEXAMPLE 9 - MOVE ZEROS")

print(
    move_zeros(
        [0, 1, 0, 3, 12]
    )
)


# ============================================================
# EXAMPLE 10
# SECOND LARGEST
# ============================================================

def second_largest(numbers):
    """
    Find the second-largest distinct value.

    Example:

    [10, 5, 20, 8, 15]

    Largest:
    20

    Second Largest:
    15

    Time:
    O(n)

    Space:
    O(1)
    """

    largest = float("-inf")

    second = float("-inf")

    for number in numbers:

        if number > largest:

            second = largest

            largest = number

        elif number > second and number != largest:

            second = number

    return second


print("\nEXAMPLE 10 - SECOND LARGEST")

print(
    second_largest(
        [10, 5, 20, 8, 15]
    )
)


# ============================================================
# EXAMPLE 11
# PAIR SUM - TWO POINTERS
# ============================================================

def pair_sum(numbers, target):
    """
    IMPORTANT:
    This solution assumes the list is sorted.

    Example:

    [1, 2, 4, 6, 10]

    target = 8

    Answer:

    [2, 6]

    Time:
    O(n)

    Space:
    O(1)
    """

    left = 0

    right = len(numbers) - 1

    while left < right:

        current_sum = (
            numbers[left]
            +
            numbers[right]
        )

        if current_sum == target:

            return [
                numbers[left],
                numbers[right]
            ]

        elif current_sum < target:

            left += 1

        else:

            right -= 1

    return None


print("\nEXAMPLE 11 - PAIR SUM")

print(
    pair_sum(
        [1, 2, 4, 6, 10],
        8
    )
)


# ============================================================
# EXAMPLE 12
# BRUTE FORCE PAIR SUM
# ============================================================

def pair_sum_brute_force(numbers, target):
    """
    Brute Force:

    Compare every possible pair.

    Time:
    O(n^2)

    Space:
    O(1)
    """

    for i in range(len(numbers)):

        for j in range(i + 1, len(numbers)):

            if numbers[i] + numbers[j] == target:

                return [
                    numbers[i],
                    numbers[j]
                ]

    return None


print("\nEXAMPLE 12 - BRUTE FORCE PAIR SUM")

print(
    pair_sum_brute_force(
        [1, 2, 4, 6, 10],
        8
    )
)


# ============================================================
# EXAMPLE 13
# COMPARE BRUTE FORCE VS TWO POINTERS
# ============================================================

"""
PAIR SUM COMPARISON


BRUTE FORCE

Two nested loops.

Time:

O(n^2)

Space:

O(1)


TWO POINTERS

Works well when the array is sorted.

Time:

O(n)

Space:

O(1)


This is an example of improving:

O(n^2)

to:

O(n)
"""


# ============================================================
# EXAMPLE 14
# DUPLICATE BRUTE FORCE
# ============================================================

def duplicate_brute_force(numbers):
    """
    Compare every possible pair.

    Time:
    O(n^2)

    Space:
    O(1)
    """

    for i in range(len(numbers)):

        for j in range(i + 1, len(numbers)):

            if numbers[i] == numbers[j]:

                return True

    return False


print("\nEXAMPLE 14 - DUPLICATE BRUTE FORCE")

print(
    duplicate_brute_force(
        [1, 2, 3, 1]
    )
)


# ============================================================
# EXAMPLE 15
# TIME-SPACE TRADE-OFF
# ============================================================

"""
DUPLICATE DETECTION


METHOD 1:

Nested loops

Time:

O(n^2)

Space:

O(1)


METHOD 2:

Set

Average Time:

O(n)

Space:

O(n)


The set solution is usually faster,
but it uses more memory.

This is called:

TIME-SPACE TRADE-OFF
"""


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n======================================")
print("DAY 03 EXAMPLES COMPLETE")
print("======================================")

"""
DAY 03 IMPORTANT PATTERNS


1. ONE PASS

Used for:

Find Sum
Find Maximum
Find Minimum
Count Occurrences
Second Largest


2. SET

Used for:

Duplicate detection
Remembering values already seen


3. TWO POINTERS

Used for:

Reverse Array
Palindrome
Pair Sum
Sorted Array Problems


4. IN-PLACE

Modify the original list.

Example:

Reverse using Two Pointers


5. BRUTE FORCE

Simple solution that may be slower.

Example:

Nested loops for Pair Sum


6. OPTIMIZATION

Try to improve:

O(n^2)

to:

O(n)

when the problem structure allows it.
"""