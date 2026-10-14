# Day 13 - Sorting Algorithms

Welcome to **Day 13** of my **90 Days of Data Structures and Algorithms** journey.

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
```

Today I am learning:

# Sorting Algorithms

Sorting means arranging values in a particular order.

Example:

```text
Unsorted:

[5, 2, 8, 1, 3]
```

Ascending:

```text
[1, 2, 3, 5, 8]
```

Descending:

```text
[8, 5, 3, 2, 1]
```

Today I learned:

- What Sorting Means
- Why Sorting is Important
- Ascending and Descending Order
- In-place Sorting
- Stable Sorting
- Bubble Sort
- Optimized Bubble Sort
- Selection Sort
- Insertion Sort
- Best, Average, and Worst Cases
- O(n²)
- Python `sorted()`
- Python `.sort()`
- Comparing Sorting Algorithms

---

# 1. What is Sorting?

Sorting means arranging data according to some order.

Example:

```python
numbers = [5, 2, 8, 1, 3]
```

Ascending:

```text
1 2 3 5 8
```

Descending:

```text
8 5 3 2 1
```

Sorting is one of the most important operations in computer science.

---

# 2. Why is Sorting Important?

Sorting can make other problems easier.

For example:

Binary Search requires sorted data.

Unsorted:

```text
[20, 4, 12, 1, 8]
```

Sorted:

```text
[1, 4, 8, 12, 20]
```

Now Binary Search becomes possible.

Sorting is also useful for:

- Searching
- Finding duplicates
- Finding minimum or maximum
- Ranking
- Organizing records
- Merging data
- Two Pointer problems
- Scheduling

---

# 3. Ascending Order

Ascending means:

```text
smallest to largest
```

Example:

```text
[1, 3, 5, 8, 10]
```

For strings:

```text
apple
banana
cat
dog
```

---

# 4. Descending Order

Descending means:

```text
largest to smallest
```

Example:

```text
[10, 8, 5, 3, 1]
```

---

# 5. What is an In-Place Sort?

An in-place sorting algorithm modifies the original list.

Example:

```python
numbers = [3, 1, 2]

numbers.sort()
```

Now:

```python
numbers
```

becomes:

```text
[1, 2, 3]
```

The original list was modified.

Bubble Sort, Selection Sort, and Insertion Sort can all be implemented in-place.

---

# 6. What is Stable Sorting?

A stable sorting algorithm keeps the original order of equal elements.

Imagine:

```text
(A, 90)
(B, 80)
(C, 90)
```

If we sort by score, a stable sort keeps:

```text
A before C
```

because both have score 90 and A originally came first.

Stability matters when sorting objects by multiple properties.

For Day 13, the main goal is simply to understand the idea.

---

# 7. Bubble Sort

Bubble Sort repeatedly compares adjacent values.

If they are in the wrong order:

```text
swap them
```

The larger values gradually move toward the end.

That is why it is called:

```text
Bubble Sort
```

The larger values "bubble" to the top/end.

---

# 8. Bubble Sort Example

Start:

```text
[5, 3, 8, 2]
```

Compare:

```text
5 and 3
```

Wrong order.

Swap:

```text
[3, 5, 8, 2]
```

Compare:

```text
5 and 8
```

Correct.

No swap:

```text
[3, 5, 8, 2]
```

Compare:

```text
8 and 2
```

Swap:

```text
[3, 5, 2, 8]
```

After one full pass:

```text
8
```

is now in its correct final position.

---

# 9. Bubble Sort Code

```python
def bubble_sort(numbers):

    n = len(numbers)

    for i in range(n):

        for j in range(
            0,
            n - i - 1
        ):

            if numbers[j] > numbers[j + 1]:

                numbers[j], numbers[j + 1] = (
                    numbers[j + 1],
                    numbers[j]
                )

    return numbers
```

---

# 10. Why `n - i - 1`?

After every pass, the largest remaining value reaches its correct place near the end.

So we do not need to compare that part again.

Example:

```text
Pass 1:

