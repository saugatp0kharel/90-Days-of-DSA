# Day 06 - Hash Tables, Dictionaries, and Sets

Welcome to **Day 06** of my **90 Days of Data Structures and Algorithms** journey.

So far I have learned:

```text
Day 01 - Big-O and Complexity
Day 02 - Arrays and Python Lists
Day 03 - Array Problems and Two Pointers
Day 04 - Strings
Day 05 - String Problems and Patterns
```

Today I am learning:

# Hash Tables

In Python, the most common hash-table structures are:

```python
dict
set
```

Hash tables are extremely important because they allow us to store and find information very quickly.

Today I learned:

- What is a Hash Table?
- What is Hashing?
- What is a Hash Function?
- Python Dictionary
- Python Set
- Dictionary operations
- Set operations
- Average O(1) lookup
- Frequency maps
- Duplicate detection
- Two Sum
- First unique element
- Intersection of arrays
- Grouping values
- Time-Space Trade-offs
- Common hash-table patterns

---

# 1. What is a Hash Table?

A hash table is a data structure used to store:

```text
key -> value
```

pairs.

Example:

```python
student = {
    "name": "Saugat",
    "age": 24,
    "major": "Computer Science"
}
```

Here:

```text
"name"  -> "Saugat"
"age"   -> 24
"major" -> "Computer Science"
```

Each key is connected to a value.

---

# 2. Why Use a Hash Table?

Suppose we want to find whether:

```text
apple
```

exists inside a list.

With a list:

```python
fruits = [
    "banana",
    "orange",
    "apple",
    "grape"
]
```

we may need to search one by one.

Worst case:

```text
O(n)
```

But with a set:

```python
fruits = {
    "banana",
    "orange",
    "apple",
    "grape"
}
```

checking:

```python
"apple" in fruits
```

is average:

```text
O(1)
```

That is why hash tables are powerful.

---

# 3. What is Hashing?

Hashing is the process of converting a key into a number that helps locate where the value should be stored.

Simple idea:

```text
key
↓
hash function
↓
location in memory
```

For example:

```text
"apple"
↓
hash function
↓
some internal location
```

Python handles this automatically.

We do not manually calculate the hash location.

---

# 4. What is a Hash Function?

A hash function takes a key and produces a hash value.

Python example:

```python
print(hash("apple"))
```

The exact result may differ between Python runs.

Important idea:

```text
same key
→ same hash during that process
```

The hash helps Python find the stored value quickly.

---

# 5. Python Dictionary

A dictionary stores:

```text
key -> value
```

Example:

```python
person = {
    "name": "Saugat",
    "city": "Dallas",
    "major": "Computer Science"
}
```

Access:

```python
print(person["name"])
```

Output:

```text
Saugat
```

Average lookup:

```text
O(1)
```

---

# 6. Adding Dictionary Values

Example:

```python
person = {}

person["name"] = "Saugat"

person["age"] = 24
```

Now:

```python
print(person)
```

Output:

```python
{
    "name": "Saugat",
    "age": 24
}
```

Average insertion:

```text
O(1)
```

---

# 7. Updating Dictionary Values

Example:

```python
person = {
    "age": 24
}

person["age"] = 25
```

Now:

```text
age -> 25
```

Average update:

```text
O(1)
```

---

# 8. Checking if a Key Exists

Example:

```python
person = {
    "name": "Saugat"
}

if "name" in person:
    print("Found")
```

Average lookup:

```text
O(1)
```

---

# 9. Dictionary `.get()`

Instead of:

```python
frequency[character]
```

we can use:

```python
frequency.get(character, 0)
```

Example:

```python
frequency = {}

frequency["a"] = frequency.get("a", 0) + 1
```

If `"a"` does not exist:

```text
get("a", 0)
```

returns:

```text
0
```

So:

```text
0 + 1 = 1
```

This is very useful for frequency counting.

---

# 10. Traversing a Dictionary

Example:

```python
person = {
    "name": "Saugat",
    "age": 24
}
```

Keys:

```python
for key in person:
    print(key)
```

Values:

```python
for value in person.values():
    print(value)
```

Key and value:

```python
for key, value in person.items():
    print(key, value)
```

Traversal complexity:

```text
O(n)
```

because we visit all entries.

---

# 11. Python Set

A set stores:

```text
unique values
```

Example:

```python
numbers = {
    10,
    20,
    30
}
```

Important:

A set does not store duplicates.

Example:

```python
numbers = {
    1,
    2,
    2,
    3
}
```

The set becomes:

```text
{1, 2, 3}
```

---

# 12. Add to a Set

```python
seen = set()

seen.add(10)
seen.add(20)
```

Average insertion:

```text
O(1)
```

---

# 13. Check Membership in a Set

```python
if 10 in seen:
    print("Found")
```

Average lookup:

```text
O(1)
```

This makes sets useful for:

- Duplicate detection
- Unique elements
- Membership checking
- Sliding Window

---

# 14. Remove From a Set

```python
seen.remove(10)
```

Average:

```text
O(1)
```

