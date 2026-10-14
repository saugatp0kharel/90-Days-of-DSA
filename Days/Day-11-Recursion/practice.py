"""
============================================================
DAY 11 PRACTICE
RECURSION
============================================================

Try every problem BEFORE checking solutions.

For every recursive problem ask:

1. What is the base case?
2. What is the recursive case?
3. How does the problem become smaller?
4. Will I definitely reach the base case?
5. What is the Time Complexity?
6. What is the recursion stack space?
"""


# ============================================================
# QUESTION 1
# COUNTDOWN
# ============================================================

"""
Write a recursive function:

countdown(5)

Expected:

5
4
3
2
1
Done!

MY SOLUTION:
"""


# ============================================================
# QUESTION 2
# PRINT 1 TO N
# ============================================================

"""
Write a recursive function that prints:

1
2
3
4
5

when called with:

5

MY SOLUTION:
"""


# ============================================================
# QUESTION 3
# SUM 1 TO N
# ============================================================

"""
Calculate recursively:

1 + 2 + 3 + 4 + 5

Expected:

15

MY SOLUTION:
"""


# ============================================================
# QUESTION 4
# FACTORIAL
# ============================================================

"""
Calculate:

5!

Expected:

120

MY SOLUTION:
"""


# ============================================================
# QUESTION 5
# FACTORIAL BASE CASE
# ============================================================

"""
What should:

0!

return?

Why?
"""


# ============================================================
# QUESTION 6
# FIBONACCI
# ============================================================

"""
Calculate:

fibonacci(6)

Expected:

8

Sequence:

0 1 1 2 3 5 8

MY SOLUTION:
"""


# ============================================================
# QUESTION 7
# REVERSE STRING
# ============================================================

"""
Reverse recursively:

"python"

Expected:

"nohtyp"

MY SOLUTION:
"""


# ============================================================
# QUESTION 8
# PALINDROME TRUE
# ============================================================

"""
Check recursively:

"level"

Expected:

True

MY SOLUTION:
"""


# ============================================================
# QUESTION 9
# PALINDROME FALSE
# ============================================================

"""
Check recursively:

"hello"

Expected:

False

MY SOLUTION:
"""


# ============================================================
# QUESTION 10
# ARRAY SUM
# ============================================================

"""
Recursively sum:

[1, 2, 3, 4, 5]

Expected:

15

Try using an index.

MY SOLUTION:
"""


# ============================================================
# QUESTION 11
# COUNT ARRAY ITEMS
# ============================================================

"""
Recursively count:

[10, 20, 30, 40]

Expected:

4

MY SOLUTION:
"""


# ============================================================
# QUESTION 12
# FIND MAX
# ============================================================

"""
Find recursively:

max([3, 9, 2, 7])

Expected:

9

MY SOLUTION:
"""


# ============================================================
# QUESTION 13
# RECURSIVE SEARCH
# ============================================================

"""
Search recursively:

[10, 20, 30, 40]

target = 30

Expected:

True

MY SOLUTION:
"""


# ============================================================
# QUESTION 14
# SEARCH NOT FOUND
# ============================================================

"""
Search recursively:

[10, 20, 30]

target = 100

Expected:

False

MY SOLUTION:
"""


# ============================================================
# QUESTION 15
# POWER
# ============================================================

"""
Calculate recursively:

2^5

Expected:

32

Hint:

2^5

=

2 × 2^4

MY SOLUTION:
"""


# ============================================================
# QUESTION 16
# BASE CASE
# ============================================================

"""
Explain in your own words:

What is a base case?

Why is it required?
"""


# ============================================================
# QUESTION 17
# RECURSIVE CASE
# ============================================================

"""
Explain:

What is a recursive case?
"""


# ============================================================
# QUESTION 18
# CALL STACK
# ============================================================

"""
What is the call stack?

How is it connected to:

LIFO?
"""


