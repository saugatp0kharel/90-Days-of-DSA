# Day 05 - String Problems and Patterns

Welcome to **Day 05** of my **90 Days of Data Structures and Algorithms** journey.

So far I have learned:

```text
Day 01
Big-O and Complexity

Day 02
Arrays and Python Lists

Day 03
Array Problems and Two Pointers

Day 04
Strings, Traversal, Palindrome, and Frequency Counting
```

Today I am going deeper into:

# String Problems and Patterns

The goal of Day 5 is not only to use strings.

The goal is to learn how to recognize common patterns that appear again and again in string problems.

Today I learned:

- String traversal review
- Character frequency
- Hash Map / Dictionary thinking
- Anagrams
- First unique character
- Valid palindrome with cleanup
- Remove duplicate characters
- Longest common prefix
- String compression
- Two Pointers with strings
- Sliding Window introduction
- Time Complexity
- Space Complexity
- Time-Space Trade-offs

---

# Table of Contents

1. Problem-Solving Strategy
2. Character Frequency Review
3. Hash Map / Dictionary Pattern
4. Anagrams
5. First Unique Character
6. Valid Palindrome
7. Remove Duplicate Characters
8. Longest Common Prefix
9. String Compression
10. Two Pointers Review
11. Sliding Window Introduction
12. Longest Substring Without Repeating Characters
13. Time Complexity Summary
14. Space Complexity Summary
15. Common Mistakes
16. Important Patterns
17. Day 5 Self-Test
18. Day 5 Progress
19. Next Topic

---

# 1. Problem-Solving Strategy

When I see a string problem, I should not immediately start coding.

I should first ask:

```text
Do I need to visit every character?
```

```text
Do I need to remember how many times each character appears?
```

```text
Do I need to compare characters from both ends?
```

```text
Do I need to track a substring or a moving range?
```

```text
Do I need to avoid repeated work?
```

A useful problem-solving process is:

```text
Read the problem
        ↓
Understand the input
        ↓
Understand the expected output
        ↓
Look for a pattern
        ↓
Write the simplest correct solution
        ↓
Analyze Time Complexity
        ↓
Analyze Space Complexity
        ↓
Try to improve it
```

The important Day 5 question is:

> What information should I remember while traversing the string?

---

# 2. Character Frequency Review

Character frequency means:

> Count how many times every character appears.

Example:

```text
banana
```

Characters:

```text
b -> 1
a -> 3
n -> 2
```

A dictionary is perfect for this.

---

## Solution

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
print(
    character_frequency(
        "banana"
    )
)
```

Output:

```python
{'b': 1, 'a': 3, 'n': 2}
```

---

## Step-by-Step

Start:

```text
frequency = {}
```

Read:

```text
b
```

Not in dictionary.

Add:

```text
{'b': 1}
```

Read:

```text
a
```

Add:

```text
{'b': 1, 'a': 1}
```

Read:

```text
n
```

Add:

```text
{'b': 1, 'a': 1, 'n': 1}
```

Continue.

Final:

```text
b -> 1
a -> 3
n -> 2
```

---

## Complexity

We visit every character once.

Average dictionary lookup/update is:

```text
O(1)
```

Therefore:

```text
Time = O(n)
```

If there are `k` unique characters:

```text
Space = O(k)
```

In the worst case:

```text
k = n
```

so:

```text
Space = O(n)
```

---

# 3. Hash Map / Dictionary Pattern

A dictionary lets us store:

```text
key -> value
```

For strings, common examples are:

```text
character -> count
```

```text
character -> last index
```

```text
character -> first index
```

Example:

```python
frequency = {
    "a": 3,
    "b": 1,
    "n": 2
}
```

The dictionary pattern is useful for:

- Anagrams
- Frequency counting
- First unique character
- Repeated characters
- Sliding Window problems
- Tracking indexes

A very common question is:

```text
Have I seen this character before?
```

For that, we may use:

```python
set()
```

or a dictionary.

---

# 4. Anagrams

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

So:

```text
True
```

Another example:

```text
hello
world
```

These are not anagrams.

---

# Method 1 - Sorting

```python
def are_anagrams_sorting(text1, text2):

    return sorted(text1) == sorted(text2)
