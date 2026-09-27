"""
============================================================
DAY 07 - STACKS
============================================================

Topics:

1. Basic Stack
2. Push
3. Pop
4. Peek
5. Empty Check
6. Reverse String
7. Valid Parentheses
8. Remove Adjacent Duplicates
9. Undo Example
10. Monotonic Stack Introduction
"""


# ============================================================
# EXAMPLE 1
# BASIC STACK
# ============================================================

stack = []

print("EXAMPLE 1 - BASIC STACK")

print(stack)


# ============================================================
# EXAMPLE 2
# PUSH
# ============================================================

stack.append(10)
stack.append(20)
stack.append(30)

print("\nEXAMPLE 2 - PUSH")

print(stack)


# ============================================================
# EXAMPLE 3
# PEEK
# ============================================================

print("\nEXAMPLE 3 - PEEK")

print(stack[-1])

print("Stack after peek:")

print(stack)


# ============================================================
# EXAMPLE 4
# POP
# ============================================================

removed = stack.pop()

print("\nEXAMPLE 4 - POP")

print("Removed:", removed)

print("Stack:", stack)


# ============================================================
# EXAMPLE 5
# EMPTY CHECK
# ============================================================

print("\nEXAMPLE 5 - EMPTY CHECK")

print(len(stack) == 0)

print(not stack)


# ============================================================
# EXAMPLE 6
# REVERSE STRING USING STACK
# ============================================================

def reverse_string(text):

    stack = []

    for character in text:

        stack.append(character)

    result = []

    while stack:

        result.append(
            stack.pop()
        )

    return "".join(result)


print("\nEXAMPLE 6 - REVERSE STRING")

print(
    reverse_string(
        "hello"
    )
)


# ============================================================
# EXAMPLE 7
# VALID PARENTHESES
# ============================================================

def is_valid_parentheses(text):

    stack = []

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for character in text:

        if character in "([{":

            stack.append(character)

        else:

            if not stack:

                return False

            top = stack.pop()

            if top != pairs[character]:

                return False

    return len(stack) == 0


print("\nEXAMPLE 7 - VALID PARENTHESES")

print(
    is_valid_parentheses(
        "()[]{}"
    )
)

print(
    is_valid_parentheses(
        "([)]"
    )
)

print(
    is_valid_parentheses(
        "([])"
    )
)


# ============================================================
# EXAMPLE 8
# REMOVE ADJACENT DUPLICATES
# ============================================================

def remove_adjacent_duplicates(text):

    stack = []

    for character in text:

        if (
            stack
            and
            stack[-1] == character
        ):

            stack.pop()

        else:

            stack.append(character)

    return "".join(stack)


print(
    "\nEXAMPLE 8 - REMOVE ADJACENT DUPLICATES"
)

print(
    remove_adjacent_duplicates(
        "abbaca"
    )
)


# ============================================================
# EXAMPLE 9
# STACK WITH NUMBERS
# ============================================================

number_stack = []

number_stack.append(5)
number_stack.append(10)
number_stack.append(15)

print("\nEXAMPLE 9 - NUMBER STACK")

print("Stack:", number_stack)

print(
    "Top:",
    number_stack[-1]
)

print(
    "Removed:",
    number_stack.pop()
)

print(
    "Remaining:",
    number_stack
)


# ============================================================
# EXAMPLE 10
# SIMPLE UNDO
# ============================================================

history = []

history.append("Hello")

history.append("Hello World")

history.append("Hello World!")

print("\nEXAMPLE 10 - UNDO")

print("Current:", history[-1])

history.pop()

print("After Undo:", history[-1])


# ============================================================
# EXAMPLE 11
# MANUAL STACK PROCESS
# ============================================================

stack = []

print("\nEXAMPLE 11 - MANUAL PROCESS")

for number in [1, 2, 3]:

    stack.append(number)

    print(
        "Push:",
        number,
        "Stack:",
        stack
    )

while stack:

    removed = stack.pop()

    print(
        "Pop:",
        removed,
        "Stack:",
        stack
    )


# ============================================================
# EXAMPLE 12
# NEXT GREATER ELEMENT
# BASIC MONOTONIC STACK INTRODUCTION
# ============================================================

def next_greater(numbers):

    result = [-1] * len(numbers)

    stack = []

    for i in range(len(numbers)):

        while (
            stack
            and
            numbers[i] > numbers[stack[-1]]
        ):

            previous_index = stack.pop()

            result[previous_index] = numbers[i]

        stack.append(i)

    return result


print(
    "\nEXAMPLE 12 - NEXT GREATER ELEMENT"
)

print(
    next_greater(
        [2, 1, 4, 3]
    )
)

"""
Input:

[2, 1, 4, 3]

Output:

[4, 4, -1, -1]

Explanation:

Next greater after 2 = 4
Next greater after 1 = 4
Next greater after 4 = none
Next greater after 3 = none
"""


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n======================================")
print("DAY 07 EXAMPLES COMPLETE")
print("======================================")

"""
STACK PATTERNS


LIFO

Last In
First Out


-----------------------------------------


PUSH

stack.append(value)


-----------------------------------------


POP

stack.pop()


-----------------------------------------


PEEK

stack[-1]


-----------------------------------------


PARENTHESES

Use stack for matching


-----------------------------------------


ADJACENT DUPLICATES

Compare:

stack[-1]

with current value


-----------------------------------------


MONOTONIC STACK

Keep useful values/indexes
in ordered stack form.
"""