[?, ?, ?, 8]
```

8 is finished.

Next pass does not need to compare it again.

---

# 11. Bubble Sort Complexity

There are nested loops.

Roughly:

```text
n comparisons
×
n comparisons
```

So:

```text
Time = O(n²)
```

Standard simple version:

```text
Best = O(n²)
Average = O(n²)
Worst = O(n²)
```

Extra space:

```text
O(1)
```

because we swap in the same list.

---

# 12. Optimized Bubble Sort

If the list is already sorted, we can stop early.

Use:

```python
swapped = False
```

If no swap happened during a complete pass:

```text
the array is already sorted
```

---

# Optimized Bubble Sort

```python
def bubble_sort_optimized(numbers):

    n = len(numbers)

    for i in range(n):

        swapped = False

        for j in range(
            0,
            n - i - 1
        ):

            if numbers[j] > numbers[j + 1]:

                numbers[j], numbers[j + 1] = (
                    numbers[j + 1],
                    numbers[j]
                )

                swapped = True

        if not swapped:

            break

    return numbers
```

---

# 13. Optimized Bubble Sort Complexity

Best case:

```text
Already sorted
```

Only one pass.

So:

```text
Best = O(n)
```

Average:

```text
O(n²)
```

Worst:

```text
O(n²)
```

Space:

```text
O(1)
```

---

# 14. Selection Sort

Selection Sort repeatedly finds the smallest value from the unsorted section.

Then it places that value at the beginning of the unsorted section.

Think:

```text
Find smallest
Put it here
Find next smallest
Put it next
```

---

# 15. Selection Sort Example

Start:

```text
[5, 3, 8, 2]
```

Find smallest:

```text
2
```

Swap it with first:

```text
[2, 3, 8, 5]
```

Now first position is complete.

Remaining unsorted:

```text
[3, 8, 5]
```

Smallest:

```text
3
```

Already in correct position.

Then:

```text
[8, 5]
```

Smallest:

```text
5
```

Swap:

```text
[2, 3, 5, 8]
```

Sorted.

---

# 16. Selection Sort Code

```python
def selection_sort(numbers):

    n = len(numbers)

    for i in range(n):

        min_index = i

        for j in range(
            i + 1,
            n
        ):

            if numbers[j] < numbers[min_index]:

                min_index = j

        numbers[i], numbers[min_index] = (
            numbers[min_index],
            numbers[i]
        )

    return numbers
```

---

# 17. Selection Sort Main Idea

At every step:

```text
Left side = sorted
Right side = unsorted
```

Example:

```text
[2, 3 | 8, 5]
```

The left side is done.

We search only the right side for the next smallest element.

---

# 18. Selection Sort Complexity

Even if the list is already sorted, Selection Sort still searches the remaining section for the minimum.

Therefore:

```text
Best = O(n²)
Average = O(n²)
Worst = O(n²)
```

Space:

```text
O(1)
```

---

# 19. Bubble Sort vs Selection Sort

Bubble Sort:

```text
Compare adjacent values
Swap many times
```

Selection Sort:

```text
Find minimum
Usually one swap per outer loop
```

Both:

```text
O(n²)
```

---

# 20. Insertion Sort

Insertion Sort builds a sorted section one value at a time.

A good real-life example is:

```text
sorting playing cards in your hand
```

You pick one new card and insert it into the correct position.

---

# 21. Insertion Sort Example

Start:

```text
[5, 3, 8, 2]
```

Assume first value is sorted:

```text
[5]
```

Take:

```text
3
```

Insert before 5:

```text
[3, 5, 8, 2]
```

Take:

```text
8
```

Already correctly placed:

```text
[3, 5, 8, 2]
```

Take:

```text
2
```

Shift:

```text
8
5
3
```

to the right.

Insert 2:

```text
[2, 3, 5, 8]
```

---

# 22. Insertion Sort Code

```python
def insertion_sort(numbers):

    for i in range(
        1,
        len(numbers)
    ):

        current = numbers[i]

        j = i - 1

        while (
            j >= 0
            and
            numbers[j] > current
        ):

            numbers[j + 1] = numbers[j]

            j -= 1

        numbers[j + 1] = current

    return numbers