```

Example:

```python
print(
    are_anagrams_sorting(
        "listen",
        "silent"
    )
)
```

Output:

```text
True
```

---

## Complexity

Sorting usually costs:

```text
O(n log n)
```

So:

```text
Time = O(n log n)
```

---

# Method 2 - Frequency Dictionary

A better DSA approach is to count characters.

```python
def are_anagrams(text1, text2):

    if len(text1) != len(text2):
        return False

    frequency = {}

    for character in text1:

        frequency[character] = (
            frequency.get(character, 0) + 1
        )

    for character in text2:

        if character not in frequency:
            return False

        frequency[character] -= 1

        if frequency[character] < 0:
            return False

    return True
```

---

## Why Check Length First?

If:

```text
len(text1) != len(text2)
```

they cannot contain exactly the same number of characters.

So we can immediately return:

```python
False
```

---

## Complexity

We traverse each string once.

```text
Time = O(n)
```

Dictionary stores character counts.

```text
Space = O(k)
```

where `k` is the number of unique characters.

---

# 5. First Unique Character

A unique character appears only once.

Example:

```text
leetcode
```

Frequency:

```text
l -> 1
e -> 3
t -> 1
c -> 1
o -> 1
d -> 1
```

The first character with frequency `1` is:

```text
l
```

---

# Solution

We use two passes.

First pass:

```text
count every character
```

Second pass:

```text
find the first character with count 1
```

Code:

```python
def first_unique_character(text):

    frequency = {}

    for character in text:

        frequency[character] = (
            frequency.get(character, 0) + 1
        )

    for character in text:

        if frequency[character] == 1:
            return character

    return None
```

---

## Why Two Passes?

The first pass tells us:

```text
how many times each character appears
```

The second pass preserves the original order and finds the first unique one.

---

## Complexity

First traversal:

```text
O(n)
```

Second traversal:

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

Space:

```text
O(k)
```

---

# 6. Valid Palindrome

Sometimes a palindrome problem contains:

- Spaces
- Capital letters
- Punctuation

Example:

```text
A man, a plan, a canal: Panama
```

If we ignore:

```text
spaces
punctuation
capitalization
```

it becomes:

```text
amanaplanacanalpanama
```

This reads the same forward and backward.

So:

```text
True
```

---

# Method 1 - Clean the String First

```python
def valid_palindrome_clean(text):

    cleaned = []

    for character in text:

        if character.isalnum():
            cleaned.append(
                character.lower()
            )

    cleaned = "".join(cleaned)

    return cleaned == cleaned[::-1]
```

---

## Complexity

Cleaning:

```text
O(n)
```

Reversing:

```text
O(n)
```

Total:

```text
O(n)
```

But we create a new string/list.

```text
Space = O(n)
```

---

# Method 2 - Two Pointers

We can avoid creating the cleaned string.

Use:

```python
left
right
```

Move inward.

Skip non-alphanumeric characters.

---

## Solution

```python
def valid_palindrome(text):

    left = 0
    right = len(text) - 1

    while left < right:

        while (
            left < right
            and
            not text[left].isalnum()
        ):
            left += 1

        while (
            left < right
            and
            not text[right].isalnum()
        ):
            right -= 1

        if (
            text[left].lower()
            !=
            text[right].lower()
        ):
            return False

        left += 1
        right -= 1

    return True
