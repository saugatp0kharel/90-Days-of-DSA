"""
============================================================
DAY 12 PRACTICE
BINARY SEARCH
============================================================

Try every problem before reading the solutions.

For every Binary Search problem ask:

1. Is the data sorted?
2. What does left represent?
3. What does right represent?
4. What is mid?
5. Is the target smaller or larger?
6. Which half can I eliminate?
7. Does my search area shrink?
8. What is the Time Complexity?
"""


# ============================================================
# QUESTION 1
# LINEAR SEARCH
# ============================================================

numbers = [
    3,
    6,
    9,
    12,
    15
]

"""
Find:

12

using Linear Search.

Expected index:

3

MY SOLUTION:
"""


# ============================================================
# QUESTION 2
# BASIC BINARY SEARCH
# ============================================================

numbers = [
    2,
    5,
    8,
    10,
    15,
    20,
    30
]

"""
Find:

15

using Binary Search.

Expected index:

4

MY SOLUTION:
"""


# ============================================================
# QUESTION 3
# NOT FOUND
# ============================================================

"""
Use Binary Search to find:

17

in:

[2, 5, 8, 10, 15, 20, 30]

Expected:

-1

MY SOLUTION:
"""


# ============================================================
# QUESTION 4
# MIDDLE INDEX
# ============================================================

"""
If:

left = 0
right = 8

What is:

mid = (left + right) // 2

Expected:

4
"""


# ============================================================
# QUESTION 5
# MOVE LEFT OR RIGHT
# ============================================================

"""
Middle value = 20
Target = 30

Should we search:

Left half

or

Right half?

Which pointer changes?
"""


# ============================================================
# QUESTION 6
# MOVE LEFT
# ============================================================

"""
Middle value = 50
Target = 20

Which half do we search?

Which pointer changes?
"""


# ============================================================
# QUESTION 7
# WHY SORTED?
# ============================================================

"""
Why does Binary Search normally
require sorted data?
"""


# ============================================================
# QUESTION 8
# COMPLEXITY
# ============================================================

"""
Linear Search:

Worst Time = ?

Binary Search:

Worst Time = ?
"""


# ============================================================
# QUESTION 9
# ITERATIVE BINARY SEARCH
# ============================================================

"""
Write complete iterative
Binary Search.

Return index when found.

Return -1 when not found.

MY SOLUTION:
"""


# ============================================================
# QUESTION 10
# RECURSIVE BINARY SEARCH
# ============================================================

"""
Write recursive Binary Search.

What is the base case?

MY SOLUTION:
"""


# ============================================================
# QUESTION 11
# RECURSIVE COMPLEXITY
# ============================================================

"""
Recursive Binary Search:

Time = ?

Stack Space = ?
"""


# ============================================================
# QUESTION 12
# ITERATIVE COMPLEXITY
# ============================================================

"""
Iterative Binary Search:

Time = ?

Extra Space = ?
"""


# ============================================================
# QUESTION 13
# FIRST OCCURRENCE
# ============================================================

numbers = [
    1,
    2,
    2,
    2,
    3,
    4
]

"""
Find the FIRST index of:

2

Expected:

1

MY SOLUTION:
"""


# ============================================================
# QUESTION 14
# LAST OCCURRENCE
# ============================================================

"""
For:

[1, 2, 2, 2, 3, 4]

Find LAST occurrence of:

2

Expected:

3

MY SOLUTION:
"""


# ============================================================
# QUESTION 15
# FIRST AND LAST
# ============================================================

"""
Target:

2

Array:

[1, 2, 2, 2, 3, 4]

Expected:

First = 1
Last = 3
"""


# ============================================================
# QUESTION 16
# SEARCH INSERT
# ============================================================

numbers = [
    1,
    3,
    5,
    6
]

"""
Target:

2

Expected insertion index:

1

MY SOLUTION:
"""


# ============================================================
# QUESTION 17
# SEARCH INSERT
# ============================================================

