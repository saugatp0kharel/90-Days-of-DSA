# Day 11 - Recursion

Welcome to **Day 11** of my **90 Days of Data Structures and Algorithms** journey.

So far I have learned:

```text
Day 01 - Big-O and Complexity
Day 02 - Arrays and Python Lists
Day 03 - Array Problems and Two Pointers
Day 04 - Strings
Day 05 - String Problems and Patterns
Day 06 - Hash Tables, Dictionaries, and Sets
Day 07 - Stacks
Day 08 - Queues and Deques
Day 09 - Linked Lists
Day 10 - Linked List Problems and Pointer Patterns
```

Today I am learning:

# Recursion

Recursion happens when a function calls itself.

The main idea is:

```text
Take a big problem
        ↓
Solve a smaller version
        ↓
Solve an even smaller version
        ↓
Eventually reach a simple case
```

The simple stopping condition is called:

# Base Case

Today I learned:

- What recursion is
- Base case
- Recursive case
- Call stack
- Recursive thinking
- Countdown
- Sum from 1 to n
- Factorial
- Fibonacci
- Reverse a string recursively
- Palindrome recursively
- Sum an array recursively
- Find maximum recursively
- Recursion vs iteration
- Recursion Time Complexity
- Recursion Space Complexity
- Common recursion mistakes

---

# 1. What is Recursion?

Recursion means:

> A function calls itself.

Example:

```python
def hello():

    print("Hello")

    hello()
```

This function calls itself.

But this code has a serious problem.

It never stops.

Eventually Python will raise:

```text
RecursionError
```

So recursion needs a stopping condition.

That condition is called:

```text
Base Case
```

---

# 2. Two Main Parts of Recursion

A recursive function normally needs:

```text
1. Base Case
2. Recursive Case
```

---

# 3. Base Case

The base case tells the function:

```text
STOP
```

Example:

```python
def countdown(number):

    if number == 0:

        return
```

This is the base case.

When:

```text
number == 0
```

the recursion stops.

---

# 4. Recursive Case

The recursive case calls the function again with a smaller problem.

Example:

```python
countdown(number - 1)
```

The input becomes smaller every time.

---

# 5. Complete Countdown Example

```python
def countdown(number):

    if number == 0:

        print("Done!")

        return

    print(number)

    countdown(number - 1)
```

Call:

```python
countdown(5)
```

Output:

```text
5
4
3
2
1
Done!
```

---

# 6. How Countdown Works

Start:

```text
countdown(5)
```

Print:

```text
5
```

Call:

```text
countdown(4)
```

Then:

```text
countdown(3)
```

Then:

```text
countdown(2)
```

Then:

```text
countdown(1)
```

Then:

```text
countdown(0)
```

Base case:

```text
STOP
```

---

# 7. Recursion Visualization

Think about this:

```text
countdown(3)

    countdown(2)

        countdown(1)

            countdown(0)
```

The calls become smaller until reaching the base case.

---

# 8. The Call Stack

Remember Day 7?

We learned:

```text
Stack = LIFO
```

Python uses a stack internally when functions are called.

This is called:

# Call Stack

Suppose:

```python
countdown(3)
```

Calls:

```text
countdown(3)
countdown(2)
countdown(1)
countdown(0)
```

They are placed on the call stack.

---

# 9. Call Stack Visualization

```text
Top

countdown(0)
countdown(1)
countdown(2)
countdown(3)

Bottom
```

Once the base case finishes:

```text
countdown(0)
```

returns.

Then:

```text
countdown(1)
```

returns.

Then:

```text
countdown(2)
```

returns.

Then:

```text
countdown(3)
```

returns.

This is LIFO.

---

# 10. Recursive Thinking

When solving recursively, ask:

```text
What is the smallest possible version
of this problem?
```

That is usually the base case.

Then ask:

```text
How can I reduce the current problem
into a smaller version?
```

That becomes the recursive case.

---

# 11. Sum from 1 to n

Problem:

```text
sum(5)
```

