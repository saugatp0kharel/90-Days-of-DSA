"""
============================================================
DAY 14 PRACTICE
MERGE SORT AND DIVIDE & CONQUER
============================================================

Try every question before checking solutions.

Ask:

1. What is the base case?
2. How is the problem divided?
3. What smaller problems are solved?
4. How are answers combined?
5. What do i and j point to?
6. What is the Time Complexity?
7. What is the Space Complexity?
"""


# ============================================================
# QUESTION 1
# DIVIDE AND CONQUER
# ============================================================

"""
Explain:

What are the three main steps
of Divide and Conquer?
"""


# ============================================================
# QUESTION 2
# SPLIT ARRAY
# ============================================================

numbers = [
    8,
    3,
    5,
    1
]

"""
Split this list in half.

Expected:

Left:

[8, 3]

Right:

[5, 1]

MY SOLUTION:
"""


# ============================================================
# QUESTION 3
# BASE CASE
# ============================================================

"""
What is the Merge Sort base case?

Why is it correct?
"""


# ============================================================
# QUESTION 4
# MERGE
# ============================================================

"""
Merge:

[1, 4, 7]

and:

[2, 3, 8]

Expected:

[1, 2, 3, 4, 7, 8]

MY SOLUTION:
"""


# ============================================================
# QUESTION 5
# MERGE UNEQUAL LENGTH
# ============================================================

"""
Merge:

[1, 5]

and:

[2, 3, 4, 8]

Expected:

[1, 2, 3, 4, 5, 8]

MY SOLUTION:
"""


# ============================================================
# QUESTION 6
# EMPTY SIDE
# ============================================================

"""
Merge:

[]

and:

[1, 2, 3]

Expected:

[1, 2, 3]

MY SOLUTION:
"""


# ============================================================
# QUESTION 7
# MERGE SORT
# ============================================================

"""
Implement Merge Sort.

Input:

[8, 3, 5, 1]

Expected:

[1, 3, 5, 8]

MY SOLUTION:
"""


# ============================================================
# QUESTION 8
# TRACE SPLITS
# ============================================================

"""
Show how this splits:

[8, 3, 5, 1]

until every list has
one element.
"""


# ============================================================
# QUESTION 9
# TRACE MERGES
# ============================================================

"""
For:

[8, 3, 5, 1]

show the merge process
back to the final sorted list.
"""


# ============================================================
# QUESTION 10
# MERGE POINTERS
# ============================================================

"""
What does:

i

represent?

What does:

j

represent?
"""


# ============================================================
# QUESTION 11
# POINTER MOVEMENT
# ============================================================

"""
Left:

[2, 5]

Right:

[3, 4]

If:

2 < 3

which pointer moves?
"""


# ============================================================
# QUESTION 12
# REMAINING VALUES
# ============================================================

"""
Why do we need to append
remaining values after the
main merge loop?
"""


# ============================================================
# QUESTION 13
# TIME COMPLEXITY
# ============================================================

"""
Merge Sort:

Best = ?

Average = ?

Worst = ?
"""


# ============================================================
# QUESTION 14
# SPACE COMPLEXITY
# ============================================================

"""
Typical Merge Sort extra space:

?
"""


# ============================================================
# QUESTION 15
# WHY LOG N
# ============================================================

"""
Why does Merge Sort have
approximately log n levels?
"""


# ============================================================
# QUESTION 16
# WHY N PER LEVEL
# ============================================================

"""
Why is the total merge work
on each recursion level
approximately O(n)?
"""


# ============================================================
# QUESTION 17
# FINAL COMPLEXITY
# ============================================================

"""
Explain why:

O(n)

×

O(log n)

=

O(n log n)
"""


# ============================================================
# QUESTION 18
# COMPARE SORTS
# ============================================================

"""
Which usually scales better
for large general inputs?

Bubble Sort:

O(n^2)

or

Merge Sort:

O(n log n)

Why?
"""


# ============================================================
# QUESTION 19
# STABILITY
# ============================================================

"""
Is Merge Sort stable when
implemented correctly?

What does stable mean?
"""


