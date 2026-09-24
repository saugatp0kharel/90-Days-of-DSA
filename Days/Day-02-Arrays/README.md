# Day 02 - Arrays and Python Lists

Welcome to **Day 02** of my **90 Days of Data Structures and Algorithms** journey.

Today I learned one of the most important data structures in programming:

# Arrays

In Python, we commonly use a:

```text
list
```

as an array-like structure.

Today I learned how to:

- Create a list
- Access elements
- Understand indexes
- Use zero-based indexing
- Update elements
- Traverse a list
- Search for values
- Use `append()`
- Use `insert()`
- Use `remove()`
- Use `pop()`
- Use `len()`
- Use negative indexing
- Use slicing
- Understand the Big-O complexity of common list operations

---

# Table of Contents

1. What is an Array?
2. Arrays in Python
3. Indexing
4. Zero-Based Indexing
5. Accessing Elements
6. Updating Elements
7. Traversing an Array
8. Traversing with Indexes
9. Linear Search
10. Append
11. Insert
12. Remove
13. Pop
14. Length
15. Negative Indexing
16. Slicing
17. Array Time Complexity
18. Common Mistakes
19. Practice Questions
20. Day 2 Summary

---

# 1. What is an Array?

An array is a data structure used to store multiple values together.

Instead of creating many separate variables like:

```python
number1 = 10
number2 = 20
number3 = 30
number4 = 40
number5 = 50
```

we can store them together:

```python
numbers = [10, 20, 30, 40, 50]
```

This makes the data easier to:

- Store
- Read
- Update
- Search
- Loop through
- Organize

---

# 2. Arrays in Python

Python has a built-in data structure called:

```text
list
```

A Python list works like a dynamic array.

Example:

```python
numbers = [10, 20, 30, 40, 50]
```

The list contains:

```text
10
20
30
40
50
```

The number of elements is:

```text
5
```

So:

```python
len(numbers)
```

returns:

```text
5
```

---

# 3. Indexing

Every element inside a list has a position.

That position is called an:

```text
index
```

For this list:

```python
numbers = [10, 20, 30, 40, 50]
```

we can visualize it like this:

```text
Index:   0   1   2   3   4
Value:  10  20  30  40  50
```

So:

```python
numbers[0]
```

returns:

```text
10
```

And:

```python
numbers[2]
```

returns:

```text
30
```

And:

```python
numbers[4]
```

returns:

```text
50
```

---

# 4. Zero-Based Indexing

Python list indexes start at:

```text
0
```

not:

```text
1
```

This is called:

# Zero-Based Indexing

Example:

```python
numbers = [10, 20, 30]
```

The indexes are:

```text
Index 0 -> 10

Index 1 -> 20

Index 2 -> 30
```

So the first item is:

```python
numbers[0]
```

not:

```python
numbers[1]
```

This is very important in programming.

---

# 5. Accessing Elements

We can access an element by using its index.

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])
print(numbers[4])
```

Output:

```text
10
30
50
```

---

## Time Complexity of Accessing

Accessing an element by index is usually:

```text
O(1)
```

Why?

Because Python can directly access the position.

It does not need to search through the entire list.

Example:

```python
numbers[3]
```

Python knows which location contains index 3.

Therefore:

```text
Time Complexity = O(1)
```

---

# 6. Updating Elements

We can change a value by using its index.

Example:

```python
numbers = [10, 20, 30, 40, 50]

numbers[2] = 100

print(numbers)
```

Output:

```text
[10, 20, 100, 40, 50]
```

We changed:

```text
30
```

to:

```text
100
```

---

## Complexity of Updating

Updating an element at a known index is:

```text
O(1)
```

because we directly access the position.

Example:

```python
numbers[2] = 100
```

There is no need to search through the entire list.

---

# 7. Traversing an Array

Traversal means:

> Visiting every element in the list.

Example:

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)
```

Output:

```text
10
20
30
40
50
```

We visit every value once.

Therefore:

```text
Time Complexity = O(n)
```

because if the list grows, the number of loop iterations also grows.

---

## Example

If:

```text
n = 5
```

we visit:

```text
5 elements
```

If:

```text
n = 100
```

we visit:

```text
100 elements
```

If:

```text
n = 1,000,000
```

we may visit:

```text
1,000,000 elements
```

So traversal is:

```text
O(n)
```

---

# 8. Traversing with Indexes

Sometimes we need both:

- The index
- The value

We can write:

```python
numbers = [10, 20, 30, 40, 50]

for i in range(len(numbers)):
    print("Index:", i, "Value:", numbers[i])
```

Output:

