"""
============================================================
DAY 13 PRACTICE
SORTING ALGORITHMS
============================================================

Try all questions before checking solutions.

Ask:

1. What part is sorted?
2. What part is unsorted?
3. Am I swapping or shifting?
4. How many loops are involved?
5. What is the Time Complexity?
6. Is the algorithm in-place?
"""


# ============================================================
# QUESTION 1
# ASCENDING
# ============================================================

numbers = [
    5,
    1,
    8,
    3,
    2
]

"""
Sort ascending.

Expected:

[1, 2, 3, 5, 8]

MY SOLUTION:
"""


# ============================================================
# QUESTION 2
# DESCENDING
# ============================================================

"""
Sort:

[5, 1, 8, 3, 2]

descending.

Expected:

[8, 5, 3, 2, 1]

MY SOLUTION:
"""


# ============================================================
# QUESTION 3
# BUBBLE SORT
# ============================================================

"""
Implement Bubble Sort.

Input:

[5, 3, 8, 2]

Expected:

[2, 3, 5, 8]

MY SOLUTION:
"""


# ============================================================
# QUESTION 4
# BUBBLE FIRST PASS
# ============================================================

"""
Perform ONLY ONE Bubble Sort pass:

[5, 3, 8, 2]

What does the list become?

Expected:

[3, 5, 2, 8]
"""


# ============================================================
# QUESTION 5
# WHY BUBBLE?
# ============================================================

"""
Why is Bubble Sort called
Bubble Sort?
"""


# ============================================================
# QUESTION 6
# OPTIMIZED BUBBLE
# ============================================================

"""
Implement Bubble Sort with:

swapped = False

Stop if no swap happens.

MY SOLUTION:
"""


# ============================================================
# QUESTION 7
# BUBBLE COMPLEXITY
# ============================================================

"""
Basic Bubble Sort:

Best = ?
Average = ?
Worst = ?

Extra Space = ?
"""


# ============================================================
# QUESTION 8
# OPTIMIZED BUBBLE COMPLEXITY
# ============================================================

"""
Optimized Bubble Sort
on already sorted data:

Best Time = ?
"""


# ============================================================
# QUESTION 9
# SELECTION SORT
# ============================================================

"""
Implement Selection Sort.

Input:

[5, 3, 8, 2]

Expected:

[2, 3, 5, 8]

MY SOLUTION:
"""


# ============================================================
# QUESTION 10
# SELECTION FIRST PASS
# ============================================================

"""
Input:

[5, 3, 8, 2]

During the first pass:

What is the smallest value?

What is its index?

What is the list after the swap?
"""


# ============================================================
# QUESTION 11
# SELECTION COMPLEXITY
# ============================================================

"""
Selection Sort:

Best = ?
Average = ?
Worst = ?

Space = ?
"""


# ============================================================
# QUESTION 12
# INSERTION SORT
# ============================================================

"""
Implement Insertion Sort.

Input:

[5, 3, 8, 2]

Expected:

[2, 3, 5, 8]

MY SOLUTION:
"""


# ============================================================
# QUESTION 13
# INSERTION STEP
# ============================================================

"""
Suppose the array is:

[3, 5, 8, 2]

and current = 2.

Which values need to shift?
"""


# ============================================================
# QUESTION 14
# INSERTION BEST CASE
# ============================================================

"""
Why can Insertion Sort have:

O(n)

best-case time?
"""


# ============================================================
# QUESTION 15
# INSERTION WORST CASE
# ============================================================

"""
Give an example of a worst-case
array for ascending Insertion Sort.
"""


# ============================================================
# QUESTION 16
# INSERTION COMPLEXITY
# ============================================================

"""
Insertion Sort:

Best = ?
Average = ?
Worst = ?

Space = ?
"""


# ============================================================
# QUESTION 17
# MATCH ALGORITHM
# ============================================================

"""
Match:

A. Compare neighbors
B. Find minimum
C. Insert into sorted left side

Algorithms:

Bubble
Selection
Insertion
"""


