"""
============================================================
DAY 07 PRACTICE
STACKS
============================================================

Try every question before checking solutions.

Ask:

1. Does this problem need LIFO?
2. What should be pushed?
3. When should I pop?
4. Do I need to peek at stack[-1]?
5. What is the Time Complexity?
6. What is the Space Complexity?
"""


# ============================================================
# QUESTION 1
# CREATE STACK
# ============================================================

"""
Create an empty stack.

MY SOLUTION:
"""


# ============================================================
# QUESTION 2
# PUSH
# ============================================================

"""
Push:

10
20
30

Expected stack:

[10, 20, 30]

MY SOLUTION:
"""


# ============================================================
# QUESTION 3
# PEEK
# ============================================================

"""
Using:

[10, 20, 30]

print the top value
without removing it.

Expected:

30

MY SOLUTION:
"""


# ============================================================
# QUESTION 4
# POP
# ============================================================

"""
Remove the top value.

Expected removed:

30

Remaining:

[10, 20]

MY SOLUTION:
"""


# ============================================================
# QUESTION 5
# EMPTY STACK
# ============================================================

"""
Check whether:

[]

is empty.

Expected:

True

MY SOLUTION:
"""


# ============================================================
# QUESTION 6
# REVERSE STRING
# ============================================================

text = "python"

"""
Reverse using a stack.

Expected:

nohtyp

MY SOLUTION:
"""


# ============================================================
# QUESTION 7
# VALID PARENTHESES
# ============================================================

text = "()[]{}"

"""
Expected:

True

MY SOLUTION:
"""


# ============================================================
# QUESTION 8
# INVALID PARENTHESES
# ============================================================

text = "([)]"

"""
Expected:

False

MY SOLUTION:
"""


# ============================================================
# QUESTION 9
# VALID NESTED PARENTHESES
# ============================================================

text = "{[()]}"

"""
Expected:

True

MY SOLUTION:
"""


# ============================================================
# QUESTION 10
# UNFINISHED PARENTHESES
# ============================================================

text = "((("

"""
Expected:

False

Why must we check the stack
at the end?

MY SOLUTION:
"""


# ============================================================
# QUESTION 11
# REMOVE ADJACENT DUPLICATES
# ============================================================

text = "abbaca"

"""
Expected:

ca

MY SOLUTION:
"""


# ============================================================
# QUESTION 12
# REMOVE ADJACENT DUPLICATES
# ============================================================

text = "azxxzy"

"""
Expected:

ay

MY SOLUTION:
"""


# ============================================================
# QUESTION 13
# STACK NUMBERS
# ============================================================

"""
Push:

5
10
15
20

Then pop two values.

What remains?

Expected:

[5, 10]

MY SOLUTION:
"""


# ============================================================
# QUESTION 14
# COMPLEXITY
# ============================================================

"""
stack.append(x)

Average Time = ?

MY ANSWER:
"""


# ============================================================
# QUESTION 15
# COMPLEXITY
# ============================================================

"""
stack.pop()

from the END.

Time = ?

MY ANSWER:
"""


# ============================================================
# QUESTION 16
# COMPLEXITY
# ============================================================

"""
stack[-1]

Time = ?

MY ANSWER:
"""


# ============================================================
# QUESTION 17
# REVERSE COMPLEXITY
# ============================================================

"""
Reverse n characters using stack.

Time = ?

Space = ?

MY ANSWER:
"""


# ============================================================
# QUESTION 18
# VALID PARENTHESES COMPLEXITY
# ============================================================

"""
Valid Parentheses:

Time = ?

Space = ?

MY ANSWER:
"""


# ============================================================
# QUESTION 19
# STACK VS QUEUE
# ============================================================

"""
Explain:

Stack = ?

Queue = ?

What does:

LIFO

mean?

What does:

FIFO

mean?
"""


# ============================================================
# QUESTION 20
# PATTERN RECOGNITION
# ============================================================

"""
Which problems are good stack problems?

A. Valid Parentheses
B. Undo
C. Reverse Data
D. Adjacent Duplicate Removal
E. Next Greater Element

Answer:

?
"""


# ============================================================
# QUESTION 21
# CALL STACK
# ============================================================

"""
Explain what a call stack is.

If:

main()
calls function_a()

and function_a()
calls function_b()

which function finishes first?
"""


# ============================================================
# QUESTION 22
# POP EMPTY STACK
# ============================================================

"""
What happens here?

stack = []

stack.pop()

How can you avoid the problem?
"""


# ============================================================
# QUESTION 23
# MONOTONIC STACK
# ============================================================

"""
In simple words:

What is a Monotonic Stack?

Name one type of problem
where it is useful.
"""


# ============================================================
# QUESTION 24
# NEXT GREATER ELEMENT
# ============================================================

numbers = [2, 1, 4, 3]

"""
Find the next greater value
for every element.

Expected:

[4, 4, -1, -1]

This is an advanced Day 7 challenge.

MY SOLUTION:
"""


