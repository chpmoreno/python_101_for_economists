"""Lists in Python"""
from typing import Union

# Create a list
fruits: list[str] = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple

# Create a list with multiple types
multiple_types_list: list[Union[str, int]] = ["apple", 1, "banana", 2, "cherry", 3]
print(multiple_types_list) # Output: ['apple', 1, 'banana', 2, 'cherry', 3]

# Access the element in position 1 (banana). Remember that lists are 0-indexed.
print(fruits[1])  # Output: banana

# Add an element
fruits.append("orange")

# Remove an element
fruits.remove("banana")

# Get the length of the list
print(len(fruits)) # Output: 3

# Get a slice of the list
# From index 1 to 3 (not including 3)
print(fruits[1:2])  # Output: ['cherry', 'orange']

#Modify an element of a list
fruits[0] = "grape"
print(fruits) # Output: ['grape', 'cherry', 'orange']

