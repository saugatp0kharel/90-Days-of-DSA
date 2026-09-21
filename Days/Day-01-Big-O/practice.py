"""
Day 01 Practice
Big-O Notation

Instructions:

Try to answer every question BEFORE reading
the solutions at the bottom of this file.

For every problem identify:

1. Time Complexity
2. Space Complexity when possible
3. Why
"""


# ============================================================
# QUESTION 1
# ============================================================

def question_1(arr):

    return arr[0]


"""
What is the Time Complexity?

A. O(1)
B. O(log n)
C. O(n)
D. O(n^2)

Your Answer:
"""


# ============================================================
# QUESTION 2
# ============================================================

def question_2(arr):

    for item in arr:

        print(item)


"""
What is the Time Complexity?

A. O(1)
B. O(log n)
C. O(n)
D. O(n^2)

Your Answer:
"""


# ============================================================
# QUESTION 3
# ============================================================

def question_3(arr):

    for i in arr:

        for j in arr:

            print(i, j)


"""
What is the Time Complexity?

A. O(1)
B. O(n)
C. O(n log n)
D. O(n^2)

Your Answer:
"""


# ============================================================
# QUESTION 4
# ============================================================

def question_4(arr):

    print(arr[0])
    print(arr[1])
    print(arr[2])


"""
What is the Time Complexity?

Your Answer:
"""


# ============================================================
# QUESTION 5
# ============================================================

def question_5(arr):

    for item in arr:

        print(item)

    for item in arr:

        print(item)


"""
First loop  = ?

Second loop = ?

Total complexity = ?

Your Answer:
"""


# ============================================================
# QUESTION 6
# ============================================================

def question_6(arr):

    for i in arr:

        for j in arr:

            print(i, j)

    for item in arr:

        print(item)


"""
Nested loops = ?

Last loop = ?

Total = ?

Final Big-O = ?

Your Answer:
"""


# ============================================================
# QUESTION 7
# ============================================================

def question_7(n):

    while n > 1:

        print(n)

        n = n // 2


"""
What happens to n after every iteration?

What is the Time Complexity?

Your Answer:
"""


# ============================================================
# QUESTION 8
# ============================================================

def question_8(arr):

    result = []

    for number in arr:

        result.append(number * 2)

    return result


"""
Question A:

What is the Time Complexity?

Question B:

What is the Space Complexity?

Your Answer:
"""


# ============================================================
# QUESTION 9
# ============================================================

def question_9(arr):

    total = 0

    for number in arr:

        total += number

    return total


"""
What is the Time Complexity?

What is the extra Space Complexity?

Your Answer:
"""


# ============================================================
# QUESTION 10
# ============================================================

def question_10(arr):

    for i in arr:

        print(i)

        for j in arr:

            print(j)


"""
What is the Time Complexity?

Think carefully about the nested loop.

Your Answer:
"""


# ============================================================
# QUESTION 11
# ============================================================

def question_11(arr):

    if len(arr) == 0:

        return None

    return arr[-1]


"""
What is the Time Complexity?

Your Answer:
"""


# ============================================================
# QUESTION 12
# ============================================================

def question_12(arr):

    maximum = arr[0]

    for number in arr:

        if number > maximum:

            maximum = number

    return maximum


"""
What is the Time Complexity?

Why?

Your Answer:
"""


# ============================================================
# QUESTION 13
# ============================================================

def question_13(arr):

    for i in range(100):

        print(i)


"""
Important:

The loop runs exactly 100 times.

It does NOT depend on the size of arr.

What is the Time Complexity?

Your Answer:
"""


# ============================================================
# QUESTION 14
# ============================================================

def question_14(arr):

    for number in arr:

        print(number)

    print("Finished")


"""
What is the Time Complexity?

Does the final print change the Big-O?

Your Answer:
"""


# ============================================================
# QUESTION 15
# ============================================================

def question_15(list_a, list_b):

    for a in list_a:

        for b in list_b:

            print(a, b)


"""
Assume:

len(list_a) = n
len(list_b) = m

What is the complexity?

A. O(n)
B. O(n^2)
C. O(nm)
D. O(m)

Your Answer:
"""


# ============================================================
# SOLUTIONS
# ============================================================