```text
Index: 0 Value: 10
Index: 1 Value: 20
Index: 2 Value: 30
Index: 3 Value: 40
Index: 4 Value: 50
```

This still visits every element.

Therefore:

```text
Time Complexity = O(n)
```

---

# 9. Linear Search

Searching means trying to find a value inside the list.

A simple search algorithm is:

# Linear Search

Linear Search checks items one by one.

Example:

```python
def linear_search(arr, target):

    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1
```

Test:

```python
numbers = [10, 20, 30, 40, 50]

print(linear_search(numbers, 30))
```

Output:

```text
2
```

because:

```text
30
```

is at index:

```text
2
```

---

## Searching for a Missing Value

```python
print(linear_search(numbers, 100))
```

Output:

```text
-1
```

We use:

```text
-1
```

to mean:

```text
Not Found
```

---

## Complexity of Linear Search

Worst case:

```text
O(n)
```

Why?

Because we may need to check every element.

Example:

```text
[10, 20, 30, 40, 50]
```

If we search for:

```text
50
```

we may check:

```text
10
20
30
40
50
```

If the value is not present, we may still check every element.

Therefore:

```text
O(n)
```

---

# 10. Append

`append()` adds an element to the end of a list.

Example:

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

---

## Complexity of Append

Appending to the end of a Python list is usually:

```text
O(1) amortized
```

For now, the simple idea is:

> Adding an item to the end is usually very fast.

Later I will learn more about why it is called:

```text
amortized
```

---

# 11. Insert

`insert()` allows us to add an element at a specific index.

Example:

```python
numbers = [10, 20, 30, 40]

numbers.insert(1, 99)

print(numbers)
```

Output:

```text
[10, 99, 20, 30, 40]
```

We inserted:

```text
99
```

at index:

```text
1
```

---

## Why Insertion Can Be O(n)

Before:

```text
10 20 30 40
```

Insert:

```text
99
```

at index 1.

Result:

```text
10 99 20 30 40
```

The values:

```text
20
30
40
```

may need to move to new positions.

Because many elements may need to shift:

```text
Time Complexity = O(n)
```

---

# 12. Remove

`remove()` removes a value from a list.

Example:

```python
numbers = [10, 20, 30, 40]

numbers.remove(30)

print(numbers)
```

Output:

```text
[10, 20, 40]
```

---

## Why remove() Can Be O(n)

Python may first need to search for:

```text
30
```

Searching can take:

```text
O(n)
```

Then elements may need to shift.

So:

```text
remove() = O(n)
```

in the general case.

---

# 13. Pop

`pop()` removes an element and returns it.

Example:

```python
numbers = [10, 20, 30, 40]

removed = numbers.pop()

print(removed)

print(numbers)
```

Output:

```text
40

[10, 20, 30]
```

---

## Pop From End

Removing the last item is usually:

```text
O(1)
```

because other elements do not need to shift.

Example:

```python
numbers.pop()
```

---

## Pop From Middle

Example:

```python
numbers.pop(1)
```

Suppose:

```text
[10, 20, 30, 40]
```

Removing index 1 gives:

```text
[10, 30, 40]
```

Values may need to shift left.

Therefore:

```text
O(n)
```

---

# 14. Length

We can find the number of elements using:

```python
len()
```

Example:

```python
numbers = [10, 20, 30, 40]

print(len(numbers))
```

Output:

```text
4
```

For Python lists:

```text
len(numbers)
```

is:

```text
O(1)
```

because Python already keeps track of the list length.

---

# 15. Negative Indexing

Python also allows negative indexes.

Example:

```python
numbers = [10, 20, 30, 40, 50]
```

We can use:

```python
numbers[-1]
```

to get:

```text
50
```

And:

```python
numbers[-2]
```

returns:

```text
40
```

---

## Negative Index Meaning

```text
-1 = last element

-2 = second last element

-3 = third last element
```

Example:

```text
Index:     0   1   2   3   4
Value:    10  20  30  40  50
Negative: -5 -4  -3  -2  -1
```

---

# 16. Slicing

Slicing allows us to get part of a list.

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

Important:

```text
Start index is included.

End index is NOT included.
```

So:

```text
1:4
```

means:

```text
index 1
index 2
index 3
```

but not:

```text
index 4
```

---

## More Slicing Examples

### First Three Elements

```python
numbers[:3]
```

Output:

```text
[10, 20, 30]
```

---

### From Index 2 to End

```python
numbers[2:]
```

Output:

```text
[30, 40, 50]
```

---

### Reverse a List

```python
numbers[::-1]
```

Output:

```text
[50, 40, 30, 20, 10]
```

