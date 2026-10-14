# Day 14 - Merge Sort and Divide & Conquer

Welcome to **Day 14** of my **90 Days of Data Structures and Algorithms** journey.

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
Day 12 - Binary Search
Day 13 - Sorting Basics
```

Today I am learning:

# Merge Sort

Merge Sort is a sorting algorithm based on:

# Divide and Conquer

The main idea is:

```text
Break a big problem
into smaller problems
↓
solve the smaller problems
↓
combine the results
```

Today I learned:

- What Divide and Conquer means
- How arrays are split
- How recursion is used
- How to merge two sorted arrays
- Merge Sort
- Base Case
- Recursive Case
- Recursion Tree
- Why Merge Sort is O(n log n)
- Space Complexity
- Stability
- Merge Sort vs Bubble / Selection / Insertion Sort

---

# 1. What is Divide and Conquer?

Divide and Conquer is a problem-solving strategy.

It has three main steps:

```text
1. Divide
2. Conquer
3. Combine
```

---

# 2. Divide

Take one big problem and split it into smaller problems.

Example:

```text
[8, 3, 5, 1]
```

Split:

```text
[8, 3]

[5, 1]
```

Split again:

```text
[8]
[3]
[5]
[1]
```

---

# 3. Conquer

Solve the smaller problems.

A list with one element is already sorted.

Example:

```text
[8]
```

is sorted.

```text
[3]
```

is sorted.

---

# 4. Combine

Now merge the sorted pieces.

Example:

```text
[8]

and

[3]
```

become:

```text
[3, 8]
```

And:

```text
[5]

and

[1]
```

become:

```text
[1, 5]
```

Then merge:

```text
[3, 8]

and

[1, 5]
```

Result:

```text
[1, 3, 5, 8]
```

---

# 5. What is Merge Sort?

Merge Sort repeatedly:

```text
splits the array in half
```

until each part contains:

```text
one element
```

Then it merges the pieces back together in sorted order.

---

# 6. Merge Sort Example

Start:

```text
[8, 3, 5, 1]
```

Split:

```text
[8, 3]     [5, 1]
```

Split:

```text
[8] [3]    [5] [1]
```

Now merge:

```text
[8] + [3]

→

[3, 8]
```

And:

```text
[5] + [1]

→

[1, 5]
```

Then:

```text
[3, 8] + [1, 5]
```

becomes:

```text
[1, 3, 5, 8]
```

---

# 7. Merge Sort Uses Recursion

Remember Day 11?

Recursion solves:

```text
a smaller version of the same problem
```

Merge Sort does exactly that.

We call Merge Sort on:

```text
left half
```

and:

```text
right half
```

---

# 8. Base Case

The smallest useful array is:

```text
0 or 1 element
```

Such an array is already sorted.

Base case:

```python
if len(numbers) <= 1:

    return numbers
```

---

# 9. Recursive Case

If the array contains more than one element:

```text
split it
```

Then:

```text
sort left half recursively
```

and:

```text
sort right half recursively
```

Then:

```text
merge them
```

---

# 10. Finding the Middle

Use:

```python
mid = len(numbers) // 2
```

Example:

```text
[8, 3, 5, 1]

length = 4

mid = 2
```

Left:

```python
numbers[:mid]
```

gives:

```text
[8, 3]
```

Right:

```python
numbers[mid:]
```

gives:

```text
[5, 1]
```

---

# 11. The Merge Step

This is the most important part.

Suppose we already have:

```text
left = [2, 5, 8]

right = [1, 3, 7]
```

Both are already sorted.

We need to create:

```text
[1, 2, 3, 5, 7, 8]
```

---

# 12. Merge Two Sorted Arrays

We use two pointers:

```text
i
j
```

`i` points into the left array.

`j` points into the right array.

Compare:

```text
left[i]
right[j]
```

Take the smaller value.

---

# 13. Merge Step-by-Step

Left:

```text
[2, 5, 8]
```

Right:

```text
[1, 3, 7]
```

Compare:

```text
2 and 1
```

Take:

```text
1
```

Result:

```text
[1]
```

Compare:

```text
2 and 3
```

Take:

```text
2
```

Result:

```text
[1, 2]
```

Compare:

```text
5 and 3
```

Take:

```text
3
```

Result:

```text
[1, 2, 3]
```

Continue until one side finishes.

Then append the remaining values.

---

# 14. Merge Function

```python
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

    while i < len(left):

        result.append(
            left[i]
        )

        i += 1

    while j < len(right):

        result.append(
            right[j]
        )

        j += 1

    return result
```

---

# 15. Why Append Remaining Values?

Suppose:

```text
left = [1, 4, 8]

right = [2, 3]
```

After comparisons, the right side may finish first.

We might already have:

```text
[1, 2, 3, 4]
```

But:

```text
8
```

is still left.

Since each side was already sorted, we can simply append the remaining values.

---

# 16. Complete Merge Sort

```python
def merge_sort(numbers):

    if len(numbers) <= 1:

        return numbers

    mid = len(numbers) // 2

    left_half = numbers[:mid]

    right_half = numbers[mid:]

    sorted_left = merge_sort(
        left_half
    )

    sorted_right = merge_sort(
        right_half
    )

    return merge(
        sorted_left,
        sorted_right
    )
