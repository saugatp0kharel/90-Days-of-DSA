# Day 03 - Array Problems and Two Pointers

Welcome to **Day 03** of my **90 Days of Data Structures and Algorithms** journey.

Day 1 was about understanding:

```text
Big-O
Time Complexity
Space Complexity
```

Day 2 was about learning:

```text
Arrays
Python Lists
Indexing
Traversal
Searching
Insertion
Deletion
Slicing
```

Day 3 is where I start using those ideas to solve real problems.

The main goal today is:

> Learn how to think about an array problem, build a simple solution, analyze the solution, and improve it when possible.

Today I learned:

- Problem-solving steps
- Find Sum
- Find Maximum
- Find Minimum
- Count Occurrences
- Contains Duplicate
- Reverse Array
- Two Pointers
- In-place algorithms
- Palindrome
- Move Zeros
- Second Largest
- Pair Sum
- Brute Force
- Optimized Solutions
- Time-Space Trade-offs
- Time Complexity
- Space Complexity

---

# 1. Problem-Solving Process

Before writing code, I should first understand the problem.

A good beginner problem-solving process is:

```text
Read the problem
        ↓
Understand the input
        ↓
Understand the expected output
        ↓
Think of the easiest correct solution
        ↓
Write the code
        ↓
Test the code
        ↓
Find Time Complexity
        ↓
Find Space Complexity
        ↓
Ask if the solution can be improved
```

The goal is not to memorize every solution.

The goal is to learn:

```text
How do I create a solution?
```

---

# 2. Find Sum

## Problem

Given:

```python
numbers = [5, 10, 15, 20, 25]
```

find the sum of all values.

Expected output:

```text
75
```

We will not use:

```python
sum()
```

because we want to understand the algorithm.

## Solution

```python
def find_sum(numbers):

    total = 0

    for number in numbers:
        total += number

    return total
```

Test:

```python
numbers = [5, 10, 15, 20, 25]

print(find_sum(numbers))
```

Output:

```text
75
```

## Step-by-Step

Start:

```text
total = 0
```

Read `5`:

```text
total = 5
```

Read `10`:

```text
total = 15
```

Read `15`:

```text
total = 30
```

Read `20`:

```text
total = 50
```

Read `25`:

```text
total = 75
```

Final answer:

```text
75
```

## Complexity

We visit every element once.

```text
Time Complexity = O(n)
```

We only use a small fixed number of variables.

```text
Extra Space = O(1)
```

---

# 3. Find Maximum

## Problem

Given:

```python
numbers = [14, 3, 99, 21, 7]
```

find the largest number.

Expected:

```text
99
```

Do not use:

```python
max()
```

## Main Idea

Keep one variable:

```text
largest
```

which stores the largest value seen so far.

Start with:

```python
largest = numbers[0]
```

Then compare every number.

If a number is bigger:

```text
update largest
```

## Solution

```python
def find_maximum(numbers):

    largest = numbers[0]

    for number in numbers:

        if number > largest:
            largest = number

    return largest
```

## Step-by-Step

Input:

```text
[14, 3, 99, 21, 7]
```

Start:

```text
largest = 14
```

Compare:

```text
3 > 14?
```

No.

Compare:

```text
99 > 14?
```

Yes.

Update:

```text
largest = 99
```

Compare:

```text
21 > 99?
```

No.

Compare:

```text
7 > 99?
```

No.

Final answer:

```text
99
```

## Why Not Start With 0?

This is unsafe:

```python
largest = 0
```

because the input could be:

```text
[-10, -5, -3]
```

Then `0` would incorrectly become the answer even though `0` is not in the list.

Better:

```python
largest = numbers[0]
```

## Complexity

```text
Time = O(n)
Space = O(1)
```

---

# 4. Find Minimum

The minimum problem is similar to maximum.

## Problem

```python
numbers = [14, 3, 99, 21, 7]
```

Expected:

```text
3
```

## Solution

```python
def find_minimum(numbers):

    smallest = numbers[0]

    for number in numbers:

        if number < smallest:
            smallest = number

    return smallest
```

## Complexity

```text
Time = O(n)
Space = O(1)
```

---

# 5. Count Occurrences

## Problem

Given:

```python
numbers = [1, 2, 3, 2, 4, 2, 5]
```