# ============================================================
# QUESTION 19
# FACTORIAL COMPLEXITY
# ============================================================

"""
Recursive factorial:

Time = ?

Recursive Stack Space = ?
"""


# ============================================================
# QUESTION 20
# FIBONACCI COMPLEXITY
# ============================================================

"""
Naive recursive Fibonacci:

Approximate Time = ?

Stack Depth / Space = ?
"""


# ============================================================
# QUESTION 21
# ITERATION VS RECURSION
# ============================================================

"""
Factorial:

Recursive version:

Time = ?
Space = ?

Iterative version:

Time = ?
Extra Space = ?
"""


# ============================================================
# QUESTION 22
# FIND THE ERROR
# ============================================================

"""
What is wrong with:

def countdown(n):

    print(n)

    countdown(n - 1)
"""


# ============================================================
# QUESTION 23
# FIND ANOTHER ERROR
# ============================================================

"""
What is wrong with:

def countdown(n):

    if n == 0:
        return

    countdown(n + 1)

when starting with n = 5?
"""


# ============================================================
# QUESTION 24
# STACK UNWINDING
# ============================================================

"""
What does stack unwinding mean?

What happens after the
base case returns?
"""


# ============================================================
# QUESTION 25
# PATTERN RECOGNITION
# ============================================================

"""
Match the pattern:

A. Factorial
B. Array traversal
C. Palindrome
D. Fibonacci
E. Countdown

Patterns:

- n - 1
- index + 1
- smaller inside string
- two recursive calls
- n - 1
"""


# ============================================================
# QUESTION 26
# PRINT ORDER
# ============================================================

"""
What does this print?

def mystery(n):

    if n == 0:
        return

    print(n)

    mystery(n - 1)


mystery(3)
"""


# ============================================================
# QUESTION 27
# PRINT ORDER 2
# ============================================================

"""
What does this print?

def mystery(n):

    if n == 0:
        return

    mystery(n - 1)

    print(n)


mystery(3)
"""


# ============================================================
# QUESTION 28
# RECURSION USE CASES
# ============================================================

"""
Name at least 5 topics where
recursion is useful.
"""


# ============================================================
# QUESTION 29
# SLICING
# ============================================================

"""
Why can this:

text[1:]

or:

numbers[1:]

make some recursive Python
solutions less efficient?
"""


# ============================================================
# QUESTION 30
# BIG IDEA
# ============================================================

"""
Complete this sentence:

Recursion is useful when a big problem
can be solved by ______________________.
"""


# ============================================================
#
# STOP HERE
#
# TRY EVERYTHING BEFORE READING SOLUTIONS
#
# ============================================================































# ============================================================
# SOLUTIONS
# ============================================================


# ============================================================
# SOLUTION 1
# ============================================================

def countdown(n):

    if n == 0:

        print("Done!")

        return

    print(n)

    countdown(n - 1)


# ============================================================
# SOLUTION 2
# ============================================================

def print_increasing(n):

    if n == 0:

        return

    print_increasing(n - 1)

    print(n)


# ============================================================
# SOLUTION 3
# ============================================================

def recursive_sum(n):

    if n == 0:

        return 0

    return (
        n
        +
        recursive_sum(n - 1)
    )


# ============================================================
# SOLUTION 4
# ============================================================

def factorial(n):

    if n <= 1:

        return 1

    return (
        n
        *
        factorial(n - 1)
    )


# ============================================================
# SOLUTION 5
# ============================================================

"""
0! = 1

This is the standard mathematical
definition.

It also gives factorial recursion
a clean base case.
"""


# ============================================================
# SOLUTION 6
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


# ============================================================
# SOLUTION 7
# ============================================================

def reverse_string(text):

    if len(text) <= 1:

        return text

    return (
        reverse_string(text[1:])
        +
        text[0]
    )


# ============================================================
# SOLUTION 8 AND 9
# ============================================================