```

---

# 23. Understanding Insertion Sort

Suppose:

```text
[3, 5, 8, 2]
```

Current value:

```text
2
```

Compare with:

```text
8
```

8 > 2.

Shift 8 right.

Then compare:

```text
5 > 2
```

Shift.

Then:

```text
3 > 2
```

Shift.

Now insert:

```text
2
```

at the beginning.

---

# 24. Insertion Sort Complexity

If the list is already sorted:

```text
no major shifting
```

So:

```text
Best = O(n)
```

Average:

```text
O(n²)
```

Worst:

```text
O(n²)
```

Worst case example:

```text
[5, 4, 3, 2, 1]
```

Space:

```text
O(1)
```

---

# 25. Why Insertion Sort Can Be Useful

Insertion Sort can perform well when:

```text
the data is small
```

or:

```text
the data is already almost sorted
```

It is also important because more advanced sorting algorithms sometimes use insertion sort for small sections.

---

# 26. Comparison Table

| Algorithm | Best | Average | Worst | Extra Space |
|---|---:|---:|---:|---:|
| Bubble Sort basic | O(n²) | O(n²) | O(n²) | O(1) |
| Bubble Sort optimized | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |

---

# 27. Which One Should I Remember?

Bubble Sort:

```text
Compare neighbors
Swap if wrong
```

Selection Sort:

```text
Find minimum
Put minimum in correct position
```

Insertion Sort:

```text
Take current item
Insert into sorted left side
```

---

# 28. O(n²) Visualization

If:

```text
n = 5
```

we may perform around:

```text
25
```

units of work.

If:

```text
n = 1000
```

then:

```text
n² = 1,000,000
```

This is why quadratic algorithms become slow for large inputs.

---

# 29. Python `sorted()`

Python has a built-in:

```python
sorted()
```

Example:

```python
numbers = [
    5,
    2,
    8,
    1
]

result = sorted(numbers)
```

Result:

```text
[1, 2, 5, 8]
```

Important:

```text
sorted()
```

returns a new list.

The original list remains unchanged.

---

# 30. Example of `sorted()`

```python
numbers = [
    3,
    1,
    2
]

result = sorted(numbers)

print(numbers)

print(result)
```

Output:

```text
[3, 1, 2]

[1, 2, 3]
```

---

# 31. Python `.sort()`

Python lists also have:

```python
.sort()
```

Example:

```python
numbers = [
    3,
    1,
    2
]

numbers.sort()
```

Now:

```text
numbers
```

becomes:

```text
[1, 2, 3]
```

`.sort()` modifies the original list.

---

# 32. `sorted()` vs `.sort()`

`sorted()`:

```text
returns a new list
```

`.sort()`:

```text
changes the original list
```

Example:

```python
numbers = [3, 1, 2]

new_numbers = sorted(numbers)
```

Original:

```text
[3, 1, 2]
```

New:

```text
[1, 2, 3]
```

But:

```python
numbers.sort()
```

changes:

```text
numbers
```

directly.

---

# 33. Descending Sort

Using:

```python
reverse=True
```

Example:

```python
numbers = [
    3,
    1,
    2
]

numbers.sort(
    reverse=True
)
```

Result:

```text
[3, 2, 1]
```

Or:

```python
sorted(
    numbers,
    reverse=True
)
```

---

# 34. Python Sorting Complexity

Python uses a highly optimized sorting algorithm called:

```text
Timsort
```

Typical worst-case time complexity:

```text
O(n log n)
```

This is much better than:

```text
O(n²)
```

for large inputs.

---

# 35. Why Learn Bubble / Selection / Insertion if Python Can Sort?

Because the goal is not only to sort numbers.

The goal is to learn:

- Nested loops
- Swapping
- Shifting
- Comparing algorithms
- Best / Average / Worst case
- In-place modification
- Algorithm design
- Complexity analysis

These concepts prepare us for:

```text
Merge Sort
Quick Sort
Heap Sort
```

---

# 36. Stable Sorting

Bubble Sort can be stable when we swap only when:

```python
left > right
```

not when equal.

Insertion Sort is normally stable.

Standard Selection Sort is generally not stable because swapping can change the relative order of equal items.

Python's built-in sort is stable.

---

# 37. In-Place Comparison

Bubble Sort:

```text
In-place
```

Selection Sort:

```text
In-place
```

Insertion Sort:

```text
In-place
```

Python `.sort()`:

```text
modifies original list
```

`sorted()`:

```text
creates a new list
```

---

# 38. Common Mistake - Wrong Bubble Loop

We compare:

```python
numbers[j]
```

with:

```python
numbers[j + 1]
```

So `j` cannot reach the last index.

That is why:

```python
range(0, n - i - 1)
```

is important.

---

# 39. Common Mistake - Swapping Too Soon in Selection Sort

Selection Sort should first:

```text
find the smallest index
```

Then swap after finishing the inner loop.

Correct idea:

```python
min_index = i

for j:
    find minimum

