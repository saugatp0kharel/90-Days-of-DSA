"""
============================================================
DAY 15 PRACTICE
QUICK SORT
============================================================

Try every problem before reading solutions.

Ask:

1. What is the pivot?
2. What goes left?
3. What goes right?
4. What is the base case?
5. Is the partition balanced?
6. What is the Time Complexity?
7. What is the recursion depth?
"""


# ============================================================
# QUESTION 1
# DEFINE QUICK SORT
# ============================================================

"""
Explain Quick Sort in your
own words.
"""


# ============================================================
# QUESTION 2
# PIVOT
# ============================================================

"""
What is a pivot?

Why is it important?
"""


# ============================================================
# QUESTION 3
# PARTITION
# ============================================================

numbers = [
    7,
    2,
    5,
    1,
    9,
    3
]

"""
Use pivot:

5

Create:

less
equal
greater

Expected:

less = [2, 1, 3]

equal = [5]

greater = [7, 9]
"""


# ============================================================
# QUESTION 4
# BASE CASE
# ============================================================

"""
What is the base case
for the simple recursive
Quick Sort?
"""


# ============================================================
# QUESTION 5
# FUNCTIONAL QUICK SORT
# ============================================================

"""
Implement Quick Sort using:

less
equal
greater

MY SOLUTION:
"""


# ============================================================
# QUESTION 6
# SORT
# ============================================================

"""
Sort:

[8, 3, 5, 1, 7, 2]

Expected:

[1, 2, 3, 5, 7, 8]

MY SOLUTION:
"""


# ============================================================
# QUESTION 7
# DUPLICATES
# ============================================================

"""
Sort:

[4, 2, 4, 1, 4]

Expected:

[1, 2, 4, 4, 4]
"""


# ============================================================
# QUESTION 8
# NEGATIVE NUMBERS
# ============================================================

"""
Sort:

[-3, 5, 0, -1, 2]

Expected:

[-3, -1, 0, 2, 5]
"""


# ============================================================
# QUESTION 9
# PARTITION MEANING
# ============================================================

"""
What does it mean to partition
an array around a pivot?
"""


# ============================================================
# QUESTION 10
# LOMUTO PIVOT
# ============================================================

"""
In the Lomuto version in this lesson,
which element is used as pivot?
"""


# ============================================================
# QUESTION 11
# PARTITION TRACE
# ============================================================

numbers = [
    4,
    2,
    7,
    3,
    6
]

"""
Pivot = 6

Show the array after partitioning.

Expected:

One valid result:

[4, 2, 3, 6, 7]

Pivot index:

3
"""


# ============================================================
# QUESTION 12
# I POINTER
# ============================================================

"""
In Lomuto partitioning,
what does:

i

help track?
"""


# ============================================================
# QUESTION 13
# J POINTER
# ============================================================

"""
What does:

j

do during partitioning?
"""


# ============================================================
# QUESTION 14
# FINAL PIVOT SWAP
# ============================================================

"""
Why do we swap the pivot
with:

numbers[i + 1]

after scanning?
"""


# ============================================================
# QUESTION 15
# IN-PLACE QUICK SORT
# ============================================================

"""
Write in-place Quick Sort
using a partition function.

MY SOLUTION:
"""


# ============================================================
# QUESTION 16
# AVERAGE COMPLEXITY
# ============================================================

"""
Quick Sort Average Time:

?
"""


# ============================================================
# QUESTION 17
# BEST CASE
# ============================================================

"""
Quick Sort Best Time:

?

What kind of partitions
create this case?
"""


# ============================================================
# QUESTION 18
# WORST CASE
# ============================================================

"""
Quick Sort Worst Time:

?

What causes it?
"""


# ============================================================
# QUESTION 19
# SORTED WORST CASE
# ============================================================

"""
Why can:

[1, 2, 3, 4, 5]

be bad for Quick Sort
if we always choose the
last item as pivot?
"""


# ============================================================
# QUESTION 20
# RANDOM PIVOT
# ============================================================

"""
Why can choosing a random pivot
help Quick Sort?
"""


# ============================================================
# QUESTION 21
# QUICK VS MERGE
# ============================================================

"""
Compare:

Quick Sort

and:

Merge Sort

in terms of:

main idea
average time
worst time
extra space
stability
"""


# ============================================================
# QUESTION 22
# STABILITY
# ============================================================

"""
Is standard in-place Quick Sort
usually stable?

Explain.
"""


# ============================================================
# QUESTION 23
# RECURSION
# ============================================================

"""
After partitioning,
which parts do we recursively sort?
"""


# ============================================================
# QUESTION 24
# WHY SKIP PIVOT
# ============================================================

"""
Why do we not recursively sort
the pivot again after partitioning?
"""


# ============================================================
# QUESTION 25
# FIND THE BUG
# ============================================================

"""
Why can this be wrong
with our Lomuto implementation?

quick_sort_in_place(
    numbers,
    low,
    pivot_index
)
"""


# ============================================================
# QUESTION 26
# FUNCTIONAL SPACE
# ============================================================

"""
Why does the simple:

less
equal
greater

Quick Sort use more memory?
"""


# ============================================================
# QUESTION 27
# RECURSION DEPTH
# ============================================================

"""
Balanced Quick Sort recursion depth:

?

Worst-case recursion depth:

?
"""


# ============================================================
# QUESTION 28
# PATTERN
# ============================================================

"""
Put these in the correct order:

Recurse left/right
Choose pivot
Partition
Base case check
"""


# ============================================================
# QUESTION 29
# DIVIDE AND CONQUER
# ============================================================