Safer version:

```python
seen.discard(10)
```

`discard()` does not raise an error if the value does not exist.

---

# 15. Dictionary vs Set

Dictionary:

```text
key -> value
```

Example:

```python
{
    "a": 3,
    "b": 2
}
```

Set:

```text
unique values only
```

Example:

```python
{
    "a",
    "b",
    "c"
}
```

Use a dictionary when you need:

```text
value associated with a key
```

Use a set when you mainly need:

```text
Have I seen this?
```

---

# 16. Frequency Map

A frequency map counts occurrences.

Input:

```text
banana
```

Expected:

```text
b -> 1
a -> 3
n -> 2
```

Solution:

```python
def frequency_map(text):

    frequency = {}

    for character in text:

        frequency[character] = (
            frequency.get(character, 0) + 1
        )

    return frequency
```

Complexity:

```text
Time = O(n)
Space = O(k)
```

where:

```text
k = number of unique characters
```

---

# 17. Duplicate Detection

Problem:

```python
numbers = [1, 2, 3, 4, 2]
```

Expected:

```text
True
```

Solution:

```python
def contains_duplicate(numbers):

    seen = set()

    for number in numbers:

        if number in seen:
            return True

        seen.add(number)

    return False
```

Average:

```text
Time = O(n)
Space = O(n)
```

---

# 18. Two Sum

This is one of the most famous hash-table problems.

Problem:

```python
numbers = [2, 7, 11, 15]
target = 9
```

We want two values whose sum equals:

```text
9
```

Answer:

```text
2 + 7
```

---

# Brute Force

```python
for i in range(len(numbers)):

    for j in range(i + 1, len(numbers)):

        if numbers[i] + numbers[j] == target:
            return [i, j]
```

Time:

```text
O(n²)
```

---

# Better Solution - Dictionary

For every number:

```text
current number
```

calculate:

```text
needed = target - current
```

Example:

```text
target = 9
current = 2

needed = 7
```

Store numbers we have already seen.

---

## Solution

```python
def two_sum(numbers, target):

    seen = {}

    for index, number in enumerate(numbers):

        needed = target - number

        if needed in seen:

            return [
                seen[needed],
                index
            ]

        seen[number] = index

    return None
```

Example:

```python
print(
    two_sum(
        [2, 7, 11, 15],
        9
    )
)
```

Output:

```text
[0, 1]
```

---

## Complexity

One traversal:

```text
O(n)
```

Dictionary lookup:

```text
O(1) average
```

Therefore:

```text
Time = O(n)
```

Dictionary can hold:

```text
n
```

elements.

```text
Space = O(n)
```

---

# 19. Two Sum Step-by-Step

Input:

```text
[2, 7, 11, 15]
```

Target:

```text
9
```

Start:

```text
seen = {}
```

Read:

```text
2
```

Need:

```text
9 - 2 = 7
```

7 not found.

Store:

```text
2 -> index 0
```

Now:

```text
seen = {
    2: 0
}
```

Read:

```text
7
```

Need:

```text
9 - 7 = 2
```

2 exists.

Therefore:

```text
index 0
index 1
```

Answer:

```text
[0, 1]
```

---

# 20. First Unique Element

Input:

```python
numbers = [4, 5, 4, 6, 5, 7]
```

Frequency:

```text
4 -> 2
5 -> 2
6 -> 1
7 -> 1
```

First unique value:

```text
6
```

Solution:

```python
def first_unique(numbers):

    frequency = {}

    for number in numbers:

        frequency[number] = (
            frequency.get(number, 0) + 1
        )

    for number in numbers:

        if frequency[number] == 1:
            return number

    return None
```

Time:

```text
O(n)
```

Space:

```text
O(n)
```

---

# 21. Array Intersection

Problem:

```python
a = [1, 2, 2, 3, 4]
b = [2, 3, 5]
```

Common values:

```text
2
3
```

---

## Solution

```python
def intersection(a, b):

    set_a = set(a)

    result = []

    for number in b:

        if number in set_a:
            result.append(number)

    return result
```

A cleaner unique-result version:

```python
def intersection(a, b):

    return list(
        set(a) & set(b)
    )
```

---

# 22. Why Sets Help Intersection

Without a set, we might repeatedly search a list.

List membership:

```text
O(n)
```

Set membership:

```text
O(1) average
```

So sets can make repeated membership checks much faster.

---

# 23. Group Values by Frequency

Example:

```python
words = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple"
]
```

Frequency:

```text
apple -> 3
banana -> 2
orange -> 1
```

Solution:

```python
def word_frequency(words):

    frequency = {}

    for word in words:

        frequency[word] = (
            frequency.get(word, 0) + 1
        )

    return frequency
```

---

# 24. Time-Space Trade-off

Hash-table solutions often use:

```text
more memory
```

to get:

```text
faster lookup
```

Example:

Two Sum brute force:

```text
Time = O(n²)
Space = O(1)
```

Hash table:

```text
Time = O(n)
Space = O(n)
```

We traded:

```text
more memory
```

