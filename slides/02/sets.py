"""Sets in Python"""
from typing import Union

# Create a set
fruits: set[str] = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'apple', 'banana', 'cherry'}

# Create a set with multiple types
multiple_types_set: set[Union[str, int]] = {"apple", 1, "banana", 2, "cherry", 3}
print(multiple_types_set) # Output: {1, 2, 3, 'apple', 'banana', 'cherry'}

# Add an element
fruits.add("orange")

# Remove an element
fruits.remove("banana")

# Get the length of the set
print(len(fruits)) # Output: 3

# Check if an element is in the set
print("cherry" in fruits)  # Output: True

# Add an element to a set
fruits_set = {"apple", "banana", "cherry"}
fruits_set.add("orange")
print(fruits_set)  # Output: {'apple', 'orange', 'banana', 'cherry'}

# Find the intersection of two sets
another_set = {"cherry", "grape"}
common_fruits = fruits_set.intersection(another_set)
print(common_fruits)  # Output: {'cherry'}

# Find the union of two sets
all_fruits = fruits_set.union(another_set)
print(all_fruits)  # Output: {'apple',  'grape', 'orange', 'banana', 'cherry'}

# Find the difference of two sets
unique_fruits = fruits_set.difference(another_set)
print(unique_fruits)  # Output: {'banana',  'orange', 'apple'}

# Check if one set is a subset of another
subset_fruits = {"apple", "banana"}
print(subset_fruits.issubset(fruits_set))  # Output: True