count how many times:

```text
2
```

appears.

Expected:

```text
3
```

## Solution

```python
def count_occurrences(numbers, target):

    count = 0

    for number in numbers:

        if number == target:
            count += 1

    return count
```

## Step-by-Step

Start:

```text
count = 0
```

Read:

```text
1
```

No match.

Read:

```text
2
```

Match:

```text
count = 1
```

Continue through the list.

Every time we see `2`:

```python
count += 1
```

Final:

```text
3
```

## Complexity

```text
Time = O(n)
Space = O(1)
```

---

# 6. Contains Duplicate

## Problem

Given:

```python
numbers = [1, 2, 3, 4, 2]
```

determine whether any number appears more than once.

Expected:

```text
True
```

## Brute Force Idea

One possible solution is:

```python
for i in range(len(numbers)):

    for j in range(i + 1, len(numbers)):

        if numbers[i] == numbers[j]:
            return True
```

This compares many pairs.

Worst-case:

```text
O(n²)
```

We can improve it.

## Better Idea - Use a Set

A set helps us remember values we already saw.

Start:

```python
seen = set()
```

For each number:

```text
If number is already in seen
→ duplicate found

Otherwise
→ add it to seen
```

## Solution

```python
def contains_duplicate(numbers):

    seen = set()

    for number in numbers:

        if number in seen:
            return True

        seen.add(number)

    return False
```

## Step-by-Step

Input:

```text
[1, 2, 3, 4, 2]
```

Start:

```text
seen = {}
```

Read `1`:

```text
seen = {1}
```

Read `2`:

```text
seen = {1, 2}
```

Read `3`:

```text
seen = {1, 2, 3}
```

Read `4`:

```text
seen = {1, 2, 3, 4}
```

Read `2` again.

`2` is already inside the set.

Therefore:

```python
return True
```

## Complexity

Average set lookup is:

```text
O(1)
```

We do that for up to `n` values.

So average:

```text
Time = O(n)
```

The set can contain up to `n` values.

```text
Space = O(n)
```

---

# 7. Reverse Array Using Slicing

Python allows:

```python
numbers[::-1]
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

reversed_numbers = numbers[::-1]
```

Result:

```text
[5, 4, 3, 2, 1]
```

## Complexity

Python creates another list.

Therefore:

```text
Time = O(n)
Space = O(n)
```

---

# 8. Two Pointers

Two Pointers is an important DSA pattern.

We use two indexes or positions.

Usually:

```python
left
right
```

Example:

```text
[1, 2, 3, 4, 5]

 ^           ^
left        right
```

The pointers can move toward each other:

```text
left  ---->

<---- right
```

Two Pointers can help solve problems involving:

```text
Reverse Array
Palindrome
Pair Sum
Move Zeros
Sorted Arrays
Removing Duplicates
```

---

# 9. Reverse Array Using Two Pointers

## Problem

Reverse:

```text
[1, 2, 3, 4, 5]
```

without creating another large list.

## Step 1

Start:

```text
left = 0
right = 4
```

```text
[1, 2, 3, 4, 5]

 ^           ^
left        right
```

## Step 2

Swap the values.

```text
1 ↔ 5
```

Now:

```text
[5, 2, 3, 4, 1]
```

## Step 3

Move inward.

```python
left += 1
right -= 1
```

Now:

```text
[5, 2, 3, 4, 1]

    ^     ^
   left  right
```

## Step 4

Swap:

```text
2 ↔ 4
```

Result:

```text
[5, 4, 3, 2, 1]
```

## Solution

```python
def reverse_array(numbers):

    left = 0
    right = len(numbers) - 1

    while left < right:

        numbers[left], numbers[right] = \
            numbers[right], numbers[left]

        left += 1
        right -= 1

    return numbers
```

## Complexity

```text
Time = O(n)
Extra Space = O(1)
```

---

# 10. What Does In-Place Mean?

An in-place algorithm changes the original data instead of creating another large data structure.

Example:

```python
reverse_array(numbers)
```

changes:

```text
[1, 2, 3, 4, 5]
```

directly into:

```text
[5, 4, 3, 2, 1]
```

Because we are not creating another list of size `n`:

```text
Extra Space = O(1)
```

---

# 11. Palindrome

A palindrome reads the same forward and backward.