means:

```text
1 + 2 + 3 + 4 + 5
```

Answer:

```text
15
```

---

# 12. Recursive Relationship

We can say:

```text
sum(5)
=
5 + sum(4)
```

And:

```text
sum(4)
=
4 + sum(3)
```

So:

```text
sum(n)
=
n + sum(n - 1)
```

---

# 13. Base Case for Sum

Eventually:

```text
sum(1)
```

The answer is simply:

```text
1
```

So:

```python
if n == 1:

    return 1
```

---

# 14. Recursive Sum Solution

```python
def recursive_sum(n):

    if n == 1:

        return 1

    return n + recursive_sum(n - 1)
```

Example:

```python
print(
    recursive_sum(5)
)
```

Output:

```text
15
```

---

# 15. Sum Step-by-Step

```text
sum(5)

= 5 + sum(4)

= 5 + 4 + sum(3)

= 5 + 4 + 3 + sum(2)

= 5 + 4 + 3 + 2 + sum(1)

= 5 + 4 + 3 + 2 + 1

= 15
```

---

# 16. Factorial

Factorial is written:

```text
n!
```

Example:

```text
5!
```

means:

```text
5 × 4 × 3 × 2 × 1
```

Answer:

```text
120
```

---

# 17. Factorial Relationship

We can write:

```text
5!
=
5 × 4!
```

And:

```text
4!
=
4 × 3!
```

Therefore:

```text
n!
=
n × (n - 1)!
```

---

# 18. Factorial Base Case

We define:

```text
0! = 1
```

and:

```text
1! = 1
```

So a common base case is:

```python
if n <= 1:

    return 1
```

---

# 19. Recursive Factorial

```python
def factorial(n):

    if n <= 1:

        return 1

    return n * factorial(n - 1)
```

Example:

```python
print(
    factorial(5)
)
```

Output:

```text
120
```

---

# 20. Factorial Step-by-Step

```text
factorial(5)

= 5 × factorial(4)

= 5 × 4 × factorial(3)

= 5 × 4 × 3 × factorial(2)

= 5 × 4 × 3 × 2 × factorial(1)

= 5 × 4 × 3 × 2 × 1

= 120
```

---

# 21. Time Complexity of Factorial

Each call decreases `n` by 1.

For:

```text
factorial(n)
```

there are approximately:

```text
n calls
```

Therefore:

```text
Time = O(n)
```

---

# 22. Space Complexity of Factorial

Because recursive calls remain on the call stack:

```text
n calls
```

can exist at once.

Therefore:

```text
Space = O(n)
```

This is an important difference between recursive and iterative solutions.

---

# 23. Iterative Factorial

The same problem can be solved without recursion:

```python
def factorial_iterative(n):

    result = 1

    for number in range(2, n + 1):

        result *= number

    return result
```

Time:

```text
O(n)
```

Extra space:

```text
O(1)
```

Recursive version:

```text
Time = O(n)
Space = O(n)
```

Iterative version:

```text
Time = O(n)
Space = O(1)
```

---

# 24. Fibonacci Sequence

The Fibonacci sequence begins:

```text
0
1
1
2
3
5
8
13
21
...
```

Each number is the sum of the previous two.

Formula:

```text
F(n)
=
F(n - 1) + F(n - 2)
```

---

# 25. Fibonacci Base Cases

```text
F(0) = 0

F(1) = 1
```

---

# 26. Recursive Fibonacci

```python
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
```

Example:

```python
print(
    fibonacci(6)
)
```

Output:

```text
8
```

---

# 27. Why Simple Recursive Fibonacci is Slow

Consider:

```text
fibonacci(5)
```

It calculates:

```text
fibonacci(4)
fibonacci(3)
```

But inside:

```text
fibonacci(4)
```

it calculates:

```text
fibonacci(3)
```

again.

The same problems are repeatedly solved.

This causes a lot of repeated work.

---

# 28. Fibonacci Recursion Tree

