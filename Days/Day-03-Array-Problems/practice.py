"""
============================================================
DAY 03 PRACTICE
Array Problems and Two Pointers
============================================================

Try every question before looking at the solutions.

For every problem think about:

1. What is the input?
2. What output is expected?
3. Can I solve it with one loop?
4. Do I need extra memory?
5. Can Two Pointers help?
6. What is the Time Complexity?
7. What is the Space Complexity?
"""


# ============================================================
# QUESTION 1
# Find Sum
# ============================================================

numbers = [10, 20, 30, 40]

"""
Find the sum WITHOUT using sum().

Expected:

100


MY SOLUTION:
"""


# ============================================================
# QUESTION 2
# Find Maximum
# ============================================================

numbers = [4, 88, 10, 32]

"""
Find the largest value WITHOUT using max().

Expected:

88


MY SOLUTION:
"""


# ============================================================
# QUESTION 3
# Find Minimum
# ============================================================

numbers = [4, 88, 10, 2, 32]

"""
Find the smallest value WITHOUT using min().

Expected:

2


MY SOLUTION:
"""


# ============================================================
# QUESTION 4
# Count Occurrences
# ============================================================

numbers = [5, 1, 5, 2, 5, 3]

"""
Count how many times 5 appears.

Expected:

3


MY SOLUTION:
"""


# ============================================================
# QUESTION 5
# Contains Duplicate
# ============================================================

numbers = [1, 2, 3, 1]

"""
Return True if any duplicate exists.

Expected:

True

Try to use a set.


MY SOLUTION:
"""


# ============================================================
# QUESTION 6
# Reverse Using Slicing
# ============================================================

numbers = [10, 20, 30, 40]

"""
Reverse using slicing.

Expected:

[40, 30, 20, 10]


MY SOLUTION:
"""


# ============================================================
# QUESTION 7
# Reverse Using Two Pointers
# ============================================================

numbers = [10, 20, 30, 40]

"""
Reverse the list IN PLACE.

Do not create another list.

Expected:

[40, 30, 20, 10]


MY SOLUTION:
"""


# ============================================================
# QUESTION 8
# Palindrome
# ============================================================

numbers = [1, 2, 3, 2, 1]

"""
Use Two Pointers.

Expected:

True


MY SOLUTION:
"""


# ============================================================
# QUESTION 9
# Not a Palindrome
# ============================================================

numbers = [1, 2, 3, 4]

"""
Expected:

False


MY SOLUTION:
"""


# ============================================================
# QUESTION 10
# Move Zeros
# ============================================================

numbers = [0, 5, 0, 2, 0, 8]

"""
Move zeros to the end.

Keep non-zero values in the same order.

Expected:

[5, 2, 8, 0, 0, 0]


MY SOLUTION:
"""


# ============================================================
# QUESTION 11
# Second Largest
# ============================================================

numbers = [7, 20, 5, 18, 3]

"""
Find the second-largest distinct value.

Expected:

18


MY SOLUTION:
"""


# ============================================================
# QUESTION 12
# Pair Sum
# ============================================================

numbers = [1, 3, 4, 6, 8, 10]

target = 14

"""
The array is sorted.

Use Two Pointers.

Possible answers:

[4, 10]

or

[6, 8]


MY SOLUTION:
"""


# ============================================================
# QUESTION 13
# Complexity
# ============================================================

numbers = [1, 2, 3, 4, 5]

total = 0

for number in numbers:
    total += number


"""
What is:

Time Complexity = ?

Extra Space = ?

Explain why.
"""


# ============================================================
# QUESTION 14
# Complexity
# ============================================================

numbers = [1, 2, 3, 4, 5]

reversed_numbers = numbers[::-1]


"""
What is:

Time Complexity = ?

Extra Space = ?

Why?
"""


# ============================================================
# QUESTION 15
# Complexity
# ============================================================

def reverse_example(numbers):

    left = 0
    right = len(numbers) - 1

    while left < right:

        numbers[left], numbers[right] = \
            numbers[right], numbers[left]

        left += 1
        right -= 1


"""
What is:

Time Complexity = ?

Extra Space = ?

Why?
"""


