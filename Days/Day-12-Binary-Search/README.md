# Day 12 - Binary Search

Welcome to **Day 12** of my **90 Days of Data Structures and Algorithms** journey.

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
Day 10 - Linked List Problems
Day 11 - Recursion
```

Today I am learning:

# Binary Search

Binary Search is an efficient algorithm for searching inside a:

```text
sorted collection
```

The main idea is:

```text
Do not check every value.

Keep cutting the search area in half.
```

Today I learned:

- Linear Search Review
- Binary Search
- Sorted Array Requirement
- Left Pointer
- Right Pointer
- Middle Index
- Search Space
- Iterative Binary Search
- Recursive Binary Search
- First Occurrence
- Last Occurrence
- Search Insert Position
- Lower Bound idea
- O(log n)
- Common Binary Search Mistakes

---

# 1. Linear Search Review

Suppose:

```python
numbers = [3, 5, 8, 12, 15, 20]
```

We want to find:

```text
15
```

Linear Search checks:

```text
3
5
8
12
15
```

one by one.

Example:

```python
def linear_search(numbers, target):

    for index in range(len(numbers)):

        if numbers[index] == target:

            return index

    return -1
```

Worst case:

```text
O(n)
```

because we may need to inspect every value.

---

# 2. What is Binary Search?

Binary Search does not check every item.

It looks at the:

```text
middle
```

Then it decides whether the target must be:

```text
left side
```

or:

```text
right side
```

Then half of the remaining values are ignored.

---

# 3. Very Important Requirement

Binary Search normally requires the data to be:

# Sorted

Example:

```text
[2, 5, 8, 10, 15, 20, 30]
```

This is sorted.

Binary Search can use the ordering.

But:

```text
[20, 2, 30, 8, 5]
```

is not sorted.

We cannot safely say:

```text
target is smaller than middle,
therefore go left
```

because the values are not ordered.

---

# 4. Binary Search Example

Array:

```text
[2, 5, 8, 10, 15, 20, 30]
```

Find:

```text
20
```

Start:

```text
left = 0

right = 6
```

Middle:

```text
mid = 3
```

Value:

```text
numbers[3] = 10
```

Compare:

```text
20 > 10
```

Therefore:

```text
target must be on the right
```

We can ignore:

```text
2 5 8 10
```

New search:

```text
15 20 30
```

---

# 5. Left, Right, and Mid

Binary Search normally uses three indexes:

```text
left
right
mid
```

Example:

```text
[2, 5, 8, 10, 15, 20, 30]

 L        M             R
```

---

# 6. Calculate Middle

Use:

```python
mid = (left + right) // 2
```

Example:

```text
left = 0
right = 6

mid = (0 + 6) // 2

mid = 3
```

---

# 7. Compare Middle with Target

There are three possibilities.

## Target Found

```python
if numbers[mid] == target:
```

Return:

```python
mid
```

---

## Target is Smaller

If:

```python
target < numbers[mid]
```

the target must be on the left.

So:

```python
right = mid - 1
```

---

## Target is Larger

If:

```python
target > numbers[mid]
```

the target must be on the right.

So:

```python
left = mid + 1
```

---

# 8. Complete Iterative Binary Search

```python
def binary_search(numbers, target):

    left = 0

    right = len(numbers) - 1

    while left <= right:

        mid = (left + right) // 2

        if numbers[mid] == target:

            return mid

        elif target < numbers[mid]:

            right = mid - 1

        else:

            left = mid + 1

    return -1
```

---

# 9. Example

```python
numbers = [
    2,
    5,
    8,
    10,
    15,
    20,
    30
]

print(
    binary_search(
        numbers,
        20
    )
)
```

Output:

```text
5
```

Because:

```text
numbers[5] = 20
```

---

# 10. Binary Search Step-by-Step

Search:

```text
20
```

Inside:

```text
[2, 5, 8, 10, 15, 20, 30]
```

Start:

```text
left = 0
right = 6
```

Middle:

```text
mid = 3