```text
                 F(5)

           /               \

        F(4)               F(3)

      /     \             /    \

   F(3)     F(2)       F(2)   F(1)

   ...
```

Notice:

```text
F(3)
```

and:

```text
F(2)
```

are calculated many times.

---

# 29. Fibonacci Complexity

The simple recursive implementation is approximately:

```text
Time = O(2^n)
```

This is exponential.

It becomes slow very quickly.

The recursion depth is:

```text
O(n)
```

So stack space is:

```text
O(n)
```

Later we will learn:

```text
Memoization
Dynamic Programming
```

to make Fibonacci much faster.

---

# 30. Reverse String Recursively

Problem:

```text
hello
```

Expected:

```text
olleh
```

We can think:

```text
reverse("hello")
```

as:

```text
reverse("ello") + "h"
```

---

# Solution

```python
def reverse_string(text):

    if len(text) <= 1:

        return text

    return (
        reverse_string(text[1:])
        +
        text[0]
    )
```

Example:

```python
print(
    reverse_string(
        "hello"
    )
)
```

Output:

```text
olleh
```

---

# 31. Reverse Step-by-Step

```text
reverse("cat")

=
reverse("at") + "c"

=
reverse("t") + "a" + "c"

=
"t" + "a" + "c"

=
"tac"
```

---

# 32. Important Python Complexity Note

This implementation uses:

```python
text[1:]
```

Python slicing creates a new string.

That means the simple recursive implementation can use more time and memory than it first appears.

For learning recursion, it is still a useful example.

Later we can optimize using indexes.

---

# 33. Recursive Palindrome

A palindrome reads the same forward and backward.

Examples:

```text
racecar
level
madam
```

Main idea:

Compare:

```text
first character
last character
```

If they differ:

```text
False
```

If they match:

```text
check the inside
```

---

# 34. Palindrome Solution

```python
def is_palindrome(text):

    if len(text) <= 1:

        return True

    if text[0] != text[-1]:

        return False

    return is_palindrome(
        text[1:-1]
    )
```

Example:

```python
print(
    is_palindrome(
        "racecar"
    )
)
```

Output:

```text
True
```

---

# 35. Palindrome Step-by-Step

```text
racecar

r == r
```

Check:

```text
aceca
```

Then:

```text
a == a
```

Check:

```text
cec
```

Then:

```text
c == c
```

Check:

```text
e
```

One character means:

```text
True
```

---

# 36. Sum an Array Recursively

Problem:

```python
[1, 2, 3, 4]
```

Expected:

```text
10
```

Think:

```text
sum([1,2,3,4])

=
1 + sum([2,3,4])
```

---

# Solution

```python
def array_sum(numbers):

    if len(numbers) == 0:

        return 0

    return (
        numbers[0]
        +
        array_sum(numbers[1:])
    )
```

---

# 37. Array Sum Step-by-Step

```text
sum([1,2,3])

=
1 + sum([2,3])

=
1 + 2 + sum([3])

=
1 + 2 + 3 + sum([])

=
1 + 2 + 3 + 0

=
6
```

---

# 38. Better Recursive Array Sum with Index

Instead of slicing:

```python
numbers[1:]
```

we can pass an index.

```python
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
```

This avoids creating a new list every call.

---

# 39. Find Maximum Recursively

Problem:

```python
[4, 8, 2, 10, 5]
```

Expected:

```text
10
```

Solution:

```python
def recursive_max(numbers, index=0):

    if index == len(numbers) - 1:

        return numbers[index]

    max_of_rest = recursive_max(
        numbers,
        index + 1
    )

    return max(
        numbers[index],
        max_of_rest
    )
```

---

# 40. How Recursive Maximum Works

For:

```text
[4, 8, 2]
```

We compare:

```text
4
```

with the maximum of:

```text
[8, 2]
```

Then compare:

```text
8
```

with maximum of:

```text
[2]
```

Base case:

```text
2
```

Then answers return upward.

---

# 41. Print Numbers Increasing Recursively

Suppose we want:

```text
1
2
3
4
5
```

Interesting recursion trick:

```python
def print_increasing(n):

    if n == 0:

        return

    print_increasing(n - 1)

    print(n)
```

Notice:

```python
print(n)
```

comes AFTER the recursive call.

---

# 42. Recursion Before vs After

Consider:

```python
def example(n):

    if n == 0:

        return

    print(n)

    example(n - 1)
```

This prints:

```text
3
2
1
```

But:

```python
def example(n):

    if n == 0:

        return

    example(n - 1)

    print(n)
```

prints:

```text
1
2
3
```

This is because code after the recursive call runs while the call stack is unwinding.

---

# 43. Recursion Has Two Directions

Think of recursion as:

```text
Going down
```

and:

```text
Coming back up
```

Example:

```text
function(3)
↓
function(2)
↓
function(1)
↓
base case
↑
return
↑
return
↑
return
```

Understanding both directions is very important.

---

# 44. Recursion vs Iteration

## Iteration

Uses:

```text
for
while
```

Example:

```python
for i in range(5):
```

---

## Recursion

Uses:

```text
function calling itself
```

Example:

```python
function(n - 1)
```

---

# 45. When is Recursion Useful?

Recursion is especially useful when a problem naturally contains smaller versions of itself.

Examples:

- Trees
- Graph traversal
- Divide and Conquer
- Binary Search
- Merge Sort
- Quick Sort
- Backtracking
- Permutations
- Combinations
- File/folder structures

We will use recursion much more later.

---

# 46. Recursive Problem-Solving Template

A basic recursive function often looks like:

```python
def function(problem):

    # Base case
    if smallest_case:

        return answer

    # Recursive case
    return something + function(smaller_problem)
```

---

# 47. Three Questions for Recursion

Whenever I solve a recursive problem, I should ask:

```text
1. What is my base case?
```

```text
2. How does the problem become smaller?
```

```text
3. Am I guaranteed to eventually reach the base case?
```

If question 3 is:

```text
No
```

the recursion may never stop.

---

# 48. Common Mistake - Missing Base Case

Bad:

```python
def countdown(n):

    print(n)

    countdown(n - 1)
```

This continues forever until Python stops it.

Correct:

```python
if n == 0:

    return
```

---

# 49. Common Mistake - Base Case Never Reached

Example:

```python
def countdown(n):

    if n == 0:

        return

    countdown(n + 1)
```

Starting with:

```text
5
```

gives:

```text
6
7
8
9
...
```

We are moving away from the base case.

Correct:

```python
countdown(n - 1)
```

---

# 50. Common Mistake - Forgetting return

Consider:

```python
def factorial(n):

    if n <= 1:

        return 1

    factorial(n - 1)
```

This does not return the recursive result.

Correct:

```python
return n * factorial(n - 1)
```

---

# 51. Recursion Limit

Python prevents unlimited recursion.

Example:

```python
import sys

print(
    sys.getrecursionlimit()
)
```

Python's recursion limit is usually around a thousand calls, although the exact setting can vary.

Deep recursion may therefore cause:

```text
RecursionError
```

---

# 52. Recursive Time Complexity

There is no single complexity for all recursive functions.

It depends on:

```text
how many recursive calls happen
```

and:

```text
how much work each call performs
```

Examples:

```text
Factorial
O(n)
```

```text
Simple Fibonacci
O(2^n)
```

---

# 53. Recursive Space Complexity

Recursive functions use the call stack.

If recursion depth is:

```text
n
```

then stack space is often:

```text
O(n)
```

Example:

```text
factorial(n)
```

has:

```text
O(n)
```

recursive depth.

---

# 54. Complexity Summary

| Problem | Time | Recursive Stack |
|---|---:|---:|
| Countdown | O(n) | O(n) |
| Sum 1 to n | O(n) | O(n) |
| Factorial | O(n) | O(n) |
| Fibonacci naive | O(2^n) | O(n) |
| Indexed Array Sum | O(n) | O(n) |
| Recursive Max | O(n) | O(n) |
| Simple recursive string slicing | can be O(n²) | O(n) plus created slices |

