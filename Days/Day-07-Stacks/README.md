# Day 07 - Stacks

Welcome to **Day 07** of my **90 Days of Data Structures and Algorithms** journey.

So far I have learned:

```text
Day 01 - Big-O and Complexity
Day 02 - Arrays and Python Lists
Day 03 - Array Problems and Two Pointers
Day 04 - Strings
Day 05 - String Problems and Patterns
Day 06 - Hash Tables, Dictionaries, and Sets
```

Today I am learning:

# Stacks

A stack is a data structure where the most recently added item is usually the first one removed.

This idea is called:

# LIFO

LIFO means:

```text
Last In
First Out
```

Today I learned:

- What is a Stack?
- LIFO
- Push
- Pop
- Peek
- Empty Stack
- Stack using Python list
- Valid Parentheses
- Reverse a String using Stack
- Remove Adjacent Duplicates
- Stack for Undo Operations
- Time Complexity
- Space Complexity
- Monotonic Stack introduction

---

# 1. What is a Stack?

A stack is similar to a stack of plates.

Imagine:

```text
        Plate 3
        Plate 2
        Plate 1
```

If I add another plate:

```text
        Plate 4
        Plate 3
        Plate 2
        Plate 1
```

Which plate should I remove first?

```text
Plate 4
```

because it was the last plate added.

This is:

```text
Last In
First Out
```

or:

```text
LIFO
```

---

# 2. LIFO

LIFO means:

```text
Last item added
        ↓
First item removed
```

Example:

```text
Push 10
Push 20
Push 30
```

Stack:

```text
Top
 ↓
30
20
10
```

If we pop:

```text
30
```

is removed first.

Then:

```text
20
```

Then:

```text
10
```

---

# 3. Stack Operations

The main stack operations are:

```text
push
pop
peek
is empty
```

---

# 4. Push

Push means:

```text
add an item to the top of the stack
```

In Python, we can use:

```python
append()
```

Example:

```python
stack = []

stack.append(10)
stack.append(20)
stack.append(30)
```

Stack:

```text
[10, 20, 30]
```

The top is:

```text
30
```

Average push complexity:

```text
O(1)
```

---

# 5. Pop

Pop means:

```text
remove the top item
```

Python:

```python
stack.pop()
```

Example:

```python
stack = [10, 20, 30]

removed = stack.pop()

print(removed)
```

Output:

```text
30
```

Stack becomes:

```text
[10, 20]
```

Pop from the end is:

```text
O(1)
```

---

# 6. Peek

Peek means:

```text
look at the top item
without removing it
```

Python:

```python
stack[-1]
```

Example:

```python
stack = [10, 20, 30]

print(stack[-1])
```

Output:

```text
30
```

Stack remains:

```text
[10, 20, 30]
```

Complexity:

```text
O(1)
```

---

# 7. Check if Stack is Empty

A simple way:

```python
if not stack:
    print("Stack is empty")
```

Example:

```python
stack = []

print(len(stack) == 0)
```

Output:

```text
True
```

---

# 8. Stack Using Python List

Python lists can be used as stacks.

Example:

```python
stack = []

stack.append("A")
stack.append("B")
stack.append("C")

print(stack)
```

Output:

```text
['A', 'B', 'C']
```

Pop:

```python
stack.pop()
```

removes:

```text
C
```

---

# 9. Stack Visualization

Start:

```text
[]
```

Push:

```text
10
```

Now:

```text
[10]
```

Push:

```text
20
```

Now:

```text
[10, 20]
```

Push:

```text
30
```

Now:

```text
[10, 20, 30]
```

Pop:

```text
30
```

Now:

```text
[10, 20]
```

This is LIFO.

---

# 10. Why Use a Stack?

Stacks are useful when the most recent thing matters first.

Examples:

- Undo
- Redo
- Browser back button
- Function calls
- Expression evaluation
- Parentheses checking
- Reversing data
- Depth-First Search
- Parsing

---

# 11. Reverse a String Using Stack

Problem:

```text
hello
```

Expected:

```text
olleh
```

Main idea:

Push every character.

Then pop characters.

Because stack is LIFO, the order becomes reversed.

---

## Solution

```python
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
```

Example:

```python
print(
    reverse_string(
        "hello"
    )
)
```

Output:

```text
olleh
```

---

## Step-by-Step

Input:

```text
hello
```

Push:

```text
h
e
l
l
o
```

Stack:

```text
[h, e, l, l, o]
```