"""
How does Quick Sort use
Divide and Conquer?
"""


# ============================================================
# QUESTION 30
# BIG IDEA
# ============================================================

"""
Complete:

Quick Sort organizes the array
by choosing a __________ and
__________ the remaining values
around it.
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

"""
Quick Sort:

Choose a pivot.

Separate values around it.

Recursively sort the smaller
and larger sections.
"""


# ============================================================
# SOLUTION 2
# ============================================================

"""
A pivot is the value used
to divide the current array
into partitions.

Pivot choice affects how balanced
the recursive problems are.
"""


# ============================================================
# SOLUTION 3
# ============================================================

numbers = [
    7,
    2,
    5,
    1,
    9,
    3
]

pivot = 5

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

print(less)
print(equal)
print(greater)


# ============================================================
# SOLUTION 4
# ============================================================

"""
Base case:

len(numbers) <= 1

Zero or one value is
already sorted.
"""


# ============================================================
# SOLUTION 5, 6, 7, 8
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


# ============================================================
# SOLUTION 9
# ============================================================

"""
Partitioning means rearranging
values so that values on one
side are smaller than or equal
to the chosen pivot and values
on the other side are larger,
according to the partition scheme.
"""


# ============================================================
# SOLUTION 10
# ============================================================

"""
This lesson's Lomuto partition
uses:

numbers[high]

the final element of the
current range.
"""


# ============================================================
# SOLUTION 11
# ============================================================

"""
Input:

[4, 2, 7, 3, 6]

Pivot:

6

One partition result:

[4, 2, 3, 6, 7]

Pivot index:

3
"""


# ============================================================
# SOLUTION 12
# ============================================================

"""
i tracks the end of the
section containing values
that belong before the pivot.
"""


# ============================================================
# SOLUTION 13
# ============================================================

"""
j scans the current partition
from left to right and checks
each value against the pivot.
"""


# ============================================================
# SOLUTION 14
# ============================================================

"""
After scanning, i marks the end
of the smaller section.

So:

i + 1

is the correct final position
for the pivot.
"""


# ============================================================
# SOLUTION 15
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
# SOLUTION 16
# ============================================================

"""
Average:

O(n log n)
"""


# ============================================================
# SOLUTION 17
# ============================================================

"""
Best:

O(n log n)

This happens when partitions
stay reasonably balanced.
"""


# ============================================================
# SOLUTION 18
# ============================================================

"""
Worst:

O(n^2)

This happens when partitions
are extremely unbalanced
again and again.
"""


# ============================================================
# SOLUTION 19
# ============================================================

"""
If we always choose the last item:

5

is the pivot.

Everything else goes left.

Then:

4

becomes pivot.

Again everything goes left.

The recursion becomes:

n
n - 1
n - 2
...

instead of balanced halves.
"""


# ============================================================
# SOLUTION 20
# ============================================================

"""
Random pivot selection reduces
the chance of repeatedly choosing
a very bad pivot for a particular
input ordering.
"""


# ============================================================
# SOLUTION 21
# ============================================================

"""
MERGE SORT

Main idea:

Split + Merge

Average:

O(n log n)

Worst:

O(n log n)

Extra Space:

Usually O(n)

Stable:

Usually yes


QUICK SORT

Main idea:

Pivot + Partition

Average:

O(n log n)

Worst:

O(n^2)

Extra Space:

Can be lower with in-place
partitioning

Stable:

Usually no
"""


# ============================================================
# SOLUTION 22
# ============================================================

"""
No.

Standard in-place Quick Sort
is generally not stable.

Swapping can change the
relative order of equal values.
"""


# ============================================================
# SOLUTION 23
# ============================================================

"""
After partitioning:

sort the section left
of the pivot

and:

sort the section right
of the pivot.
"""


# ============================================================
# SOLUTION 24
# ============================================================

"""
Partitioning puts the pivot
in its final correct sorted
position.

So it does not need to be
included in recursive calls.
"""


# ============================================================
# SOLUTION 25
# ============================================================

"""
If pivot_index is included again,
the recursion may fail to shrink
correctly.

For this implementation use:

pivot_index - 1

on the left side.
"""


# ============================================================
# SOLUTION 26
# ============================================================

"""
The simple version creates
new lists:

less

equal

greater

during recursive calls.

That requires additional memory.
"""


# ============================================================
# SOLUTION 27
# ============================================================

"""
Balanced recursion depth:

O(log n)

Worst recursion depth:

O(n)
"""


# ============================================================
# SOLUTION 28
# ============================================================

"""
Correct order:

1. Base case check

2. Choose pivot

3. Partition

4. Recurse left/right
"""


# ============================================================
# SOLUTION 29
# ============================================================

"""
DIVIDE

Partition the array around
a pivot.


CONQUER

Recursively sort the two
remaining partitions.


COMBINE

The pivot and sorted partitions
naturally form the final
sorted order.
"""


# ============================================================
# SOLUTION 30
# ============================================================

"""
Quick Sort organizes the array
by choosing a:

pivot

and:

partitioning

the remaining values around it.
"""


# ============================================================
# FINAL DAY 15 SUMMARY
# ============================================================

"""
QUICK SORT


PIVOT

Choose dividing value


-----------------------------------------


PARTITION

Arrange around pivot


-----------------------------------------


RECURSE

Sort left

Sort right


-----------------------------------------


AVERAGE

O(n log n)


-----------------------------------------


WORST

O(n^2)


-----------------------------------------


GOOD PERFORMANCE

Balanced partitions


-----------------------------------------


KEY PATTERN

Base
Pivot
Partition
Recurse
"""