---

# 55. Recursion vs Loop Example

Countdown with loop:

```python
def countdown_loop(n):

    while n > 0:

        print(n)

        n -= 1
```

Recursive:

```python
def countdown_recursive(n):

    if n == 0:

        return

    print(n)

    countdown_recursive(n - 1)
```

Both work.

The loop usually uses less extra memory.

But recursion may express some problems more naturally.

---

# 56. Important Recursion Patterns

## Pattern 1 - Reduce Number

```python
function(n - 1)
```

Examples:

```text
factorial
countdown
sum
```

---

## Pattern 2 - Reduce Index

```python
function(index + 1)
```

Examples:

```text
array traversal
recursive maximum
```

---

## Pattern 3 - Reduce String

```python
function(text[1:])
```

Useful for learning:

```text
reverse
palindrome
```

---

## Pattern 4 - Multiple Recursive Calls

```python
function(n - 1)
+
function(n - 2)
```

Example:

```text
Fibonacci
```

This can cause exponential growth.

---

# 57. Day 11 Self-Test

Before completing Day 11, I should be able to explain:

1. What is recursion?
2. What is a base case?
3. What is a recursive case?
4. Why does recursion need a base case?
5. What is the call stack?
6. How does LIFO relate to recursion?
7. What happens when recursion reaches the base case?
8. How does countdown work recursively?
9. How does recursive sum work?
10. What is factorial?
11. What is the factorial recursive formula?
12. Why is factorial O(n)?
13. Why does recursive factorial use O(n) stack space?
14. What is Fibonacci?
15. Why is naive recursive Fibonacci slow?
16. Why is Fibonacci approximately O(2^n)?
17. How can recursion reverse a string?
18. How can recursion check a palindrome?
19. How can we recursively sum an array?
20. Why can using indexes be better than slicing?
21. How can we find maximum recursively?
22. What happens before a recursive call?
23. What happens after a recursive call?
24. What is stack unwinding?
25. When is recursion useful?

---

# My Day 11 Progress

- [x] Learned Recursion
- [x] Learned Base Case
- [x] Learned Recursive Case
- [x] Learned Call Stack
- [x] Built Recursive Countdown
- [x] Built Recursive Sum
- [x] Built Recursive Factorial
- [x] Learned Fibonacci Recursion
- [x] Reversed String Recursively
- [x] Checked Palindrome Recursively
- [x] Summed Array Recursively
- [x] Found Maximum Recursively
- [x] Compared Recursion and Iteration
- [x] Learned Stack Unwinding
- [x] Analyzed Recursive Time Complexity
- [x] Analyzed Recursive Space Complexity

---

# Day 11 Quick Cheat Sheet

```text
Recursion
→ function calls itself
```

```text
Base Case
→ stops recursion
```

```text
Recursive Case
→ smaller version of problem
```

```text
Call Stack
→ stores active function calls
```

```text
Factorial
→ n × factorial(n - 1)
```

```text
Factorial
→ O(n) Time
→ O(n) Stack Space
```

```text
Naive Fibonacci
→ O(2^n)
```

```text
Always ask:

1. What is the base case?
2. How does the problem get smaller?
3. Will it reach the base case?
```

---

# Files in Day 11

```text
Day-11-Recursion/
├── README.md
├── examples.py
└── practice.py
```

---

# Next - Day 12

Next topic:

# Binary Search

Possible topics:

- Linear Search Review
- Why Binary Search is Faster
- Sorted Arrays
- Left / Right / Middle
- O(log n)
- Iterative Binary Search
- Recursive Binary Search
- First and Last Occurrence
- Search Insert Position

---

# 90 Days of DSA

Day 11 is not about memorizing recursive code.

The important goal is learning to think:

```text
Can I solve this big problem
by solving a smaller version
of the same problem?
```

If yes, recursion may be a useful tool.