```

---

## Why This is Better in Space

We do not create another cleaned string.

We only use:

```text
left
right
```

Therefore:

```text
Extra Space = O(1)
```

Time:

```text
O(n)
```

---

# 7. Remove Duplicate Characters

Problem:

```text
programming
```

Remove repeated characters while keeping the first occurrence.

One possible output:

```text
progamin
```

---

# Main Idea

Use a set:

```python
seen = set()
```

If a character has not been seen:

```text
keep it
```

If already seen:

```text
skip it
```

---

## Solution

```python
def remove_duplicates(text):

    seen = set()

    result = []

    for character in text:

        if character not in seen:

            seen.add(character)

            result.append(character)

    return "".join(result)
```

---

## Step-by-Step

Input:

```text
programming
```

Read:

```text
p
```

Keep:

```text
p
```

Read:

```text
r
```

Keep:

```text
pr
```

Continue.

When a repeated character appears:

```text
skip it
```

Final:

```text
progamin
```

---

## Complexity

Average:

```text
Time = O(n)
```

Set:

```text
O(n)
```

Result:

```text
O(n)
```

So:

```text
Space = O(n)
```

---

# 8. Longest Common Prefix

A prefix is the beginning part of a string.

Example:

```text
flower
```

Prefixes include:

```text
f
fl
flo
flow
flowe
flower
```

Problem:

```python
["flower", "flow", "flight"]
```

The longest common prefix is:

```text
fl
```

---

# Simple Solution

Start with the first word:

```text
flower
```

Use it as the current prefix.

Compare it with the next word.

If the word does not start with the prefix:

```text
shorten the prefix
```

---

## Solution

```python
def longest_common_prefix(words):

    if not words:
        return ""

    prefix = words[0]

    for word in words[1:]:

        while not word.startswith(prefix):

            prefix = prefix[:-1]

            if prefix == "":
                return ""

    return prefix
```

---

## Example

Input:

```text
flower
flow
flight
```

Start:

```text
prefix = flower
```

Compare with:

```text
flow
```

Shorten:

```text
flowe
```

Still no.

Shorten:

```text
flow
```

Match.

Now compare:

```text
flight
```

Shorten:

```text
flo
```

No.

Shorten:

```text
fl
```

Match.

Answer:

```text
fl
```

---

## Complexity

Let:

```text
n = number of words
m = length of compared characters
```

A simple way to describe this is:

```text
O(n × m)
```

---

# 9. String Compression

Problem:

```text
aaabbc
```

We want:

```text
a3b2c1
```

This means:

```text
a appears 3 times
b appears 2 times
c appears 1 time
```

This version compresses consecutive repeated characters.

---

# Main Idea

Track:

```text
current character
count
```

When the character changes:

```text
save previous character + count
```

---

## Solution

```python
def compress_string(text):

    if not text:
        return ""

    result = []

    count = 1

    for i in range(1, len(text)):

        if text[i] == text[i - 1]:

            count += 1

        else:

            result.append(
                text[i - 1] + str(count)
            )

            count = 1

    result.append(
        text[-1] + str(count)
    )

    return "".join(result)
```

---

## Step-by-Step

Input:

```text
aaabbc
```

Start:

```text
a
count = 1
```

Next `a`:

```text
count = 2
```

Next `a`:

```text
count = 3
```

Now `b` appears.

Store:

```text
a3
```

Then count `b`:

```text
b2
```

Finally:

```text
c1
```

Result:

```text
a3b2c1
```

---

## Complexity

We traverse once.

```text
Time = O(n)
```

The result can grow with `n`.

```text
Space = O(n)
```

---

# 10. Two Pointers Review

Two Pointers means using two positions.

Example:

```text
racecar

