"""
Day 02 Practice
Arrays and Python Lists

Try every question yourself first.

Topics:
- Indexing
- Updating
- Traversal
- Search
- append()
- insert()
- remove()
- pop()
- len()
- Negative indexing
- Slicing
- Time Complexity
"""


# ============================================================
# QUESTION 1
# Accessing elements
# ============================================================

numbers = [10, 20, 30, 40, 50]

"""
Find:

1. First element
2. Third element
3. Last element

Write your answers below:

First =
Third =
Last =
"""


# ============================================================
# QUESTION 2
# Updating an element
# ============================================================

numbers = [5, 10, 15, 20]

"""
Change:

15

to:

100

Expected result:

[5, 10, 100, 20]
"""


# ============================================================
# QUESTION 3
# Traversal
# ============================================================

numbers = [1, 2, 3, 4, 5]

"""
Print every number using a loop.

Expected:

1
2
3
4
5
"""


# ============================================================
# QUESTION 4
# Index + Value
# ============================================================

numbers = [10, 20, 30, 40]

"""
Print this:

Index: 0 Value: 10
Index: 1 Value: 20
Index: 2 Value: 30
Index: 3 Value: 40
"""


# ============================================================
# QUESTION 5
# append()
# ============================================================

numbers = [10, 20, 30]

"""
Add:

40

to the end.

Expected:

[10, 20, 30, 40]
"""


# ============================================================
# QUESTION 6
# insert()
# ============================================================

numbers = [10, 20, 30, 40]

"""
Insert:

99

at index:

2

Expected:

[10, 20, 99, 30, 40]
"""


# ============================================================
# QUESTION 7
# remove()
# ============================================================

numbers = [10, 20, 30, 40, 50]

"""
Remove the value:

30

Expected:

[10, 20, 40, 50]
"""


# ============================================================
# QUESTION 8
# pop()
# ============================================================

numbers = [10, 20, 30, 40]

"""
Remove the final element using pop().

Expected:

[10, 20, 30]

Also store the removed value.
"""


# ============================================================
# QUESTION 9
# Linear Search
# ============================================================

def find_number(arr, target):
    pass


"""
Write Linear Search.

Requirements:

- Check every element
- Return the index if target is found
- Return -1 if target is not found

Example:

numbers = [10, 20, 30, 40, 50]

find_number(numbers, 30)

should return:

2
"""


# ============================================================
# QUESTION 10
# Negative Indexing
# ============================================================

numbers = [10, 20, 30, 40, 50]

"""
Using negative indexes:

1. Print the last element
2. Print the second-last element

Expected:

50
40
"""


# ============================================================
# QUESTION 11
# Slicing
# ============================================================

numbers = [10, 20, 30, 40, 50]

"""
Print:

1. First 3 elements
2. Last 3 elements
3. Elements from index 1 to 3
4. Reversed list

Expected:

[10, 20, 30]

[30, 40, 50]

[20, 30, 40]

[50, 40, 30, 20, 10]
"""


# ============================================================
# QUESTION 12
# Find Sum
# ============================================================

numbers = [5, 10, 15, 20, 25]

"""
Find the total WITHOUT using sum().

Expected:

75
"""


# ============================================================
# QUESTION 13
# Find Maximum
# ============================================================

numbers = [14, 3, 99, 21, 7]

"""
Find the largest number WITHOUT using max().

Expected:

99
"""


# ============================================================
# QUESTION 14
# Find Minimum
# ============================================================

numbers = [14, 3, 99, 21, 7]

"""
Find the smallest number WITHOUT using min().

Expected:

3
"""


# ============================================================
# QUESTION 15
# Count Occurrences
# ============================================================

numbers = [1, 2, 3, 2, 4, 2, 5]

"""
Count how many times:

2

appears.

Expected:

3
"""


# ============================================================
# QUESTION 16
# Check if value exists
# ============================================================

numbers = [10, 20, 30, 40, 50]

"""
Check whether:

40

exists in the list.

Do it manually using a loop.

Expected:

True
"""


# ============================================================
# QUESTION 17
# Big-O
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[2])

"""
What is the Time Complexity?

Your Answer:
"""


# ============================================================
# QUESTION 18
# Big-O
# ============================================================

for number in numbers:
    print(number)

"""
What is the Time Complexity?

Your Answer:
"""


# ============================================================
# QUESTION 19
# Big-O
# ============================================================

numbers.insert(0, 100)

"""
What is the Time Complexity?

Your Answer:
"""


# ============================================================
# QUESTION 20
# Big-O
# ============================================================

numbers.append(100)

"""
What is the Time Complexity?

Your Answer:
"""


# ============================================================
# QUESTION 21
# Big-O
# ============================================================

numbers.pop()

"""
What is the Time Complexity?

Your Answer:
"""


# ============================================================
# QUESTION 22
# Big-O
# ============================================================

numbers.pop(0)

"""
What is the Time Complexity?

Your Answer:
"""


# ============================================================
# QUESTION 23
# Big-O
# ============================================================

print(len(numbers))

"""
What is the Time Complexity?

Your Answer:
"""


# ============================================================
# QUESTION 24
# Big-O
# ============================================================

print(numbers[1:4])

"""
Suppose this slice contains k elements.

What is the Time Complexity?

Your Answer:
"""


# ============================================================
# QUESTION 25
# Concept question
# ============================================================

"""
Explain in your own words:

Why is:

numbers[3]

O(1)

but searching for:

40

using Linear Search:

O(n)?
"""


