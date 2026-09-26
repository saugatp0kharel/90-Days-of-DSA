"""
============================================================
DAY 06 - HASH TABLES, DICTIONARIES, AND SETS
============================================================
"""


# ============================================================
# EXAMPLE 1
# DICTIONARY
# ============================================================

person = {
    "name": "Saugat",
    "age": 24,
    "major": "Computer Science"
}

print("EXAMPLE 1 - DICTIONARY")
print(person)

print(person["name"])


# ============================================================
# EXAMPLE 2
# ADD / UPDATE
# ============================================================

person["city"] = "Dallas"

person["age"] = 25

print("\nEXAMPLE 2 - ADD AND UPDATE")
print(person)


# ============================================================
# EXAMPLE 3
# CHECK KEY
# ============================================================

print("\nEXAMPLE 3 - CHECK KEY")

if "name" in person:

    print("name exists")


# ============================================================
# EXAMPLE 4
# GET METHOD
# ============================================================

frequency = {}

frequency["a"] = (
    frequency.get("a", 0) + 1
)

print("\nEXAMPLE 4 - GET")
print(frequency)


# ============================================================
# EXAMPLE 5
# DICTIONARY TRAVERSAL
# ============================================================

print("\nEXAMPLE 5 - DICTIONARY TRAVERSAL")

for key, value in person.items():

    print(key, value)


# ============================================================
# EXAMPLE 6
# SET
# ============================================================

numbers = {
    1,
    2,
    2,
    3
}

print("\nEXAMPLE 6 - SET")
print(numbers)


# ============================================================
# EXAMPLE 7
# SET ADD
# ============================================================

seen = set()

seen.add(10)

seen.add(20)

seen.add(10)

print("\nEXAMPLE 7 - SET ADD")
print(seen)


# ============================================================
# EXAMPLE 8
# FREQUENCY MAP
# ============================================================

def frequency_map(text):

    frequency = {}

    for character in text:

        frequency[character] = (
            frequency.get(character, 0) + 1
        )

    return frequency


print("\nEXAMPLE 8 - FREQUENCY MAP")

print(
    frequency_map(
        "banana"
    )
)


# ============================================================
# EXAMPLE 9
# DUPLICATE DETECTION
# ============================================================

def contains_duplicate(numbers):

    seen = set()

    for number in numbers:

        if number in seen:

            return True

        seen.add(number)

    return False


print("\nEXAMPLE 9 - DUPLICATE DETECTION")

print(
    contains_duplicate(
        [1, 2, 3, 4, 2]
    )
)


# ============================================================
# EXAMPLE 10
# TWO SUM BRUTE FORCE
# ============================================================

def two_sum_brute(numbers, target):

    for i in range(len(numbers)):

        for j in range(i + 1, len(numbers)):

            if numbers[i] + numbers[j] == target:

                return [i, j]

    return None


print("\nEXAMPLE 10 - TWO SUM BRUTE FORCE")

print(
    two_sum_brute(
        [2, 7, 11, 15],
        9
    )
)


# ============================================================
# EXAMPLE 11
# TWO SUM HASH TABLE
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


print("\nEXAMPLE 11 - TWO SUM HASH TABLE")

print(
    two_sum(
        [2, 7, 11, 15],
        9
    )
)


# ============================================================
# EXAMPLE 12
# FIRST UNIQUE ELEMENT
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


print("\nEXAMPLE 12 - FIRST UNIQUE")

print(
    first_unique(
        [4, 5, 4, 6, 5, 7]
    )
)


# ============================================================
# EXAMPLE 13
# INTERSECTION
# ============================================================

def intersection(a, b):

    set_a = set(a)

    result = []

    seen_result = set()

    for number in b:

        if (
            number in set_a
            and
            number not in seen_result
        ):

            result.append(number)

            seen_result.add(number)

    return result


print("\nEXAMPLE 13 - INTERSECTION")

print(
    intersection(
        [1, 2, 2, 3, 4],
        [2, 3, 5]
    )
)


# ============================================================
# EXAMPLE 14
# WORD FREQUENCY
# ============================================================

def word_frequency(words):

    frequency = {}

    for word in words:

        frequency[word] = (
            frequency.get(word, 0) + 1
        )

    return frequency


print("\nEXAMPLE 14 - WORD FREQUENCY")

print(
    word_frequency(
        [
            "apple",
            "banana",
            "apple",
            "orange",
            "banana",
            "apple"
        ]
    )
)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n======================================")
print("DAY 06 EXAMPLES COMPLETE")
print("======================================")

"""
PATTERNS

Dictionary
→ key -> value

Set
→ unique values

Frequency Map
→ count occurrences

Seen Set
→ detect duplicates

Complement Lookup
→ Two Sum

Hash Table Average Lookup
→ O(1)
"""