Pop:

```text
o
l
l
e
h
```

Result:

```text
olleh
```

---

## Complexity

Push all characters:

```text
O(n)
```

Pop all characters:

```text
O(n)
```

Total:

```text
O(n)
```

Stack uses:

```text
O(n)
```

extra space.

---

# 12. Valid Parentheses

This is one of the most important stack problems.

Input:

```text
()
```

Valid:

```text
True
```

Input:

```text
()[]{}
```

Valid:

```text
True
```

Input:

```text
(]
```

Valid:

```text
False
```

Input:

```text
([)]
```

Valid:

```text
False
```

---

# Main Idea

Opening brackets:

```text
(
[
{
```

go into the stack.

Closing brackets:

```text
)
]
}
```

must match the most recent opening bracket.

This is exactly a:

```text
LIFO
```

problem.

---

# 13. Valid Parentheses Solution

```python
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
```

---

# Step-by-Step Example

Input:

```text
([])
```

Read:

```text
(
```

Push:

```text
[
(
]
```

Read:

```text
[
```

Push:

```text
[
[
(
]
```

Read:

```text
]
```

It should match:

```text
[
```

It does.

Pop it.

Read:

```text
)
```

It should match:

```text
(
```

It does.

Stack becomes empty.

Therefore:

```text
True
```

---

# Complexity

Each character is processed once.

```text
Time = O(n)
```

Worst-case stack:

```text
O(n)
```

So:

```text
Space = O(n)
```

---

# 14. Why Stack Works for Parentheses

Suppose:

```text
({[]})
```

The opening order is:

```text
(
{
[
```

The closing order must be:

```text
]
}
)
```

Notice:

```text
last opening
must close first
```

This is exactly:

```text
LIFO
```

---

# 15. Remove Adjacent Duplicates

Problem:

```text
abbaca
```

Remove adjacent equal characters repeatedly.

Expected:

```text
ca
```

---

# Step-by-Step

Input:

```text
abbaca
```

Read:

```text
a
```

Push:

```text
[a]
```

Read:

```text
b
```

Push:

```text
[a, b]
```

Read another:

```text
b
```

Top is also:

```text
b
```

So pop.

Stack becomes:

```text
[a]
```

Read:

```text
a
```

Top is:

```text
a
```

Pop.

Stack:

```text
[]
```

Then:

```text
c
a
```

Final:

```text
ca
```

---

# Solution

```python
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
```

---

# Complexity

Every character is pushed or popped at most once.

```text
Time = O(n)
```

Stack:

```text
Space = O(n)
```

---

# 16. Stack and Undo

Stacks are often used for Undo.

Imagine typing:

```text
Hello
```

Then:

```text
Hello World
```

Then:

```text
Hello World!
```

The stack can store previous states:

```text
Hello
Hello World
Hello World!
```

Undo removes:

```text
Hello World!
```

and returns to:

```text
Hello World
```

The most recent action is undone first.

Again:

```text
LIFO
```

---

# 17. Stack and Function Calls

Programming languages internally use a:

```text
call stack
```

When functions call other functions, their information is stored on a stack.

Example:

```text
main()
↓
function_a()
↓
function_b()
```

`function_b()` finishes first.

Then:

```text
function_a()
```

Then:

```text
main()
```

Again:

```text
LIFO
```

---

# 18. Stack Complexity

Using a Python list:

| Operation | Complexity |
|---|---:|
| Push / append | O(1) amortized |
| Pop from top | O(1) |
| Peek | O(1) |
| Empty check | O(1) |
| Search entire stack | O(n) |

---

# 19. Stack vs Queue

Stack:

```text
LIFO
```

```text
Last In
First Out
```

Queue:

```text
FIFO
```

```text
First In
First Out
```

Example stack:

```text
plates
```

Example queue:

```text
people waiting in line
```

We will study queues later.

---

# 20. Introduction to Monotonic Stack

A Monotonic Stack is a stack that keeps values in a specific order.

For example:

```text
increasing
```

or:

```text
decreasing
```

It is useful for problems like:

- Next Greater Element
- Next Smaller Element
- Daily Temperatures
- Stock Span

For Day 7, the goal is only to understand the idea.

---

# 21. Next Greater Element Idea

Input:

```text
[2, 1, 4, 3]
```

For:

```text
2
```

the next greater value is:

```text
4
```

For:

```text
1
```

the next greater value is:

```text
4
```

For:

```text
4
```

there is none.

