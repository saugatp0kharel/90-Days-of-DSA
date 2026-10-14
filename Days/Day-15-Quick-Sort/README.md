# Day 15 - Quick Sort

Welcome to **Day 15** of my **90 Days of Data Structures and Algorithms** journey.

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
Day 14 - Merge Sort
```

Today I am learning:

# Quick Sort

Quick Sort is another important:

```text
Divide and Conquer
```

sorting algorithm.

The main idea is:

```text
Choose a pivot
↓
Put smaller values on one side
↓
Put larger values on the other side
↓
Recursively sort both sides
```

Today I learned:

- What Quick Sort is
- Divide and Conquer review
- Pivot
- Partitioning
- Smaller and Larger Partitions
- Recursive Quick Sort
- Simple Python Quick Sort
- In-place Quick Sort
- Lomuto Partition Scheme
- Best / Average / Worst Complexity
- Why Quick Sort can become O(n²)
- Quick Sort vs Merge Sort
- Stability
- Space Complexity
- Common Quick Sort mistakes

---

# 1. What is Quick Sort?

Quick Sort is a comparison sorting algorithm.

It chooses one element called the:

```text
pivot
```

Then it organizes the other values around that pivot.

Example:

```text
[8, 3, 5, 1, 7]
```

Suppose pivot is:

```text
5
```

We can divide values into:

```text
smaller than 5
```

```text
equal to 5
```

and:

```text
greater than 5
```

Example:

```text
Smaller:

[3, 1]

Pivot:

[5]

Larger:

[8, 7]
```

Then recursively sort:

```text
[3, 1]
```

and:

```text
[8, 7]
```

Final:

```text
[1, 3, 5, 7, 8]
```

---

# 2. Divide and Conquer Review

Quick Sort follows:

```text
Divide
Conquer
Combine
```

But its combine step is much simpler than Merge Sort.

## Divide

Choose a pivot and partition the array.

## Conquer

Recursively Quick Sort the left and right partitions.

## Combine

The partitions are already positioned around the pivot.

In a simple functional version, we can combine:

```python
left + middle + right
```

---

# 3. What is a Pivot?

The pivot is the value used to divide the list.

Example:

```text
[6, 2, 8, 3, 5]
```

We might choose:

```text
pivot = 5
```

Then:

```text
smaller = [2, 3]

pivot = [5]

