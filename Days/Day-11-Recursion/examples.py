"""
============================================================
DAY 11 - RECURSION
============================================================
"""


# ============================================================
# EXAMPLE 1
# COUNTDOWN
# ============================================================

def countdown(n):

    if n == 0:

        print("Done!")

        return

    print(n)

    countdown(n - 1)


print("EXAMPLE 1 - COUNTDOWN")

countdown(5)


# ============================================================
# EXAMPLE 2
# PRINT INCREASING
# ============================================================

def print_increasing(n):

    if n == 0:

        return

    print_increasing(n - 1)

    print(n)


print("\nEXAMPLE 2 - PRINT INCREASING")

print_increasing(5)


# ============================================================
# EXAMPLE 3
# SUM 1 TO N
# ============================================================

def recursive_sum(n):

    if n == 0:

        return 0

    return (
        n
        +
        recursive_sum(n - 1)
    )


print("\nEXAMPLE 3 - SUM 1 TO N")

print(
    recursive_sum(5)
)


# ============================================================
# EXAMPLE 4
# FACTORIAL
# ============================================================

def factorial(n):

    if n <= 1:

        return 1

    return (
        n
        *
        factorial(n - 1)
    )


print("\nEXAMPLE 4 - FACTORIAL")

print(
    factorial(5)
)


# ============================================================
# EXAMPLE 5
# FACTORIAL ITERATIVE
# ============================================================

def factorial_iterative(n):

    result = 1

    for number in range(
        2,
        n + 1
    ):

        result *= number

    return result


print("\nEXAMPLE 5 - ITERATIVE FACTORIAL")

print(
    factorial_iterative(5)
)


# ============================================================
# EXAMPLE 6
# FIBONACCI
# ============================================================

def fibonacci(n):

    if n == 0:

        return 0

    if n == 1:

        return 1

    return (
        fibonacci(n - 1)
        +
        fibonacci(n - 2)
    )


print("\nEXAMPLE 6 - FIBONACCI")

for i in range(8):

    print(
        fibonacci(i),
        end=" "
    )

print()


# ============================================================
# EXAMPLE 7
# REVERSE STRING
# ============================================================

def reverse_string(text):

    if len(text) <= 1:

        return text

    return (
        reverse_string(text[1:])
        +
        text[0]
    )


print("\nEXAMPLE 7 - REVERSE STRING")

print(
    reverse_string(
        "hello"
    )
)


# ============================================================
# EXAMPLE 8
# PALINDROME
# ============================================================

def is_palindrome(text):

    if len(text) <= 1:

        return True

    if text[0] != text[-1]:

        return False

    return is_palindrome(
        text[1:-1]
    )


print("\nEXAMPLE 8 - PALINDROME")

print(
    is_palindrome(
        "racecar"
    )
)

print(
    is_palindrome(
        "python"
    )
)


# ============================================================
# EXAMPLE 9
# ARRAY SUM USING SLICING
# ============================================================

def array_sum_slice(numbers):

    if not numbers:

        return 0

    return (
        numbers[0]
        +
        array_sum_slice(
            numbers[1:]
        )
    )


print("\nEXAMPLE 9 - ARRAY SUM SLICING")

print(
    array_sum_slice(
        [1, 2, 3, 4]
    )
)


# ============================================================
# EXAMPLE 10
# ARRAY SUM USING INDEX
# ============================================================

def array_sum(numbers, index=0):

    if index == len(numbers):

        return 0

    return (
        numbers[index]
        +
        array_sum(
            numbers,
            index + 1
        )
    )


print("\nEXAMPLE 10 - ARRAY SUM INDEX")

print(
    array_sum(
        [10, 20, 30, 40]
    )
)


# ============================================================
# EXAMPLE 11
# COUNT ARRAY ELEMENTS
# ============================================================

def count_items(numbers, index=0):

    if index == len(numbers):

        return 0

    return (
        1
        +
        count_items(
            numbers,
            index + 1
        )
    )


print("\nEXAMPLE 11 - COUNT ITEMS")

print(
    count_items(
        [10, 20, 30, 40, 50]
    )
)


# ============================================================
# EXAMPLE 12
# FIND MAXIMUM
# ============================================================

def recursive_max(numbers, index=0):

    if not numbers:

        return None

    if index == len(numbers) - 1:

        return numbers[index]

    maximum_of_rest = recursive_max(
        numbers,
        index + 1
    )

    return max(
        numbers[index],
        maximum_of_rest
    )


print("\nEXAMPLE 12 - MAXIMUM")

print(
    recursive_max(
        [4, 8, 2, 10, 5]
    )
)


# ============================================================
# EXAMPLE 13
# SEARCH ARRAY RECURSIVELY
# ============================================================

def recursive_search(
    numbers,
    target,
    index=0
):

    if index == len(numbers):

        return False

    if numbers[index] == target:

        return True

    return recursive_search(
        numbers,
        target,
        index + 1
    )


print("\nEXAMPLE 13 - RECURSIVE SEARCH")

print(
    recursive_search(
        [10, 20, 30],
        20
    )
)

print(
    recursive_search(
        [10, 20, 30],
        100
    )
)


# ============================================================
# EXAMPLE 14
# POWER
# ============================================================

def power(base, exponent):

    if exponent == 0:

        return 1

    return (
        base
        *
        power(
            base,
            exponent - 1
        )
    )


print("\nEXAMPLE 14 - POWER")

print(
    power(
        2,
        5
    )
)


# ============================================================
# EXAMPLE 15
# RECURSION BEFORE AND AFTER
# ============================================================

def recursion_order(n):

    if n == 0:

        return

    print(
        "Going down:",
        n
    )

    recursion_order(
        n - 1
    )

    print(
        "Coming back:",
        n
    )


print(
    "\nEXAMPLE 15 - RECURSION ORDER"
)

recursion_order(3)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n======================================")
print("DAY 11 EXAMPLES COMPLETE")
print("======================================")

"""
RECURSION

Function calls itself


-----------------------------------------


BASE CASE

Stops recursion


-----------------------------------------


RECURSIVE CASE

Solves smaller problem


-----------------------------------------


CALL STACK

Stores active calls


-----------------------------------------


FACTORIAL

Time:

O(n)

Stack:

O(n)


-----------------------------------------


NAIVE FIBONACCI

Time:

O(2^n)

Stack Depth:

O(n)


-----------------------------------------


THINK:

What is the smallest case?

How does my problem become smaller?

Will I reach the base case?
"""