# ============================================================
# QUESTION 18
# SORTED
# ============================================================

"""
What is the difference between:

sorted(numbers)

and:

numbers.sort()
"""


# ============================================================
# QUESTION 19
# ORIGINAL LIST
# ============================================================

"""
numbers = [3, 1, 2]

result = sorted(numbers)

What is:

numbers?

What is:

result?
"""


# ============================================================
# QUESTION 20
# SORT METHOD
# ============================================================

"""
numbers = [3, 1, 2]

result = numbers.sort()

What is:

numbers?

What is:

result?

Hint:

.sort() changes the list
and returns None.
"""


# ============================================================
# QUESTION 21
# DESCENDING PYTHON
# ============================================================

"""
How do you sort a Python list
in descending order?
"""


# ============================================================
# QUESTION 22
# IN-PLACE
# ============================================================

"""
What does:

in-place sorting

mean?
"""


# ============================================================
# QUESTION 23
# STABLE
# ============================================================

"""
What does:

stable sorting

mean?
"""


# ============================================================
# QUESTION 24
# COMPLEXITY COMPARISON
# ============================================================

"""
Which grows faster?

O(n log n)

or

O(n^2)

for large n?
"""


# ============================================================
# QUESTION 25
# NESTED LOOP
# ============================================================

"""
Why are Bubble Sort and
Selection Sort commonly O(n^2)?
"""


# ============================================================
# QUESTION 26
# SWAP
# ============================================================

"""
Write Python code to swap:

a
b

without a temporary variable.
"""


# ============================================================
# QUESTION 27
# SHIFT VS SWAP
# ============================================================

"""
Explain the difference between:

swap

and

shift

in today's sorting algorithms.
"""


# ============================================================
# QUESTION 28
# SORT STRINGS
# ============================================================

words = [
    "banana",
    "apple",
    "dog",
    "cat"
]

"""
Sort alphabetically.

Expected:

['apple', 'banana', 'cat', 'dog']

MY SOLUTION:
"""


# ============================================================
# QUESTION 29
# SORT BY LENGTH
# ============================================================

words = [
    "elephant",
    "cat",
    "python",
    "hi"
]

"""
Sort based on word length.

MY SOLUTION:
"""


# ============================================================
# QUESTION 30
# BIG IDEA
# ============================================================

"""
Explain:

Why do we study multiple
sorting algorithms if Python
already has built-in sorting?
"""


# ============================================================
#
# STOP HERE
#
# TRY EVERYTHING BEFORE SOLUTIONS
#
# ============================================================































# ============================================================
# SOLUTIONS
# ============================================================


# ============================================================
# SOLUTION 1
# ============================================================

numbers = [
    5,
    1,
    8,
    3,
    2
]

print(
    sorted(numbers)
)


# ============================================================
# SOLUTION 2
# ============================================================

print(
    sorted(
        numbers,
        reverse=True
    )
)


# ============================================================
# SOLUTION 3
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


# ============================================================
# SOLUTION 4
# ============================================================

"""
Start:

[5, 3, 8, 2]


5 and 3:

swap

[3, 5, 8, 2]


5 and 8:

no swap


8 and 2:

swap

[3, 5, 2, 8]


Answer:

[3, 5, 2, 8]
"""


# ============================================================
# SOLUTION 5
# ============================================================

"""
Larger values move toward the end
after repeated adjacent swaps.

They appear to "bubble" toward
their final positions.
"""


# ============================================================
# SOLUTION 6
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


# ============================================================
# SOLUTION 7
# ============================================================

"""
Basic Bubble Sort:

Best:

O(n^2)

Average:

O(n^2)

Worst:

O(n^2)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 8
# ============================================================

"""
Optimized Bubble Sort:

Best:

O(n)

when the list is already sorted.
"""


# ============================================================
# SOLUTION 9
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


# ============================================================
# SOLUTION 10
# ============================================================

"""
Input:

[5, 3, 8, 2]

Smallest:

2

Index:

3