```

---

# 17. Complete Program

```python
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

            result.append(left[i])

            i += 1

        else:

            result.append(right[j])

            j += 1

    result.extend(
        left[i:]
    )

    result.extend(
        right[j:]
    )

    return result


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
```

---

# 18. Example

```python
numbers = [
    8,
    3,
    5,
    1,
    9,
    2
]

print(
    merge_sort(numbers)
)
```

Output:

```text
[1, 2, 3, 5, 8, 9]
```

---

# 19. Merge Sort Recursion Tree

Suppose:

```text
[8, 3, 5, 1]
```

The recursion looks like:

```text
              [8,3,5,1]

              /       \

          [8,3]       [5,1]

          /   \       /   \

        [8]   [3]   [5]   [1]
```

Then the merging happens upward:

```text
[8] + [3]

→ [3,8]
```

```text
[5] + [1]

→ [1,5]
```

Then:

```text
[3,8] + [1,5]

→ [1,3,5,8]
```

---

# 20. Why is Merge Sort O(n log n)?

This is very important.

There are approximately:

```text
log n
```

levels of splitting.

Why?

Because every level divides the array in half.

Example:

```text
n = 8
```

Split:

```text
8
↓
4
↓
2
↓
1
```

That is:

```text
log₂(8) = 3
```

levels.

---

# 21. Work at Each Level

Although the array is divided into smaller pieces, all pieces together still contain:

```text
n elements
```

During merging, each level processes about:

```text
O(n)
```

elements.

So:

```text
number of levels
×
work per level
```

becomes:

```text
O(log n)
×
O(n)
```

Therefore:

```text
O(n log n)
```

---

# 22. Merge Sort Time Complexity

Best:

```text
O(n log n)
```

Average:

```text
O(n log n)
```

Worst:

```text
O(n log n)
```

Unlike Bubble or Insertion Sort, the worst case does not become:

```text
O(n²)
```

---

# 23. Merge Sort Space Complexity

The simple Python version creates:

```text
left slices
right slices
merged arrays
```

So it uses additional memory.

Typical auxiliary space:

```text
O(n)
```

The recursion stack also uses:

```text
O(log n)
```

depth.

The main extra storage is still:

```text
O(n)
```

---

# 24. Merge Sort vs Bubble Sort

Bubble Sort:

```text
O(n²)
```

Merge Sort:

```text
O(n log n)
```

For large inputs, Merge Sort usually scales much better.

---

# 25. Example Growth

Suppose:

```text
n = 1000
```

Bubble Sort:

```text
n²

≈ 1,000,000
```

Merge Sort:

```text
n log₂ n

≈ 1000 × 10

≈ 10,000
```

This is a huge difference.

---

# 26. Merge Sort is Stable

If implemented correctly, Merge Sort can be stable.

Suppose:

```text
A = score 90
B = score 90
```

If A appears before B originally, stable Merge Sort keeps:

```text
A before B
```

when their keys are equal.

This is one reason we use:

```python
if left[i] <= right[j]:
```

Choosing the left element first when values are equal helps preserve order.

---

# 27. Is Merge Sort In-Place?

The common Merge Sort implementation:

```text
is not in-place
```

because it creates additional lists.

Extra space:

```text
O(n)
```

This is different from:

```text
Bubble
Selection
Insertion
```

which can use:

```text
O(1)
```

extra space.

---

# 28. Merge Sort vs Insertion Sort

Insertion Sort:

```text
Best = O(n)
Worst = O(n²)
```

Merge Sort:

```text
Best = O(n log n)
Worst = O(n log n)
```

For very small or nearly sorted inputs, Insertion Sort can still be useful.

For large general datasets, Merge Sort scales much better.

---

# 29. Why Merge Sort Works

Merge Sort works because:

```text
1 element is already sorted
```

and:

```text
two sorted arrays can be merged efficiently
```

That is the key insight.

---

# 30. Merging Complexity

Suppose:

```text
left has n values
right has m values
```

We examine each value at most once.

So:

```text
Time = O(n + m)
```

This is why the merge step is efficient.

---

# 31. Common Mistake - Missing Base Case

Bad:

```python
def merge_sort(numbers):

    mid = len(numbers) // 2

    return merge_sort(
        numbers[:mid]
    )
```

Without a base case, recursion never finishes correctly.

Correct:

```python
if len(numbers) <= 1:

    return numbers
