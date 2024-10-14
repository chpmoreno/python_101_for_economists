"""Lists in Python"""
from typing import Union

# Create a dictionary
person: dict[str, Union[str, int, float]] = {
    "name": "José",
    "age": 35,
    "city": "Barcelona"
}
print(person["name"])  # Output: José

# Access
print(person["age"])  # Output: 35

# Add
person["profession"] = "Economist"

# Modify
person["age"] = 36

# Remove
del person["city"]

# Keys and values
print(person.keys())  # dict_keys(['name', 'age', 'profession'])
print(person.values())  # dict_values(['José', 36, 'Economist'])
print(person.items())  # dict_items([('name', 'José'), ('age', 36), ('profession', 'Economist')])

# Check if a key exists
print("name" in person)  # Output: True
print("city" in person)  # Output: False

# Get the length of the dictionary
print(len(person))  # Output: 3
