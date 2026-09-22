# Day 02 - Arrays and Python Lists


# -----------------------------------------
# 1. Creating a list
# -----------------------------------------

numbers = [10, 20, 30, 40, 50]

print("Original List:")
print(numbers)


# -----------------------------------------
# 2. Accessing elements - O(1)
# -----------------------------------------

print("\nAccessing Elements:")

print(numbers[0])
print(numbers[2])
print(numbers[-1])


# -----------------------------------------
# 3. Updating an element - O(1)
# -----------------------------------------

numbers[2] = 100

print("\nAfter Update:")
print(numbers)


# -----------------------------------------
# 4. Traversing - O(n)
# -----------------------------------------

print("\nTraversal:")

for number in numbers:
    print(number)


# -----------------------------------------
# 5. Traversing with index
# -----------------------------------------

print("\nIndex + Value:")

for i in range(len(numbers)):
    print("Index:", i, "Value:", numbers[i])


# -----------------------------------------
# 6. Append
# -----------------------------------------

numbers.append(60)

print("\nAfter Append:")
print(numbers)


# -----------------------------------------
# 7. Insert - O(n)
# -----------------------------------------

numbers.insert(1, 99)

print("\nAfter Insert:")
print(numbers)


# -----------------------------------------
# 8. Remove by value
# -----------------------------------------

numbers.remove(40)

print("\nAfter Remove:")
print(numbers)


# -----------------------------------------
# 9. Pop from end
# -----------------------------------------

removed = numbers.pop()

print("\nRemoved:")
print(removed)

print("After Pop:")
print(numbers)


# -----------------------------------------
# 10. Linear Search - O(n)
# -----------------------------------------

def linear_search(arr, target):

    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1


print("\nLinear Search:")

print("99 found at index:", linear_search(numbers, 99))
print("500 found at index:", linear_search(numbers, 500))


# -----------------------------------------
# 11. Length - O(1)
# -----------------------------------------

print("\nLength:")

print(len(numbers))


# -----------------------------------------
# 12. Slicing
# -----------------------------------------

print("\nSlicing:")

print("First 3:", numbers[:3])
print("From index 2:", numbers[2:])
print("Index 1 to 3:", numbers[1:4])
print("Reversed:", numbers[::-1])