def is_palindrome(text):

    if len(text) <= 1:

        return True

    if text[0] != text[-1]:

        return False

    return is_palindrome(
        text[1:-1]
    )


# ============================================================
# SOLUTION 10
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


# ============================================================
# SOLUTION 11
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


# ============================================================
# SOLUTION 12
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


# ============================================================
# SOLUTION 13 AND 14
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


# ============================================================
# SOLUTION 15
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


# ============================================================
# SOLUTION 16
# ============================================================

"""
A base case is the simplest
version of the problem.

It stops recursion.

Without a reachable base case,
the function may keep calling
itself until Python raises
RecursionError.
"""


# ============================================================
# SOLUTION 17
# ============================================================

"""
The recursive case reduces
the current problem into a
smaller version of the same
problem and calls the function
again.
"""


# ============================================================
# SOLUTION 18
# ============================================================

"""
The call stack stores active
function calls.

It behaves like a stack:

LIFO

Last In
First Out.

The most recent function call
returns first.
"""


# ============================================================
# SOLUTION 19
# ============================================================

"""
Factorial:

Time:

O(n)

Recursive Stack:

O(n)
"""


# ============================================================
# SOLUTION 20
# ============================================================

"""
Naive Fibonacci:

Time:

Approximately O(2^n)

Stack Depth:

O(n)
"""


# ============================================================
# SOLUTION 21
# ============================================================

"""
RECURSIVE FACTORIAL

Time:

O(n)

Stack Space:

O(n)


ITERATIVE FACTORIAL

Time:

O(n)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 22
# ============================================================

"""
There is no base case.

The function continues calling
itself until Python raises:

RecursionError
"""


# ============================================================
# SOLUTION 23
# ============================================================

"""
The function moves away from
the base case.

Starting:

5

becomes:

6
7
8
9
...

It never reaches:

0
"""


# ============================================================
# SOLUTION 24
# ============================================================

"""
Stack unwinding happens after
the base case finishes.

The most recent recursive call
returns first.

Then the call before it returns.

This continues until the original
function call finishes.
"""


# ============================================================
# SOLUTION 25
# ============================================================

"""
A. Factorial

n - 1


B. Array Traversal

index + 1


C. Palindrome

smaller inside string


D. Fibonacci

two recursive calls


E. Countdown

n - 1
"""


# ============================================================
# SOLUTION 26
# ============================================================

"""
Output:

3
2
1

Printing happens BEFORE
the recursive call.
"""


# ============================================================
# SOLUTION 27
# ============================================================

"""
Output:

1
2
3

Printing happens AFTER
the recursive call.

So it happens while the
call stack is unwinding.
"""


# ============================================================
# SOLUTION 28
# ============================================================

"""
Examples:

1. Trees
2. Graph traversal
3. Binary Search
4. Merge Sort
5. Quick Sort
6. Backtracking
7. Permutations
8. Combinations
9. Divide and Conquer
"""


# ============================================================
# SOLUTION 29
# ============================================================

"""
Python slicing creates a
new object containing the
selected elements.

Repeated slicing can therefore
add extra copying, time,
and memory.

Using indexes often avoids
this repeated copying.
"""


# ============================================================
# SOLUTION 30
# ============================================================

"""
Recursion is useful when a big
problem can be solved by:

solving a smaller version
of the same problem.
"""


# ============================================================
# FINAL DAY 11 SUMMARY
# ============================================================

"""
RECURSION


BASE CASE

Stops recursion


-----------------------------------------


RECURSIVE CASE

Makes problem smaller


-----------------------------------------


CALL STACK

Stores recursive calls


-----------------------------------------


FACTORIAL

O(n) Time

O(n) Stack


-----------------------------------------


NAIVE FIBONACCI

O(2^n) Time


-----------------------------------------


ALWAYS ASK

What is my base case?

How does the problem get smaller?

Will I reach the base case?
"""