value = 10
```

20 is larger.

Move:

```text
left = 4
```

Now search:

```text
[15, 20, 30]
```

Indexes:

```text
4 5 6
```

Middle:

```text
mid = 5
```

Value:

```text
20
```

Found.

---

# 11. What Happens if Target Does Not Exist?

Example:

```text
target = 17
```

Eventually:

```text
left > right
```

That means:

```text
the search area is empty
```

So return:

```python
-1
```

---

# 12. Why `left <= right`?

Suppose the search area has one element.

Example:

```text
left = 3
right = 3
```

There is still one value to check.

So we need:

```python
while left <= right:
```

not only:

```python
while left < right:
```

for this standard version.

---

# 13. Why Binary Search is Fast

Imagine:

```text
1,000,000 items
```

Linear Search may inspect close to:

```text
1,000,000 items
```

Binary Search repeatedly halves the search space.

Roughly:

```text
1,000,000
500,000
250,000
125,000
62,500
...
```

After only around:

```text
20 halvings
```

the search space is tiny.

That is why Binary Search is:

```text
O(log n)
```

---

# 14. Binary Search Complexity

Every step cuts the remaining search area approximately in half.

So:

```text
Time = O(log n)
```

Iterative version uses only a few variables:

```text
left
right
mid
```

So:

```text
Space = O(1)
```

---

# 15. Linear Search vs Binary Search

| Search | Requirement | Worst Time |
|---|---|---:|
| Linear Search | None | O(n) |
| Binary Search | Sorted data | O(log n) |

Binary Search is faster when the data is sorted.

---

# 16. Recursive Binary Search

Binary Search can also be written recursively.

Remember Day 11?

Recursion solves a smaller version of the same problem.

Binary Search naturally creates a smaller search interval.

---

# Recursive Solution

```python
def binary_search_recursive(
    numbers,
    target,
    left,
    right
):

    if left > right:

        return -1

    mid = (left + right) // 2

    if numbers[mid] == target:

        return mid

    if target < numbers[mid]:

        return binary_search_recursive(
            numbers,
            target,
            left,
            mid - 1
        )

    return binary_search_recursive(
        numbers,
        target,
        mid + 1,
        right
    )
```

Call:

```python
numbers = [2, 5, 8, 10, 15]

result = binary_search_recursive(
    numbers,
    10,
    0,
    len(numbers) - 1
)
```

---

# 17. Recursive Binary Search Base Case

The base case is:

```python
if left > right:

    return -1
```

Why?

Because:

```text
no search area remains
```

---

# 18. Recursive Binary Search Complexity

At every call:

```text
search area becomes half
```

So:

```text
Time = O(log n)
```

But recursive calls use the call stack.

Recursion depth:

```text
O(log n)
```

Therefore:

```text
Space = O(log n)
```

Iterative Binary Search:

```text
O(1) space
```

Recursive Binary Search:

```text
O(log n) stack space
```

---

# 19. Binary Search Does More Than Find a Value

Binary Search can also solve problems like:

```text
first occurrence
last occurrence
insertion position
lower bound
upper bound
answer-space searching
```

Today we will learn the beginner versions.

---

# 20. First Occurrence

Suppose:

```text
[1, 2, 2, 2, 3, 4]
```

Find:

```text
2
```

Normal Binary Search might return any matching `2`.

But sometimes we want the:

```text
first occurrence
```

Expected index:

```text
1
```

---

# 21. Main Idea for First Occurrence

When we find the target:

```text
do not stop immediately
```

Save the answer:

```python
result = mid
```

Then continue searching:

```text
left side
```

because there might be an earlier occurrence.

---

# First Occurrence Solution

```python
def first_occurrence(numbers, target):

    left = 0

    right = len(numbers) - 1

    result = -1

    while left <= right:

        mid = (left + right) // 2

        if numbers[mid] == target:

            result = mid

            right = mid - 1

        elif numbers[mid] < target:

            left = mid + 1

        else:

            right = mid - 1

    return result
```

---

# 22. Last Occurrence

Same idea, but when target is found:

```text
continue searching right
```

---

# Last Occurrence Solution

```python
def last_occurrence(numbers, target):

    left = 0

    right = len(numbers) - 1

    result = -1

    while left <= right:

        mid = (left + right) // 2

        if numbers[mid] == target:

            result = mid

            left = mid + 1

        elif numbers[mid] < target:

            left = mid + 1

        else:

            right = mid - 1

    return result