---

## Complexity of Slicing

Slicing creates a new list.

If we copy:

```text
k elements
```

the complexity is approximately:

```text
O(k)
```

Example:

```python
numbers[1:4]
```

creates a new list containing 3 elements.

---

# 17. Array Time Complexity

This is one of the most important parts of Day 2.

| Operation | Typical Complexity |
|---|---|
| Access by index | O(1) |
| Update by index | O(1) |
| `len()` | O(1) |
| Traverse entire list | O(n) |
| Linear Search | O(n) |
| Append to end | O(1) amortized |
| Pop from end | O(1) |
| Insert at beginning | O(n) |
| Insert in middle | O(n) |
| Remove by value | O(n) |
| Pop from beginning/middle | O(n) |
| Slice k elements | O(k) |

---

# Why is Access O(1)?

Example:

```python
numbers[3]
```

Python can directly go to the correct index.

It does not need to inspect:

```text
index 0
index 1
index 2
```

first.

Therefore:

```text
O(1)
```

---

# Why is Search O(n)?

Suppose:

```python
numbers = [10, 20, 30, 40, 50]
```

and we want to find:

```text
50
```

Linear Search may check:

```text
10
20
30
40
50
```

The amount of work grows with the list size.

Therefore:

```text
O(n)
```

---

# Why is Insertion in the Middle O(n)?

Suppose:

```text
[10, 20, 30, 40]
```

Insert:

```text
99
```

at index:

```text
1
```

Result:

```text
[10, 99, 20, 30, 40]
```

The elements after the insertion point may need to move.

Therefore:

```text
O(n)
```

---

# 18. Important Difference

Accessing an item:

```python
numbers[3]
```

is:

```text
O(1)
```

But searching for a value:

```python
find 40
```

in an unsorted list using Linear Search is:

```text
O(n)
```

This is a very important difference.

Why?

Because:

```text
Access by index
```

means:

> I already know the position.

But:

```text
Search by value
```

means:

> I do not know where the value is, so I may need to check many elements.

---

# 19. Examples I Practiced

## Creating a List

```python
numbers = [10, 20, 30, 40, 50]
```

---

## Access

```python
print(numbers[0])
print(numbers[2])
print(numbers[-1])
```

---

## Update

```python
numbers[2] = 100
```

---

## Traversal

```python
for number in numbers:
    print(number)
```

---

## Traversal With Index

```python
for i in range(len(numbers)):
    print(i, numbers[i])
```

---

## Append

```python
numbers.append(60)
```

---

## Insert

```python
numbers.insert(1, 99)
```

---

## Remove

```python
numbers.remove(40)
```

---

## Pop

```python
numbers.pop()
```

---

## Linear Search

```python
def linear_search(arr, target):

    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1
```

---

## Slicing

```python
numbers[:3]

numbers[2:]

numbers[1:4]

numbers[::-1]
```

---

# 20. Practice Problems

Today I practiced questions like:

1. Access the first element.
2. Access the last element.
3. Change an element.
4. Print every element.
5. Print index and value.
6. Append a value.
7. Insert a value.
8. Remove a value.
9. Pop the last item.
10. Write Linear Search.
11. Slice the first three elements.
12. Slice the last three elements.
13. Reverse a list.
14. Identify operation complexity.
15. Explain why some operations are O(1) and others are O(n).

---

# 21. Small Coding Challenges

## Challenge 1 - Find the Sum

Given:

```python
numbers = [5, 10, 15, 20, 25]
```

Find the sum.

One solution:

```python
total = 0

for number in numbers:
    total += number

print(total)
```

Output:

```text
75
```

Time Complexity:

```text
O(n)
```

Extra Space:

```text
O(1)
```

---

# Challenge 2 - Find the Largest Value

Given:

```python
numbers = [14, 3, 99, 21, 7]
```

Solution:

```python
largest = numbers[0]

for number in numbers:

    if number > largest:
        largest = number

print(largest)
```

Output:

```text
99
```

Time Complexity:

```text
O(n)
```

Extra Space:

```text
O(1)
```

---

# Challenge 3 - Reverse the List

Given:

```python
numbers = [1, 2, 3, 4, 5]
```

Using slicing:

```python
reversed_numbers = numbers[::-1]

print(reversed_numbers)
```

Output:

```text
[5, 4, 3, 2, 1]
```

The slice creates a new list.

Time Complexity:

```text
O(n)
```

Space Complexity:

```text
O(n)
```

---

# 22. Common Mistakes

## Mistake 1

Thinking the first index is:

```text
1
```

Correct:

```text
The first index is 0.
```

---