^     ^
L     R
```

Useful for:

- Palindrome
- Comparing opposite ends
- Valid palindrome
- Sorted pair problems

Typical setup:

```python
left = 0
right = len(text) - 1
```

Then:

```python
left += 1
right -= 1
```

Two Pointers is useful when:

```text
the answer depends on both ends
```

or:

```text
we can eliminate part of the search space
```

---

# 11. Sliding Window Introduction

Sliding Window is another important DSA pattern.

It is useful when a problem asks about:

```text
substring
subarray
consecutive characters
longest range
shortest range
```

Imagine:

```text
abcabcbb
```

A window might look like:

```text
[a b c] a b c b b
```

Then move:

```text
a [b c a] b c b b
```

The window changes as we process the string.

---

# Two Types of Sliding Window

## Fixed Window

The size stays the same.

Example:

```text
Find every substring of length 3.
```

## Variable Window

The size grows or shrinks based on a condition.

Example:

```text
Longest substring without repeated characters.
```

Day 5 introduces the variable window.

---

# 12. Longest Substring Without Repeating Characters

Example:

```text
abcabcbb
```

Longest substring without repeating characters:

```text
abc
```

Length:

```text
3
```

---

# Brute Force Idea

We could generate many substrings and check each one.

That can become slow:

```text
O(n²)
```

or worse depending on implementation.

---

# Sliding Window Idea

Use:

```text
left
right
```

to represent a window.

Also use a set:

```python
seen = set()
```

If the new character is not repeated:

```text
expand right
```

If duplicate appears:

```text
remove from left
```

until the window becomes valid again.

---

## Solution

```python
def longest_unique_substring(text):

    seen = set()

    left = 0

    longest = 0

    for right in range(len(text)):

        while text[right] in seen:

            seen.remove(
                text[left]
            )

            left += 1

        seen.add(
            text[right]
        )

        window_length = (
            right - left + 1
        )

        longest = max(
            longest,
            window_length
        )

    return longest
```

---

## Step-by-Step

Input:

```text
abcabcbb
```

Start:

```text
window = ""
```

Add `a`:

```text
a
```

Length:

```text
1
```

Add `b`:

```text
ab
```

Length:

```text
2
```

Add `c`:

```text
abc
```

Length:

```text
3
```

Next `a` is repeated.

So move the left side until `a` is no longer duplicated.

Continue.

Maximum length remains:

```text
3
```

---

## Complexity

Each character enters the window once and leaves at most once.

Therefore:

```text
Time = O(n)
```

The set can contain characters from the window.

```text
Space = O(k)
```

where `k` is the number of unique characters in the window.

---

# 13. Time Complexity Summary

| Problem | Typical Time |
|---|---:|
| Character Frequency | O(n) |
| Anagram using sorting | O(n log n) |
| Anagram using dictionary | O(n) |
| First Unique Character | O(n) |
| Valid Palindrome | O(n) |
| Remove Duplicates | O(n) average |
| Longest Common Prefix | O(n × m) |
| String Compression | O(n) |
| Longest Unique Substring | O(n) |

---

# 14. Space Complexity Summary

| Problem | Extra Space |
|---|---:|
| Character Frequency | O(k) |
| Anagram Dictionary | O(k) |
| First Unique Character | O(k) |
| Valid Palindrome Two Pointers | O(1) |
| Remove Duplicates | O(n) |
| Longest Common Prefix | O(1) to O(m), depending on implementation |
| String Compression | O(n) |
| Longest Unique Substring | O(k) |

---

# 15. Common Mistakes

## Mistake 1 - Sorting Everything Automatically

Anagram can be solved with sorting:

```text
O(n log n)
```

but frequency counting can give:

```text
O(n)
```

---

## Mistake 2 - Forgetting Case

Example:

```text
Listen
Silent
```

If case should not matter, normalize first:

```python
text.lower()
```

---

## Mistake 3 - Forgetting Spaces and Punctuation

For valid palindrome:

```text
A man, a plan, a canal: Panama
```

spaces and punctuation should usually be ignored.

Use:

```python
isalnum()
```

---

## Mistake 4 - Repeated String Concatenation

This:

```python
result += character
```

inside a loop can be inefficient.

Prefer:

```python
result = []

result.append(character)