"""
Array:

[1, 3, 5, 6]

Target:

7

Expected:

4
"""


# ============================================================
# QUESTION 18
# SEARCH INSERT
# ============================================================

"""
Array:

[1, 3, 5, 6]

Target:

0

Expected:

0
"""


# ============================================================
# QUESTION 19
# LOWER BOUND
# ============================================================

numbers = [
    1,
    3,
    3,
    5,
    8
]

"""
Find the first index whose value
is >= 3.

Expected:

1

MY SOLUTION:
"""


# ============================================================
# QUESTION 20
# DUPLICATE LOGIC
# ============================================================

"""
When looking for the FIRST occurrence
and you find the target at mid:

Do you:

A. Return immediately
B. Save mid and search left
C. Search right

Why?
"""


# ============================================================
# QUESTION 21
# LAST OCCURRENCE LOGIC
# ============================================================

"""
When looking for the LAST occurrence
and target is found:

What should happen next?
"""


# ============================================================
# QUESTION 22
# FIND THE BUG
# ============================================================

"""
What could go wrong with:

left = mid

instead of:

left = mid + 1

in a standard inclusive Binary Search?
"""


# ============================================================
# QUESTION 23
# FIND ANOTHER BUG
# ============================================================

"""
Standard inclusive Binary Search:

Should right start as:

len(numbers)

or:

len(numbers) - 1

?
"""


# ============================================================
# QUESTION 24
# EMPTY ARRAY
# ============================================================

"""
What should Binary Search return
for:

numbers = []

target = 5

Expected:

-1
"""


# ============================================================
# QUESTION 25
# ONE ELEMENT FOUND
# ============================================================

"""
Array:

[10]

Target:

10

Expected:

0

Trace:

left = ?
right = ?
mid = ?
"""


# ============================================================
# QUESTION 26
# ONE ELEMENT NOT FOUND
# ============================================================

"""
Array:

[10]

Target:

7

Expected:

-1
"""


# ============================================================
# QUESTION 27
# BINARY SEARCH STEPS
# ============================================================

"""
Search for:

70

inside:

[10, 20, 30, 40, 50, 60, 70, 80]

Write:

left
right
mid
middle value

for every step.
"""


# ============================================================
# QUESTION 28
# LOGARITHMIC THINKING
# ============================================================

"""
If n = 16:

Approximately how many times can
we cut the search space in half
before reaching 1?

Expected:

4

Why?
"""


# ============================================================
# QUESTION 29
# PATTERN RECOGNITION
# ============================================================

"""
Choose the correct pattern:

A. Find exact target
B. First duplicate occurrence
C. Last duplicate occurrence
D. Find insertion position

Patterns:

- Normal Binary Search
- Find + Continue Left
- Find + Continue Right
- Return left after loop
"""


# ============================================================
# QUESTION 30
# BIG IDEA
# ============================================================

"""
Complete:

Binary Search is powerful because
each comparison allows us to
eliminate ______________________.
"""


# ============================================================
#
# STOP HERE
#
# TRY QUESTIONS BEFORE READING SOLUTIONS
#
# ============================================================































# ============================================================
# SOLUTIONS
# ============================================================


# ============================================================
# SOLUTION 1
# ============================================================

def linear_search(
    numbers,
    target
):

    for index in range(
        len(numbers)
    ):

        if numbers[index] == target:

            return index

    return -1


# ============================================================
# SOLUTION 2, 3, 9, 24, 25, 26
# ============================================================