larger = [6, 8]
```

---

# 4. How Do We Choose a Pivot?

Common choices include:

```text
first element
last element
middle element
random element
median-like choice
```

For beginner examples, we can choose:

```python
pivot = numbers[len(numbers) // 2]
```

or:

```python
pivot = numbers[-1]
```

---

# 5. Why Pivot Choice Matters

A good pivot divides the array into roughly balanced parts.

Example:

```text
Left size ≈ Right size
```

This gives good performance.

A bad pivot may create:

```text
one side almost empty
other side almost the whole array
```

This can lead to:

```text
O(n²)
```

performance.

---

# 6. Simple Quick Sort

A beginner-friendly version creates three lists:

```text
less
equal
greater
```

Example:

```python
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
```

---

# 7. Base Case

Just like Merge Sort:

```python
if len(numbers) <= 1:

    return numbers
```

Why?

Because:

```text
0 or 1 element is already sorted
```

---

# 8. Quick Sort Example

Input:

```text
[6, 2, 8, 3, 5]
```

Choose pivot:

```text
8
```

or depending on implementation, middle value:

```text
8
```

Partition:

```text
less = [6, 2, 3, 5]

equal = [8]

greater = []
```

Then Quick Sort:

```text
[6, 2, 3, 5]
```

recursively.

---

# 9. Better Visualization

Suppose:

```text
[7, 2, 5, 1, 9, 3]
```

Pivot:

```text
5
```

Partition:

```text
[2, 1, 3]   [5]   [7, 9]
```

Now sort left:

```text
[2, 1, 3]
```

Suppose pivot:

```text
1
```

Then:

```text
[] [1] [2, 3]
```

Sort:

```text
[2, 3]
```

Final left:

```text
[1, 2, 3]
```

Right:

```text
[7, 9]
```

already easy to sort.

Final:

```text
[1, 2, 3, 5, 7, 9]
```

---

# 10. Partitioning

Partitioning is the key operation in Quick Sort.

It means:

```text
rearranging values around the pivot
```

After partitioning:

```text
smaller values
come before pivot
```

and:

```text
larger values
come after pivot
```

---

# 11. Functional Quick Sort vs In-Place Quick Sort

There are two common styles.

## Functional / Easy Version

Creates new lists:

```text
less
equal
greater
```

Easy to understand.

But uses more extra memory.

---

## In-Place Version

Rearranges elements inside the same list.

Uses:

```text
indexes
swaps
partition function
```

More efficient in memory.

But pointer logic is more difficult.

---

# 12. In-Place Quick Sort

A common in-place version uses:

```text
Lomuto Partition Scheme
```

Usually:

```text
pivot = last element
```

---

# 13. Lomuto Partition Idea

Suppose:

```text
[4, 2, 7, 3, 6]
```

Choose:

```text
pivot = 6
```

We want values smaller than or equal to 6 before the pivot.

Use:

```text
i
```

to track the end of the smaller section.

Use:

```text
j
```

to scan the array.

---

# 14. Partition Variables

Example:

```python
pivot = numbers[high]

i = low - 1
```

Then:

```python
for j in range(low, high):
```

If:

```python
numbers[j] <= pivot
```

increase `i` and swap.

At the end:

```text
put pivot after the smaller section
```

---

# 15. Lomuto Partition Code

```python
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
```

The returned index is:

```text
pivot's final position
```

---

# 16. Partition Example

Input:

```text
[4, 2, 7, 3, 6]
```

Pivot:

```text
6
```

Start:

```text
i = -1
```

Scan:

```text
4 <= 6
```

Move `i`:

```text
i = 0
```

Swap with itself.

Array:

```text
[4, 2, 7, 3, 6]
```

Next:

```text
2 <= 6
```

Move `i`:

```text
i = 1
```

Next:

```text
7 > 6
```

Do nothing.

Next:

```text
3 <= 6
```

Move:

```text
i = 2
```

Swap 7 and 3:

```text
[4, 2, 3, 7, 6]
```

Finally place pivot:

```text
[4, 2, 3, 6, 7]
```

Pivot index:

```text
3
```

Now:

```text
6
```

is in its final sorted position.

---

# 17. In-Place Quick Sort Code

```python
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
```

Call:

```python
numbers = [
    8,
    3,
    1,
    7,
    0,
    10,
    2
]

quick_sort_in_place(
    numbers,
    0,
    len(numbers) - 1
)
```

---

# 18. Why Skip the Pivot?

After partitioning, the pivot is already in its correct final position.

So we recursively sort:

```text
left side
```

and:

```text
right side
```

but not the pivot itself.

That is why:

```python
pivot_index - 1
```

and:

```python
pivot_index + 1
```

are used.

---

# 19. Quick Sort Average Complexity

When pivots are reasonably balanced:

```text
array divides roughly in half
```

There are around:

```text
log n
```

recursion levels.

Each level performs about:

```text
O(n)
```

partition work.

So:

```text
Average Time = O(n log n)
```

---

# 20. Quick Sort Best Case

Best case happens when the pivot divides the array evenly.

Example:

```text
n / 2
```

values on the left.

And:

```text
n / 2
```

values on the right.

Then:

```text
Best = O(n log n)
```

---

# 21. Quick Sort Worst Case

Worst case happens when the pivot creates extremely unbalanced partitions.

Example:

```text
[]
pivot
[n - 1 elements]
```

again and again.

Then recursion looks like:

```text
n
n - 1
n - 2
n - 3
...
```

This gives:

```text
O(n²)
```

---

# 22. Worst-Case Example

Suppose we always choose the last value as pivot.

Input:

```text
[1, 2, 3, 4, 5]
```

Pivot:

```text
5
```

Left:

```text
[1, 2, 3, 4]
```

Right:

```text
[]
```

Then pivot:

```text
4
```

Left:

```text
[1, 2, 3]
```

Again extremely unbalanced.

This can lead to:

```text
O(n²)
```

---

# 23. Random Pivot

One way to reduce the chance of consistently bad pivots is:

```text
choose the pivot randomly
```

Randomized Quick Sort often performs well in practice.

---

# 24. Quick Sort Space Complexity

The answer depends on implementation.

## Simple Functional Version

Creates:

```text
less
equal
greater
```

So it can use significant extra memory.

Often approximately:

```text
O(n)
```

extra storage.

---

## In-Place Version

The partition itself uses:

```text
O(1)
```

extra array space.

But recursion still uses the call stack.

Average recursion depth:

```text
O(log n)
```

Worst recursion depth:

```text
O(n)
```

---

# 25. Quick Sort is Usually Not Stable

Standard in-place Quick Sort is generally:

```text
not stable
```

Why?

Because swapping can change the order of equal elements.

---

# 26. Quick Sort vs Merge Sort

Both use:

```text
Divide and Conquer
```

But they divide differently.

Merge Sort:

```text
Split first
Sort recursively
Merge later
```

Quick Sort:

```text
Partition around pivot
Sort partitions recursively
```

---

# 27. Comparison Table

| Feature | Merge Sort | Quick Sort |
|---|---|---|
| Main idea | Split + Merge | Pivot + Partition |
| Average Time | O(n log n) | O(n log n) |
| Worst Time | O(n log n) | O(n²) |
| Typical extra array space | O(n) | O(log n) recursion average for in-place version |
| Stable | Yes, commonly | Usually No |
| In-place | Usually No | Can be |
| Pivot needed | No | Yes |

---

# 28. Why Quick Sort Can Be Fast in Practice

Quick Sort often has good:

```text
cache behavior
```

and can operate mostly in-place.

It also avoids the large merging arrays required by typical Merge Sort implementations.

So even though its theoretical worst case is:

```text
O(n²)
```

good pivot strategies make it very effective in many situations.

---

# 29. Merge Sort Guarantees vs Quick Sort Average

Merge Sort gives:

```text
O(n log n)
```

even in the worst case.

Quick Sort gives:

```text
O(n log n)
```

on average.

But can become:

```text
O(n²)
```

in the worst case.

---

# 30. Common Mistake - Missing Base Case

Functional Quick Sort needs:

```python
if len(numbers) <= 1:

    return numbers
```

In-place Quick Sort needs:

```python
if low < high:
```

Without stopping conditions, recursion can fail.

---

# 31. Common Mistake - Including Pivot Again

After partitioning, do not recursively include the pivot.

Wrong idea:

```python
quick_sort(
    low,
    pivot_index
)
```

for a scheme where pivot is already final.

This may lead to incorrect recursion.

Use:

```python
pivot_index - 1
```

and:

```python
pivot_index + 1
```

with this Lomuto implementation.

---

# 32. Common Mistake - Wrong Partition Range

When using the last element as pivot:

```python
pivot = numbers[high]
```

the scan should usually stop before `high`:

```python
range(low, high)
```

because `high` is the pivot.

---

# 33. Common Mistake - Forgetting Final Pivot Swap

After scanning:

```text
pivot is still at the end
```

You must move it between:

```text
smaller values
```

and:

```text
larger values
```

with:

```python
numbers[i + 1], numbers[high] = (
    numbers[high],
    numbers[i + 1]
)
```

---

# 34. Common Mistake - Thinking Pivot Must Be Median

The pivot does not need to be the exact median.

The algorithm still works with many pivot choices.

But pivot choice affects:

```text
performance
```

---

# 35. Quick Sort Recursion Tree

Balanced case:

```text
               n

          /         \

       n/2          n/2

      /   \        /   \

    n/4   n/4    n/4   n/4
```

Levels:

```text
O(log n)
```

Work per level:

```text
O(n)
```

Total:

```text
O(n log n)
```

---

# 36. Worst Recursion Shape

Bad pivot:

```text
n

↓

n - 1

↓

n - 2

↓

n - 3

↓

...
```

Depth:

```text
O(n)
```

Total work:

```text
O(n²)
```

---

# 37. Functional Quick Sort Example

```python
def quick_sort(numbers):

    if len(numbers) <= 1:

        return numbers

    pivot = numbers[
        len(numbers) // 2
    ]

    less = [
        number
        for number in numbers
        if number < pivot
    ]

    equal = [
        number
        for number in numbers
        if number == pivot
    ]

    greater = [
        number
        for number in numbers
        if number > pivot
    ]

    return (
        quick_sort(less)
        +
        equal
        +
        quick_sort(greater)
    )
```

This version is:

```text
very readable
```

but:

```text
not in-place
```

---

# 38. Duplicate Values

Example:

```text
[4, 2, 4, 1, 4]
```

Using:

```text
less
equal
greater
```

helps handle duplicate pivot values cleanly.

If pivot is:

```text
4
```

Then:

```text
less = [2, 1]

equal = [4, 4, 4]

greater = []
```

---

# 39. Partitioning vs Merging

Merge Sort important operation:

```text
Merge
```

Quick Sort important operation:

```text
Partition
```

Remember:

```text
Merge Sort
→ organize while combining
```

```text
Quick Sort
→ organize before recursive calls
```

---

# 40. Connection to Previous Days

Quick Sort combines ideas from many earlier days:

```text
Day 01
Big-O

Day 02
Arrays

Day 03
Pointer / array manipulation

Day 11
Recursion

Day 13
Sorting

Day 14
Divide and Conquer
```

This is why DSA topics start connecting to each other.

---

# 41. Day 15 Complexity Summary

| Version / Case | Time | Extra Space |
|---|---:|---:|
| Quick Sort Best | O(n log n) | depends on implementation |
| Quick Sort Average | O(n log n) | O(log n) stack average for in-place |
| Quick Sort Worst | O(n²) | O(n) stack worst |
| Functional Quick Sort | O(n log n) average | often O(n) or more temporary allocation across execution |
| Lomuto Partition | O(n) | O(1) |

---

# 42. Important Quick Sort Patterns

## Pivot

```text
value used to divide the problem
```

## Partition

```text
smaller values on one side
larger values on other side
```

## Recursive Left

```text
sort before pivot
```

## Recursive Right

```text
sort after pivot
```

---

# 43. Quick Sort Mental Model

Think:

```text
Pick
Separate
Repeat
```

Pick:

```text
pivot
```

Separate:

```text
smaller | pivot | larger
```

Repeat:

```text
Quick Sort smaller
Quick Sort larger
```

---

# 44. Day 15 Self-Test

Before completing Day 15, I should be able to explain:

1. What is Quick Sort?
2. What is Divide and Conquer?
3. What is a pivot?
4. What is partitioning?
5. What belongs on the left of the pivot?
6. What belongs on the right?
7. What is the Quick Sort base case?
8. How does the simple functional version work?
9. What are `less`, `equal`, and `greater`?
10. What is an in-place Quick Sort?
11. What is Lomuto Partition?
12. Why is the last element sometimes used as pivot?
13. What does `i` represent?
14. What does `j` represent?
15. What happens after partitioning?
16. Why do we skip the pivot in recursion?
17. What is Quick Sort average complexity?
18. What is its best case?
19. What is its worst case?
20. Why can Quick Sort become O(n²)?
21. What kind of pivot creates a balanced partition?
22. What does randomized pivot mean?
23. Is standard Quick Sort stable?
24. How is Quick Sort different from Merge Sort?
25. Why can Quick Sort use less extra memory than Merge Sort?

---

# My Day 15 Progress

- [x] Learned Quick Sort
- [x] Reviewed Divide and Conquer
- [x] Learned Pivot
- [x] Learned Partitioning
- [x] Built Functional Quick Sort
- [x] Learned In-place Quick Sort
- [x] Learned Lomuto Partition
- [x] Traced Partition Step-by-Step
- [x] Learned Recursive Left / Right Sorting
- [x] Understood Average O(n log n)
- [x] Understood Worst O(n²)
- [x] Learned Why Pivot Choice Matters
- [x] Learned Random Pivot Idea
- [x] Compared Quick Sort and Merge Sort
- [x] Learned Stability
- [x] Analyzed Time Complexity
- [x] Analyzed Space Complexity

---

# Day 15 Quick Cheat Sheet

```text
Quick Sort
→ Pivot + Partition
```

```text
Pivot
→ value used to divide array
```

```text
Partition
→ smaller | pivot | larger
```

```text
Average Time
→ O(n log n)
```

```text
Worst Time
→ O(n²)
```

```text
Good Pivot
→ balanced partitions
```

```text
Bad Pivot
→ very uneven partitions
```

```text
Merge Sort
→ split then merge
```

```text
Quick Sort
→ partition then recurse
```

---

# Files in Day 15

```text
Day-15-Quick-Sort/
├── README.md
├── examples.py
└── practice.py
```

---

# Next - Day 16

Next topic:

# Heap and Priority Queue Introduction

Possible topics:

- What is a Heap?
- Min Heap
- Max Heap
- Complete Binary Tree
- Parent / Child Indexes
- Python `heapq`
- Push and Pop
- Priority Queues
- Kth Smallest / Largest
- Heap Complexity

---

# 90 Days of DSA

The key idea from Day 15 is:

```text
Choose a pivot
Partition around it
Recursively sort the two sides
```

Quick Sort shows how the same Divide and Conquer idea can produce a very different algorithm from Merge Sort.