"".join(result)
```

---

## Mistake 5 - Sliding Window Without Shrinking

If a duplicate appears, the left side of the window must move.

Otherwise the window remains invalid.

---

## Mistake 6 - Forgetting Original Order

For first unique character:

```text
frequency alone is not enough
```

We also need to scan the original string again to find the first unique character.

---

# 16. Important Patterns

## Pattern 1 - Frequency Dictionary

```python
frequency = {}
```

Use when the problem asks:

```text
How many times?
```

Useful for:

- Anagrams
- Character frequency
- First unique character

---

## Pattern 2 - Seen Set

```python
seen = set()
```

Use when the problem asks:

```text
Have I seen this before?
```

Useful for:

- Remove duplicates
- Repeated characters
- Sliding Window

---

## Pattern 3 - Two Pointers

```python
left = 0
right = len(text) - 1
```

Useful for:

- Palindrome
- Valid palindrome
- Comparing opposite ends

---

## Pattern 4 - Sliding Window

```python
left = 0

for right in range(len(text)):
```

Useful for:

- Longest substring
- Shortest substring
- Consecutive character problems

---

## Pattern 5 - Build and Join

```python
result = []

result.append(...)

return "".join(result)
```

Useful because strings are immutable.

---

# 17. Day 5 Self-Test

Before completing Day 5, I should be able to explain:

1. What is a frequency dictionary?
2. Why are dictionaries useful for strings?
3. What is an anagram?
4. Why is sorting anagram O(n log n)?
5. How can frequency counting improve it?
6. What is a unique character?
7. Why does first unique character use two passes?
8. What does `isalnum()` do?
9. How does valid palindrome use Two Pointers?
10. Why can Two Pointer palindrome use O(1) space?
11. How does a set remove duplicates?
12. What is a prefix?
13. How does longest common prefix work?
14. How does string compression work?
15. What is Sliding Window?
16. What is the difference between fixed and variable window?
17. How does longest substring without repeats work?
18. Why is Sliding Window often O(n)?
19. What is a Time-Space Trade-off?
20. When should I use a set versus a dictionary?

---

# 18. My Day 5 Progress

- [x] Reviewed string traversal
- [x] Reviewed character frequency
- [x] Learned Hash Map / Dictionary pattern
- [x] Solved Anagram
- [x] Solved First Unique Character
- [x] Solved Valid Palindrome
- [x] Used Two Pointers with cleaned text
- [x] Removed duplicate characters
- [x] Solved Longest Common Prefix
- [x] Learned String Compression
- [x] Reviewed Two Pointers
- [x] Learned Sliding Window basics
- [x] Solved Longest Substring Without Repeats
- [x] Analyzed Time Complexity
- [x] Analyzed Space Complexity

---

# Day 5 Quick Cheat Sheet

```text
Frequency Dictionary
→ How many times?
```

```text
Set
→ Have I seen this before?
```

```text
Two Pointers
→ Compare from both ends
```

```text
Sliding Window
→ Work with a moving substring
```

```text
Anagram with Dictionary
→ O(n)
```

```text
First Unique Character
→ Frequency + second traversal
```

```text
Valid Palindrome
→ Two Pointers + skip non-alphanumeric
```

```text
Longest Unique Substring
→ Sliding Window + Set
```

---

# Files in Day 05

```text
Day-05-String-Problems/
│
├── README.md
├── examples.py
└── practice.py
```

`README.md`

Contains the complete Day 5 lesson.

`examples.py`

Contains working examples.

`practice.py`

Contains questions and solutions.

---

# Next - Day 06

Next topic:

# Hash Tables and Dictionaries

Possible topics:

- What is Hashing?
- Dictionary operations
- Set operations
- Frequency Maps
- Two Sum
- Duplicate Detection
- Group Anagrams
- First Unique Element
- Hash Table Complexity

---

# 90 Days of DSA

The goal is not only to memorize code.

The goal is to recognize patterns such as:

```text
Frequency Map
Set
Two Pointers
Sliding Window
```

and understand:

```text
why the solution works
```

```text
what its Time Complexity is
```

and:

```text
what its Space Complexity is
```

so that I can gradually solve new DSA problems independently.