def binary_search(
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

    return -1


# ============================================================
# SOLUTION 4
# ============================================================

"""
left = 0
right = 8

mid = (0 + 8) // 2

mid = 4
"""


# ============================================================
# SOLUTION 5
# ============================================================

"""
Middle:

20

Target:

30

Target is larger.

Search RIGHT.

Change:

left = mid + 1
"""


# ============================================================
# SOLUTION 6
# ============================================================

"""
Middle:

50

Target:

20

Target is smaller.

Search LEFT.

Change:

right = mid - 1
"""


# ============================================================
# SOLUTION 7
# ============================================================

"""
Binary Search uses ordering
to know which half cannot
contain the target.

Without sorted data,
a smaller target is not
necessarily on the left.
"""


# ============================================================
# SOLUTION 8
# ============================================================

"""
Linear Search:

O(n)


Binary Search:

O(log n)
"""


# ============================================================
# SOLUTION 10
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


# ============================================================
# SOLUTION 11
# ============================================================

"""
Recursive Binary Search:

Time:

O(log n)

Stack Space:

O(log n)
"""


# ============================================================
# SOLUTION 12
# ============================================================

"""
Iterative Binary Search:

Time:

O(log n)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 13
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


# ============================================================
# SOLUTION 14
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


# ============================================================
# SOLUTION 15
# ============================================================

"""
First:

1

Last:

3
"""


# ============================================================
# SOLUTION 16, 17, 18
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


# ============================================================
# SOLUTION 19
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


# ============================================================
# SOLUTION 20
# ============================================================

"""
Answer:

B

Save mid and search LEFT.

There may be another target
at a smaller index.
"""


# ============================================================
# SOLUTION 21
# ============================================================

"""
Save:

result = mid

Then search RIGHT:

left = mid + 1
"""


# ============================================================
# SOLUTION 22
# ============================================================

"""
Using:

left = mid

can leave left unchanged.

Then the search interval may
stop shrinking.

This can cause an infinite loop.

In the standard inclusive template:

left = mid + 1
"""


# ============================================================
# SOLUTION 23
# ============================================================

"""
For the standard inclusive version:

right = len(numbers) - 1

because the last valid index is:

len(numbers) - 1
"""


# ============================================================
# SOLUTION 24
# ============================================================

"""
Empty array:

left = 0

right = -1

Condition:

left <= right

is immediately false.

Return:

-1
"""


# ============================================================
# SOLUTION 25
# ============================================================

"""
Array:

[10]

left = 0

right = 0

mid = 0

numbers[mid] = 10

Found.

Return:

0
"""


# ============================================================
# SOLUTION 26
# ============================================================

"""
Array:

[10]

Target:

7

mid = 0

10 is too large.

right becomes:

-1

Loop ends.

Return:

-1
"""


# ============================================================
# SOLUTION 27
# ============================================================

"""
Array:

[10,20,30,40,50,60,70,80]

Target:

70


STEP 1

left = 0

right = 7

mid = 3

value = 40

70 > 40

left = 4


STEP 2

left = 4

right = 7

mid = 5

value = 60

70 > 60

left = 6


STEP 3

left = 6

right = 7

mid = 6

value = 70

Found.
"""


# ============================================================
# SOLUTION 28
# ============================================================

"""
16
↓
8
↓
4
↓
2
↓
1

Four halvings.

Because:

2^4 = 16

and:

log2(16) = 4
"""


# ============================================================
# SOLUTION 29
# ============================================================

"""
A. Exact Target

Normal Binary Search


B. First Occurrence

Find + Continue Left


C. Last Occurrence

Find + Continue Right


D. Insert Position

Return left after loop
"""


# ============================================================
# SOLUTION 30
# ============================================================

"""
Binary Search is powerful because
each comparison allows us to
eliminate:

approximately half of the
remaining possibilities.
"""


# ============================================================
# FINAL DAY 12 SUMMARY
# ============================================================

"""
BINARY SEARCH


SORTED DATA

Usually required


-----------------------------------------


LEFT / RIGHT / MID


-----------------------------------------


MID TOO SMALL

left = mid + 1


-----------------------------------------


MID TOO LARGE

right = mid - 1


-----------------------------------------


FOUND

return mid


-----------------------------------------


TIME

O(log n)


-----------------------------------------


FIRST OCCURRENCE

continue left


-----------------------------------------


LAST OCCURRENCE

continue right


-----------------------------------------


SEARCH INSERT

return left
"""