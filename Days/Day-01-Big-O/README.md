# Day 01 - Big-O Notation, Time Complexity, and Space Complexity

Welcome to **Day 01** of my **90 Days of Data Structures and Algorithms** journey.

Today I am starting with one of the most important foundations of Data Structures and Algorithms:

# Big-O Notation

Before learning Arrays, Linked Lists, Stacks, Queues, Trees, Graphs, Sorting, Searching, and Dynamic Programming, it is important to understand how we measure the efficiency of an algorithm.

In this lesson, I learned:

- Big-O Notation
- Time Complexity
- Space Complexity
- O(1) - Constant Time
- O(log n) - Logarithmic Time
- O(n) - Linear Time
- O(n log n) - Linearithmic Time
- O(n²) - Quadratic Time

---

# Table of Contents

1. What is an Algorithm?
2. What is Big-O Notation?
3. What does `n` mean?
4. Why Big-O is important
5. Time Complexity
6. Space Complexity
7. O(1) - Constant Time
8. O(log n) - Logarithmic Time
9. O(n) - Linear Time
10. O(n log n) - Linearithmic Time
11. O(n²) - Quadratic Time
12. Comparing Big-O Complexities
13. How Big-O changes when input grows
14. Dropping constants
15. Dropping smaller terms
16. Consecutive loops
17. Nested loops
18. Different input variables
19. Best, Average, and Worst Case
20. Common mistakes
21. Practice Questions
22. Day 1 Summary

---

# 1. What is an Algorithm?

An algorithm is a set of steps used to solve a problem.

For example, imagine we want to find a number inside a list:

```python
numbers = [5, 10, 15, 20, 25]
```

We want to find:

```text
20
```

One possible algorithm is:

1. Check the first number.
2. If it is not 20, check the next number.
3. Continue checking.
4. Stop when 20 is found.

In Python:

```python
def find_number(numbers, target):
    for number in numbers:
        if number == target:
            return True

    return False
```

This is an algorithm.

But there may be many different algorithms that solve the same problem.

Some algorithms are faster.

Some use less memory.

Some work better when there are millions of elements.

This is why we need Big-O.

---

# 2. What is Big-O Notation?

Big-O notation describes how the amount of work performed by an algorithm grows as the size of the input grows.

Big-O does **not normally tell us exactly how many seconds a program will take**.

Instead, it describes the growth of the algorithm.

For example:

```text
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
```

These represent different rates of growth.

Imagine two algorithms.

Algorithm A needs approximately:

```text
n operations
```

Algorithm B needs approximately:

```text
n² operations
```

If:

```text
n = 10
```

then:

```text
Algorithm A ≈ 10 operations
Algorithm B ≈ 100 operations
```

That may not seem like a huge difference.

But imagine:

```text
n = 1,000,000
```

Then approximately:

```text
Algorithm A = 1,000,000 operations

Algorithm B =
1,000,000 × 1,000,000
=
1,000,000,000,000 operations
```

Now the difference is enormous.

This is why Big-O becomes extremely important when working with large amounts of data.

---

# 3. What Does `n` Mean?

In complexity analysis, we frequently use the letter:

```text
n
```

`n` normally represents the size of the input.

Example:

```python
numbers = [10, 20, 30, 40, 50]
```

There are 5 elements.

Therefore:

```text
n = 5
```

If we have:

```python
numbers = list(range(1000))
```

then:

```text
n = 1000
```

The question Big-O asks is:

> What happens to the amount of work when `n` becomes larger?

---

# 4. Why is Big-O Important?

Suppose we create an application with only:

```text
10 users
```

An inefficient algorithm may still appear very fast.

But later our application might have:

```text
100 users
1,000 users
100,000 users
10,000,000 users
```

An algorithm that worked well with 10 users may become extremely slow with millions of users.

Big-O helps programmers predict this problem.

It allows us to compare algorithms without depending completely on:

- Computer speed
- CPU
- Operating system
- Programming language
- Internet connection
- Hardware

The main idea is:

> How well does the algorithm scale as the input becomes larger?

---

# 5. Time Complexity

Time Complexity describes how the number of operations performed by an algorithm grows when the input size increases.

It does not necessarily mean actual clock time.

For example:

```python
for number in numbers:
    print(number)
```

If there are:

```text
10 numbers
```

the loop runs approximately:

```text
10 times
```

If there are:

```text
1,000 numbers
```

the loop runs approximately:

```text
1,000 times
```

If there are:

```text
1,000,000 numbers
```

the loop runs approximately:

```text
1,000,000 times
```

The work increases with the input size.

Therefore this is:

```text
O(n)
```

Time Complexity is mainly concerned with how quickly the number of operations grows.

---

# 6. Space Complexity

Time is not the only thing that matters.

Programs also use memory.

Space Complexity describes how much **additional memory** an algorithm requires as the input becomes larger.

Consider:

```python
def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total
```

We have:

```text
total
number
```

Only a small, fixed amount of extra memory is being used.

Even if the input grows from:

```text
10 elements
```

to:

```text
10,000,000 elements
```

the algorithm does not create another list containing all those elements.

The auxiliary space complexity is:

```text
O(1)
```

---

## Example of O(n) Space

Now consider:

```python
def double_numbers(numbers):
    result = []

    for number in numbers:
        result.append(number * 2)

    return result
```

If the input has:

```text
10 elements
```

the new list contains:

```text
10 elements
```

If the input contains:

```text
1,000 elements
```

the new list contains:

```text
1,000 elements
```

Therefore the extra memory grows with `n`.

Space Complexity:

```text
O(n)
```

---

# 7. O(1) - Constant Time

`O(1)` is called **Constant Time**.

It means that the amount of work does not grow with the input size.

Consider:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
```

We are accessing one known position.

Python does not need to search through every value before accessing index `0`.

Therefore the operation is approximately:

```text
O(1)
```

---

## Another Example

```python
def get_first_element(numbers):
    return numbers[0]
```

Whether the list contains:

```text
5 elements
```

or:

```text
5,000,000 elements
```

we still perform one direct access.

Therefore:

```text
O(1)
```

---

## Another O(1) Example

```python
def add_numbers(a, b):
    return a + b
```

There is no loop depending on `n`.

Therefore, for standard complexity analysis:

```text
O(1)
```

---

## Important Idea

`O(1)` does NOT mean:

> The algorithm performs exactly one operation.

It means:

> The number of operations does not increase based on the input size.

For example:

```python
def example(arr):
    print(arr[0])
    print(arr[1])
    print(arr[2])
```

There are three operations.

But there are always approximately three operations regardless of whether the array contains:

```text
10 elements
```

or:

```text
10 million elements
```

Therefore it is still:

```text
O(1)
```

---

# 8. O(log n) - Logarithmic Time

`O(log n)` is called **Logarithmic Time**.

This complexity usually appears when the algorithm reduces the problem size significantly during every step.

One of the most famous examples is:

# Binary Search

Suppose we have a sorted list:

```text
1  3  5  7  9  11  13  15
```

We want to find:

```text
13
```

Instead of checking:

```text
1
3
5
7
9
11
13
```

one by one, Binary Search looks near the middle.

If the target is larger than the middle number, we can ignore the entire left half.

Each step removes approximately half of the remaining search space.

---

## Example

Suppose there are:

```text
1,024 elements
```

Binary Search reduces the search space like this:

```text
1024
512
256
128
64
32
16
8
4
2
1
```

That requires only around:

```text
10 steps
```

Compare that with a linear search, which may require:

```text
1,024 steps
```

This is why Binary Search is extremely efficient.

---

## Why is it called logarithmic?

Because we repeatedly divide the input.

For Binary Search:

```text
n
n/2
n/4
n/8
n/16
...
```

until approximately:

```text
1
```

The number of times we can divide by 2 is approximately:

```text
log₂(n)
```

Therefore:

```text
O(log n)
```

---

## Growth Example

For Binary Search:

```text
n = 8
≈ 3 steps

n = 16
≈ 4 steps

n = 1,024
≈ 10 steps

n = 1,048,576
≈ 20 steps
```

Notice something very important.

The data can grow to more than one million elements, but Binary Search still needs only around 20 comparisons in the ideal model.

That is the power of:

```text
O(log n)
```

---

# 9. O(n) - Linear Time

`O(n)` is called **Linear Time**.

The amount of work grows roughly in proportion to the input size.

Consider:

```python
def print_numbers(numbers):
    for number in numbers:
        print(number)
```

Every element is visited once.

If:

```text
n = 5
```

we perform approximately:

```text
5 iterations
```

If:

```text
n = 100
```

we perform approximately:

```text
100 iterations
```

If:

```text
n = 1,000,000
```

we perform approximately:

```text
1,000,000 iterations
```

Therefore:

```text
O(n)
```

---

## Searching Example

```python
def find_number(numbers, target):
    for number in numbers:
        if number == target:
            return True

    return False
