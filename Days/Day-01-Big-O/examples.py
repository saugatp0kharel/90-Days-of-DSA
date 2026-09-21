"""
Day 01 - Big-O Notation
90 Days of Data Structures and Algorithms

This file contains simple examples of:

1. O(1)       - Constant Time
2. O(log n)   - Logarithmic Time
3. O(n)       - Linear Time
4. O(n log n) - Linearithmic Time
5. O(n^2)     - Quadratic Time
6. Space Complexity
"""


# ============================================================
# EXAMPLE 1: O(1) - CONSTANT TIME
# ============================================================

def get_first_element(numbers):
    """
    Return the first element of a list.

    Time Complexity: O(1)
    Space Complexity: O(1)

    Why?

    We directly access index 0.

    The operation does not depend on how many elements
    are inside the list.
    """

    return numbers[0]


numbers = [10, 20, 30, 40, 50]

print("Example 1 - O(1)")
print(get_first_element(numbers))


# ============================================================
# EXAMPLE 2: O(1) - MULTIPLE CONSTANT OPERATIONS
# ============================================================

def print_some_elements(numbers):
    """
    Even though we perform three operations,
    the number of operations is always fixed.

    Therefore:

    Time Complexity = O(1)
    """

    print(numbers[0])
    print(numbers[1])
    print(numbers[2])


print("\nExample 2 - O(1)")
print_some_elements(numbers)


# ============================================================
# EXAMPLE 3: O(n) - LINEAR TIME
# ============================================================

def print_all_numbers(numbers):
    """
    Visit every element once.

    If n = 5:
    approximately 5 iterations

    If n = 100:
    approximately 100 iterations

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    for number in numbers:
        print(number)


print("\nExample 3 - O(n)")
print_all_numbers(numbers)


# ============================================================
# EXAMPLE 4: O(n) - LINEAR SEARCH
# ============================================================

def linear_search(numbers, target):
    """
    Search for a target by checking elements one by one.

    Worst-case Time Complexity: O(n)
    Space Complexity: O(1)
    """

    for number in numbers:

        if number == target:
            return True

    return False


print("\nExample 4 - Linear Search O(n)")

print(linear_search(numbers, 30))
print(linear_search(numbers, 100))


# ============================================================
# EXAMPLE 5: TWO CONSECUTIVE LOOPS
# ============================================================

def two_loops(numbers):
    """
    First loop  = O(n)
    Second loop = O(n)

    Total:

    O(n + n)
    O(2n)

    Big-O ignores constants.

    Final:

    O(n)
    """

    for number in numbers:
        print(number)

    for number in numbers:
        print(number)


print("\nExample 5 - Two loops = O(n)")


# Uncomment this if you want to see the output.

# two_loops(numbers)


# ============================================================
# EXAMPLE 6: O(n^2) - QUADRATIC TIME
# ============================================================

def print_pairs(numbers):
    """
    A loop inside another loop.

    Outer loop = n times
    Inner loop = n times

    n * n = n^2

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    for first in numbers:

        for second in numbers:

            print(first, second)


print("\nExample 6 - O(n^2)")
print_pairs([1, 2, 3])


# ============================================================
# EXAMPLE 7: O(log n)
# ============================================================

def divide_by_two(n):
    """
    Keep dividing n by 2.

    Example:

    64
    32
    16
    8
    4
    2
    1

    The number of iterations grows logarithmically.

    Time Complexity: O(log n)
    """

    while n > 1:

        print(n)

        n = n // 2


print("\nExample 7 - O(log n)")
divide_by_two(64)


# ============================================================
# EXAMPLE 8: BINARY SEARCH - O(log n)
# ============================================================

def binary_search(numbers, target):
    """
    Binary Search works on sorted data.

    Every step removes approximately half
    of the remaining search area.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """

    left = 0
    right = len(numbers) - 1

    while left <= right:

        middle = (left + right) // 2

        if numbers[middle] == target:

            return middle

        elif numbers[middle] < target:

            left = middle + 1

        else:

            right = middle - 1

    return -1


sorted_numbers = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80
]

print("\nExample 8 - Binary Search O(log n)")

result = binary_search(sorted_numbers, 70)

print("Index:", result)


# ============================================================
# EXAMPLE 9: O(n) SPACE
# ============================================================

def double_numbers(numbers):
    """
    We create a new list.

    If the input contains n elements,
    the new list will also contain n elements.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    result = []

    for number in numbers:

        result.append(number * 2)

    return result


print("\nExample 9 - O(n) Space")

print(double_numbers(numbers))


# ============================================================
# EXAMPLE 10: O(1) EXTRA SPACE
# ============================================================

def find_sum(numbers):
    """
    We do not create another list.

    We only keep one variable named total.

    Time Complexity: O(n)
    Extra Space Complexity: O(1)
    """

    total = 0

    for number in numbers:

        total += number

    return total


print("\nExample 10 - O(1) Extra Space")

print(find_sum(numbers))