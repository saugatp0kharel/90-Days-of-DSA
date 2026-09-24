"""
============================================================
DAY 05 PRACTICE
STRING PROBLEMS AND PATTERNS
============================================================

IMPORTANT:

Try every question before reading the solutions.

For every problem ask:

1. Do I need traversal?
2. Do I need a dictionary?
3. Do I need a set?
4. Can Two Pointers help?
5. Can Sliding Window help?
6. What is the Time Complexity?
7. What is the Space Complexity?
"""


# ============================================================
# QUESTION 1
# CHARACTER FREQUENCY
# ============================================================

text = "mississippi"

"""
Build a frequency dictionary.

Expected idea:

m -> 1
i -> 4
s -> 4
p -> 2


MY SOLUTION:
"""


# ============================================================
# QUESTION 2
# ANAGRAM USING SORTING
# ============================================================

text1 = "earth"
text2 = "heart"

"""
Check whether they are anagrams using sorted().

Expected:

True


MY SOLUTION:
"""


# ============================================================
# QUESTION 3
# ANAGRAM USING DICTIONARY
# ============================================================

text1 = "listen"
text2 = "silent"

"""
Solve without sorting.

Use character frequencies.

Expected:

True


MY SOLUTION:
"""


# ============================================================
# QUESTION 4
# FIRST UNIQUE CHARACTER
# ============================================================

text = "aabbcddee"

"""
Find the first character that appears once.

Expected:

c


MY SOLUTION:
"""


# ============================================================
# QUESTION 5
# VALID PALINDROME
# ============================================================

text = "A man, a plan, a canal: Panama"

"""
Ignore:

spaces
punctuation
capitalization

Expected:

True

Try Two Pointers.


MY SOLUTION:
"""


# ============================================================
# QUESTION 6
# INVALID PALINDROME
# ============================================================

text = "race a car"

"""
Expected:

False


MY SOLUTION:
"""


# ============================================================
# QUESTION 7
# REMOVE DUPLICATES
# ============================================================

text = "banana"

"""
Keep only the first occurrence
of each character.

Expected:

ban


MY SOLUTION:
"""


# ============================================================
# QUESTION 8
# LONGEST COMMON PREFIX
# ============================================================

words = [
    "interview",
    "internet",
    "internal"
]

"""
Find the longest common prefix.

Expected:

inter


MY SOLUTION:
"""


# ============================================================
# QUESTION 9
# NO COMMON PREFIX
# ============================================================

words = [
    "dog",
    "racecar",
    "car"
]

"""
Expected:

""


MY SOLUTION:
"""


# ============================================================
# QUESTION 10
# STRING COMPRESSION
# ============================================================

text = "aaaabbcc"

"""
Compress consecutive characters.

Expected:

a4b2c2


MY SOLUTION:
"""


# ============================================================
# QUESTION 11
# STRING COMPRESSION
# ============================================================

text = "abcd"

"""
Expected:

a1b1c1d1


MY SOLUTION:
"""


# ============================================================
# QUESTION 12
# SIMPLE PALINDROME TWO POINTERS
# ============================================================

text = "madam"

"""
Expected:

True


MY SOLUTION:
"""


# ============================================================
# QUESTION 13
# LONGEST UNIQUE SUBSTRING
# ============================================================

text = "abcabcbb"

"""
Find the LENGTH of the longest substring
without repeating characters.

Expected:

3


MY SOLUTION:
"""


# ============================================================
# QUESTION 14
# LONGEST UNIQUE SUBSTRING
# ============================================================

text = "bbbbb"

"""
Expected:

1


MY SOLUTION:
"""


# ============================================================
# QUESTION 15
# LONGEST UNIQUE SUBSTRING
# ============================================================

text = "pwwkew"

"""
Expected:

3

One valid substring:

wke


MY SOLUTION:
"""


# ============================================================
# QUESTION 16
# COMPLEXITY - ANAGRAM SORTING
# ============================================================

"""
If we solve anagram using:

sorted(text1) == sorted(text2)

What is the typical Time Complexity?

MY ANSWER:

Time = ?
"""


# ============================================================
# QUESTION 17
# COMPLEXITY - FREQUENCY ANAGRAM
# ============================================================

"""
If we use a frequency dictionary and
traverse each string once:

What is:

Time Complexity?

Space Complexity?

MY ANSWER:

Time = ?
Space = ?
"""