swap once
```

---

# 40. Common Mistake - Losing Current Value in Insertion Sort

Before shifting values, save:

```python
current = numbers[i]
```

Otherwise the current value could be overwritten.

---

# 41. Common Mistake - Confusing Swap and Shift

Bubble Sort often uses:

```text
swap
```

Insertion Sort mostly uses:

```text
shift
```

Example shift:

```python
numbers[j + 1] = numbers[j]
```

This moves an element right without immediately swapping.

---

# 42. Sorting and Binary Search

Remember Day 12:

```text
Binary Search = O(log n)
```

But Binary Search requires sorted data.

If data is unsorted and we first sort it:

```text
Sorting ≈ O(n log n)
Binary Search = O(log n)
```

If we only need to search once, sorting first may not always be worth it.

If we need to perform many searches, sorting can be useful.

---

# 43. Day 13 Complexity Summary

| Operation | Time |
|---|---:|
| Bubble Sort | O(n²) |
| Optimized Bubble Best | O(n) |
| Selection Sort | O(n²) |
| Insertion Sort Best | O(n) |
| Insertion Sort Average/Worst | O(n²) |
| Python Sort | O(n log n) worst-case |

---

# 44. Day 13 Important Patterns

## Bubble Sort

```text
Compare neighbors
```

```python
if numbers[j] > numbers[j + 1]:
```

Then swap.

---

## Selection Sort

```text
Find minimum index
```

Then:

```text
swap into position
```

---

## Insertion Sort

```text
Sorted left side
Unsorted right side
```

Take current item and insert it into the sorted section.

---

# 45. Day 13 Self-Test

Before completing Day 13, I should be able to explain:

1. What is sorting?
2. What is ascending order?
3. What is descending order?
4. Why is sorting useful?
5. What is an in-place sort?
6. What is a stable sort?
7. How does Bubble Sort work?
8. Why is it called Bubble Sort?
9. What is Bubble Sort's average complexity?
10. How can Bubble Sort be optimized?
11. What is Selection Sort?
12. What does `min_index` represent?
13. Why is Selection Sort O(n²)?
14. What is Insertion Sort?
15. How is it similar to sorting playing cards?
16. Why can Insertion Sort be O(n) in the best case?
17. What is the worst case for Insertion Sort?
18. Difference between swapping and shifting?
19. Difference between `sorted()` and `.sort()`?
20. How do I sort descending?
21. Why should I still learn simple sorting algorithms?
22. Which algorithms use O(1) extra space?
23. Which of today's algorithms are stable?
24. Why are O(n²) algorithms slow on large inputs?
25. How does sorting connect to Binary Search?

---

# My Day 13 Progress

- [x] Learned Sorting Basics
- [x] Learned Ascending / Descending
- [x] Learned In-place Sorting
- [x] Learned Stable Sorting
- [x] Implemented Bubble Sort
- [x] Implemented Optimized Bubble Sort
- [x] Implemented Selection Sort
- [x] Implemented Insertion Sort
- [x] Compared Best / Average / Worst Case
- [x] Learned O(n²)
- [x] Used `sorted()`
- [x] Used `.sort()`
- [x] Learned Descending Sorting
- [x] Compared Sorting Algorithms
- [x] Analyzed Time Complexity
- [x] Analyzed Space Complexity

---

# Day 13 Quick Cheat Sheet

```text
Bubble Sort
→ compare neighbors
→ swap
```

```text
Selection Sort
→ find minimum
→ place it correctly
```

```text
Insertion Sort
→ insert current value
→ into sorted left section
```

```text
Bubble
→ O(n²)
```

```text
Selection
→ O(n²)
```

```text
Insertion
→ O(n) best
→ O(n²) worst
```

```text
sorted()
→ returns new list
```

```text
.sort()
→ modifies original list
```

```text
Python sorting
→ O(n log n) worst-case
```

---

# Files in Day 13

```text
Day-13-Sorting-Basics/
├── README.md
├── examples.py
└── practice.py
```

---

# Next - Day 14

Next topic:

# Merge Sort

Possible topics:

- Divide and Conquer
- Splitting Arrays
- Recursion Review
- Merge Two Sorted Arrays
- Merge Sort
- O(n log n)
- Recursive Tree
- Space Complexity
- Merge Sort vs O(n²) Sorts

---

# 90 Days of DSA

Day 13 teaches an important lesson:

```text
Different algorithms can solve
the same problem but with
different performance.
```

The goal is not only:

```text
Does the code work?
```

but also:

```text
How efficiently does it work?
```