```

In the worst case, the target may be:

```text
the last element
```

or:

```text
not present at all
```

Then we may need to check every element.

Therefore the worst-case Time Complexity is:

```text
O(n)
```

This algorithm is called:

```text
Linear Search
```

---

# 10. O(n log n) - Linearithmic Time

`O(n log n)` is commonly called:

**Linearithmic Time**

or sometimes:

**Log-linear Time**

This complexity appears frequently in efficient sorting algorithms.

Examples include:

```text
Merge Sort
Heap Sort
```

It can be understood as a combination of:

```text
n
```

and:

```text
log n
```

---

## Intuition

Imagine we divide a list into smaller pieces.

If we repeatedly divide the list in half, there are approximately:

```text
log n
```

levels.

But at every level, we may process approximately:

```text
n
```

elements.

Therefore:

```text
n × log n
```

which gives:

```text
O(n log n)
```

---

## Example Values

For:

```text
n = 8
```

approximately:

```text
8 × log₂(8)

8 × 3

= 24
```

For:

```text
n = 1,024
```

approximately:

```text
1024 × 10

= 10,240
```

Compare this with:

```text
O(n²)
```

For the same:

```text
n = 1,024
```

quadratic growth would be approximately:

```text
1,024 × 1,024

= 1,048,576
```

That difference becomes extremely important for large datasets.

---

# 11. O(n²) - Quadratic Time

`O(n²)` is called:

**Quadratic Time**

A common sign of O(n²) is a nested loop where both loops depend on `n`.

Example:

```python
def print_pairs(numbers):

    for first in numbers:

        for second in numbers:

            print(first, second)
```

Suppose:

```text
n = 3
```

The first loop runs:

```text
3 times
```

For every iteration of the first loop, the second loop also runs:

```text
3 times
```

Therefore:

```text
3 × 3 = 9
```

operations.

---

## If n = 10

```text
10 × 10 = 100
```

---

## If n = 100

```text
100 × 100 = 10,000
```

---

## If n = 1,000

```text
1,000 × 1,000
=
1,000,000
```

The growth becomes very fast.

Therefore:

```text
O(n²)
```

---

## Visual Example

```python
numbers = [1, 2, 3]

for i in numbers:
    for j in numbers:
        print(i, j)
```

Output:

```text
1 1
1 2
1 3

2 1
2 2
2 3

3 1
3 2
3 3
```

There are:

```text
9 outputs
```

because:

```text
3² = 9
```

---

# 12. Comparing Big-O Complexities

From generally better scaling to worse scaling:

```text
O(1)
   ↓
O(log n)
   ↓
O(n)
   ↓
O(n log n)
   ↓
O(n²)
```

This does not mean that an O(1) implementation will always be faster than every O(n) implementation for every tiny input.

Big-O is mainly about:

> How the algorithm behaves as the input becomes very large.

---

# Big-O Comparison Table

| Complexity | Name | Example |
|---|---|---|
| O(1) | Constant | Access array by index |
| O(log n) | Logarithmic | Binary Search |
| O(n) | Linear | Linear Search |
| O(n log n) | Linearithmic | Merge Sort |
| O(n²) | Quadratic | Two nested loops |

---

# 13. How Input Size Changes Performance

Consider approximate operation growth:

| n | O(1) | O(log n) | O(n) | O(n log n) | O(n²) |
|---:|---:|---:|---:|---:|---:|
| 10 | 1 | ~3 | 10 | ~33 | 100 |
| 100 | 1 | ~7 | 100 | ~664 | 10,000 |
| 1,000 | 1 | ~10 | 1,000 | ~9,966 | 1,000,000 |
| 10,000 | 1 | ~13 | 10,000 | ~132,877 | 100,000,000 |

This table shows why understanding complexity matters.

When `n` is small, many algorithms seem fast.

But when `n` becomes large, the growth rate becomes extremely important.

---

# 14. Big-O Drops Constants

Consider:

```python
def print_numbers(numbers):

    for number in numbers:
        print(number)

    for number in numbers:
        print(number)