```

---

# 23. First vs Last Occurrence

Input:

```text
[1, 2, 2, 2, 3]
```

Target:

```text
2
```

First:

```text
index 1
```

Last:

```text
index 3
```

Main difference:

```text
Found target
```

For first:

```text
move left
```

For last:

```text
move right
```

---

# 24. Search Insert Position

Problem:

```text
[1, 3, 5, 6]
```

Target:

```text
5
```

Answer:

```text
2
```

because 5 already exists at index 2.

---

Target:

```text
2
```

Where should it be inserted?

```text
[1, 2, 3, 5, 6]
```

Answer:

```text
1
```

---

# 25. Search Insert Solution

```python
def search_insert(numbers, target):

    left = 0

    right = len(numbers) - 1

    while left <= right:

        mid = (left + right) // 2

        if numbers[mid] == target:

            return mid

        elif numbers[mid] < target:

            left = mid + 1

        else:

            right = mid - 1

    return left
```

Important:

When the loop ends:

```text
left
```

is the correct insertion position.

---

# 26. Search Insert Examples

```text
[1, 3, 5, 6]
```

Target:

```text
2
```

Output:

```text
1
```

Target:

```text
7
```

Output:

```text
4
```

Target:

```text
0
```

Output:

```text
0
```

---

# 27. Lower Bound Idea

A lower bound means:

> Find the first position where a value greater than or equal to the target could appear.

Example:

```text
numbers = [1, 3, 3, 5, 8]

target = 3
```

Lower bound:

```text
index 1
```

because the first value:

```text
>= 3
```

is at index 1.

This is closely related to:

```text
Search Insert Position
```

---

# 28. Lower Bound Solution

```python
def lower_bound(numbers, target):

    left = 0

    right = len(numbers)

    while left < right:

        mid = (left + right) // 2

        if numbers[mid] < target:

            left = mid + 1

        else:

            right = mid

    return left
```

Notice this version uses:

```text
right = len(numbers)
```

and:

```text
while left < right
```

Binary Search can have several correct templates.

The important thing is:

> Do not mix rules from different templates randomly.

---

# 29. Binary Search Invariant

During Binary Search, we maintain a region where the answer may still exist.

Example:

```text
left ........ right
```

Everything outside that region has already been eliminated.

Each comparison must make the region:

```text
smaller
```

If the region does not shrink, we may create an infinite loop.

---

# 30. Common Mistake - Unsorted Input

Bad:

```python
numbers = [
    20,
    3,
    15,
    1,
    10
]
```

Using normal Binary Search here is incorrect.

Binary Search depends on ordering.

---

# 31. Common Mistake - Wrong Right Index

For an inclusive Binary Search:

```python
right = len(numbers) - 1
```

not:

```python
right = len(numbers)
```

because the final valid index is:

```text
len(numbers) - 1
```

---

# 32. Common Mistake - Forgetting +1 or -1

If:

```text
target > numbers[mid]
```

use:

```python
left = mid + 1
```

not:

```python
left = mid
```

Why?

Because we already checked:

```text
mid
```

Keeping it can prevent the search interval from shrinking.

Similarly:

```python
right = mid - 1
```

---

# 33. Common Mistake - Wrong Comparison Direction

Remember:

```python
if numbers[mid] < target:
```

the middle is too small.

Go:

```text
right side
```

So:

```python
left = mid + 1
```

---

# 34. Common Mistake - Returning Too Early

For normal search:

```python
return mid
```

when target is found.

But for:

```text
first occurrence
```

or:

```text
last occurrence
```

do not immediately return.

Save the index and continue searching.

---

# 35. Common Mistake - Mixing Binary Search Templates

One version may use:

```text
left <= right
```

and:

```text
right = mid - 1
```

Another version may use:

```text
left < right
```

and:

```text
right = mid
```

Both can be correct.

But mixing them without understanding can create bugs.

---

# 36. Why Binary Search is O(log n)

Suppose:

```text
n = 16
```

Search sizes:

```text
16
8
4
2
1
```

Only about:

```text
4
```

halving steps.

Because:

```text
2^4 = 16
```

For:

```text
n = 32
```

about:

```text
5 steps
```

because:

```text
2^5 = 32
```

This relationship gives:

```text
log₂(n)
```

Therefore:

```text
O(log n)
```

---

# 37. Binary Search Complexity Summary

| Problem | Time | Extra Space |
|---|---:|---:|
| Linear Search | O(n) | O(1) |
| Iterative Binary Search | O(log n) | O(1) |
| Recursive Binary Search | O(log n) | O(log n) |
| First Occurrence | O(log n) | O(1) |
| Last Occurrence | O(log n) | O(1) |
| Search Insert Position | O(log n) | O(1) |
| Lower Bound | O(log n) | O(1) |

---

# 38. Binary Search Pattern

The standard pattern is:

```python
left = 0