Example:

```text
[1, 2, 3, 2, 1]
```

Forward:

```text
1 2 3 2 1
```

Backward:

```text
1 2 3 2 1
```

So it is a palindrome.

## Two Pointer Idea

Compare:

```text
first item
```

with:

```text
last item
```

If different:

```text
False
```

If equal:

```text
move inward
```

## Solution

```python
def is_palindrome(numbers):

    left = 0
    right = len(numbers) - 1

    while left < right:

        if numbers[left] != numbers[right]:
            return False

        left += 1
        right -= 1

    return True
```

## Complexity

```text
Time = O(n)
Space = O(1)
```

---

# 12. Move Zeros

## Problem

Input:

```text
[0, 1, 0, 3, 12]
```

Expected:

```text
[1, 3, 12, 0, 0]
```

The order of non-zero values should stay the same.

## Main Idea

Use:

```python
insert_position = 0
```

This tells us where the next non-zero number should be placed.

## Solution

```python
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
```

## Step-by-Step

Input:

```text
[0, 1, 0, 3, 12]
```

First move all non-zero values forward:

```text
1
3
12
```

Then fill the remaining positions with:

```text
0
```

Final:

```text
[1, 3, 12, 0, 0]
```

## Complexity

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
=
O(2n)
=
O(n)
```

Extra Space:

```text
O(1)
```

---

# 13. Second Largest

## Problem

Input:

```python
numbers = [10, 5, 20, 8, 15]
```

Largest:

```text
20
```

Second largest:

```text
15
```

## Sorting Approach

We could sort the list.

Sorting generally costs:

```text
O(n log n)
```

But we can solve this in one pass.

## Better Idea

Track:

```text
largest
second
```

## Solution

```python
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
```

## Step-by-Step

Input:

```text
[10, 5, 20, 8, 15]
```

Start:

```text
largest = -infinity
second = -infinity
```

Read `10`:

```text
largest = 10
```

Read `5`:

```text
second = 5
```

Read `20`:

```text
second = 10
largest = 20
```

Read `8`:

```text
no change
```

Read `15`:

```text
second = 15
```

Final:

```text
15
```

## Complexity

```text
Time = O(n)
Space = O(1)
```

---

# 14. Pair Sum

## Problem

Given a sorted list:

```text
[1, 2, 4, 6, 10]
```

Target:

```text
8
```

Find two values that add to 8.

Possible answer:

```text
2 + 6
```

---

# Brute Force Solution

We could compare every possible pair.

```python
for i in range(len(numbers)):

    for j in range(i + 1, len(numbers)):

        if numbers[i] + numbers[j] == target:
            return [numbers[i], numbers[j]]