# ============================================================
# SOLUTION 1
# ============================================================

"""
QUESTION 1

Answer:

O(1)

Explanation:

arr[0] directly accesses one position.

It does not matter whether the list contains:

10 elements

or

10 million elements.

The number of operations does not grow with n.
"""


# ============================================================
# SOLUTION 2
# ============================================================

"""
QUESTION 2

Answer:

O(n)

Explanation:

The loop visits every element exactly once.

If there are n elements,
the loop runs approximately n times.
"""


# ============================================================
# SOLUTION 3
# ============================================================

"""
QUESTION 3

Answer:

O(n^2)

Explanation:

We have a loop inside another loop.

Outer loop:

n iterations

Inner loop:

n iterations for every outer iteration.

Therefore:

n * n = n^2
"""


# ============================================================
# SOLUTION 4
# ============================================================

"""
QUESTION 4

Answer:

O(1)

Explanation:

There are exactly three accesses:

arr[0]
arr[1]
arr[2]

The number of operations does not increase
when the array becomes larger.

Three constant operations are still O(1).
"""


# ============================================================
# SOLUTION 5
# ============================================================

"""
QUESTION 5

Answer:

O(n)

Explanation:

First loop:

O(n)

Second loop:

O(n)

Together:

O(n + n)

=

O(2n)

Big-O ignores constant multipliers.

Therefore:

O(n)
"""


# ============================================================
# SOLUTION 6
# ============================================================

"""
QUESTION 6

Answer:

O(n^2)

Explanation:

Nested loops:

O(n^2)

Final loop:

O(n)

Together:

O(n^2 + n)

The dominant term is:

n^2

Therefore:

O(n^2)
"""


# ============================================================
# SOLUTION 7
# ============================================================

"""
QUESTION 7

Answer:

O(log n)

Explanation:

n is divided by 2 after every iteration.

Example:

64
32
16
8
4
2
1

The number of iterations grows logarithmically.

Therefore:

O(log n)
"""


# ============================================================
# SOLUTION 8
# ============================================================

"""
QUESTION 8

Time Complexity:

O(n)

because every input element is visited once.

Space Complexity:

O(n)

because a new list is created containing
approximately n elements.
"""


# ============================================================
# SOLUTION 9
# ============================================================

"""
QUESTION 9

Time Complexity:

O(n)

because every number is visited.

Extra Space Complexity:

O(1)

because only a fixed number of variables
are created.

The algorithm does not create another list
that grows with n.
"""


# ============================================================
# SOLUTION 10
# ============================================================

"""
QUESTION 10

Answer:

O(n^2)

Explanation:

The outer loop runs n times.

For every outer iteration,
the inner loop runs n times.

Therefore:

n * n

=

n^2
"""


# ============================================================
# SOLUTION 11
# ============================================================

"""
QUESTION 11

Answer:

O(1)

Explanation:

Checking len(arr) is constant time.

Accessing arr[-1] is also constant time.

There is no loop depending on n.

Therefore:

O(1)
"""


# ============================================================
# SOLUTION 12
# ============================================================

"""
QUESTION 12

Answer:

O(n)

Explanation:

To find the maximum value,
we may need to inspect every element.

Therefore the number of operations
grows with the size of the array.

O(n)
"""


# ============================================================
# SOLUTION 13
# ============================================================

"""
QUESTION 13

Answer:

O(1)

This may look confusing because there is a loop.

But the loop always runs exactly:

100 times

It does not depend on input size n.

100 is a constant.

Therefore:

O(100)

simplifies to:

O(1)
"""


# ============================================================
# SOLUTION 14
# ============================================================

"""
QUESTION 14

Answer:

O(n)

Explanation:

The loop is:

O(n)

The final print is:

O(1)

Together:

O(n + 1)

Big-O removes the smaller constant term.

Therefore:

O(n)
"""


# ============================================================
# SOLUTION 15
# ============================================================

"""
QUESTION 15

Answer:

O(nm)

Explanation:

list_a contains n elements.

list_b contains m elements.

The outer loop runs n times.

For every outer iteration,
the inner loop runs m times.

Therefore:

n * m

=

O(nm)

We should NOT automatically say O(n^2)
because the two inputs can have different sizes.
"""