"""
============================================================
DAY 04 - STRINGS
============================================================

Topics:

1. Creating Strings
2. Indexing
3. Negative Indexing
4. Traversal
5. Slicing
6. Immutability
7. Case Conversion
8. String Comparison
9. Count Character
10. Count Vowels
11. Count Consonants
12. Reverse String
13. Palindrome
14. Two Pointer Palindrome
15. Remove Spaces
16. Character Frequency
17. First Repeated Character
18. Unique Characters
19. Anagram
"""


# ============================================================
# EXAMPLE 1
# CREATE A STRING
# ============================================================

text = "hello"

print("EXAMPLE 1 - STRING")
print(text)


# ============================================================
# EXAMPLE 2
# STRING INDEXING
# ============================================================

text = "hello"

print("\nEXAMPLE 2 - INDEXING")

print(text[0])
print(text[1])
print(text[4])


# ============================================================
# EXAMPLE 3
# NEGATIVE INDEXING
# ============================================================

print("\nEXAMPLE 3 - NEGATIVE INDEXING")

print(text[-1])
print(text[-2])


# ============================================================
# EXAMPLE 4
# STRING LENGTH
# ============================================================

print("\nEXAMPLE 4 - LENGTH")

print(len(text))


# ============================================================
# EXAMPLE 5
# TRAVERSAL
# ============================================================

print("\nEXAMPLE 5 - TRAVERSAL")

for character in text:
    print(character)


# ============================================================
# EXAMPLE 6
# TRAVERSAL WITH INDEX
# ============================================================

print("\nEXAMPLE 6 - INDEX + CHARACTER")

for i in range(len(text)):

    print(
        "Index:",
        i,
        "Character:",
        text[i]
    )


# ============================================================
# EXAMPLE 7
# SLICING
# ============================================================

text = "hello"

print("\nEXAMPLE 7 - SLICING")

print("0:3 =", text[0:3])

print(":3 =", text[:3])

print("2: =", text[2:])

print("-2: =", text[-2:])

print("Reverse =", text[::-1])


# ============================================================
# EXAMPLE 8
# STRING IMMUTABILITY
# ============================================================

text = "hello"

print("\nEXAMPLE 8 - IMMUTABILITY")

# This would cause an error:
#
# text[0] = "H"

new_text = "H" + text[1:]

print("Original:", text)

print("New:", new_text)


# ============================================================
# EXAMPLE 9
# UPPERCASE / LOWERCASE
# ============================================================

text = "Hello World"

print("\nEXAMPLE 9 - CASE")

print(text.upper())

print(text.lower())


# ============================================================
# EXAMPLE 10
# STRING COMPARISON
# ============================================================

print("\nEXAMPLE 10 - COMPARISON")

print("hello" == "hello")

print("Hello" == "hello")

print(
    "Hello".lower()
    ==
    "hello".lower()
)


# ============================================================
# EXAMPLE 11
# COUNT CHARACTER
# ============================================================

def count_character(text, target):

    count = 0

    for character in text:

        if character == target:

            count += 1

    return count


print("\nEXAMPLE 11 - COUNT CHARACTER")

print(
    count_character(
        "banana",
        "a"
    )
)


# ============================================================
# EXAMPLE 12
# COUNT VOWELS
# ============================================================

def count_vowels(text):

    vowels = "aeiou"

    count = 0

    for character in text.lower():

        if character in vowels:

            count += 1

    return count


print("\nEXAMPLE 12 - COUNT VOWELS")

print(
    count_vowels(
        "Hello World"
    )
)


# ============================================================
# EXAMPLE 13
# COUNT CONSONANTS
# ============================================================

def count_consonants(text):

    vowels = "aeiou"

    count = 0

    for character in text.lower():

        if (
            character.isalpha()
            and
            character not in vowels
        ):
            count += 1

    return count


print("\nEXAMPLE 13 - COUNT CONSONANTS")

print(
    count_consonants(
        "Hello World"
    )
)


# ============================================================
# EXAMPLE 14
# REVERSE STRING
# ============================================================

def reverse_string(text):

    return text[::-1]


print("\nEXAMPLE 14 - REVERSE STRING")

print(
    reverse_string(
        "hello"
    )
)


# ============================================================
# EXAMPLE 15
# PALINDROME USING SLICING
# ============================================================

def palindrome_slicing(text):

    return text == text[::-1]


print("\nEXAMPLE 15 - PALINDROME WITH SLICING")

print(
    palindrome_slicing(
        "racecar"
    )
)

print(
    palindrome_slicing(
        "hello"
    )
)


# ============================================================
# EXAMPLE 16
# PALINDROME USING TWO POINTERS
# ============================================================

def palindrome_two_pointers(text):

    left = 0

    right = len(text) - 1

    while left < right:

        if text[left] != text[right]:

            return False

        left += 1

        right -= 1

    return True


print("\nEXAMPLE 16 - TWO POINTER PALINDROME")

print(
    palindrome_two_pointers(
        "racecar"
    )
)

print(
    palindrome_two_pointers(
        "python"
    )
)


# ============================================================
# EXAMPLE 17
# REMOVE SPACES
# ============================================================

def remove_spaces(text):

    characters = []

    for character in text:

        if character != " ":

            characters.append(character)

    return "".join(characters)


print("\nEXAMPLE 17 - REMOVE SPACES")

print(
    remove_spaces(
        "hello world"
    )
)


# ============================================================
# EXAMPLE 18
# CHARACTER FREQUENCY
# ============================================================

def character_frequency(text):

    frequency = {}

    for character in text:

        if character in frequency:

            frequency[character] += 1

        else:

            frequency[character] = 1

    return frequency


print("\nEXAMPLE 18 - CHARACTER FREQUENCY")

print(
    character_frequency(
        "banana"
    )
)


# ============================================================
# EXAMPLE 19
# FIRST REPEATED CHARACTER
# ============================================================

def first_repeated_character(text):

    seen = set()

    for character in text:

        if character in seen:

            return character

        seen.add(character)

    return None


print("\nEXAMPLE 19 - FIRST REPEATED CHARACTER")

print(
    first_repeated_character(
        "abca"
    )
)


# ============================================================
# EXAMPLE 20
# ALL UNIQUE CHARACTERS
# ============================================================

def all_unique(text):

    seen = set()

    for character in text:

        if character in seen:

            return False

        seen.add(character)

    return True


print("\nEXAMPLE 20 - UNIQUE CHARACTERS")

print(
    all_unique(
        "abcde"
    )
)

print(
    all_unique(
        "hello"
    )
)


# ============================================================
# EXAMPLE 21
# ANAGRAM
# ============================================================

def are_anagrams(text1, text2):

    return sorted(text1) == sorted(text2)


print("\nEXAMPLE 21 - ANAGRAM")

print(
    are_anagrams(
        "listen",
        "silent"
    )
)

print(
    are_anagrams(
        "hello",
        "world"
    )
)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n======================================")
print("DAY 04 EXAMPLES COMPLETE")
print("======================================")

"""
IMPORTANT DAY 4 PATTERNS


TRAVERSAL

for character in text:

Useful for:

counting
searching
vowels
consonants


-----------------------------------------


TWO POINTERS

left = 0
right = len(text) - 1

Useful for:

palindrome


-----------------------------------------


SET

seen = set()

Useful for:

duplicates
unique characters
first repeated character


-----------------------------------------


DICTIONARY

frequency = {}

Useful for:

character frequency
counting


-----------------------------------------


SLICING

text[::-1]

Useful for:

reverse
substrings


-----------------------------------------


STRING IMMUTABILITY

Strings cannot be changed
character-by-character.

Create a new string instead.
"""