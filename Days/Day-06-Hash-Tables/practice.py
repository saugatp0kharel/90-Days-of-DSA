"""
============================================================
DAY 06 PRACTICE
HASH TABLES, DICTIONARIES, AND SETS
============================================================

Try every question BEFORE checking solutions.
"""


# ============================================================
# QUESTION 1
# CREATE DICTIONARY
# ============================================================

"""
Create:

student = {
    "name": "Saugat",
    "major": "Computer Science"
}

Then print the name.

MY SOLUTION:
"""


# ============================================================
# QUESTION 2
# ADD VALUE
# ============================================================

"""
Add:

"age": 24

to the student dictionary.

MY SOLUTION:
"""


# ============================================================
# QUESTION 3
# FREQUENCY MAP
# ============================================================

text = "mississippi"

"""
Build a frequency dictionary.

Expected:

m -> 1
i -> 4
s -> 4
p -> 2

MY SOLUTION:
"""


# ============================================================
# QUESTION 4
# DUPLICATE DETECTION
# ============================================================

numbers = [1, 2, 3, 4, 2]

"""
Return True if a duplicate exists.

Use a set.

Expected:

True

MY SOLUTION:
"""


# ============================================================
# QUESTION 5
# NO DUPLICATE
# ============================================================

numbers = [1, 2, 3, 4, 5]

"""
Expected:

False

MY SOLUTION:
"""


# ============================================================
# QUESTION 6
# TWO SUM
# ============================================================

numbers = [2, 7, 11, 15]

target = 9

"""
Use a dictionary.

Return indexes.

Expected:

[0, 1]

MY SOLUTION:
"""


# ============================================================
# QUESTION 7
# TWO SUM
# ============================================================

numbers = [3, 2, 4]

target = 6

"""
Expected:

[1, 2]

MY SOLUTION:
"""


# ============================================================
# QUESTION 8
# FIRST UNIQUE
# ============================================================

numbers = [4, 5, 4, 6, 5, 7]

"""
Find first unique value.

Expected:

6

MY SOLUTION:
"""


# ============================================================
# QUESTION 9
# INTERSECTION
# ============================================================

a = [1, 2, 2, 3, 4]

b = [2, 3, 5]

"""
Find unique common values.

Expected:

[2, 3]

MY SOLUTION:
"""


# ============================================================
# QUESTION 10
# WORD FREQUENCY
# ============================================================

words = [
    "cat",
    "dog",
    "cat",
    "bird",
    "dog",
    "cat"
]

"""
Expected:

cat -> 3
dog -> 2
bird -> 1

MY SOLUTION:
"""


# ============================================================
# QUESTION 11
# SET MEMBERSHIP
# ============================================================

seen = {
    10,
    20,
    30
}

"""
Check whether:

20

exists.

Expected:

True

MY SOLUTION:
"""


# ============================================================
# QUESTION 12
# UNIQUE VALUES
# ============================================================

numbers = [
    1,
    2,
    2,
    3,
    3,
    4
]

"""
Convert to unique values.

Expected idea:

{1, 2, 3, 4}

MY SOLUTION:
"""


# ============================================================
# QUESTION 13
# COMPLEXITY
# ============================================================

"""
Dictionary lookup:

x in dictionary

Average Time = ?

MY ANSWER:
"""


# ============================================================
# QUESTION 14
# COMPLEXITY
# ============================================================

"""
Set lookup:

x in seen

Average Time = ?

MY ANSWER:
"""


# ============================================================
# QUESTION 15
# COMPLEXITY
# ============================================================

"""
Frequency map over n items.

What is:

Time?

Space?

MY ANSWER:

Time = ?
Space = ?
"""


# ============================================================
# QUESTION 16
# COMPLEXITY
# ============================================================

"""
Two Sum with nested loops:

Time = ?

Two Sum with dictionary:

Average Time = ?
Space = ?
"""


# ============================================================
# QUESTION 17
# DICTIONARY VS SET
# ============================================================

"""
Explain:

When should I use a dictionary?

When should I use a set?
"""


# ============================================================
# QUESTION 18
# GET METHOD
# ============================================================

"""
Explain what this does:

frequency.get("a", 0)

What happens if "a" does not exist?
"""


# ============================================================
# QUESTION 19
# TIME-SPACE TRADE-OFF
# ============================================================

"""
Two Sum:

Brute Force:
Time = ?
Space = ?

Hash Table:
Time = ?
Space = ?

Explain the trade-off.
"""


# ============================================================
# QUESTION 20
# PATTERN RECOGNITION
# ============================================================

