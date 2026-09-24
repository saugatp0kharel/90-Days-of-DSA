"""
============================================================
DAY 04 PRACTICE
STRINGS
============================================================

IMPORTANT:

Try every problem yourself before reading the solutions.

For every question ask:

1. What is the input?
2. What output should I produce?
3. Do I need to traverse the string?
4. Can Two Pointers help?
5. Do I need a set?
6. Do I need a dictionary?
7. Am I creating a new string?
8. What is the Time Complexity?
9. What is the Space Complexity?
"""


# ============================================================
# QUESTION 1
# FIRST AND LAST CHARACTER
# ============================================================

text = "python"

"""
Print:

first character
last character


Expected:

p
n


MY SOLUTION:
"""


# ============================================================
# QUESTION 2
# STRING LENGTH
# ============================================================

text = "algorithm"

"""
Find the number of characters.

Expected:

9


MY SOLUTION:
"""


# ============================================================
# QUESTION 3
# TRAVERSE STRING
# ============================================================

text = "hello"

"""
Print every character on a separate line.


Expected:

h
e
l
l
o


MY SOLUTION:
"""


# ============================================================
# QUESTION 4
# INDEX + CHARACTER
# ============================================================

text = "code"

"""
Print:

0 c
1 o
2 d
3 e


MY SOLUTION:
"""


# ============================================================
# QUESTION 5
# SLICING
# ============================================================

text = "computer"

"""
Using slicing, print:

First 3 characters
Last 3 characters
Characters from index 2 to 5
Reversed string


MY SOLUTION:
"""


# ============================================================
# QUESTION 6
# COUNT CHARACTER
# ============================================================

text = "banana"

target = "a"

"""
Count the number of a characters.

Do not use count().

Expected:

3


MY SOLUTION:
"""


# ============================================================
# QUESTION 7
# COUNT VOWELS
# ============================================================

text = "Programming"

"""
Count vowels.

Expected:

3

o
a
i


MY SOLUTION:
"""


# ============================================================
# QUESTION 8
# COUNT CONSONANTS
# ============================================================

text = "hello"

"""
Count consonants.

Expected:

3


MY SOLUTION:
"""


# ============================================================
# QUESTION 9
# REVERSE STRING
# ============================================================

text = "python"

"""
Reverse using slicing.

Expected:

nohtyp


MY SOLUTION:
"""


# ============================================================
# QUESTION 10
# PALINDROME USING SLICING
# ============================================================

text = "level"

"""
Return True if palindrome.

Use slicing.

Expected:

True


MY SOLUTION:
"""


# ============================================================
# QUESTION 11
# PALINDROME USING TWO POINTERS
# ============================================================

text = "racecar"

"""
Use Two Pointers.

Do not create the reversed string.

Expected:

True


MY SOLUTION:
"""


# ============================================================
# QUESTION 12
# NOT A PALINDROME
# ============================================================

text = "python"

"""
Use Two Pointers.

Expected:

False


MY SOLUTION:
"""


# ============================================================
# QUESTION 13
# REMOVE SPACES
# ============================================================

text = "data structures"

"""
Remove spaces.

Expected:

datastructures

Try to use:

list + join


MY SOLUTION:
"""


# ============================================================
# QUESTION 14
# CASE CONVERSION
# ============================================================

text = "Hello World"

"""
Print:

HELLO WORLD

hello world


MY SOLUTION:
"""


# ============================================================
# QUESTION 15
# CASE-INSENSITIVE COMPARISON
# ============================================================

text1 = "Python"
text2 = "python"

"""
Compare the strings while ignoring case.

Expected:

True


MY SOLUTION:
"""


# ============================================================
# QUESTION 16
# CHARACTER FREQUENCY
# ============================================================

text = "banana"

"""
Build a dictionary.

Expected:

{
    'b': 1,
    'a': 3,
    'n': 2
}


MY SOLUTION:
"""


# ============================================================
# QUESTION 17
# FIRST REPEATED CHARACTER
# ============================================================

text = "abcdbea"

"""
Find the first repeated character encountered.

Reading left to right:

a
b
c
d
b

The repeated character is:

b


MY SOLUTION:
"""


# ============================================================
# QUESTION 18
# UNIQUE CHARACTERS
# ============================================================