```

The first loop performs approximately:

```text
n
```

operations.

The second performs approximately:

```text
n
```

operations.

Together:

```text
n + n
```

which is:

```text
2n
```

Technically:

```text
O(2n)
```

But Big-O ignores constant multipliers.

Therefore:

```text
O(2n)
```

becomes:

```text
O(n)
```

Why?

Because we care about how the algorithm grows.

Both:

```text
n
```

and:

```text
2n
```

grow linearly.

---

# 15. Big-O Drops Smaller Terms

Consider:

```text
O(n² + n + 10)
```

When `n` becomes very large, the `n²` term dominates.

Suppose:

```text
n = 1,000
```

Then:

```text
n² = 1,000,000

n = 1,000

constant = 10
```

The `n²` term is far larger.

Therefore:

```text
O(n² + n + 10)
```

is simplified to:

```text
O(n²)
```

---

# 16. Consecutive Loops

Consider:

```python
for number in numbers:
    print(number)

for number in numbers:
    print(number)
```

First loop:

```text
O(n)
```

Second loop:

```text
O(n)
```

Together:

```text
O(n + n)
```

which simplifies to:

```text
O(n)
```

The loops are one after another.

We **add** their complexities.

---

# 17. Nested Loops

Consider:

```python
for i in numbers:
    for j in numbers:
        print(i, j)
```

Outer loop:

```text
n times
```

Inner loop:

```text
n times for every outer iteration
```

Therefore:

```text
n × n
```

which becomes:

```text
O(n²)
```

For nested loops, we often multiply the number of iterations.

---

# Important Difference

Consecutive loops:

```python
for i in numbers:
    pass

for j in numbers:
    pass
```

approximately:

```text
n + n
=
O(n)
```

Nested loops:

```python
for i in numbers:
    for j in numbers:
        pass
```

approximately:

```text
n × n
=
O(n²)
```

This difference is very important.

---

# 18. Different Input Variables

Not every nested loop is automatically O(n²).

Consider:

```python
def print_pairs(list_a, list_b):

    for a in list_a:

        for b in list_b:

            print(a, b)
```

Suppose:

```text
list_a has n elements
```

and:

```text
list_b has m elements
```

Then the complexity is:

```text
O(n × m)
```

or:

```text
O(nm)
```

It would be incorrect to automatically call this:

```text
O(n²)
```

because the two lists may have different sizes.

This is an important detail when analyzing real algorithms.

---

# 19. Best Case, Average Case, and Worst Case

Sometimes an algorithm does not always perform the same number of operations.

Consider Linear Search:

```python
def search(numbers, target):

    for number in numbers:

        if number == target:
            return True

    return False
```

Suppose:

```python
numbers = [10, 20, 30, 40, 50]
```

and we search for:

```text
10
```

We find it immediately.

This is the:

```text
Best Case
```

approximately:

```text
O(1)
```

---

If we search for:

```text
50
```

we may check every element.

Worst case:

```text
O(n)
```

---

If the target is somewhere around the middle, we might check approximately half of the elements.

That describes an average type of behavior.

When discussing Big-O, we often focus on the upper growth bound and commonly discuss worst-case behavior, but the exact convention depends on the algorithm and context.

---

# 20. Common Big-O Mistakes

## Mistake 1: Thinking O(1) means one operation

Incorrect idea:

```text
O(1) = exactly one operation
```

Correct idea:

```text
The work does not grow with input size.
```

---

## Mistake 2: Every loop is O(n)

Not necessarily.

Example:

```python
i = 1

while i < n:
    i *= 2
```

The values may grow:

```text
1
2
4
8
16
32
64
...
```

The input is effectively reduced or jumped through exponentially.

This loop performs approximately:

```text
O(log n)
```

not:

```text
O(n)
```

---

## Mistake 3: Every nested loop is O(n²)

Not always.

Example:

```python
for a in list_a:
    for b in list_b:
        print(a, b)
```

Complexity:

```text
O(nm)
```

if the inputs have different sizes.

---

## Mistake 4: Counting exact seconds

Big-O is not normally:

```text
This code takes 0.5 seconds.
```

Big-O describes:

```text
How the amount of work grows as input grows.
```

Actual runtime depends on many factors.

---

# 21. Practice Questions

Try these before checking the answers.

---

## Question 1

```python
def example(arr):
    return arr[0]
```

What is the complexity?

<details>

<summary>Show Answer</summary>

```text
O(1)
```

We directly access one element.

</details>

---

## Question 2

```python
def example(arr):
    for item in arr:
        print(item)
```

What is the complexity?

<details>

<summary>Show Answer</summary>

```text
O(n)
```

We visit every element once.

</details>

---

## Question 3

```python
def example(arr):
    for i in arr:
        for j in arr:
            print(i, j)