# ============================================================
# SOLUTIONS
# ============================================================


# ============================================================
# SOLUTION 1
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])
print(numbers[-1])

"""
Answers:

First  = 10
Third  = 30
Last   = 50

Access by known index:

O(1)
"""


# ============================================================
# SOLUTION 2
# ============================================================

numbers = [5, 10, 15, 20]

numbers[2] = 100

print(numbers)

"""
Result:

[5, 10, 100, 20]

Updating known index:

O(1)
"""


# ============================================================
# SOLUTION 3
# ============================================================

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

"""
Time Complexity:

O(n)
"""


# ============================================================
# SOLUTION 4
# ============================================================

numbers = [10, 20, 30, 40]

for i in range(len(numbers)):
    print("Index:", i, "Value:", numbers[i])

"""
Time Complexity:

O(n)
"""


# ============================================================
# SOLUTION 5
# ============================================================

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)

"""
Result:

[10, 20, 30, 40]

Typical Complexity:

O(1) amortized
"""


# ============================================================
# SOLUTION 6
# ============================================================

numbers = [10, 20, 30, 40]

numbers.insert(2, 99)

print(numbers)

"""
Result:

[10, 20, 99, 30, 40]

Typical Complexity:

O(n)

because elements may need to shift.
"""


# ============================================================
# SOLUTION 7
# ============================================================

numbers = [10, 20, 30, 40, 50]

numbers.remove(30)

print(numbers)

"""
Result:

[10, 20, 40, 50]

Typical Complexity:

O(n)
"""


# ============================================================
# SOLUTION 8
# ============================================================

numbers = [10, 20, 30, 40]

removed = numbers.pop()

print("Removed:", removed)
print(numbers)

"""
Removed:

40

List:

[10, 20, 30]

Pop from end:

O(1)
"""


# ============================================================
# SOLUTION 9
# ============================================================

def find_number(arr, target):

    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1


numbers = [10, 20, 30, 40, 50]

print(find_number(numbers, 30))
print(find_number(numbers, 100))

"""
Output:

2
-1

Worst-case Time Complexity:

O(n)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 10
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[-1])
print(numbers[-2])

"""
Output:

50
40

Negative indexing still gives direct access.

O(1)
"""


# ============================================================
# SOLUTION 11
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers[:3])
print(numbers[-3:])
print(numbers[1:4])
print(numbers[::-1])

"""
Output:

[10, 20, 30]

[30, 40, 50]

[20, 30, 40]

[50, 40, 30, 20, 10]
"""


# ============================================================
# SOLUTION 12
# ============================================================

numbers = [5, 10, 15, 20, 25]

total = 0

for number in numbers:
    total += number

print(total)

"""
Output:

75

Time Complexity:

O(n)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 13
# ============================================================

numbers = [14, 3, 99, 21, 7]

largest = numbers[0]

for number in numbers:

    if number > largest:
        largest = number

print(largest)

"""
Output:

99

Time Complexity:

O(n)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 14
# ============================================================

numbers = [14, 3, 99, 21, 7]

smallest = numbers[0]

for number in numbers:

    if number < smallest:
        smallest = number

print(smallest)

"""
Output:

3

Time Complexity:

O(n)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 15
# ============================================================

numbers = [1, 2, 3, 2, 4, 2, 5]

count = 0

for number in numbers:

    if number == 2:
        count += 1

print(count)

"""
Output:

3

Time Complexity:

O(n)

Extra Space:

O(1)
"""


# ============================================================
# SOLUTION 16
# ============================================================

numbers = [10, 20, 30, 40, 50]

found = False

for number in numbers:

    if number == 40:
        found = True
        break

print(found)

"""
Output:

True

Worst-case Time:

O(n)
"""


# ============================================================
# SOLUTION 17
# ============================================================

"""
numbers[2]

Time Complexity:

O(1)

Why?

We know the index already.
"""


# ============================================================
# SOLUTION 18
# ============================================================

"""
for number in numbers:

Time Complexity:

O(n)

Why?

Every element is visited.
"""


# ============================================================
# SOLUTION 19
# ============================================================

"""
numbers.insert(0, 100)

Time Complexity:

O(n)

Why?

Existing elements may need to move right.
"""


# ============================================================
# SOLUTION 20
# ============================================================

"""
numbers.append(100)

Typical Complexity:

O(1) amortized
"""


# ============================================================
# SOLUTION 21
# ============================================================

"""
numbers.pop()

Time Complexity:

O(1)

because the final element can be removed
without shifting the remaining elements.
"""


# ============================================================
# SOLUTION 22
# ============================================================

"""
numbers.pop(0)

Time Complexity:

O(n)

because the remaining elements may need
to shift left.
"""


# ============================================================
# SOLUTION 23
# ============================================================

"""
len(numbers)

Time Complexity:

O(1)

Python keeps track of the list size.
"""


# ============================================================
# SOLUTION 24
# ============================================================

"""
numbers[1:4]

If the slice contains k elements:

Time Complexity:

O(k)

Space Complexity:

O(k)

because Python creates a new list containing
those k elements.
"""


# ============================================================
# SOLUTION 25
# ============================================================

"""
numbers[3]

is O(1) because we already know
the exact position we want.

Linear Search is O(n) because we do not
know where the value is.

We may need to check:

index 0
index 1
index 2
...
until we find the target.

In the worst case, we check every element.
"""