After swap:

[2, 3, 8, 5]
"""


# ============================================================
# SOLUTION 11
# ============================================================

"""
Selection Sort:

Best:

O(n^2)

Average:

O(n^2)

Worst:

O(n^2)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 12
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


# ============================================================
# SOLUTION 13
# ============================================================

"""
Array:

[3, 5, 8, 2]

Current:

2

Shift:

8
5
3

Then insert:

2

Result:

[2, 3, 5, 8]
"""


# ============================================================
# SOLUTION 14
# ============================================================

"""
If the list is already sorted,
the while loop performs almost
no shifting.

We mainly make one comparison
per item.

So:

O(n)
"""


# ============================================================
# SOLUTION 15
# ============================================================

"""
Example:

[5, 4, 3, 2, 1]

For ascending sorting,
every new item must move
far to the left.
"""


# ============================================================
# SOLUTION 16
# ============================================================

"""
Insertion Sort:

Best:

O(n)

Average:

O(n^2)

Worst:

O(n^2)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 17
# ============================================================

"""
A. Compare Neighbors

Bubble Sort


B. Find Minimum

Selection Sort


C. Insert Into Sorted Left Side

Insertion Sort
"""


# ============================================================
# SOLUTION 18
# ============================================================

"""
sorted(numbers)

returns a NEW sorted list.

It does not modify the original.


numbers.sort()

sorts the original list itself.
"""


# ============================================================
# SOLUTION 19
# ============================================================

"""
numbers:

[3, 1, 2]

result:

[1, 2, 3]
"""


# ============================================================
# SOLUTION 20
# ============================================================

"""
After:

result = numbers.sort()

numbers:

[1, 2, 3]

result:

None
"""


# ============================================================
# SOLUTION 21
# ============================================================

"""
numbers.sort(
    reverse=True
)

or:

sorted(
    numbers,
    reverse=True
)
"""


# ============================================================
# SOLUTION 22
# ============================================================

"""
In-place means the algorithm
modifies the original collection
instead of creating a complete
separate copy for the result.
"""


# ============================================================
# SOLUTION 23
# ============================================================

"""
A stable sort preserves
the original relative order
of equal elements.
"""


# ============================================================
# SOLUTION 24
# ============================================================

"""
O(n^2)

grows faster.

So for large inputs:

O(n log n)

is usually much better.
"""


# ============================================================
# SOLUTION 25
# ============================================================

"""
They commonly use nested loops.

The outer loop can run about n times.

The inner work can also run
about n times.

Therefore:

O(n * n)

=

O(n^2)
"""


# ============================================================
# SOLUTION 26
# ============================================================

a, b = b, a


# ============================================================
# SOLUTION 27
# ============================================================

"""
SWAP:

Two values exchange positions.

Example:

5, 3
→
3, 5


SHIFT:

An item is moved one position
to make space for another value.

Insertion Sort commonly shifts
values right.
"""


# ============================================================
# SOLUTION 28
# ============================================================

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
# SOLUTION 29
# ============================================================

words = [
    "elephant",
    "cat",
    "python",
    "hi"
]

print(
    sorted(
        words,
        key=len
    )
)


# ============================================================
# SOLUTION 30
# ============================================================

"""
We study sorting algorithms
to understand:

algorithm design

comparisons

swapping

shifting

nested loops

time complexity

space complexity

best and worst cases

and why one algorithm can be
better than another.

These ideas are more important
than simply calling a built-in
sorting function.
"""


# ============================================================
# FINAL DAY 13 SUMMARY
# ============================================================

"""
BUBBLE SORT

Compare neighbors

O(n^2)


-----------------------------------------


SELECTION SORT

Find minimum

O(n^2)


-----------------------------------------


INSERTION SORT

Insert into sorted section

Best:

O(n)

Worst:

O(n^2)


-----------------------------------------


sorted()

New list


-----------------------------------------


.sort()

Changes original


-----------------------------------------


KEY LESSON

Correct code is important.

Efficient code is also important.
"""