# Day 04 - Strings in Python

Welcome to **Day 04** of my **90 Days of Data Structures and Algorithms** journey.

So far I have learned:

```text
Day 01
Big-O and Complexity

Day 02
Arrays and Python Lists

Day 03
Array Problems and Two Pointers
```

Today I am learning:

# Strings

A string is one of the most common data types used in programming.

Strings are used for:

- Names
- Messages
- Passwords
- Search queries
- Email addresses
- Sentences
- Documents
- User input
- URLs
- Text processing

The main goal of Day 4 is to understand how strings work and how to solve common string problems.

---

# Topics Covered

Today I learned:

1. What is a String?
2. Creating Strings
3. String Indexing
4. Negative Indexing
5. String Length
6. Traversing a String
7. Traversal with Index
8. String Slicing
9. String Immutability
10. String Concatenation
11. Uppercase and Lowercase
12. String Comparison
13. Count a Character
14. Count Vowels
15. Count Consonants
16. Reverse a String
17. Palindrome
18. Two Pointers with Strings
19. Remove Spaces
20. Character Frequency
21. First Repeated Character
22. Unique Characters
23. Basic Anagram Idea
24. Time Complexity
25. Space Complexity
26. Common Mistakes
27. Important Patterns
28. Day 4 Self-Test

---

# 1. What is a String?

A string is a sequence of characters.

Example:

```python
name = "Saugat"
```

The string contains:

```text
S
a
u
g
a
t
```

Another example:

```python
message = "Hello World"
```

A string can contain:

- Letters
- Numbers
- Spaces
- Symbols

Example:

```python
text = "Hello123!"
```

---

# 2. Creating Strings

In Python, strings can use:

```python
"double quotes"
```

or:

```python
'single quotes'
```

Example:

```python
name = "Saugat"
city = 'Dallas'
```

Both are strings.

We can check the type:

```python
name = "Saugat"

print(type(name))
```

Output:

```text
<class 'str'>
```

---

# 3. String Indexing

Every character has a position called an:

```text
index
```

Consider:

```python
text = "hello"
```

The indexes are:

```text
Index:       0   1   2   3   4
Character:   h   e   l   l   o
```

Python starts indexes from:

```text
0
```

This is called:

```text
zero-based indexing
```

Example:

```python
text = "hello"

print(text[0])
```

Output:

```text
h
```

Example:

```python
print(text[1])
```

Output:

```text
e
```

Example:

```python
print(text[4])
```

Output:

```text
o
```

---

# Complexity of Indexing

Accessing a known character position is:

```text
O(1)
```

Example:

```python
text[2]
```

Python can directly access that position.

---

# 4. Negative Indexing

Python also lets us count from the end.

Example:

```python
text = "hello"
```

We can represent the indexes as:

```text
Positive:    0   1   2   3   4
Character:   h   e   l   l   o
Negative:   -5  -4  -3  -2  -1
```

Example:

```python
print(text[-1])
```

Output:

```text
o
```

Example:

```python
print(text[-2])
```

Output:

```text
l
```

Important:

```text
-1
```

means:

```text
last character
```

---

# 5. String Length

Python provides:

```python
len()
```

Example:

```python
text = "hello"

print(len(text))
```

Output:

```text
5
```

Another example:

```python
name = "Saugat"

print(len(name))
```

Output:

```text
6
```

For Python strings:

```text
len(text)
```

is generally:

```text
O(1)
```

---

# 6. Traversing a String

Traversal means visiting every character.

Example:

```python
text = "hello"

for character in text:
    print(character)
```

Output:

```text
h
e
l
l
o
```

If the string has:

```text
n characters
```

then the loop visits approximately:

```text
n characters
```

Therefore:

```text
Time Complexity = O(n)
```

---

# 7. Traversing with Index

Sometimes we need both:

```text
index
```

and:

```text
character
```

Example:

```python
text = "hello"

for i in range(len(text)):
    print(i, text[i])
```

Output:

```text
0 h
1 e
2 l
3 l
4 o
```

Time Complexity:

```text
O(n)
```

because every character is visited.