```

---

# 32. Common Mistake - Forgetting Remaining Values

During merge, one list may finish first.

You must append:

```text
remaining left values
```

or:

```text
remaining right values
```

Otherwise data is lost.

---

# 33. Common Mistake - Comparing Wrong Pointers

Use:

```python
left[i]
```

and:

```python
right[j]
```

Then update the pointer from the side whose value was selected.

If left was selected:

```python
i += 1
```

If right was selected:

```python
j += 1
```

---

# 34. Common Mistake - Forgetting Return

The recursive calls need the sorted result.

Bad:

```python
merge_sort(left)
```

Correct:

```python
sorted_left = merge_sort(left)
```

Then use that result.

---

# 35. Common Mistake - Thinking Splitting is the Sorting

Splitting does not actually sort anything.

This:

```text
[8,3,5,1]
```

becoming:

```text
[8]
[3]
[5]
[1]
```

is only preparation.

The actual sorted order is created during:

```text
merge
```

---

# 36. Divide and Conquer Pattern

Merge Sort follows:

## Divide

```text
split in half
```

## Conquer

```text
sort each half recursively
```

## Combine

```text
merge sorted halves
```

This same strategy appears in many advanced algorithms.

---

# 37. Merge Sort Connection to Recursion

Remember Day 11:

```text
base case
recursive case
call stack
```

Merge Sort uses all of them.

Base:

```text
length <= 1
```

Recursive case:

```text
sort left
sort right
```

Combine:

```text
merge
```

---

# 38. Merge Sort Connection to Two Pointers

Remember Day 3?

We learned Two Pointers.

The merge function uses:

```text
i
j
```

Two pointers move through two sorted arrays.

So Merge Sort combines multiple earlier DSA ideas:

```text
Recursion
Two Pointers
Big-O
Sorting
```

---

# 39. Trace Example

Input:

```text
[6, 2, 4, 1]
```

Split:

```text
[6,2]
[4,1]
```

Split:

```text
[6]
[2]
[4]
[1]
```

Merge:

```text
[6] + [2]

→ [2,6]
```

Merge:

```text
[4] + [1]

→ [1,4]
```

Final:

```text
[2,6] + [1,4]

→ [1,2,4,6]
```

---

# 40. Complexity Comparison

| Algorithm | Best | Average | Worst | Extra Space |
|---|---:|---:|---:|---:|
| Bubble Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |

---

# 41. Important Merge Sort Pattern

```python
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
```

Remember the structure:

```text
Base
Split
Recurse
Merge
```

---

# 42. Day 14 Self-Test

Before completing Day 14, I should be able to explain:

1. What is Divide and Conquer?
2. What are the three steps?
3. What is Merge Sort?
4. What is the base case?
5. Why is a one-element array sorted?
6. How do we split an array?
7. What does the merge function do?
8. Why do we use two pointers during merge?
9. What happens when one side becomes empty?
10. Why must remaining values be added?
11. How does recursion work in Merge Sort?
12. What is a recursion tree?
13. Why are there O(log n) splitting levels?
14. Why does each level do O(n) merging work?
15. Why is Merge Sort O(n log n)?
16. What is Merge Sort's best case?
17. What is its worst case?
18. What is its extra space?
19. Is Merge Sort normally in-place?
20. Is Merge Sort stable?
21. Why do we often use <= during merge?
22. How is Merge Sort better than Bubble Sort?
23. How does Merge Sort connect to recursion?
24. How does Merge Sort use Two Pointers?
25. What does Divide, Conquer, Combine mean?

---

# My Day 14 Progress

- [x] Learned Divide and Conquer
- [x] Learned Merge Sort
- [x] Reviewed Recursion
- [x] Learned Merge Two Sorted Arrays
- [x] Used Two Pointers in Merge
- [x] Learned Merge Sort Base Case
- [x] Learned Recursive Splitting
- [x] Learned Recursive Merging
- [x] Learned Recursion Tree
- [x] Understood O(n log n)
- [x] Learned Merge Sort Space Complexity
- [x] Learned Stable Sorting
- [x] Compared Merge Sort to O(n²) Sorts
- [x] Traced Merge Sort by Hand
- [x] Analyzed Time and Space Complexity

---

# Day 14 Quick Cheat Sheet

```text
Merge Sort
→ Divide and Conquer
```

```text
Divide
→ split array
```

```text
Conquer
→ recursively sort halves
```

```text
Combine
→ merge sorted halves
```

```text
Base Case
→ len <= 1
```

```text
Merge
→ Two Pointers
```

```text
Time
→ O(n log n)
```

```text
Extra Space
→ O(n)
```

```text
Stable
→ Yes, with proper merge logic
```

```text
Main Pattern

Base
Split
Recurse
Merge
```

---

# Files in Day 14

```text
Day-14-Merge-Sort/
├── README.md
├── examples.py
└── practice.py
```

---

# Next - Day 15

Next topic:

# Quick Sort

Possible topics:

- Divide and Conquer Review
- Pivot
- Partitioning
- Smaller / Larger Values
- Recursive Quick Sort
- In-place Partitioning
- Average O(n log n)
- Worst O(n²)
- Quick Sort vs Merge Sort

---

# 90 Days of DSA

The key lesson from Day 14 is:

```text
Breaking a problem into smaller
parts can create a much faster
algorithm.
```

Merge Sort improves sorting from:

```text
O(n²)
```

to:

```text
O(n log n)
```

by combining:

```text
Recursion
Divide and Conquer
Two Pointers
Efficient Merging
```