# ============================================================
# QUESTION 20
# IN-PLACE
# ============================================================

"""
Is the common Python Merge Sort
implementation in-place?

Why or why not?
"""


# ============================================================
# QUESTION 21
# EMPTY LIST
# ============================================================

"""
What should:

merge_sort([])

return?
"""


# ============================================================
# QUESTION 22
# ONE ELEMENT
# ============================================================

"""
What should:

merge_sort([10])

return?

Does it need further sorting?
"""


# ============================================================
# QUESTION 23
# DUPLICATES
# ============================================================

"""
Sort using Merge Sort:

[4, 2, 4, 1, 2]

Expected:

[1, 2, 2, 4, 4]
"""


# ============================================================
# QUESTION 24
# NEGATIVE VALUES
# ============================================================

"""
Sort:

[-3, 5, -1, 0, 2]

Expected:

[-3, -1, 0, 2, 5]
"""


# ============================================================
# QUESTION 25
# RECURSION CONNECTION
# ============================================================

"""
How does Merge Sort use:

Base Case

Recursive Case

Stack Unwinding
"""


# ============================================================
# QUESTION 26
# TWO POINTER CONNECTION
# ============================================================

"""
How does the merge step
use the Two Pointer pattern
from earlier days?
"""


# ============================================================
# QUESTION 27
# FIND THE BUG
# ============================================================

"""
What is wrong if Merge Sort
has no:

if len(numbers) <= 1:
    return numbers
"""


# ============================================================
# QUESTION 28
# FIND ANOTHER BUG
# ============================================================

"""
Suppose the merge code stops
as soon as either left or right
is empty.

What important step might
still be missing?
"""


# ============================================================
# QUESTION 29
# PATTERN RECOGNITION
# ============================================================

"""
Match:

A. Divide
B. Conquer
C. Combine
D. Base Case

With:

- Merge sorted halves
- Split in half
- Length <= 1
- Recursively sort each half
"""


# ============================================================
# QUESTION 30
# BIG IDEA
# ============================================================

"""
Complete:

Merge Sort becomes efficient
because it divides the list
into __________ and merges
them in __________ time per level.
"""


# ============================================================
#
# STOP HERE
#
# TRY QUESTIONS BEFORE SOLUTIONS
#
# ============================================================































# ============================================================
# SOLUTIONS
# ============================================================


# ============================================================
# SOLUTION 1
# ============================================================

"""
Divide

Break problem into smaller parts.


Conquer

Solve the smaller parts.


Combine

Combine the smaller answers.
"""


# ============================================================
# SOLUTION 2
# ============================================================

numbers = [
    8,
    3,
    5,
    1
]

mid = len(numbers) // 2

left = numbers[:mid]

right = numbers[mid:]

print(left)

print(right)


# ============================================================
# SOLUTION 3
# ============================================================

"""
Base Case:

len(numbers) <= 1

A list containing zero or one
element is already sorted.
"""


# ============================================================
# SOLUTION 4, 5, 6
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

    result.extend(
        left[i:]
    )

    result.extend(
        right[j:]
    )

    return result


# ============================================================
# SOLUTION 7
# ============================================================

def merge_sort(numbers):

    if len(numbers) <= 1:

        return numbers

    mid = len(numbers) // 2

    left = merge_sort(
        numbers[:mid]
    )

    right = merge_sort(
        numbers[mid:]
    )

    return merge(
        left,
        right
    )


# ============================================================
# SOLUTION 8
# ============================================================

"""
[8,3,5,1]

↓          ↓

[8,3]    [5,1]

↓   ↓    ↓   ↓

[8] [3] [5] [1]
"""


# ============================================================
# SOLUTION 9
# ============================================================

"""
[8] + [3]

→ [3,8]


[5] + [1]

→ [1,5]


[3,8] + [1,5]

→ [1,3,5,8]
"""


# ============================================================
# SOLUTION 10
# ============================================================

"""
i

points to the current value
inside the left array.


j

points to the current value
inside the right array.
"""


# ============================================================
# SOLUTION 11
# ============================================================

"""
If:

left[i] = 2

right[j] = 3

we take:

2

Then:

i += 1
"""