---

# 8. String Slicing

Slicing allows us to get part of a string.

General format:

```python
text[start:end]
```

Important:

```text
start is included
end is excluded
```

Example:

```python
text = "hello"

print(text[0:3])
```

Output:

```text
hel
```

Why?

Indexes:

```text
0 = h
1 = e
2 = l
3 = l
```

The ending index `3` is not included.

---

# More Slicing Examples

```python
text = "hello"
```

First three characters:

```python
print(text[:3])
```

Output:

```text
hel
```

From index 2 to the end:

```python
print(text[2:])
```

Output:

```text
llo
```

Last two characters:

```python
print(text[-2:])
```

Output:

```text
lo
```

Reverse:

```python
print(text[::-1])
```

Output:

```text
olleh
```

---

# Slicing Complexity

If a slice creates:

```text
k characters
```

then roughly:

```text
Time = O(k)
Space = O(k)
```

because Python creates a new string.

---

# 9. String Immutability

This is one of the most important properties of strings.

Python strings are:

# Immutable

Immutable means:

> After a string is created, its individual characters cannot be changed directly.

Example:

```python
text = "hello"

text[0] = "H"
```

This will produce an error.

Why?

Because:

```text
text[0]
```

cannot be modified directly.

---

# Correct Way

Create a new string.

Example:

```python
text = "hello"

new_text = "H" + text[1:]

print(new_text)
```

Output:

```text
Hello
```

The original string was not edited directly.

A new string was created.

---

# Why Immutability Matters

Consider:

```python
text = "hello"
```

You cannot change:

```text
h
```

directly into:

```text
H
```

Instead, Python must create another string.

This matters when analyzing:

```text
Space Complexity
```

and repeated string operations.

---

# 10. String Concatenation

Concatenation means joining strings.

Example:

```python
first = "Hello"
second = "World"

result = first + " " + second

print(result)
```

Output:

```text
Hello World
```

Because strings are immutable, concatenation creates a new string.

---

# Important Performance Idea

This code works:

```python
result = ""

for character in text:
    result += character
```

But repeatedly adding to a string may require repeatedly creating larger strings.

For DSA analysis, repeated concatenation inside a loop can become approximately:

```text
O(n²)
```

A better pattern for building large strings is:

```python
characters = []

for character in text:
    characters.append(character)

result = "".join(characters)
```

This can be handled in roughly:

```text
O(n)
```

time.

This is an important Python string optimization.

---

# 11. Uppercase and Lowercase

Python provides:

```python
.upper()
```

and:

```python
.lower()
```

Example:

```python
text = "Hello World"

print(text.upper())
```

Output:

```text
HELLO WORLD
```

Example:

```python
print(text.lower())
```

Output:

```text
hello world
```

Because strings are immutable, these return new strings.

---

# 12. String Comparison

We can compare strings using:

```python
==
```

Example:

```python
text1 = "hello"
text2 = "hello"

print(text1 == text2)
```

Output:

```text
True
```

Example:

```python
print("Hello" == "hello")
```

Output:

```text
False
```

String comparison is:

```text
case-sensitive
```

That means:

```text
H
```

and:

```text
h
```

are different.

---

# Case-Insensitive Comparison

We can normalize both strings.

Example:

```python
text1 = "Hello"
text2 = "hello"

print(text1.lower() == text2.lower())
```

Output:

```text
True
```

---

# 13. Count a Character

Problem:

Count how many times a specific character appears.

Example:

```text
banana
```

Target:

```text
a
```

Expected:

```text
3
```

---

# Solution

```python
def count_character(text, target):

    count = 0

    for character in text:

        if character == target:
            count += 1

    return count
```

Example:

```python
print(
    count_character(
        "banana",
        "a"
    )
)
```

Output:

```text
3
```

---

# Complexity

We visit every character once.

```text
Time = O(n)
```

Only one counter is used.

```text
Space = O(1)
```

---

# 14. Count Vowels

Vowels are:

```text
a
e
i
o
u
```

Problem:

Count the vowels inside:

```text
Hello World
```

Vowels:

```text
e
o
o
```