right = len(numbers) - 1

while left <= right:

    mid = (left + right) // 2

    if numbers[mid] == target:

        return mid

    elif numbers[mid] < target:

        left = mid + 1

    else:

        right = mid - 1

return -1
```

Memorizing this template is useful.

But understanding WHY each pointer moves is more important.

---

# 39. Questions to Ask

When considering Binary Search, ask:

```text
1. Is the data sorted?
```

```text
2. Can I eliminate half the possibilities?
```

```text
3. What does left mean?
```

```text
4. What does right mean?
```

```text
5. Is mid too small, too large, or correct?
```

```text
6. Does the search space shrink every time?
```

---

# 40. Binary Search and Recursion

Day 11 taught recursion.

Binary Search is a good example of divide and conquer.

Each recursive call solves:

```text
half of the previous problem
```

Example:

```text
100 elements
↓
50
↓
25
↓
12
↓
6
↓
3
↓
1
```

---

# 41. Binary Search in Real Problems

Binary Search is useful for more than searching numbers.

Later we may use it for:

```text
minimum possible answer
maximum possible answer
capacity problems
speed problems
scheduling
optimization
rotated arrays
matrix searching
```

The deeper idea is:

```text
eliminate half of the possible answers
```

---

# 42. Day 12 Self-Test

Before completing Day 12, I should be able to explain:

1. What is Binary Search?
2. Why must normal Binary Search use sorted data?
3. What does left represent?
4. What does right represent?
5. How is mid calculated?
6. What happens when target equals middle?
7. What happens when target is smaller?
8. What happens when target is larger?
9. Why use `left <= right`?
10. Why is Binary Search O(log n)?
11. Difference between Linear Search and Binary Search?
12. What is iterative Binary Search?
13. What is recursive Binary Search?
14. What is the recursive base case?
15. Why does recursive Binary Search use O(log n) stack space?
16. How do we find the first occurrence?
17. How do we find the last occurrence?
18. Why do we continue searching after finding a duplicate?
19. What is Search Insert Position?
20. Why does `left` become the insertion index?
21. What is lower bound?
22. What happens if the array is unsorted?
23. Why use `mid + 1`?
24. Why use `mid - 1`?
25. Why should Binary Search templates not be mixed carelessly?

---

# My Day 12 Progress

- [x] Reviewed Linear Search
- [x] Learned Binary Search
- [x] Learned Sorted Array Requirement
- [x] Learned Left / Right / Mid
- [x] Built Iterative Binary Search
- [x] Built Recursive Binary Search
- [x] Understood O(log n)
- [x] Found First Occurrence
- [x] Found Last Occurrence
- [x] Solved Search Insert Position
- [x] Learned Lower Bound
- [x] Learned Search Space
- [x] Learned Binary Search Mistakes
- [x] Analyzed Time Complexity
- [x] Analyzed Space Complexity

---

# Day 12 Quick Cheat Sheet

```text
Binary Search
→ sorted data
```

```text
left = 0
right = n - 1
```

```text
mid = (left + right) // 2
```

```text
target > middle
→ go right
```

```text
target < middle
→ go left
```

```text
Time
→ O(log n)
```

```text
Iterative Space
→ O(1)
```

```text
Recursive Space
→ O(log n)
```

```text
First Occurrence
→ find target, continue left
```

```text
Last Occurrence
→ find target, continue right
```

```text
Search Insert
→ return left
```

---

# Files in Day 12

```text
Day-12-Binary-Search/
├── README.md
├── examples.py
└── practice.py
```

---

# Next - Day 13

Next topic:

# Sorting Algorithms - Bubble Sort, Selection Sort, and Insertion Sort

Possible topics:

- What is Sorting?
- Stable Sorting
- In-place Sorting
- Bubble Sort
- Selection Sort
- Insertion Sort
- Best / Average / Worst Case
- O(n²)
- Comparing Sorting Algorithms
- Python `sorted()` and `.sort()`

---

# 90 Days of DSA

The main idea from Day 12 is:

```text
Do not search everything
if ordering lets you eliminate half.
```

Binary Search turns:

```text
O(n)
```

search into:

```text
O(log n)
```

when the conditions are right.