# ============================================================
# QUESTION 16
# Brute Force Duplicate
# ============================================================

def duplicate_brute_force(numbers):

    for i in range(len(numbers)):

        for j in range(i + 1, len(numbers)):

            if numbers[i] == numbers[j]:
                return True

    return False


"""
What is the worst-case Time Complexity?

Why?
"""


# ============================================================
# QUESTION 17
# Set Duplicate
# ============================================================

def duplicate_set(numbers):

    seen = set()

    for number in numbers:

        if number in seen:
            return True

        seen.add(number)

    return False


"""
What is:

Average Time Complexity = ?

Extra Space = ?

Why?
"""


# ============================================================
# QUESTION 18
# Pair Sum Concept
# ============================================================

"""
Explain:

Why do we move LEFT forward when the sum is too small?

Why do we move RIGHT backward when the sum is too large?

Why does the array need to be sorted?
"""


# ============================================================
# QUESTION 19
# Time-Space Trade-off
# ============================================================

"""
Compare these two duplicate solutions:

1. Nested loops

Time:
Space:


2. Set

Time:
Space:


Which one uses more memory?

Which one is usually faster?
"""


# ============================================================
# QUESTION 20
# Pattern Recognition
# ============================================================

"""
Which pattern would you consider for each problem?

A. Reverse an array
B. Check palindrome
C. Detect duplicates
D. Find maximum
E. Pair Sum in sorted array

Possible patterns:

- One Pass
- Set
- Two Pointers
"""


# ============================================================
#
# STOP
#
# TRY ALL QUESTIONS BEFORE READING SOLUTIONS
#
# ============================================================


































# ============================================================
# SOLUTIONS
# ============================================================


# ============================================================
# SOLUTION 1
# ============================================================

numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
    total += number

print(total)

"""
Output:

100

Time:

O(n)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 2
# ============================================================

numbers = [4, 88, 10, 32]

largest = numbers[0]

for number in numbers:

    if number > largest:
        largest = number

print(largest)

"""
Output:

88

Time:

O(n)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 3
# ============================================================

numbers = [4, 88, 10, 2, 32]

smallest = numbers[0]

for number in numbers:

    if number < smallest:
        smallest = number

print(smallest)

"""
Output:

2

Time:

O(n)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 4
# ============================================================

numbers = [5, 1, 5, 2, 5, 3]

count = 0

for number in numbers:

    if number == 5:
        count += 1

print(count)

"""
Output:

3

Time:

O(n)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 5
# ============================================================

def contains_duplicate(numbers):

    seen = set()

    for number in numbers:

        if number in seen:
            return True

        seen.add(number)

    return False


print(
    contains_duplicate(
        [1, 2, 3, 1]
    )
)

"""
Output:

True

Average Time:

O(n)

Space:

O(n)
"""


# ============================================================
# SOLUTION 6
# ============================================================

numbers = [10, 20, 30, 40]

reversed_numbers = numbers[::-1]

print(reversed_numbers)

"""
Output:

[40, 30, 20, 10]

Time:

O(n)

Space:

O(n)
"""


# ============================================================
# SOLUTION 7
# ============================================================

def reverse_array(numbers):

    left = 0
    right = len(numbers) - 1

    while left < right:

        numbers[left], numbers[right] = \
            numbers[right], numbers[left]

        left += 1
        right -= 1

    return numbers


print(
    reverse_array(
        [10, 20, 30, 40]
    )
)

"""
Output:

[40, 30, 20, 10]

Time:

O(n)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 8
# ============================================================

def is_palindrome(numbers):

    left = 0
    right = len(numbers) - 1

    while left < right:

        if numbers[left] != numbers[right]:
            return False

        left += 1
        right -= 1

    return True


print(
    is_palindrome(
        [1, 2, 3, 2, 1]
    )
)

"""
Output:

True

Time:

O(n)

Space:

O(1)
"""


# ============================================================
# SOLUTION 9
# ============================================================

print(
    is_palindrome(
        [1, 2, 3, 4]
    )
)

"""
Output:

False
"""


# ============================================================
# SOLUTION 10
# ============================================================

def move_zeros(numbers):

    insert_position = 0

    for number in numbers:

        if number != 0:

            numbers[insert_position] = number

            insert_position += 1

    while insert_position < len(numbers):

        numbers[insert_position] = 0

        insert_position += 1

    return numbers


print(
    move_zeros(
        [0, 5, 0, 2, 0, 8]
    )
)

"""
Output:

[5, 2, 8, 0, 0, 0]

Time:

O(n)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 11
# ============================================================

def second_largest(numbers):

    largest = float("-inf")

    second = float("-inf")

    for number in numbers:

        if number > largest:

            second = largest

            largest = number

        elif number > second and number != largest:

            second = number

    return second


print(
    second_largest(
        [7, 20, 5, 18, 3]
    )
)

"""
Output:

18

Time:

O(n)

Space:

O(1)
"""


# ============================================================
# SOLUTION 12
# ============================================================

def pair_sum(numbers, target):

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


print(
    pair_sum(
        [1, 3, 4, 6, 8, 10],
        14
    )
)

"""
Possible Output:

[4, 10]

Time:

O(n)

Space:

O(1)
"""


# ============================================================
# SOLUTION 13
# ============================================================

"""
One full traversal:

Time = O(n)

Only fixed variables:

total
number

Extra Space = O(1)
"""


# ============================================================
# SOLUTION 14
# ============================================================

"""
numbers[::-1]

creates a new list containing n elements.

Time:

O(n)

Extra Space:

O(n)
"""


# ============================================================
# SOLUTION 15
# ============================================================

"""
Two Pointer reverse:

Time:

O(n)

The pointers together move through the array.

Extra Space:

O(1)

Only fixed variables are used:

left
right
"""


# ============================================================
# SOLUTION 16
# ============================================================

"""
Worst Case:

O(n^2)

Why?

We have a nested comparison.

The outer loop can run approximately n times.

The inner loop can also process many values.

Therefore the number of comparisons grows
quadratically.
"""


# ============================================================
# SOLUTION 17
# ============================================================

"""
Average Time:

O(n)

We process each number once and average
set membership/addition is O(1).


Space:

O(n)

The set can store up to n values.
"""


# ============================================================
# SOLUTION 18
# ============================================================

"""
PAIR SUM POINTER MOVEMENT


If sum is too small:

Move left forward.

Why?

The list is sorted.

Moving left forward gives a larger value,
which increases the sum.


If sum is too large:

Move right backward.

Why?

Moving right backward gives a smaller value,
which decreases the sum.


Why must the list be sorted?

Because the pointer movement depends on
knowing that values become larger as we
move right and smaller as we move left.

Without sorted order, we cannot safely know
which pointer movement improves the sum.
"""


# ============================================================
# SOLUTION 19
# ============================================================

"""
BRUTE FORCE DUPLICATE

Time:

O(n^2)

Space:

O(1)


SET DUPLICATE

Average Time:

O(n)

Space:

O(n)


The set solution uses more memory.

But it is usually much faster for large input.

This is a:

TIME-SPACE TRADE-OFF.
"""


# ============================================================
# SOLUTION 20
# ============================================================

"""
A. Reverse Array

Two Pointers


B. Palindrome

Two Pointers


C. Detect Duplicates

Set


D. Find Maximum

One Pass


E. Pair Sum in Sorted Array

Two Pointers
"""


# ============================================================
# FINAL DAY 3 PRACTICE SUMMARY
# ============================================================

"""
IMPORTANT PATTERNS


ONE PASS

Useful for:

Sum
Maximum
Minimum
Counting
Second Largest


--------------------------------------------


SET

Useful when asking:

Have I seen this value before?

Examples:

Duplicates
Unique values


--------------------------------------------


TWO POINTERS

Useful for:

Reverse
Palindrome
Pair Sum
Sorted Arrays


--------------------------------------------


IN-PLACE

Modify the original list.

Can reduce extra space.


--------------------------------------------


TIME-SPACE TRADE-OFF

Sometimes:

More memory

can give:

Faster execution.


Example:

Duplicate Detection


Nested loops:

O(n^2) Time
O(1) Space


Set:

O(n) average Time
O(n) Space
"""