"""
Choose the best pattern:

A. Count characters
B. Detect duplicates
C. Two Sum
D. First unique item
E. Check if value exists quickly

Patterns:

- Frequency Dictionary
- Seen Set
- Complement Dictionary
"""


# ============================================================
#
# STOP HERE
#
# TRY BEFORE CHECKING SOLUTIONS
#
# ============================================================































# ============================================================
# SOLUTIONS
# ============================================================


# ============================================================
# SOLUTION 1
# ============================================================

student = {
    "name": "Saugat",
    "major": "Computer Science"
}

print(student["name"])


# ============================================================
# SOLUTION 2
# ============================================================

student["age"] = 24

print(student)


# ============================================================
# SOLUTION 3
# ============================================================

text = "mississippi"

frequency = {}

for character in text:

    frequency[character] = (
        frequency.get(character, 0) + 1
    )

print(frequency)


# ============================================================
# SOLUTION 4
# ============================================================

def contains_duplicate(numbers):

    seen = set()

    for number in numbers:

        if number in seen:
            return True

        seen.add(number)

    return False


print(
    contains_duplicate(
        [1, 2, 3, 4, 2]
    )
)


# ============================================================
# SOLUTION 5
# ============================================================

print(
    contains_duplicate(
        [1, 2, 3, 4, 5]
    )
)


# ============================================================
# SOLUTION 6
# ============================================================

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


print(
    two_sum(
        [2, 7, 11, 15],
        9
    )
)


# ============================================================
# SOLUTION 7
# ============================================================

print(
    two_sum(
        [3, 2, 4],
        6
    )
)


# ============================================================
# SOLUTION 8
# ============================================================

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


print(
    first_unique(
        [4, 5, 4, 6, 5, 7]
    )
)


# ============================================================
# SOLUTION 9
# ============================================================

a = [1, 2, 2, 3, 4]

b = [2, 3, 5]

result = list(
    set(a) & set(b)
)

print(result)


# ============================================================
# SOLUTION 10
# ============================================================

words = [
    "cat",
    "dog",
    "cat",
    "bird",
    "dog",
    "cat"
]

frequency = {}

for word in words:

    frequency[word] = (
        frequency.get(word, 0) + 1
    )

print(frequency)


# ============================================================
# SOLUTION 11
# ============================================================

seen = {
    10,
    20,
    30
}

print(
    20 in seen
)


# ============================================================
# SOLUTION 12
# ============================================================

numbers = [
    1,
    2,
    2,
    3,
    3,
    4
]

unique = set(numbers)

print(unique)


# ============================================================
# SOLUTION 13
# ============================================================

"""
Dictionary lookup:

Average:

O(1)
"""


# ============================================================
# SOLUTION 14
# ============================================================

"""
Set lookup:

Average:

O(1)
"""


# ============================================================
# SOLUTION 15
# ============================================================

"""
Frequency Map:

Time:

O(n)

Space:

O(k)

k = unique values

Worst-case space:

O(n)
"""


# ============================================================
# SOLUTION 16
# ============================================================

"""
Two Sum Brute Force:

O(n^2)


Two Sum Dictionary:

Average Time:

O(n)

Space:

O(n)
"""


# ============================================================
# SOLUTION 17
# ============================================================

"""
DICTIONARY

Use when you need:

key -> value

Examples:

character -> count
number -> index


SET

Use when you mainly need:

Have I seen this?

or:

Does this value exist?
"""


# ============================================================
# SOLUTION 18
# ============================================================

"""
frequency.get("a", 0)

means:

Give me the value stored for "a".

If "a" does not exist:

return 0.
"""


# ============================================================
# SOLUTION 19
# ============================================================

"""
BRUTE FORCE TWO SUM

Time:

O(n^2)

Space:

O(1)


HASH TABLE TWO SUM

Average Time:

O(n)

Space:

O(n)


TRADE-OFF:

We use extra memory
to reduce execution time.
"""


# ============================================================
# SOLUTION 20
# ============================================================

"""
A. Count characters

Frequency Dictionary


B. Detect duplicates

Seen Set


C. Two Sum

Complement Dictionary


D. First unique

Frequency Dictionary


E. Fast membership

Set
"""


# ============================================================
# FINAL DAY 6 SUMMARY
# ============================================================

"""
HASH TABLE PATTERNS


FREQUENCY MAP

Question:

How many times?


-----------------------------------------


SET

Question:

Have I seen this?


-----------------------------------------


DICTIONARY

Question:

What value belongs to this key?


-----------------------------------------


TWO SUM

Question:

What number do I need?

needed = target - current


-----------------------------------------


AVERAGE HASH LOOKUP

O(1)


-----------------------------------------


COMMON HASH SOLUTIONS

Time:

O(n)

Space:

O(n)
"""