## Mistake 2

Confusing:

```python
numbers[2]
```

with:

```text
the second element
```

Actually:

```text
index 2 = third element
```

because indexing starts at 0.

---

## Mistake 3

Thinking every list operation is O(1).

Not true.

Examples:

```text
Access = O(1)

Search = O(n)

Insert middle = O(n)
```

---

## Mistake 4

Thinking `append()` and `insert()` are the same.

They are different.

```python
append(value)
```

adds to the end.

```python
insert(index, value)
```

adds at a specific position.

---

## Mistake 5

Thinking `remove()` uses an index.

Incorrect:

```python
numbers.remove(30)
```

removes the value:

```text
30
```

But:

```python
numbers.pop(2)
```

removes the element at:

```text
index 2
```

---

# 23. Quick Recognition Guide

When I see:

```python
arr[i]
```

think:

```text
O(1)
```

---

When I see:

```python
for item in arr:
```

think:

```text
O(n)
```

---

When I see:

```python
arr.append(x)
```

think:

```text
O(1) amortized
```

---

When I see:

```python
arr.insert(0, x)
```

think:

```text
O(n)
```

---

When I see:

```python
arr.pop()
```

think:

```text
O(1)
```

---

When I see:

```python
arr.pop(0)
```

think:

```text
O(n)
```

---

When I see Linear Search:

```python
for i in range(len(arr)):

    if arr[i] == target:
```

think:

```text
O(n)
```

---

# 24. What I Learned Today

Today I learned that an array/list is not only a way to store values.

I also need to understand how expensive each operation is.

The most important Day 2 idea is:

```text
Knowing the index
is different from
searching for the value.
```

If I know the index:

```python
arr[5]
```

the access is:

```text
O(1)
```

But if I need to find a value:

```text
find 50
```

I may need to inspect the entire list:

```text
O(n)
```

---

# My Day 2 Progress

- [x] Learned what an array is
- [x] Learned Python lists
- [x] Learned indexing
- [x] Learned zero-based indexing
- [x] Learned array access
- [x] Learned array update
- [x] Learned traversal
- [x] Learned traversal using indexes
- [x] Learned Linear Search
- [x] Learned `append()`
- [x] Learned `insert()`
- [x] Learned `remove()`
- [x] Learned `pop()`
- [x] Learned `len()`
- [x] Learned negative indexing
- [x] Learned slicing
- [x] Learned common list Big-O complexities
- [x] Solved basic array practice questions
- [x] Solved beginner array coding challenges

---

# Important Things to Remember

```text
Index starts at 0.
```

```text
arr[index] = O(1)
```

```text
Traversal = O(n)
```

```text
Linear Search = O(n)
```

```text
append() = O(1) amortized
```

```text
pop() from end = O(1)
```

```text
insert() in beginning/middle = O(n)
```

```text
remove() = O(n)
```

```text
slicing k elements = O(k)
```

---

# Files in Day 02

```text
Day-02-Arrays/
│
├── README.md
├── examples.py
└── practice.py
```

### `README.md`

Contains my detailed Day 2 notes.

### `examples.py`

Contains working examples of Python list operations.

### `practice.py`

Contains Day 2 practice problems and my solutions.

---

# Day 2 Final Self-Test

Before completing Day 2, I should be able to answer:

1. What is an array?
2. What is a Python list?
3. Why does indexing start at 0?
4. What does `arr[2]` mean?
5. Why is accessing `arr[2]` O(1)?
6. What is traversal?
7. Why is traversal O(n)?
8. What is Linear Search?
9. Why is Linear Search O(n)?
10. What does `append()` do?
11. What does `insert()` do?
12. Why can insertion be O(n)?
13. What does `remove()` do?
14. What does `pop()` do?
15. Why is `pop()` from the end O(1)?
16. What does `arr[-1]` mean?
17. What does `arr[1:4]` mean?
18. Why can slicing take O(k)?
19. What is the difference between accessing by index and searching by value?
20. What is the difference between O(1) and O(n)?

---

# Next - Day 03

The next topic will be:

# Array Problems and Problem-Solving Patterns

I will start solving more real coding problems using arrays, including:

- Find maximum
- Find minimum
- Find sum
- Count occurrences
- Check duplicates
- Reverse an array
- Move values
- Basic Two Pointer ideas
- More Time and Space Complexity analysis

---

# 90 Days of DSA

This repository is part of my **90 Days of Data Structures and Algorithms** open-source learning journey.

My goal is to learn DSA step by step, understand the reason behind every solution, practice coding problems, and create beginner-friendly notes that other students can also use.<!-- Day 2 notes complete -->