A monotonic stack can solve this efficiently.

We will study this more deeply later.

---

# 22. Common Stack Patterns

## Pattern 1 - Matching

Use stack when things must match in reverse order.

Example:

```text
Parentheses
```

---

## Pattern 2 - Reverse

Because:

```text
Last In
First Out
```

popping naturally reverses data.

---

## Pattern 3 - Undo

Most recent operation should be removed first.

---

## Pattern 4 - Adjacent Comparison

Compare:

```python
stack[-1]
```

with the current item.

Useful for:

```text
duplicate removal
```

---

## Pattern 5 - Monotonic Stack

Keep elements in:

```text
increasing
```

or:

```text
decreasing
```

order.

Useful for:

```text
next greater / next smaller
```

---

# 23. Common Mistakes

## Mistake 1 - Pop From Empty Stack

This causes an error:

```python
stack = []

stack.pop()
```

Always check:

```python
if stack:
```

before popping when needed.

---

## Mistake 2 - Using pop(0)

For a stack, do not use:

```python
stack.pop(0)
```

That removes the beginning and costs:

```text
O(n)
```

Use:

```python
stack.pop()
```

which removes the end:

```text
O(1)
```

---

## Mistake 3 - Confusing Stack and Queue

Stack:

```text
Last In First Out
```

Queue:

```text
First In First Out
```

---

## Mistake 4 - Forgetting Final Stack Check

For parentheses:

```text
(((
```

there is no wrong closing bracket, but the string is still invalid.

So after processing, check:

```python
return len(stack) == 0
```

---

# 24. Day 7 Complexity Summary

| Problem | Time | Space |
|---|---:|---:|
| Push | O(1) | — |
| Pop | O(1) | — |
| Peek | O(1) | — |
| Reverse String | O(n) | O(n) |
| Valid Parentheses | O(n) | O(n) |
| Remove Adjacent Duplicates | O(n) | O(n) |
| Stack Search | O(n) | O(1) |

---

# 25. Day 7 Self-Test

Before finishing Day 7, I should be able to explain:

1. What is a stack?
2. What does LIFO mean?
3. What is push?
4. What is pop?
5. What is peek?
6. How do Python lists act as stacks?
7. Why is append O(1) amortized?
8. Why is pop from end O(1)?
9. Why should I avoid pop(0) for stacks?
10. Why does a stack reverse data?
11. Why is a stack useful for parentheses?
12. What happens when we pop an empty stack?
13. How does Remove Adjacent Duplicates work?
14. What is a call stack?
15. How does Undo use a stack?
16. Difference between stack and queue?
17. What is a monotonic stack?
18. What kind of problems use monotonic stacks?
19. What is the Time Complexity of Valid Parentheses?
20. What is its Space Complexity?

---

# My Day 7 Progress

- [x] Learned Stack basics
- [x] Learned LIFO
- [x] Learned Push
- [x] Learned Pop
- [x] Learned Peek
- [x] Used Python list as Stack
- [x] Reversed a String with Stack
- [x] Solved Valid Parentheses
- [x] Solved Remove Adjacent Duplicates
- [x] Learned Undo Stack idea
- [x] Learned Call Stack idea
- [x] Compared Stack vs Queue
- [x] Learned Monotonic Stack introduction
- [x] Analyzed Time Complexity
- [x] Analyzed Space Complexity

---

# Day 7 Quick Cheat Sheet

```text
Stack
→ LIFO
```

```text
Push
→ stack.append(x)
```

```text
Pop
→ stack.pop()
```

```text
Peek
→ stack[-1]
```

```text
Push
→ O(1) amortized
```

```text
Pop
→ O(1)
```

```text
Peek
→ O(1)
```

```text
Parentheses
→ Stack
```

```text
Undo
→ Stack
```

```text
Reverse
→ Stack
```

```text
Adjacent duplicate
→ compare current with stack[-1]
```

---

# Files in Day 07

```text
Day-07-Stacks/
├── README.md
├── examples.py
└── practice.py
```

---

# Next - Day 08

Next topic:

# Queues and Deques

Possible topics:

- FIFO
- enqueue
- dequeue
- `collections.deque`
- Queue vs Stack
- BFS introduction
- Moving Average
- Queue-based problems

---

# 90 Days of DSA

The goal is not only to memorize:

```text
append()
pop()
```

The goal is to understand:

```text
When does LIFO behavior solve the problem?
```

and recognize stack patterns in new problems.