text = "abcdef"

"""
Return True if every character is unique.

Expected:

True


MY SOLUTION:
"""


# ============================================================
# QUESTION 19
# UNIQUE CHARACTERS - FALSE CASE
# ============================================================

text = "hello"

"""
Expected:

False


MY SOLUTION:
"""


# ============================================================
# QUESTION 20
# ANAGRAM
# ============================================================

text1 = "listen"
text2 = "silent"

"""
Check whether the strings are anagrams.

Use sorted() for today's solution.

Expected:

True


MY SOLUTION:
"""


# ============================================================
# QUESTION 21
# COMPLEXITY
# ============================================================

text = "hello"

for character in text:
    print(character)


"""
What is the Time Complexity?

What is the Extra Space Complexity?

MY ANSWER:

Time = ?

Space = ?
"""


# ============================================================
# QUESTION 22
# COMPLEXITY
# ============================================================

text = "hello"

reversed_text = text[::-1]


"""
What is:

Time Complexity?

Space Complexity?

MY ANSWER:

Time = ?

Space = ?
"""


# ============================================================
# QUESTION 23
# COMPLEXITY
# ============================================================

def palindrome_example(text):

    left = 0
    right = len(text) - 1

    while left < right:

        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True


"""
What is:

Time Complexity?

Extra Space?

MY ANSWER:

Time = ?

Space = ?
"""


# ============================================================
# QUESTION 24
# IMMUTABILITY
# ============================================================

"""
Explain why this does not work:


text = "hello"

text[0] = "H"


What does immutable mean?
"""


# ============================================================
# QUESTION 25
# PATTERN RECOGNITION
# ============================================================

"""
Choose the best pattern:

A. Check palindrome
B. Character frequency
C. First repeated character
D. Count vowels
E. Reverse with slicing


Patterns:

- Traversal
- Two Pointers
- Set
- Dictionary
- Slicing
"""


# ============================================================
#
# STOP HERE
#
# TRY ALL QUESTIONS BEFORE READING THE SOLUTIONS
#
# ============================================================






























# ============================================================
# SOLUTIONS
# ============================================================


# ============================================================
# SOLUTION 1
# ============================================================

text = "python"

print(text[0])

print(text[-1])

"""
Output:

p
n

Access:

O(1)
"""


# ============================================================
# SOLUTION 2
# ============================================================

text = "algorithm"

print(len(text))

"""
Output:

9
"""


# ============================================================
# SOLUTION 3
# ============================================================

text = "hello"

for character in text:

    print(character)

"""
Time:

O(n)
"""


# ============================================================
# SOLUTION 4
# ============================================================

text = "code"

for i in range(len(text)):

    print(i, text[i])


# ============================================================
# SOLUTION 5
# ============================================================

text = "computer"

print(text[:3])

print(text[-3:])

print(text[2:6])

print(text[::-1])


# ============================================================
# SOLUTION 6
# ============================================================

text = "banana"

target = "a"

count = 0

for character in text:

    if character == target:

        count += 1

print(count)

"""
Output:

3

Time:

O(n)

Space:

O(1)
"""


# ============================================================
# SOLUTION 7
# ============================================================

text = "Programming"

vowels = "aeiou"

count = 0

for character in text.lower():

    if character in vowels:

        count += 1

print(count)

"""
Output:

3
"""


# ============================================================
# SOLUTION 8
# ============================================================

text = "hello"

vowels = "aeiou"

count = 0

for character in text.lower():

    if (
        character.isalpha()
        and
        character not in vowels
    ):

        count += 1

print(count)

"""
Output:

3
"""


# ============================================================
# SOLUTION 9
# ============================================================

text = "python"

print(text[::-1])

"""
Output:

nohtyp

Time:

O(n)

Space:

O(n)
"""


# ============================================================
# SOLUTION 10
# ============================================================

text = "level"

print(
    text == text[::-1]
)

"""
Output:

True
"""


# ============================================================
# SOLUTION 11
# ============================================================

def is_palindrome(text):

    left = 0

    right = len(text) - 1

    while left < right:

        if text[left] != text[right]:

            return False

        left += 1

        right -= 1

    return True