# ============================================================
# SOLUTION 12
# ============================================================

"""
One side may become empty
before the other side.

The remaining side can still
contain values that belong
in the final result.

Because that side is already
sorted, we can append the
remaining values directly.
"""


# ============================================================
# SOLUTION 13
# ============================================================

"""
Merge Sort:

Best:

O(n log n)

Average:

O(n log n)

Worst:

O(n log n)
"""


# ============================================================
# SOLUTION 14
# ============================================================

"""
Typical extra space:

O(n)

for temporary merge storage.

Recursion depth is:

O(log n)
"""


# ============================================================
# SOLUTION 15
# ============================================================

"""
The input is divided in half
on each recursion level.

Example:

8
4
2
1

The number of halvings is:

log2(n)

So the recursion depth is:

O(log n)
"""


# ============================================================
# SOLUTION 16
# ============================================================

"""
At one recursion level,
all smaller pieces together
still contain all n elements.

Each element participates
in merging at that level.

So total merge work per level:

O(n)
"""


# ============================================================
# SOLUTION 17
# ============================================================

"""
Number of levels:

O(log n)

Work per level:

O(n)

Therefore:

O(n log n)
"""


# ============================================================
# SOLUTION 18
# ============================================================

"""
Merge Sort usually scales
better for large inputs.

O(n log n)

grows much more slowly than:

O(n^2)
"""


# ============================================================
# SOLUTION 19
# ============================================================

"""
Yes.

Merge Sort can be stable.

Stable means equal elements
keep their original relative order.

Using:

left[i] <= right[j]

helps select the left equal item
before the right equal item.
"""


# ============================================================
# SOLUTION 20
# ============================================================

"""
The common Python implementation
is not in-place.

It creates:

left slices
right slices
temporary result lists

So it uses extra memory.
"""


# ============================================================
# SOLUTION 21
# ============================================================

"""
[]
"""


# ============================================================
# SOLUTION 22
# ============================================================

"""
[10]

No additional sorting is needed
because one value is already sorted.
"""


# ============================================================
# SOLUTION 23
# ============================================================

print(
    merge_sort(
        [4, 2, 4, 1, 2]
    )
)


# ============================================================
# SOLUTION 24
# ============================================================

print(
    merge_sort(
        [-3, 5, -1, 0, 2]
    )
)


# ============================================================
# SOLUTION 25
# ============================================================

"""
BASE CASE

Stop when length <= 1.


RECURSIVE CASE

Sort the left half.

Sort the right half.


STACK UNWINDING

As recursive calls return,
the smaller sorted lists are
merged back together.
"""


# ============================================================
# SOLUTION 26
# ============================================================

"""
The merge function has:

i → left array
j → right array

We compare both current values.

Whichever value is smaller
is added to the result.

Then only that pointer moves.

This is a Two Pointer pattern.
"""


# ============================================================
# SOLUTION 27
# ============================================================

"""
Without a base case,
recursive splitting has no
proper stopping condition.

The function would continue
calling itself incorrectly.
"""


# ============================================================
# SOLUTION 28
# ============================================================

"""
We still need to append any
remaining values from the
non-empty side.
"""


# ============================================================
# SOLUTION 29
# ============================================================

"""
A. Divide

Split in half


B. Conquer

Recursively sort each half


C. Combine

Merge sorted halves


D. Base Case

Length <= 1
"""


# ============================================================
# SOLUTION 30
# ============================================================

"""
Merge Sort becomes efficient
because it divides the list
into:

halves

and merges them in:

O(n)

time per recursion level.
"""


# ============================================================
# FINAL DAY 14 SUMMARY
# ============================================================

"""
MERGE SORT


DIVIDE

Split into halves


-----------------------------------------


CONQUER

Recursively sort


-----------------------------------------


COMBINE

Merge


-----------------------------------------


BASE CASE

len <= 1


-----------------------------------------


MERGE

Two Pointers


-----------------------------------------


TIME

O(n log n)


-----------------------------------------


SPACE

O(n)


-----------------------------------------


KEY IDEA

Base
Split
Recurse
Merge
"""