```

What is the complexity?

<details>

<summary>Show Answer</summary>

```text
O(n²)
```

The loops are nested.

</details>

---

## Question 4

```python
def example(arr):
    print(arr[0])
    print(arr[1])
    print(arr[2])
```

What is the complexity?

<details>

<summary>Show Answer</summary>

```text
O(1)
```

The amount of work remains constant regardless of input size.

</details>

---

## Question 5

```python
def example(arr):

    for item in arr:
        print(item)

    for item in arr:
        print(item)
```

What is the complexity?

<details>

<summary>Show Answer</summary>

```text
O(n)
```

The raw expression is approximately:

```text
O(n + n)
=
O(2n)
```

Big-O drops the constant:

```text
O(n)
```

</details>

---

## Question 6

```python
def example(arr):

    for i in arr:

        for j in arr:

            print(i, j)

    for item in arr:
        print(item)
```

We have:

```text
O(n²)
```

from the nested loops.

And:

```text
O(n)
```

from the final loop.

Together:

```text
O(n² + n)
```

The dominant term is:

```text
n²
```

Therefore:

```text
O(n²)
```

---

# 22. Quick Recognition Guide

When reading code, this can help:

```text
Direct access
→ O(1)

Input repeatedly cut approximately in half
→ O(log n)

One full traversal
→ O(n)

Divide-and-conquer with linear work per level
→ Often O(n log n)

Two full nested traversals
→ O(n²)
```

This is only a quick guide.

Real algorithms sometimes require deeper analysis.

---

# Big-O Cheat Sheet

```text
O(1)
Constant Time
Example: arr[0]

O(log n)
Logarithmic Time
Example: Binary Search

O(n)
Linear Time
Example: Traverse an array

O(n log n)
Linearithmic Time
Example: Merge Sort

O(n²)
Quadratic Time
Example: Nested loops over the same input
```

---

# What I Learned on Day 1

After completing Day 1, I understand that Big-O is not simply about whether code is "fast" or "slow."

It is mainly about:

> How an algorithm grows when the amount of input grows.

I learned that:

### O(1)

The work remains approximately constant.

```python
return arr[0]
```

---

### O(log n)

The problem becomes much smaller after every step.

Example:

```text
Binary Search
```

---

### O(n)

The work grows directly with the input size.

Example:

```python
for item in arr:
    print(item)
```

---

### O(n log n)

There are approximately `log n` levels of work, with approximately `n` work across each level.

Example:

```text
Merge Sort
```

---

### O(n²)

The work can grow roughly as the square of the input.

Example:

```python
for i in arr:
    for j in arr:
        print(i, j)
```

---

# My Day 1 Progress

- [x] Learned Big-O basics
- [x] Learned Time Complexity
- [x] Learned Space Complexity
- [x] Learned O(1)
- [x] Learned O(log n)
- [x] Learned O(n)
- [x] Learned O(n log n)
- [x] Learned O(n²)
- [x] Learned how consecutive loops affect complexity
- [x] Learned how nested loops affect complexity
- [x] Learned why constants are removed
- [x] Learned why smaller terms are removed
- [x] Practiced identifying complexity from Python code

---

# Important Things to Remember

Do not only memorize:

```text
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
```

The real goal is to understand:

```text
What is the input?

What grows when the input grows?

How many times does the code repeat?

Does the algorithm process everything?

Does it divide the problem?

Are the loops consecutive?

Are the loops nested?

Does the algorithm create extra memory?
```

If I can answer these questions, I can begin analyzing algorithms instead of only memorizing complexity names.

---

# Files in Day 01

```text
Day-01-Big-O/
│
├── README.md
├── examples.py
└── practice.py
```

### `README.md`

Detailed explanation and notes from Day 1.

### `examples.py`

Python examples demonstrating different complexity classes.

### `practice.py`

Practice problems for identifying Time Complexity.

---

# Next: Day 02

The next topic will be:

# Arrays and Python Lists

I will learn:

- What an Array is
- How arrays store data
- Indexes
- Accessing elements
- Traversing arrays
- Updating elements
- Inserting elements
- Removing elements
- Searching arrays
- Array Time Complexity
- Python Lists
- Common Array interview problems

---

# 90 Days of DSA

This repository is part of my **90 Days of Data Structures and Algorithms** learning journey.

My goal is not only to solve coding problems.

I want to understand **why algorithms work, how efficient they are, and how to explain them clearly**.

All notes and examples are being documented so that other beginners can also use this repository as a free learning resource.