# ============================================================
# QUESTION 25
# EXPLAIN WHY STACK
# ============================================================

"""
Why is a stack perfect for:

Valid Parentheses?

Explain using:

Last In First Out.
"""


# ============================================================
#
# STOP HERE
#
# TRY EVERYTHING BEFORE SOLUTIONS
#
# ============================================================





























# ============================================================
# SOLUTIONS
# ============================================================


# ============================================================
# SOLUTION 1
# ============================================================

stack = []

print(stack)


# ============================================================
# SOLUTION 2
# ============================================================

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)


# ============================================================
# SOLUTION 3
# ============================================================

print(
    stack[-1]
)


# ============================================================
# SOLUTION 4
# ============================================================

removed = stack.pop()

print("Removed:", removed)

print("Remaining:", stack)


# ============================================================
# SOLUTION 5
# ============================================================

stack = []

print(
    not stack
)


# ============================================================
# SOLUTION 6
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


print(
    reverse_string(
        "python"
    )
)


# ============================================================
# SOLUTION 7
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


print(
    is_valid_parentheses(
        "()[]{}"
    )
)


# ============================================================
# SOLUTION 8
# ============================================================

print(
    is_valid_parentheses(
        "([)]"
    )
)


# ============================================================
# SOLUTION 9
# ============================================================

print(
    is_valid_parentheses(
        "{[()]}"
    )
)


# ============================================================
# SOLUTION 10
# ============================================================

print(
    is_valid_parentheses(
        "((("
    )
)

"""
The final stack contains
unmatched opening brackets.

Therefore:

False
"""


# ============================================================
# SOLUTION 11
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
    remove_adjacent_duplicates(
        "abbaca"
    )
)


# ============================================================
# SOLUTION 12
# ============================================================

print(
    remove_adjacent_duplicates(
        "azxxzy"
    )
)


# ============================================================
# SOLUTION 13
# ============================================================

stack = []

stack.append(5)
stack.append(10)
stack.append(15)
stack.append(20)

stack.pop()
stack.pop()

print(stack)

"""
Output:

[5, 10]
"""


# ============================================================
# SOLUTION 14
# ============================================================

"""
stack.append(x)

Average / Amortized:

O(1)
"""


# ============================================================
# SOLUTION 15
# ============================================================

"""
stack.pop()

from end:

O(1)
"""


# ============================================================
# SOLUTION 16
# ============================================================

"""
stack[-1]

O(1)
"""


# ============================================================
# SOLUTION 17
# ============================================================

"""
Reverse with Stack:

Push n characters:

O(n)

Pop n characters:

O(n)

Total:

O(n)


Extra Space:

O(n)
"""


# ============================================================
# SOLUTION 18
# ============================================================

"""
Valid Parentheses:

Time:

O(n)

Space:

O(n)
"""


# ============================================================
# SOLUTION 19
# ============================================================

"""
STACK:

LIFO

Last In
First Out


QUEUE:

FIFO

First In
First Out
"""


# ============================================================
# SOLUTION 20
# ============================================================

"""
All of them can use stacks:

A. Valid Parentheses
B. Undo
C. Reverse
D. Adjacent Duplicate Removal
E. Next Greater Element
"""


# ============================================================
# SOLUTION 21
# ============================================================

"""
A call stack stores active
function calls.

If:

main()
→ function_a()
→ function_b()

function_b() finishes first.

Then function_a().

Then main().

This is LIFO.
"""


# ============================================================
# SOLUTION 22
# ============================================================

"""
Calling:

stack.pop()

on an empty list causes:

IndexError


Safer:

if stack:

    stack.pop()
"""


# ============================================================
# SOLUTION 23
# ============================================================

"""
A Monotonic Stack keeps values
in increasing or decreasing order.

Useful for:

Next Greater Element
Next Smaller Element
Daily Temperatures
Stock Span
"""


# ============================================================
# SOLUTION 24
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
    next_greater(
        [2, 1, 4, 3]
    )
)

"""
Output:

[4, 4, -1, -1]
"""


# ============================================================
# SOLUTION 25
# ============================================================

"""
Parentheses close in the
opposite order from which
they open.

Example:

(

then [

means:

]

must close first,

then:

)

This is:

Last In
First Out

So a stack is the correct
data structure.
"""


# ============================================================
# FINAL DAY 7 SUMMARY
# ============================================================

"""
STACK

LIFO

Last In
First Out


-----------------------------------------


PUSH

stack.append(x)

O(1) amortized


-----------------------------------------


POP

stack.pop()

O(1)


-----------------------------------------


PEEK

stack[-1]

O(1)


-----------------------------------------


USE STACK WHEN

Most recent item
must be handled first.


-----------------------------------------


COMMON PROBLEMS

Valid Parentheses
Reverse
Undo
Adjacent Duplicates
Next Greater Element
"""