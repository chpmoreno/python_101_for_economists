"""Tuples in Python"""
from typing import Union

# Create a tuple
coordinates: tuple[int, int] = (10, 20)
print(coordinates[0])  # Output: 10
print(coordinates[1])  # Output: 20

# Create a tuple
fruits: tuple[str, str, str] = ("apple", "banana", "cherry")
print(fruits[0])  # Output: apple

# Create a tuple with multiple types
multiple_types_tuple: tuple[Union[str, int], ...] = ("apple", 1, "banana", 2, "cherry", 3)
print(multiple_types_tuple) # Output: ('apple', 1, 'banana', 2, 'cherry', 3)

# Access the element in position 1 (banana). Remember that tuples are 0-indexed.
print(fruits[1])  # Output: banana

# Get the length of the tuple
print(len(fruits)) # Output: 3

# Get a slice of the tuple
# From index 1 to 3 (not including 3)
print(fruits[1:3])  # Output: ('banana', 'cherry')

#Tuple concatenation
coordinates1 = (10, 20)
coordinates2 = (30, 40)
coordinates_concatenation = coordinates1 + coordinates2
print(coordinates_concatenation) # Output: (10, 20, 30, 40)