# ============================================================
# QUESTION 18
# COMPLEXITY - VALID PALINDROME
# ============================================================

"""
Two Pointer valid palindrome:

What is:

Time Complexity?

Extra Space?

MY ANSWER:

Time = ?
Space = ?
"""


# ============================================================
# QUESTION 19
# COMPLEXITY - REMOVE DUPLICATES
# ============================================================

"""
If we use:

seen = set()

and a result list:

What is:

Average Time?

Space?

MY ANSWER:

Time = ?
Space = ?
"""


# ============================================================
# QUESTION 20
# SLIDING WINDOW CONCEPT
# ============================================================

"""
Explain in your own words:

What is Sliding Window?

Why do we use left and right pointers?

When do we shrink the window?
"""


# ============================================================
# QUESTION 21
# PATTERN RECOGNITION
# ============================================================

"""
Choose the best pattern:

A. Anagram
B. First Unique Character
C. Valid Palindrome
D. Remove Duplicate Characters
E. Longest Substring Without Repeating

Choose from:

- Frequency Dictionary
- Set
- Two Pointers
- Sliding Window
"""


# ============================================================
# QUESTION 22
# FIXED WINDOW
# ============================================================

text = "abcdef"

"""
Print all substrings of length 3.

Expected:

abc
bcd
cde
def


MY SOLUTION:
"""


# ============================================================
# QUESTION 23
# CASE INSENSITIVE ANAGRAM
# ============================================================

text1 = "Listen"
text2 = "Silent"

"""
Check anagram while ignoring case.

Expected:

True


MY SOLUTION:
"""


# ============================================================
# QUESTION 24
# REMOVE DUPLICATES WITH SPACES
# ============================================================

text = "hello world"

"""
Remove duplicate characters.

Keep spaces only once.

One expected result:

helo wrd


MY SOLUTION:
"""


# ============================================================
# QUESTION 25
# EXPLAIN THE PATTERN
# ============================================================

"""
Explain:

Dictionary:
What question does it help answer?

Set:
What question does it help answer?

Two Pointers:
What kind of string problems use it?

Sliding Window:
What kind of substring problems use it?
"""


# ============================================================
#
# STOP HERE
#
# TRY QUESTIONS BEFORE READING SOLUTIONS
#
# ============================================================































# ============================================================
# SOLUTIONS
# ============================================================


# ============================================================
# SOLUTION 1
# ============================================================

text = "mississippi"

frequency = {}

for character in text:

    frequency[character] = (
        frequency.get(character, 0) + 1
    )

print(frequency)

"""
Output:

{
    'm': 1,
    'i': 4,
    's': 4,
    'p': 2
}

Time:

O(n)

Space:

O(k)
"""


# ============================================================
# SOLUTION 2
# ============================================================

text1 = "earth"
text2 = "heart"

print(
    sorted(text1)
    ==
    sorted(text2)
)

"""
Output:

True

Typical Time:

O(n log n)
"""


# ============================================================
# SOLUTION 3
# ============================================================

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

O(n)

Space:

O(k)
"""


# ============================================================
# SOLUTION 4
# ============================================================

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


print(
    first_unique_character(
        "aabbcddee"
    )
)

"""
Output:

c

Time:

O(n)
"""


# ============================================================
# SOLUTION 5
# ============================================================

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


print(
    valid_palindrome(
        "A man, a plan, a canal: Panama"
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
# SOLUTION 6
# ============================================================

print(
    valid_palindrome(
        "race a car"
    )
)

"""
Output:

False
"""


# ============================================================
# SOLUTION 7
# ============================================================

def remove_duplicates(text):

    seen = set()

    result = []

    for character in text:

        if character not in seen:

            seen.add(character)

            result.append(character)

    return "".join(result)


print(
    remove_duplicates(
        "banana"
    )
)

"""
Output:

ban

Average Time:

O(n)

Space:

O(n)
"""


# ============================================================
# SOLUTION 8
# ============================================================

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


print(
    longest_common_prefix(
        [
            "interview",
            "internet",
            "internal"
        ]
    )
)

"""
Output:

inter
"""


# ============================================================
# SOLUTION 9
# ============================================================

print(
    longest_common_prefix(
        [
            "dog",
            "racecar",
            "car"
        ]
    )
)

"""
Output:

""
"""


# ============================================================
# SOLUTION 10
# ============================================================

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
                text[i - 1]
                +
                str(count)
            )

            count = 1

    result.append(
        text[-1]
        +
        str(count)
    )

    return "".join(result)


print(
    compress_string(
        "aaaabbcc"
    )
)

"""
Output:

a4b2c2
"""


# ============================================================
# SOLUTION 11
# ============================================================

print(
    compress_string(
        "abcd"
    )
)

"""
Output:

a1b1c1d1
"""


# ============================================================
# SOLUTION 12
# ============================================================

def simple_palindrome(text):

    left = 0
    right = len(text) - 1

    while left < right:

        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True


print(
    simple_palindrome(
        "madam"
    )
)

"""
Output:

True
"""


# ============================================================
# SOLUTION 13
# ============================================================

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

        current_length = (
            right - left + 1
        )

        longest = max(
            longest,
            current_length
        )

    return longest


print(
    longest_unique_substring(
        "abcabcbb"
    )
)

"""
Output:

3
"""


# ============================================================
# SOLUTION 14
# ============================================================

print(
    longest_unique_substring(
        "bbbbb"
    )
)

"""
Output:

1
"""


# ============================================================
# SOLUTION 15
# ============================================================

print(
    longest_unique_substring(
        "pwwkew"
    )
)

"""
Output:

3
"""


# ============================================================
# SOLUTION 16
# ============================================================

"""
Sorting-based anagram:

Time:

O(n log n)
"""


# ============================================================
# SOLUTION 17
# ============================================================

"""
Frequency dictionary anagram:

Time:

O(n)

Space:

O(k)

k = number of unique characters
"""


# ============================================================
# SOLUTION 18
# ============================================================

"""
Two Pointer valid palindrome:

Time:

O(n)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 19
# ============================================================

"""
Remove duplicates using Set:

Average Time:

O(n)

Space:

O(n)
"""


# ============================================================
# SOLUTION 20
# ============================================================

"""
SLIDING WINDOW

Sliding Window means maintaining
a moving range inside the string.

Usually:

left
right

Right expands the window.

Left shrinks the window when the
current window breaks a rule.

Example:

Longest substring without repeating
characters.

If a duplicate appears:

move left until the window becomes
valid again.
"""


# ============================================================
# SOLUTION 21
# ============================================================

"""
A. Anagram

Frequency Dictionary


B. First Unique Character

Frequency Dictionary


C. Valid Palindrome

Two Pointers


D. Remove Duplicate Characters

Set


E. Longest Substring Without Repeating

Sliding Window + Set
"""


# ============================================================
# SOLUTION 22
# ============================================================

text = "abcdef"

window_size = 3

for i in range(
    len(text) - window_size + 1
):

    print(
        text[
            i:i + window_size
        ]
    )

"""
Output:

abc
bcd
cde
def
"""


# ============================================================
# SOLUTION 23
# ============================================================

text1 = "Listen".lower()
text2 = "Silent".lower()

print(
    sorted(text1)
    ==
    sorted(text2)
)

"""
Output:

True
"""


# ============================================================
# SOLUTION 24
# ============================================================

print(
    remove_duplicates(
        "hello world"
    )
)

"""
One possible output:

helo wrd
"""


# ============================================================
# SOLUTION 25
# ============================================================

"""
DICTIONARY

Useful when asking:

How many times?

What value/index belongs to this key?


SET

Useful when asking:

Have I seen this before?


TWO POINTERS

Useful when:

Comparing opposite ends
Checking palindromes


SLIDING WINDOW

Useful when:

Working with a substring
Finding longest/shortest valid range
Tracking consecutive characters
"""


# ============================================================
# FINAL DAY 5 SUMMARY
# ============================================================

"""
DAY 5 IMPORTANT PATTERNS


FREQUENCY DICTIONARY

Useful for:

Anagrams
Frequency
First unique character


-----------------------------------------


SET

Useful for:

Duplicates
Unique characters
Sliding Window


-----------------------------------------


TWO POINTERS

Useful for:

Palindrome
Valid palindrome


-----------------------------------------


SLIDING WINDOW

Useful for:

Longest substring
Shortest substring
Substring conditions


-----------------------------------------


TIME COMPLEXITY

Many optimized Day 5 problems:

O(n)


-----------------------------------------


SPACE COMPLEXITY

Sets and dictionaries often require:

O(k)

or

O(n)

extra space.
"""