Answer:

```text
3
```

---

# Solution

```python
def count_vowels(text):

    vowels = "aeiou"

    count = 0

    for character in text.lower():

        if character in vowels:
            count += 1

    return count
```

Example:

```python
print(count_vowels("Hello World"))
```

Output:

```text
3
```

---

# Complexity

We traverse the string.

```text
Time = O(n)
```

The vowel collection has only five characters.

For DSA purposes, checking:

```python
character in "aeiou"
```

is constant-sized work.

---

# 15. Count Consonants

A consonant is a letter that is not a vowel.

Example:

```text
hello
```

Letters:

```text
h
e
l
l
o
```

Vowels:

```text
e
o
```

Consonants:

```text
h
l
l
```

Count:

```text
3
```

---

# Solution

```python
def count_consonants(text):

    vowels = "aeiou"

    count = 0

    for character in text.lower():

        if character.isalpha() and character not in vowels:
            count += 1

    return count
```

Using:

```python
isalpha()
```

ensures spaces and punctuation are not counted as consonants.

---

# 16. Reverse a String

Input:

```text
hello
```

Expected:

```text
olleh
```

---

# Method 1 - Slicing

```python
def reverse_string(text):

    return text[::-1]
```

Example:

```python
print(reverse_string("hello"))
```

Output:

```text
olleh
```

---

# Complexity

Python creates a new reversed string.

```text
Time = O(n)
Space = O(n)
```

---

# 17. Palindrome

A palindrome reads the same forward and backward.

Examples:

```text
racecar
level
madam
```

Not palindrome:

```text
hello
python
```

---

# Simple Slicing Solution

```python
def is_palindrome(text):

    return text == text[::-1]
```

Example:

```python
print(is_palindrome("racecar"))
```

Output:

```text
True
```

---

# Complexity

Reversing creates a new string.

```text
Time = O(n)
Space = O(n)
```

---

# 18. Palindrome Using Two Pointers

We can use the Two Pointer pattern from Day 3.

Example:

```text
racecar

^     ^
L     R
```

Compare:

```text
r == r
```

Move inward.

```text
racecar

 ^   ^
 L   R
```

Compare:

```text
a == a
```

Continue.

---

# Solution

```python
def is_palindrome_two_pointers(text):

    left = 0

    right = len(text) - 1

    while left < right:

        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True
```

---

# Complexity

We process the characters from both ends.

```text
Time = O(n)
```

We only use:

```text
left
right
```

Therefore:

```text
Extra Space = O(1)
```

This uses less extra memory than creating:

```python
text[::-1]
```

---

# 19. Remove Spaces

Input:

```text
hello world
```

Expected:

```text
helloworld
```

---

# Simple Python Method

```python
text = "hello world"

result = text.replace(" ", "")
```

Output:

```text
helloworld
```

---

# Manual DSA-Friendly Method

Because strings are immutable, it is better to collect characters and join them.

```python
def remove_spaces(text):

    characters = []

    for character in text:

        if character != " ":
            characters.append(character)

    return "".join(characters)
```

Example:

```python
print(remove_spaces("hello world"))
```

Output:

```text
helloworld
```

---

# Complexity

We traverse the string:

```text
O(n)
```

The result may contain up to `n` characters.

```text
Space = O(n)
```

---

# 20. Character Frequency

Character frequency means:

> Count how many times every character appears.

Example:

```text
banana
```

Expected:

```text
b -> 1
a -> 3
n -> 2
```

A dictionary is useful.

---

# Dictionary Idea

A dictionary stores:

```text
key -> value
```

For frequency counting:

```text
character -> count
```

Example:

```text
b -> 1
a -> 3
n -> 2
```

---

# Solution

```python
def character_frequency(text):

    frequency = {}

    for character in text:

        if character in frequency:
            frequency[character] += 1

        else:
            frequency[character] = 1

    return frequency
```

Example:

```python
print(character_frequency("banana"))
```

Output:

```python
{'b': 1, 'a': 3, 'n': 2}
```

---

# Complexity

We visit each character once.

Dictionary lookup and update are average:

```text
O(1)
```

Therefore average:

```text
Time = O(n)
```

The dictionary may contain many different characters.

If there are:

```text
k unique characters
```

then:

```text
Space = O(k)
```

In the worst case:

```text
k = n
```

so this can be:

```text
O(n)
```

space.

---

# 21. First Repeated Character

Problem:

Find the first character that appears again.

Example:

```text
abca
```

Read:

```text
a
b
c
a
```

The first repeated character encountered is:

```text
a
```

---

# Solution

```python
def first_repeated_character(text):

    seen = set()

    for character in text:

        if character in seen:
            return character

        seen.add(character)

    return None
```

Example:

```python
print(
    first_repeated_character(
        "abca"
    )
)
```

Output:

```text
a
```

---

# Complexity

Average:

```text
Time = O(n)
Space = O(n)
```

---

# 22. Check Unique Characters

Problem:

Determine whether every character is unique.

Example:

```text
abcde
```

Answer:

```text
True
```

Example:

```text
hello
```

Answer:

```text
False
```

because:

```text
l
```

appears more than once.

---

# Solution

```python
def has_all_unique_characters(text):

    seen = set()

    for character in text:

        if character in seen:
            return False

        seen.add(character)

    return True
```

---

# Complexity

Average:

```text
Time = O(n)
Space = O(n)
```

---

# 23. Basic Anagram Idea

Two strings are anagrams if they contain the same characters with the same frequencies.

Example:

```text
listen
silent
```

Both contain:

```text
l
i
s
t
e
n
```

So they are anagrams.

---

# Simple Sorting Solution

```python
def are_anagrams(text1, text2):

    return sorted(text1) == sorted(text2)
```

Example:

```python
print(
    are_anagrams(
        "listen",
        "silent"
    )
)
```

Output:

```text
True
```

Sorting generally takes:

```text
O(n log n)
```

We will study better hash-map solutions later.

---

# 24. Time Complexity Summary

| Operation | Typical Time |
|---|---:|
| Character access by index | O(1) |
| `len(text)` | O(1) |
| Full traversal | O(n) |
| Count character | O(n) |
| Count vowels | O(n) |
| Reverse with slicing | O(n) |
| Palindrome with slicing | O(n) |
| Palindrome with Two Pointers | O(n) |
| Remove spaces | O(n) |
| Frequency counting | O(n) average |
| First repeated character | O(n) average |
| Unique character check | O(n) average |
| Sort for anagram | O(n log n) |

---

# 25. Space Complexity Summary

| Problem | Extra Space |
|---|---:|
| Character access | O(1) |
| Traversal | O(1) |
| Character count | O(1) |
| Count vowels | O(1) |
| Reverse using slicing | O(n) |
| Palindrome using Two Pointers | O(1) |
| Remove spaces | O(n) |
| Character frequency | O(k) |
| First repeated character | O(n) |
| Unique character check | O(n) |
| Sorted anagram solution | O(n) |

---

# 26. Common Mistakes

## Mistake 1 - Forgetting Indexing Starts at 0

For:

```text
hello
```

the first character is:

```python
text[0]
```

not:

```python
text[1]
```

---

## Mistake 2 - Trying to Modify a String

Wrong:

```python
text[0] = "H"
```

Strings are immutable.

Correct idea:

```python
new_text = "H" + text[1:]
```

---

## Mistake 3 - Forgetting Slice End is Excluded

```python
text[0:3]
```

includes:

```text
0
1
2
```

but not:

```text
3
```

---

## Mistake 4 - Forgetting Case Sensitivity

```python
"Hello" == "hello"
```

is:

```text
False
```

---

## Mistake 5 - Building Large Strings With Repeated `+=`

This works:

```python
result += character
```

but because strings are immutable, repeated concatenation may perform unnecessary copying.

For larger string-building problems, prefer:

```python
characters.append(character)
```

then:

```python
"".join(characters)
```

---

## Mistake 6 - Using Extra Space When It Is Not Needed

Palindrome with slicing:

```text
Time = O(n)
Space = O(n)
```

Two Pointer palindrome:

```text
Time = O(n)
Space = O(1)
```

---

# 27. Important Patterns Learned

## Pattern 1 - Traversal

```python
for character in text:
```

Useful for:

```text
Counting
Searching
Vowels
Consonants
Frequency
```

---

## Pattern 2 - Two Pointers

```python
left = 0
right = len(text) - 1
```

Useful for:

```text
Palindrome
Comparing opposite ends
```

---

## Pattern 3 - Frequency Dictionary

```python
frequency = {}
```

Useful for:

```text
Character counts
Anagrams
Repeated characters
```

---

## Pattern 4 - Seen Set

```python
seen = set()
```

Useful for:

```text
Duplicates
First repeated character
Unique character problems
```

---

## Pattern 5 - Build Then Join

Instead of repeatedly changing a string:

```python
result += character
```

we can do:

```python
characters = []

characters.append(character)

result = "".join(characters)
```

This is usually a better pattern for constructing strings.

---

# 28. Day 4 Self-Test

Before finishing Day 4, I should be able to explain:

1. What is a string?
2. What does zero-based indexing mean?
3. What does `text[-1]` return?
4. Why is string traversal O(n)?
5. How does slicing work?
6. Why is the ending slice index excluded?
7. What does immutable mean?
8. Why can I not do `text[0] = "H"`?
9. Why does reversing with slicing use O(n) space?
10. How do Two Pointers check palindrome?
11. Why does Two Pointer palindrome use O(1) extra space?
12. How do I count vowels?
13. How do I count consonants?
14. How does character frequency work?
15. Why is a dictionary useful for frequency counting?
16. Why is a set useful for repeated characters?
17. What is an anagram?
18. What is the difference between `"Hello"` and `"hello"`?
19. Why can repeated string concatenation be inefficient?
20. When should I use `"".join()`?

---

# My Day 4 Progress

- [x] Learned String basics
- [x] Learned String indexing
- [x] Learned negative indexing
- [x] Learned `len()`
- [x] Learned traversal
- [x] Learned index-based traversal
- [x] Learned slicing
- [x] Learned string immutability
- [x] Learned concatenation
- [x] Learned case conversion
- [x] Learned string comparison
- [x] Solved character count
- [x] Solved vowel count
- [x] Solved consonant count
- [x] Reversed strings
- [x] Solved palindrome
- [x] Used Two Pointers with strings
- [x] Removed spaces
- [x] Learned character frequency
- [x] Used dictionaries
- [x] Found repeated characters
- [x] Checked unique characters
- [x] Learned basic anagrams
- [x] Analyzed Time Complexity
- [x] Analyzed Space Complexity

---

# Day 4 Quick Cheat Sheet

```text
text[i]
→ O(1)
```

```text
len(text)
→ O(1)
```

```text
for char in text
→ O(n)
```

```text
text[::-1]
→ O(n) Time
→ O(n) Space
```

```text
Two Pointer Palindrome
→ O(n) Time
→ O(1) Extra Space
```

```text
Character Frequency
→ O(n) average Time
→ O(k) Space
```

```text
Seen Set
→ useful for repeated / unique characters
```

```text
Strings
→ immutable
```

---

# Files in Day 04

```text
Day-04-Strings/
│
├── README.md
├── examples.py
└── practice.py
```

`README.md`

Contains the full Day 4 lesson.

`examples.py`

Contains runnable examples.

`practice.py`

Contains practice problems and solutions.

---

# Next - Day 05

Next topic:

# String Problems and Patterns

Possible topics:

- Anagrams
- Valid Palindrome
- First Unique Character
- Longest Common Prefix
- Character Frequencies
- Two Pointer String Problems
- Sliding Window Introduction

---

# 90 Days of DSA

My goal is not only to memorize Python syntax.

My goal is to understand:

```text
What is the problem?
```

```text
Which pattern can solve it?
```

```text
Why does the algorithm work?
```

```text
What is its Time Complexity?
```

and:

```text
What is its Space Complexity?
```

so that I can gradually solve new DSA problems independently.
<!-- Day 4 notes complete -->