```

This uses nested loops.

```text
Time = O(n²)
```

---

# Better Solution - Two Pointers

Because the list is sorted:

```text
[1, 2, 4, 6, 10]
```

Start:

```text
left = 1
right = 10
```

Sum:

```text
11
```

Too large.

Move `right` to a smaller number.

Now:

```text
1 + 6 = 7
```

Too small.

Move `left` to a bigger number.

Now:

```text
2 + 6 = 8
```

Found.

## Solution

```python
def pair_sum(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left < right:

        current_sum = (
            numbers[left] +
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
```

## Why Move Left?

If:

```text
current_sum < target
```

the sum is too small.

Because the list is sorted, moving `left` forward gives a larger value.

## Why Move Right?

If:

```text
current_sum > target
```

the sum is too large.

Moving `right` backward gives a smaller value.

## Important Requirement

This exact method depends on the list being:

```text
SORTED
```

## Complexity

```text
Time = O(n)
Space = O(1)
```

---

# 15. Brute Force vs Optimized

One important DSA habit is:

```text
First solve the problem correctly.
Then try to improve it.
```

## Pair Sum

Brute Force:

```text
O(n²)
```

Two Pointers:

```text
O(n)
```

## Contains Duplicate

Brute Force:

```text
Time = O(n²)
Space = O(1)
```

Using Set:

```text
Time = O(n) average
Space = O(n)
```

This introduces an important idea:

# Time-Space Trade-off

Sometimes we use more memory to make an algorithm faster.

---

# 16. Day 3 Complexity Table

| Problem | Time | Extra Space |
|---|---:|---:|
| Find Sum | O(n) | O(1) |
| Find Maximum | O(n) | O(1) |
| Find Minimum | O(n) | O(1) |
| Count Occurrences | O(n) | O(1) |
| Contains Duplicate | O(n) average | O(n) |
| Reverse with Slicing | O(n) | O(n) |
| Reverse with Two Pointers | O(n) | O(1) |
| Palindrome | O(n) | O(1) |
| Move Zeros | O(n) | O(1) |
| Second Largest | O(n) | O(1) |
| Pair Sum | O(n) | O(1) |

---

# 17. Important Patterns Learned

## Accumulator

Example:

```python
total = 0
```

Useful for:

```text
Sum
Count
```

## Track Best Value

Example:

```python
largest = numbers[0]
```

Useful for:

```text
Maximum
Minimum
Second Largest
```

## Seen Set

Example:

```python
seen = set()
```

Useful when asking:

```text
Have I seen this before?
```

## Two Pointers

Example:

```python
left = 0
right = len(numbers) - 1
```

Useful for:

```text
Reverse
Palindrome
Pair Sum
Sorted Array Problems
```

## In-Place Modification

Modify the original list rather than creating a new copy.

Can reduce extra memory from:

```text
O(n)
```

to:

```text
O(1)
```

---

# 18. Common Mistakes

Do not initialize maximum with:

```python
largest = 0
```

if negative numbers are possible.

Use:

```python
largest = numbers[0]
```

Do not assume:

```text
O(n) Time
```

means:

```text
O(n) Space
```

These are different measurements.

Do not use the sorted Pair Sum Two Pointer logic on an unsorted list.

Do not move the wrong pointer:

```text
sum too small
→ left += 1

sum too large
→ right -= 1
```

Remember that:

```python
numbers[::-1]
```

creates another list.

---

# 19. Day 3 Final Review

Today I learned that array problems are often about recognizing patterns.

Instead of thinking only:

```text
Which Python function should I use?
```

I should think:

```text
Can I solve this in one pass?
```

```text
What information do I need to remember?
```

```text
Do I need extra memory?
```

```text
Can Two Pointers help?
```

```text
Can I replace O(n²) with O(n)?
```

---

# My Day 3 Progress

- [x] Learned problem-solving steps
- [x] Solved Find Sum
- [x] Solved Find Maximum
- [x] Solved Find Minimum
- [x] Solved Count Occurrences
- [x] Learned Set basics
- [x] Solved Contains Duplicate
- [x] Reversed array using slicing
- [x] Learned Two Pointers
- [x] Reversed array in-place
- [x] Learned what in-place means
- [x] Solved Palindrome
- [x] Solved Move Zeros
- [x] Solved Second Largest
- [x] Solved Pair Sum
- [x] Compared brute force and optimized solutions
- [x] Learned Time-Space Trade-offs
- [x] Analyzed Time Complexity
- [x] Analyzed Space Complexity

---

# Day 3 Self-Test

Before completing Day 3, I should be able to explain:

```text
How does Find Sum work?

Why is Find Maximum O(n)?

Why should maximum start with numbers[0]?

How does a set find duplicates?

What is Two Pointers?

What does in-place mean?

Why does slicing use O(n) extra space?

How do Two Pointers reverse an array?

How does Palindrome checking work?

How does Move Zeros work?

How can Second Largest be found in one pass?

What is brute force?

Why is brute-force Pair Sum O(n²)?

Why is Two Pointer Pair Sum O(n)?

Why must the Pair Sum input be sorted?

What is a Time-Space Trade-off?
```

---

# Files in Day 03

```text
Day-03-Array-Problems/
│
├── README.md
├── examples.py
└── practice.py
```

`README.md` contains the complete lesson.

`examples.py` contains working examples.

`practice.py` contains questions, my answers, and solutions.

---

# Next - Day 04

Next topic:

# Strings

Topics will include:

```text
String basics
String indexing
Traversal
Slicing
Immutability
Character counting
Reverse String
Palindrome String
Frequency counting
Anagrams
Common String interview problems
```

---

# 90 Days of DSA

The goal of this repository is not only to store code.

The goal is to understand:


the problem
the solution
why it works
Time Complexity
Space Complexity
```

and slowly become able to solve new DSA problems independently.                                                                                                                                                           