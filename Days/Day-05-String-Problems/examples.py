"""
============================================================
DAY 05 - STRING PROBLEMS AND PATTERNS
============================================================

Topics:

1. Character Frequency
2. Anagram
3. First Unique Character
4. Valid Palindrome
5. Remove Duplicate Characters
6. Longest Common Prefix
7. String Compression
8. Two Pointers
9. Sliding Window
10. Longest Substring Without Repeating Characters
"""


# ============================================================
# EXAMPLE 1
# CHARACTER FREQUENCY
# ============================================================

def character_frequency(text):

    frequency = {}

    for character in text:

        frequency[character] = (
            frequency.get(character, 0) + 1
        )

    return frequency


print("EXAMPLE 1 - CHARACTER FREQUENCY")

print(
    character_frequency(
        "banana"
    )
)


# ============================================================
# EXAMPLE 2
# ANAGRAM USING SORTING
# ============================================================

def anagram_sorting(text1, text2):

    return sorted(text1) == sorted(text2)


print("\nEXAMPLE 2 - ANAGRAM USING SORTING")

print(
    anagram_sorting(
        "listen",
        "silent"
    )
)


# ============================================================
# EXAMPLE 3
# ANAGRAM USING FREQUENCY
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


print("\nEXAMPLE 3 - ANAGRAM USING FREQUENCY")

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
# EXAMPLE 4
# FIRST UNIQUE CHARACTER
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


print("\nEXAMPLE 4 - FIRST UNIQUE CHARACTER")

print(
    first_unique_character(
        "leetcode"
    )
)


# ============================================================
# EXAMPLE 5
# VALID PALINDROME - CLEAN FIRST
# ============================================================

def valid_palindrome_clean(text):

    cleaned = []

    for character in text:

        if character.isalnum():

            cleaned.append(
                character.lower()
            )

    cleaned = "".join(cleaned)

    return cleaned == cleaned[::-1]


print("\nEXAMPLE 5 - VALID PALINDROME CLEAN")

print(
    valid_palindrome_clean(
        "A man, a plan, a canal: Panama"
    )
)


# ============================================================
# EXAMPLE 6
# VALID PALINDROME - TWO POINTERS
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


print("\nEXAMPLE 6 - VALID PALINDROME TWO POINTERS")

print(
    valid_palindrome(
        "A man, a plan, a canal: Panama"
    )
)

print(
    valid_palindrome(
        "race a car"
    )
)


# ============================================================
# EXAMPLE 7
# REMOVE DUPLICATE CHARACTERS
# ============================================================

def remove_duplicates(text):

    seen = set()

    result = []

    for character in text:

        if character not in seen:

            seen.add(character)

            result.append(character)

    return "".join(result)


print("\nEXAMPLE 7 - REMOVE DUPLICATES")

print(
    remove_duplicates(
        "programming"
    )
)


# ============================================================
# EXAMPLE 8
# LONGEST COMMON PREFIX
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


print("\nEXAMPLE 8 - LONGEST COMMON PREFIX")

print(
    longest_common_prefix(
        ["flower", "flow", "flight"]
    )
)


# ============================================================
# EXAMPLE 9
# STRING COMPRESSION
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
                text[i - 1] + str(count)
            )

            count = 1

    result.append(
        text[-1] + str(count)
    )

    return "".join(result)


print("\nEXAMPLE 9 - STRING COMPRESSION")

print(
    compress_string(
        "aaabbc"
    )
)


# ============================================================
# EXAMPLE 10
# SIMPLE TWO POINTER STRING
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


print("\nEXAMPLE 10 - TWO POINTER PALINDROME")

print(
    simple_palindrome(
        "racecar"
    )
)


# ============================================================
# EXAMPLE 11
# LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
# SLIDING WINDOW
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

        window_length = (
            right - left + 1
        )

        longest = max(
            longest,
            window_length
        )

    return longest


print(
    "\nEXAMPLE 11 - LONGEST UNIQUE SUBSTRING"
)

print(
    longest_unique_substring(
        "abcabcbb"
    )
)


# ============================================================
# EXAMPLE 12
# SLIDING WINDOW VISUALIZATION
# ============================================================

def show_windows(text):

    print("\nEXAMPLE 12 - SIMPLE FIXED WINDOWS")

    window_size = 3

    for i in range(
        len(text) - window_size + 1
    ):

        window = text[
            i:i + window_size
        ]

        print(window)


show_windows(
    "abcdef"
)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n======================================")
print("DAY 05 EXAMPLES COMPLETE")
print("======================================")

"""
IMPORTANT DAY 5 PATTERNS


FREQUENCY DICTIONARY

frequency = {}

Useful for:

Anagrams
Character frequency
First unique character


-----------------------------------------


SET

seen = set()

Useful for:

Duplicates
Unique characters
Sliding Window


-----------------------------------------


TWO POINTERS

left = 0
right = len(text) - 1

Useful for:

Palindrome
Valid palindrome


-----------------------------------------


SLIDING WINDOW

left = 0

for right in range(len(text)):

Useful for:

Longest substring
Shortest substring
Consecutive ranges


-----------------------------------------


BUILD + JOIN

result = []

result.append(...)

return "".join(result)

Useful because strings are immutable.
"""