print(
    is_palindrome(
        "racecar"
    )
)

"""
Output:

True

Time:

O(n)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 12
# ============================================================

print(
    is_palindrome(
        "python"
    )
)

"""
Output:

False
"""


# ============================================================
# SOLUTION 13
# ============================================================

text = "data structures"

characters = []

for character in text:

    if character != " ":

        characters.append(character)

result = "".join(characters)

print(result)

"""
Output:

datastructures

Time:

O(n)

Space:

O(n)
"""


# ============================================================
# SOLUTION 14
# ============================================================

text = "Hello World"

print(text.upper())

print(text.lower())


# ============================================================
# SOLUTION 15
# ============================================================

text1 = "Python"

text2 = "python"

print(
    text1.lower()
    ==
    text2.lower()
)

"""
Output:

True
"""


# ============================================================
# SOLUTION 16
# ============================================================

text = "banana"

frequency = {}

for character in text:

    if character in frequency:

        frequency[character] += 1

    else:

        frequency[character] = 1

print(frequency)

"""
Output:

{'b': 1, 'a': 3, 'n': 2}

Average Time:

O(n)

Space:

O(k)

k = number of unique characters
"""


# ============================================================
# SOLUTION 17
# ============================================================

def first_repeated(text):

    seen = set()

    for character in text:

        if character in seen:

            return character

        seen.add(character)

    return None


print(
    first_repeated(
        "abcdbea"
    )
)

"""
Output:

b

Average Time:

O(n)

Space:

O(n)
"""


# ============================================================
# SOLUTION 18
# ============================================================

def all_unique(text):

    seen = set()

    for character in text:

        if character in seen:

            return False

        seen.add(character)

    return True


print(
    all_unique(
        "abcdef"
    )
)

"""
Output:

True
"""


# ============================================================
# SOLUTION 19
# ============================================================

print(
    all_unique(
        "hello"
    )
)

"""
Output:

False
"""


# ============================================================
# SOLUTION 20
# ============================================================

def are_anagrams(text1, text2):

    return sorted(text1) == sorted(text2)


print(
    are_anagrams(
        "listen",
        "silent"
    )
)

"""
Output:

True

Time:

O(n log n)

because sorting is required.
"""


# ============================================================
# SOLUTION 21
# ============================================================

"""
String traversal:

for character in text

visits each character.

Time:

O(n)


Only the loop variable is needed.

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 22
# ============================================================

"""
text[::-1]

creates a new reversed string.

Time:

O(n)

Space:

O(n)
"""


# ============================================================
# SOLUTION 23
# ============================================================

"""
Two Pointer Palindrome

Time:

O(n)

because the pointers move inward through
the string.


Extra Space:

O(1)

because only fixed variables are used:

left
right
"""


# ============================================================
# SOLUTION 24
# ============================================================

"""
Strings are immutable.

Immutable means:

An existing string's individual characters
cannot be changed directly.


This is invalid:

text[0] = "H"


Instead create another string:

new_text = "H" + text[1:]
"""


# ============================================================
# SOLUTION 25
# ============================================================

"""
A. Palindrome

Two Pointers


B. Character Frequency

Dictionary


C. First Repeated Character

Set


D. Count Vowels

Traversal


E. Reverse

Slicing
"""


# ============================================================
# FINAL DAY 4 PRACTICE SUMMARY
# ============================================================

"""
IMPORTANT DAY 4 IDEAS


STRING INDEXING

text[i]

O(1)


-----------------------------------------


TRAVERSAL

for character in text

O(n)


-----------------------------------------


STRING SLICING

text[start:end]

Creates a new string.


-----------------------------------------


REVERSE SLICING

text[::-1]

Time:

O(n)

Space:

O(n)


-----------------------------------------


IMMUTABILITY

Strings cannot be modified
character-by-character.


-----------------------------------------


TWO POINTERS

Useful for:

Palindrome


Time:

O(n)

Extra Space:

O(1)


-----------------------------------------


SET

Useful for:

Repeated characters
Unique characters


-----------------------------------------


DICTIONARY

Useful for:

Character Frequency


-----------------------------------------


BUILD + JOIN

Better pattern for creating
a string from many characters:

characters = []

characters.append(...)

result = "".join(characters)
"""