for:

```text
less time
```

This is called:

# Time-Space Trade-off

---

# 25. Hash Table Complexity

Average case:

| Operation | Dictionary | Set |
|---|---:|---:|
| Insert | O(1) | O(1) |
| Lookup | O(1) | O(1) |
| Update | O(1) | N/A |
| Delete | O(1) | O(1) |
| Full traversal | O(n) | O(n) |

Important:

These are:

```text
average-case
```

complexities.

In rare pathological collision cases, operations can become slower.

For beginner DSA problems, we normally use:

```text
O(1) average
```

for hash-table lookup/insertion.

---

# 26. What is a Hash Collision?

A collision happens when two different keys map to the same internal location.

Simple idea:

```text
key A
   \
    same location
   /
key B
```

Python handles collisions internally.

For now, the important idea is:

```text
Hash tables are O(1) average,
not guaranteed O(1) in every possible case.
```

---

# 27. Important Patterns

## Frequency Map

Question:

```text
How many times does this appear?
```

Use:

```python
frequency = {}
```

---

## Seen Set

Question:

```text
Have I already seen this value?
```

Use:

```python
seen = set()
```

---

## Complement Lookup

Question:

```text
What value do I need to complete the answer?
```

Example:

```text
Two Sum
```

Use:

```text
needed = target - current
```

---

## Key to Index

Sometimes dictionary stores:

```text
value -> index
```

Example:

```python
seen[number] = index
```

Useful for:

```text
Two Sum
```

---

# 28. Common Mistakes

## Mistake 1

Using a list for repeated membership checks.

```python
if x in list:
```

can be:

```text
O(n)
```

A set can often make it:

```text
O(1) average
```

---

## Mistake 2

Using a set when you need counts.

A set only tells:

```text
exists / does not exist
```

For counts, use:

```python
dict
```

---

## Mistake 3

Forgetting `.get()`

Instead of:

```python
frequency[x] += 1
```

when key may not exist, use:

```python
frequency[x] = frequency.get(x, 0) + 1
```

---

## Mistake 4

Forgetting Hash Tables Use Extra Memory

Hash solutions are often fast because they store extra information.

Example:

```text
Time O(n)
Space O(n)
```

---

# 29. Day 6 Complexity Summary

| Problem | Time | Space |
|---|---:|---:|
| Frequency Map | O(n) | O(k) |
| Duplicate Detection | O(n) average | O(n) |
| Two Sum | O(n) average | O(n) |
| First Unique Element | O(n) | O(n) |
| Intersection | O(n + m) average | O(n) |
| Word Frequency | O(n) | O(k) |

---

# 30. Day 6 Self-Test

Before finishing Day 6, I should be able to explain:

1. What is a Hash Table?
2. What is hashing?
3. What is a hash function?
4. What is a dictionary?
5. What is a set?
6. Difference between dictionary and set?
7. Why is dictionary lookup O(1) average?
8. What is a frequency map?
9. When should I use a set?
10. When should I use a dictionary?
11. What does `.get()` do?
12. How does Two Sum use a dictionary?
13. What is a complement?
14. Why is brute-force Two Sum O(n²)?
15. Why is hash-table Two Sum O(n)?
16. What is a Time-Space Trade-off?
17. What is a hash collision?
18. How can sets help with intersections?
19. Why do first unique problems often use two passes?
20. Why are hash tables important in DSA?

---

# My Day 6 Progress

- [x] Learned Hash Tables
- [x] Learned Hashing
- [x] Learned Hash Functions
- [x] Learned Dictionaries
- [x] Learned Sets
- [x] Learned Dictionary operations
- [x] Learned Set operations
- [x] Learned Frequency Maps
- [x] Solved Duplicate Detection
- [x] Solved Two Sum
- [x] Solved First Unique Element
- [x] Solved Array Intersection
- [x] Learned Time-Space Trade-offs
- [x] Learned Hash Collisions
- [x] Analyzed Time Complexity
- [x] Analyzed Space Complexity

---

# Day 6 Quick Cheat Sheet

```text
Dictionary
→ key -> value
```

```text
Set
→ unique values
```

```text
Lookup
→ O(1) average
```

```text
Frequency problem
→ Dictionary
```

```text
Have I seen this?
→ Set
```

```text
Two Sum
→ Dictionary + complement
```

```text
Hash Table solutions
→ often O(n) Time
→ often O(n) Space
```

---

# Files in Day 06

```text
Day-06-Hash-Tables/
├── README.md
├── examples.py
└── practice.py
```

---

# Next - Day 07

Next topic:

# Stacks

Possible topics:

- What is a Stack?
- LIFO
- push
- pop
- peek
- Valid Parentheses
- Reverse using Stack
- Monotonic Stack introduction

---

# 90 Days of DSA

The goal is not only to write working code.

The goal is to recognize:

```text
Frequency Map
Seen Set
Complement Lookup
Key-Value Mapping
```

and understand:

```text
Why the solution works
Time Complexity
Space Complexity
```

so I can solve new problems independently.